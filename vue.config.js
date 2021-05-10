module.exports = {
    devServer: {
        // host: '47.117.66.221'
        port: 8080
    },
    // 适配移动端(目前觉得没什么用)
    css: {
        loaderOptions: {
            css: {},
            postcss: {
                plugins: [
                    require('postcss-px2rem')({
                        remUnit: 75
                    })
                ]
            }
        }
    },
}