layui.define(['jquery'], function (exports) {
    let $ = layui.jquery;

    let ajaxModule = {
        setToken: function (token) {
            $.ajaxSetup({
                headers: {'X-CSRFTOKEN': `${token}`}, // 这里是headers，不是data,  CSRF
            });
        },
        get: function (url, params, successCallback) {
            $.ajax({
                type: 'GET',
                url: url,
                data: params,
                success: successCallback,
                error: function (result) {
                    layer.msg("接口错误！！", {icon: 2});
                }
            });
        },
        post: function (url, params, successCallback) {
            $.ajax({
                type: 'POST',
                url: url,
                data: params,
                success: successCallback,
                error: function () {
                    layer.msg("接口错误！！", {icon: 2});
                }
            });
        }
    };

    //输出模块
    exports('ajax', ajaxModule);
});
