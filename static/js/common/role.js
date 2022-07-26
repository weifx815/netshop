/**
 * 菜单操作相关模块
 */
$(document).ready(function(){
    $("#saveRoleForm").click(function(){
        let url = '/common/role/'+$("#form_type").val()+'/'+$("#obj").val()+"";
        if(validationFormObjects("roleForm")){
            $.ajax({
                type: 'post',
                url: url,
                data: $("#roleForm").serialize(),
                async: true,
                dataType: "json",
                success: function(rdata) {

                },
                error:function (rdata){

                },
                complete:function (rdata){
                    let obj = JSON.parse(rdata.responseText);
                    if(obj.status==true){
                        fnCloseIframe();
                        window.parent.location.reload();
                    }else if (obj.status==false){
                        let errors = obj.errors;
                        for(let key in errors){
                            $("#"+key+"_error").text(errors[key])
                        }
                        layer.msg('提示：验证失败', {icon: 5});
                    }else{
                        layer.msg('提示：操作失败', {icon: 5});
                    }
                }
            });
        }
    });
    $("#submitUseRoleForm").click(function(){
        let url = '/common/role/'+$("#form_type").val()+'/'+$("#obj").val()+"/";
        let roles = $("input[type=checkbox][name=role]:checked").length;
        if(roles==0){
            $("#role_error").text("提示：请选择角色");
            return;
        }
        $.ajax({
            type: 'post',
            url: url,
            data: $("#UserRoleForm").serialize(),
            async: true,
            dataType: "json",
            success: function(rdata) {

            },
            error:function (rdata){

            },
            complete:function (rdata){
                let obj = JSON.parse(rdata.responseText);
                if(obj.status==true){
                    fnCloseIframe();
                    window.parent.location.reload();
                }else if (obj.status==false){
                    let errors = obj.errors;
                    for(let key in errors){
                        $("#"+key+"_error").text(errors[key])
                    }
                    layer.msg('提示：验证失败', {icon: 5});
                }else{
                    layer.msg('提示：操作失败', {icon: 5});
                }
            }
        });
    });
});