/**
 * 用户注册模块
 */
$(document).ready(function(){
    registerBinOnclick();
    $("#getPhoneCode").click(getPhoneCode);
});

function registerBinOnclick(){
    $("#register").click(function(){
        if(validationFormObjects("registerForm")){
            $.ajax({
                type: 'post',
                url: '/user/register/',
                data: $("#registerForm").serialize(),
                async: true,
                dataType: "JOSN",
                success: function(rdata) {
                    if(rdata.status){
                        location.href = rdata.url
                    }else{
                        alert(rdata.error);
                    }
                }

            });
        };
    });
}
//验证是否被注册
function ifRegister(code){
    let flag = "N"
    $.ajax({
            type: 'get',
            url: '/user/register/validation/',
            data: {'code': code},
            async: false,
            success: function(rdata) {
                flag = rdata;
            }
        });
    return flag;
}
//验证邮箱是否正确
function isEmail(email){
    let szReg=/^[a-z0-9A-Z]+@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\.)+[a-z]{2,}$/;
    let bChk=szReg.test(email);
    return bChk;
}
//验证手机号码是否正确
function isPhone(code){
    let szReg=/^1[0-9]{10}$/;
    let bChk=szReg.test(code);
    return bChk;
}
//获取手机验证码
function getPhoneCode(){
    let phone_number = $("#phone_number").val();
    if(phone_number==""){
        $("#phone_number_error").text("手机号不允许为空");
        return false;
    }
        $.ajax({
            type: 'get',
            url: '/user/register/phonecode/',
            data: {'code': phone_number},
            success: function(rdata) {
                $("#phone_code").val(rdata);
                countDown();
                return false;
            },
            error:function (rdata){
                $("#phone_number_error").text("系统出错了，请重新获取");
            }
        });
}
//每1秒执行函式countDown()
function countDown(){
    $("#getPhoneCode").off('click',getPhoneCode);
    $("#getPhoneCode").prop("disabled",true);
    $("#getPhoneCode").css("cursor","not-allowed");
    $("#phone_number_error").text("");
    let times = 60;
    let times_0 = setInterval(function (){
        times = times - 1;
        if(times>0){
            $("#getPhoneCode").text(times+" 秒后重新获取验证码");
        }else{
            clearInterval(times_0);
            $("#getPhoneCode").click(getPhoneCode);
            $("#getPhoneCode").prop("disabled",false);
            $("#getPhoneCode").text("点击获取手机验证码");
            $("#getPhoneCode").css("cursor","pointer");
        }
    },1000)
}
//判断密码是否一致
function passwordVerification(){
    let password = $("#password").val();
    let repeatPassword = $("#repeatPassword").val();
    if(password != repeatPassword){
        return false;
    }
    return true;
}