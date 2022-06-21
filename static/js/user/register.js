/**
 * 用户注册模块
 */
$(document).ready(function(){
    registerBinOnclick();
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
        let verificationtype = $(ctl).attr("verificationtype");
        let errorid = id+"_error";
        let ctltype = $(ctl).attr("type").toLowerCase();
        if(ctltype != "hidden"){
            $("#"+errorid).text("");
            //验证不允许为空
            if($.trim(ctl.value) == ""){
                $("#"+errorid).text(title+"不允许为空");
                return false;
            }
            //验证长度
            let minlength = $(ctl).attr("minlength");
            let maxlength = $(ctl).attr("maxlength");
            if($.trim(ctl.value).length < minlength || $.trim(ctl.value).length > maxlength){
                $("#"+errorid).text(title+"长度应>="+minlength+"且<="+maxlength);
                return false;
            }
            //验证邮箱
            if(verificationtype=="email" && !isEmail($.trim(ctl.value))){
                $("#"+errorid).text(title+"格式不正确");
                return false;
            }
            //验证手机号
            if(verificationtype=="phonecode" && !isEmail($.trim(ctl.value))){
                $("#"+errorid).text(title+"格式不正确");
                return false;
            }
        }
    }
    return false;
}

function aa(){
    $.ajax({
            type: 'post',
            url: '/user/register/',
            data: $("#registerForm").serialize(),
            success: function(data) {
                // your code
            }
        });
}
//验证邮箱是否正确
function isEmail(email){
    let szReg=/^[A-Za-zd]+([-_.][A-Za-zd]+)*@([A-Za-zd]+[-.])+[A-Za-zd]{2,5}$/;
    let bChk=szReg.test(email);
    return bChk;
}
//验证手机号码是否正确
function isPhone(code){
    let szReg=/^1[0-9]{10}$/;
    let bChk=szReg.test(code);
    return bChk;
}
