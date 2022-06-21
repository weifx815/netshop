/**
 * 用户注册模块
 */
$(document).ready(function(){
    registerBinOnclick();
    phoneCodeBinOnclick();
});

function registerBinOnclick(){
    $("#register").click(function(){
        let user_name = $("#user_name").val();
        validationFormObjects("registerForm");
    });
}
function validationFormObjects(formId) {
    let frmForm = document.getElementById(formId);
	for (let i = 0; i < frmForm.elements.length; i++) {
        let ctl = frmForm.elements[i];
        let name = ctl.name;
        let id = $(ctl).attr("id");
        let title = $(ctl).attr("title");
        let verificationType = $(ctl).attr("verificationtype");
        let minlength = $(ctl).attr("minlength");
        let maxlength = $(ctl).attr("maxlength");
        let errorId = id+"_error";
        let ctltype = $(ctl).attr("type").toLowerCase();
        if(ctltype != "hidden"){
            $("#"+errorId).text("");
            //验证不允许为空
            if($.trim(ctl.value) == ""){
                $("#"+errorId).text(title+"不允许为空");
                return false;
            }
            //验证长度
            if($.trim(ctl.value).length < minlength || $.trim(ctl.value).length > maxlength){
                $("#"+errorId).text(title+"长度应>="+minlength+"且<="+maxlength);
                return false;
            }
            //验证邮箱
            if(verificationType=="email" && !isEmail($.trim(ctl.value))){
                $("#"+errorId).text(title+"格式不正确");
                return false;
            }
            //验证手机号
            if(verificationType=="phonecode" && !isPhone($.trim(ctl.value))){
                $("#"+errorId).text(title+"格式不正确");
                return false;
            }
            //验证用户账号是否被注册
            if(verificationType=="useraccount" && ifRegister($.trim(ctl.value)) == 'Y'){
                $("#"+errorId).text(title+"已被注册");
                return false;
            }
            //验证手机号是否被注册
            if(verificationType=="phonecode" && ifRegister($.trim(ctl.value)) == 'Y'){
                $("#"+errorId).text(title+"已被注册");
                return false;
            }
            //验证邮箱是否被注册
            if(verificationType=="email" && ifRegister($.trim(ctl.value)) == 'Y'){
                $("#"+errorId).text(title+"已被注册,请重新输入");
                return false;
            }
        }
    }
    return false;
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
//获取手机验证码
let phoneCodeBinOnclick = function(){
    $("#getPhoneCode").click(function(){
        let phone_number = $("#phone_number").val();
        if(phone_number==""){
            $("#phone_number_error").text("手机号不允许为空");
            return false;
        }
        $.ajax({
            type: 'get',
            url: '/user/register/phonecode/',
            data: {'code': phone_number},
            async: false,
            success: function(rdata) {
                $("#phone_code").val(rdata);
                $("#getPhoneCode").text("60秒后重新获取验证码");
                $("#getPhoneCode").unbind();
                $("#phone_number_error").text("");
                return false;
            }
        });
    });
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
function aa(){
    $("#getPhoneCode").on('click', phoneCodeBinOnclick);
}