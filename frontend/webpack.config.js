const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');
const webpack = require('webpack')

module.exports = {
  entry: {
    app: {
      import:"./src/index.js",
      // dependOn: 'vendors'
    },
    // "vendors": ["ol", 'axios']
  },
  mode: 'production',
  // devtool: "inline-source-map",
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader",]  ,
      },
    ],
  },
  resolve: {
    extensions: [".tsx", ".ts", ".js"],
  },
  output: {
    filename: "[name].js",
    path: path.resolve(__dirname, "public"),
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: "./src/index.html",
      scripts: ['cesium/Cesium.js']

    }),
    new MiniCssExtractPlugin(),
  ],
  devServer: {
    contentBase: path.join(__dirname, 'public'),
    compress: true,
    port: 9000
  },
  optimization:{
    runtimeChunk: "single",
    splitChunks: {
      chunks: 'all',
      maxInitialRequests: Infinity,
      minSize: 0,
      // cacheGroups:{
      //   vendor:{
      //     test: /[\\/]node_modules[\\/]/,
      //     name(module){
      //       const packageName = module.context.match(/[\\/]node_modules[\\/](.*?)([\\/]|$/)[1];
      //       return `npm.${packageName.replace('@', '')}`;
      //     }
      //   }
      // }
      
    }
  }
  // minimizer: [
  //   new UglifyJSPlugin({
  //     uglifyOptions: {
  //       sourceMap: true,
  //       compress: {
  //         drop_console: true,
  //         conditionals: true,
  //         unused: true,
  //         comparisons: true,
  //         dead_code: true,
  //         if_return: true,
  //         join_vars: true,
  //         warnings: false
  //       },
  //       output: {
  //         comments: false
  //       }
  //     }
  //   })
  // ]

};
