module.exports = {
    outputDir: '../static',
    indexPath: '../template/index.html',
    publicPath: process.env.NODE_ENV === 'production'
        ? '/static'
        : '/'
}