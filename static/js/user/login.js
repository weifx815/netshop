/**
 * 用户注册模块
 */
$(document).ready(function(){
    loginBinOnclick();
    $("input").keyup(function(e){
        if(e.which=="13"){
            $("#gologin").click();
        }
    });
});
function loginBinOnclick(){
    $("#gologin").click(function(){
        if(validationFormObjects("loginForm")){
            $("#loginForm").submit();
        };
    });
}
