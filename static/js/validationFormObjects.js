//验证表单信息
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
            //验证密码必须字符与数字结合
            if(ctltype == "password" || verificationType== "useraccount"){
                let pw = /[A-Za-z].*[0-9]|[0-9].*[A-Za-z]/;
                if(!pw.test($.trim(ctl.value))){
                    $("#"+errorId).text(title+"格式不正确");
                    return false;
                }
            }
            //验证两次密码是否一致if(val.match())
            if(verificationType == "repeatPassword"){
                if(!passwordVerification()){
                    $("#"+errorId).text("两次密码不一致，请确认");
                    return false;
                }
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
    return true;
}