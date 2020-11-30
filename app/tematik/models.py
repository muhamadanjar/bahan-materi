# coding: utf-8
from app import db


class GisBangunan(db.Model):
    __tablename__ = 'gis_bangunan'
    __table_args__ = {'schema': 'tematik'}
    __bind_key__ = 'tematik'
    id = db.Column(db.BigInteger, primary_key=True)
    gid = db.Column(db.BigInteger)
    fid_gis_ba = db.Column(db.Numeric)
    objectid = db.Column(db.Numeric)
    jenis = db.Column(db.String(250))
    nama = db.Column(db.String(250))
    sumber = db.Column(db.String(250))
    fid_batas_ = db.Column(db.Numeric)
    kecamatan = db.Column(db.String(254))


class GisPoi(db.Model):
    __tablename__ = 'gis_poi'
    __table_args__ = {'schema': 'tematik'}
    __bind_key__ = 'kotabogor'

    ogc_fid = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.Float(53))
    jenis_utam = db.Column(db.String(50))
    jenis_ = db.Column(db.String(50))
    kegiatan = db.Column(db.String(50))
    nama_objek = db.Column(db.String(100))

    def get_table_name(self):
        from sqlalchemy import inspect
        mapper = inspect(self)
        return mapper.tables[0].name


class GisBwk(db.Model):
    __tablename__ = 'gis_bwk'
    __table_args__ = {'schema': 'tematik'}
    __bind_key__ = 'kotabogor'

    id_4 = db.Column(db.Integer, primary_key=True,
                     server_default=db.FetchedValue())
    id_3 = db.Column(db.Integer)
    id_2 = db.Column(db.Integer)
    id_1 = db.Column(db.Integer)
    id_0 = db.Column(db.Integer)
    id = db.Column(db.Integer)
    kabupaten = db.Column(db.String(25))
    kecamatan = db.Column(db.String(50))
    kelurahan = db.Column(db.String(50))
    subbwk = db.Column(db.String(10))
    perimeter = db.Column(db.Float(53))
    area = db.Column(db.Float(53))
    acres = db.Column(db.Float(53))
    hectares = db.Column(db.Float(53))


class GisJenisTanah(db.Model):
    __tablename__ = 'gis_jenis_tanah'
    __table_args__ = {'schema': 'tematik'}
    __bind_key__ = 'kotabogor'

    id_2 = db.Column(db.Integer, primary_key=True,
                     server_default=db.FetchedValue())
    id_1 = db.Column(db.Integer)
    id_0 = db.Column(db.Integer)
    id = db.Column(db.Integer)
    gid = db.Column(db.Integer)
    jenis_tanah = db.Column(db.String(50))
    luas_ha = db.Column(db.Float(53))


class GisKelasLereng(db.Model):
    __tablename__ = 'gis_kelas_lereng'
    __table_args__ = {'schema': 'tematik'}

    id_2 = db.Column(db.Integer, primary_key=True,
                     server_default=db.FetchedValue())
    id_1 = db.Column(db.Integer)
    id_0 = db.Column(db.Integer)
    id = db.Column(db.Integer)
    gid = db.Column(db.Integer)
    kelerengan = db.Column(db.String(50))
    luas_ha = db.Column(db.Float(53))


class GisPenggunaanLahan(db.Model):
    __tablename__ = 'gis_penggunaan_lahan'
    __table_args__ = {'schema': 'tematik'}

    id_1 = db.Column(db.Integer, primary_key=True,
                     server_default=db.FetchedValue())
    id_0 = db.Column(db.Integer)
    id = db.Column(db.BigInteger)
    gid = db.Column(db.BigInteger)
    fid_admini = db.Column(db.Float(53))
    kabupaten = db.Column(db.String(25))
    kecamatan = db.Column(db.String(50))
    luas_ha = db.Column(db.Float(53))
    fid_penggu = db.Column(db.Float(53))
    objectid = db.Column(db.Float(53))
    shape_leng = db.Column(db.Float(53))
    shape_area = db.Column(db.Float(53))
    penggunaan = db.Column(db.String(50))
    luas_m = db.Column(db.Float(53))


