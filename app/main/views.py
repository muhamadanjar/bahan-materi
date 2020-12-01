import json
from flask import request, render_template, render_template_string, jsonify
from flask.wrappers import Response, current_app
from flask_sqlalchemy import get_debug_queries
from sqlalchemy import create_engine
from sqlalchemy import engine
from sqlalchemy.sql import text
from sqlalchemy.util.compat import b
from app.main import main
from app import config, db
from .models import Photos
from app.tematik.models import GisJenisTanah, GisPoi
from .forms import PhotoForm
from werkzeug.utils import secure_filename
from app.main.schemas import JenisTanahSchema, PoiSchema
import socket


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('map.html')


@main.route('/get_photos', methods=['GET', 'POST'])
def get_photos():
    engine = create_engine(config['default'].SQLALCHEMY_DATABASE_URI)
    minx = request.args.get('minx', 0)
    miny = request.args.get('miny', 0)
    maxx = request.args.get('maxx', 0)
    maxy = request.args.get('maxy', 0)
    bbox = str(minx) + ',' + str(miny) + ',' + str(maxx) + ',' + str(maxy)
    sql = "SELECT * FROM photos WHERE ST_Intersects(ST_SetSRID(ST_MakePoint(lon, lat), 4326), ST_MakeEnvelope(%s, 4326))='t'" % (
        bbox)
    with engine.connect() as con:
        result = con.execute(text(sql))
        resultkey = con.execute(text(sql)).keys()
        rows = result.fetchall()
        output = []
        for item in rows:
            inner = {}
            for key, val in zip(resultkey, item):
                inner[key] = str(val)
            output.append(inner)
        jsonoutput = json.dumps(output)
    return Response(jsonoutput, mimetype='application/json')


@main.route('/add_photos', methods=['GET', 'POST'])
def new_photos():
    try:
        form = PhotoForm(request.form)
        if request.method == 'POST' and form.validate():
            filename = secure_filename(form.photo.data.filename)
            form.file.data.save(f'uploads/{filename}')
            photos = Photos(lon=form.lon, lat=form.lat,
                            nama=form.nama, remark=form.remark, photo=filename)
            db.session.add(photos)
            db.session.commit()
            resp = json.dumps(
                {'status': 'success', 'message': 'Tambah objek berhasil!'})
            return Response(resp, mimetype='application/json')

        form_html = render_template('form.html', form=form)
        html = render_template_string(form_html)
        return jsonify({'html': html})
    except (socket.timeout) as e:
        return jsonify({'status': 'error', 'message': str(e)})


@main.route('/get_poi', methods=['GET'])
def get_nearest_poi():
    lat = request.args.get('lat', -6.6160933)
    lon = request.args.get('lon', 106.8266368)
    radius = request.args.get('radius', 1000)
    lonlat = str(lon) + ' ,' + str(lat)
    engine = create_engine(config['default'].SQLALCHEMY_BINDS['kotabogor'])
    sql = """SELECT kegiatan, nama_objek, 
        ST_X(st_transform(wkb_geometry, 4326)) as longitude,
        ST_Y(st_transform(wkb_geometry, 4326)) as latitude,
        wkb_geometry  FROM tematik.gis_poi 
        WHERE 
            ST_DWithin(wkb_geometry, 
                ST_TRANSFORM(ST_SetSRID(ST_MakePoint(%s), 4326), 32748), %s) """ % (lonlat, radius)
    with engine.connect() as con:
        result = con.execute(sql)
        resultkey = con.execute(sql).keys()
        rows = result.fetchall()
        output = []
        for item in rows:
            inner = {}
            for key, val in zip(resultkey, item):
                inner[key] = str(val)
            output.append(inner)
    return jsonify({'status':'success', 'data': output})


@main.route('/get_bbox', methods=['GET'])
def get_bbox():
    engine = create_engine(config['default'].SQLALCHEMY_BINDS['kotabogor'])
    minx = request.args.get('xmin', 0)
    miny = request.args.get('ymin', 0)
    maxx = request.args.get('xmax', 0)
    maxy = request.args.get('ymax', 0)
    bbox = str(minx) + ',' + str(miny) + ',' + str(maxx) + ',' + str(maxy)
    sql = """SELECT kegiatan, nama_objek  FROM tematik.gis_poi 
        WHERE ST_Intersects(
            ST_SetSRID(
                ST_MakePoint(
                    ST_X(st_transform(wkb_geometry, 4326)), 
                    ST_Y(st_transform(wkb_geometry, 4326))
                ), 4326), 
            ST_MakeEnvelope(%s, 4326)
        )='t' """ % (bbox)
    with engine.connect() as con:
        result = con.execute(text(sql))
        resultkey = con.execute(text(sql)).keys()
        rows = result.fetchall()
        output = []
        for item in rows:
            inner = {}
            for key, val in zip(resultkey, item):
                inner[key] = str(val)
            output.append(inner)
        return jsonify({'status':'success', 'data': output})


@main.route('/get_administrasi')
def get_administrasi():
    engine = create_engine(config['default'].SQLALCHEMY_BINDS['kotabogor'])
    sql = "SELECT kode_kec, kecamatan, st_asgeojson(st_transform(geom, 3857),15,0)::json as geojson from administrasi.gis_admin_kec"
    with engine.connect() as con:
        result = con.execute(text(sql))
        resultkey = con.execute(text(sql)).keys()
        rows = result.fetchall()
        output = []
        for item in rows:
            inner = {}
            for key, val in zip(resultkey, item):
                vf = val if key == 'geojson' else str(val)
                inner[key] = vf
            output.append(inner)
        return jsonify({'status': 'success', 'data': output})


@main.route('/check_point_in_poly')
def get_checkin_points_in_poly():
    engine = create_engine(config['default'].SQLALCHEMY_BINDS['kotabogor'])
    kode_kec = request.args.get('kode', 3271010)
    sql = """ 
    SELECT kegiatan , nama_objek , st_x(st_transform(wkb_geometry, 4326)) as longitude, st_y(st_transform(wkb_geometry, 4326)) as latitude
        FROM tematik.gis_poi 
    WHERE ST_Contains(
        (SELECT geom from administrasi.gis_admin_kec where kode_kec = %s limit 1), 
        tematik.gis_poi.wkb_geometry
    );
    """ % (kode_kec)
    with engine.connect() as con:
        result = con.execute(text(sql))
        resultkey = result.keys()
        rows = result.fetchall()
        output = []
        for item in rows:
            inner = {}
            for key, val in zip(resultkey, item):
                vf = val if key == 'geojson' else str(val)
                inner[key] = vf
            output.append(inner)
        return jsonify({'status': 'success', 'data': output, 'params': kode_kec})


@main.route('/get_pip')
def get_pip():
    engine = create_engine(config['default'].SQLALCHEMY_BINDS['kotabogor'])
    lat = request.args.get('lat', -6.6160933)
    lon = request.args.get('lon', 106.8266368)
    lonlat = str(lon) + ' ,' + str(lat)
    sql = """ SELECT kecamatan, kode_kec FROM administrasi.gis_admin_kec gak
              WHERE ST_Contains(
	            st_transform(gak.geom, 4326), 
	            st_setsrid(st_makepoint(%s), 4326))""" % (lonlat)
    
    with engine.connect() as con:
        result = con.execute(text(sql))
        rows = result.fetchall()
        jml = len(rows)
        return jsonify({'status': 'success', 'data': jml})