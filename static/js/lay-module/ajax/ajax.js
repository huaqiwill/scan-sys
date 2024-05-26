layui.define(['jquery'], function (exports) {
    let $ = layui.jquery;

    let ajaxModule = {
        setup(token) {
            $.ajaxSetup({
                headers: { 'X-CSRFTOKEN': `${token}` },// 这里是headers，不是data,  CSRF
                error: function (xhr, status, error) {
                    layer.msg("接口错误！！", { icon: 2 });
                },
                complete: function (XMLHttpRequest, textStatus) { //登陆超时跳转
                    if (textStatus === "parsererror") {
                        layer.msg('登陆过期, 请重新登陆', { icon: 2, time: 2000 }, function () {
                            window.location.href = '/';
                        })
                    } else if (textStatus === "error") {
                        $.messager.alert('提示信息', "请求超时！请稍后再试！", 'info');
                    }
                }
            });
        },
        get: function (url, params, successCallback) {
            $.ajax({
                type: 'GET',
                url: url,
                data: params,
                success: successCallback
            });
        },
        post: function (url, params, successCallback) {
            $.ajax({
                type: 'POST',
                url: url,
                data: params,
                success: successCallback
            });
        }
    };

    //输出模块
    exports('ajax', ajaxModule);
});
