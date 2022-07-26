/**
 * 菜单操作相关模块
 */
$(document).ready(function(){
    $("#saveForm").click(function(){
        let url = '';
        $.ajax({
            type: 'post',
            url: url,
            data: $("#form").serialize(),
            async: true,
            dataType: "json",
            success: function(rdata) {},
            error:function (rdata){},
            complete:function (rdata){
                let obj = JSON.parse(rdata.responseText);
                    if(obj.status==true){
                        fnCloseIframe();
                        window.parent.location.reload();
                    }else if (obj.status==false){
                        layer.msg('提示：验证失败', {icon: 5});
                        let errors = obj.errors;
                        for(let key in errors){
                            $("#"+key+"_error").text(errors[key])
                        }
                    }else{
                        layer.msg('提示：操作失败', {icon: 5});
                    }
            }
        });
    });
});