class GisPenutupLahan(db.Model):
    __tablename__ = 'gis_penutup_lahan'
    __table_args__ = {'schema': 'tematik'}

    id_1 = db.Column(db.Integer, primary_key=True,
                     server_default=db.FetchedValue())
    id = db.Column(db.BigInteger)
    id_0 = db.Column(db.BigInteger)
    gid = db.Column(db.BigInteger)
    fid_gis_pe = db.Column(db.Float(53))
    pntp_lhn = db.Column(db.String(200))
    sumber = db.Column(db.String(200))
    fid_batas_ = db.Column(db.Float(53))
    kecamatan = db.Column(db.String(254))


class GisPersilTanah(db.Model):
    __tablename__ = 'gis_persil_tanah'
    __table_args__ = {'schema': 'tematik'}

    id_2 = db.Column(db.Integer, primary_key=True,
                     server_default=db.FetchedValue())
    id_1 = db.Column(db.Integer)
    id_0 = db.Column(db.Integer)
    id = db.Column(db.Integer)
    gid = db.Column(db.Integer)
    layer = db.Column(db.String(17))
    penggunaan = db.Column(db.String(254))
    tipehak = db.Column(db.String(254))
    tahun = db.Column(db.Float(53))


class GisPola(db.Model):
    __tablename__ = 'gis_pola'
    __table_args__ = {'schema': 'tematik'}

    id_3 = db.Column(db.Integer, primary_key=True,
                     server_default=db.FetchedValue())
    id_2 = db.Column(db.Integer)
    id_1 = db.Column(db.Integer)
    id_0 = db.Column(db.Integer)
    id = db.Column(db.Integer)
    fid_admini = db.Column(db.BigInteger)
    kabupaten = db.Column(db.String(25))
    kecamatan = db.Column(db.String(50))
    kelurahan = db.Column(db.String(50))
    rw = db.Column(db.String(20))
    rencana = db.Column(db.String(25))
    keterangan = db.Column(db.String(100))
    luas_m = db.Column(db.Float(53))


class GisSaranaPerkotaan(db.Model):
    __tablename__ = 'gis_sarana_perkotaan'
    __table_args__ = {'schema': 'tematik'}

    id_3 = db.Column(db.Integer, primary_key=True,
                     server_default=db.FetchedValue())
    id_2 = db.Column(db.Integer)
    id_1 = db.Column(db.Integer)
    id_0 = db.Column(db.Integer)
    id = db.Column(db.Integer)
    namaobj = db.Column(db.String(100))
    orde1 = db.Column(db.String(100))
    sumber = db.Column(db.String(100))
    lokasi = db.Column(db.String(100))


class GisStatusTanah(db.Model):
    __tablename__ = 'gis_status_tanah'
    __table_args__ = {'schema': 'tematik'}

    id_3 = db.Column(db.Integer, primary_key=True,
                     server_default=db.FetchedValue())
    id_2 = db.Column(db.Integer)
    id_1 = db.Column(db.Integer)
    id_0 = db.Column(db.Integer)
    id = db.Column(db.Integer)
    penggunaan = db.Column(db.String(254))
    tipehak = db.Column(db.String(254))
    tahun = db.Column(db.Float(53))


class GisTowerExisting(db.Model):
    __tablename__ = 'gis_tower_existing'
    __table_args__ = {'schema': 'tematik'}

    id_1 = db.Column(db.Integer, primary_key=True,
                     server_default=db.FetchedValue())
    id_0 = db.Column(db.Integer)
    id = db.Column(db.Integer)
    gid = db.Column(db.Integer)
    nomor = db.Column(db.String(50))


class GisTowerNew(db.Model):
    __tablename__ = 'gis_tower_new'
    __table_args__ = {'schema': 'tematik'}

    id_1 = db.Column(db.Integer, primary_key=True,
                     server_default=db.FetchedValue())
    id_0 = db.Column(db.Integer)
    id = db.Column(db.Integer)
    gid = db.Column(db.Integer)
    nomor = db.Column(db.String(50))
