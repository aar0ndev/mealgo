module.exports = {
  devServer: {
    host: '0.0.0.0',
    proxy: {
      '^/api': {
        target: 'http://localhost:8080/',
        ws: true,
        changeOrigin: true
      }
    }
  },
  chainWebpack: config => {
    config.module
      .rule('svg')
      .resourceQuery(/url/)
      .end()

    config.module
      .rule('svg-inline')
      .test(/\.(svg)(\?.*)?$/)
      .resourceQuery(/inline/)
      .use('svg-inline-loader')
      .after('file-loader')
      .loader('svg-inline-loader')
      .end()
  }
}
