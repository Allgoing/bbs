$(function () {
    $("#submit").click(function (event) {
        event.preventDefault();

        var oldpwdE = $("input[name=oldpwd]");
        var newpwdE = $("input[name=newpwd]");
        var newpwdE2 = $("input[name=newpwd2]");

        var oldpwd = oldpwdE.val();
        var newpwd = newpwdE.val();
        var newpwd2 = newpwdE2.val();

        zlajax.post({
            'url': '/cms/resetpwd',
            'data':{
                'oldpwd': oldpwd,
                'newpwd': newpwd,
                'newpwd2': newpwd2
            },
            'success': function (data) {
                if(data['code'] == 200){
                    zlalert.alertSuccessToast("恭喜！密码修改成功")
                    oldpwdE.val("")
                    newpwdE.val("")
                    newpwdE2.val("")
                }
                else{
                    var message = data['message'];
                    zlalert.alertInfo(message);
                }
            },
            'fail': function (error) {
                zlalert.alertNetworkError("网络错误！")
            }
        });
    });
});