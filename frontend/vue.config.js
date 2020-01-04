module.exports = {
  devServer: {
    host: '0.0.0.0'
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
