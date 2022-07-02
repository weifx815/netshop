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
                dataType: "JOSN",
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
});

/**
 * 进入菜单信息页面
 */
function fngotorolepage(type,code){
    let url = '/common/role/'+type+'/'+code;
    layer.open({
        id:2,
        type: 2,//iframe
        title: ['角色信息', 'font-size:14px;font-weight:bold;'],
        shadeClose: false,
        shade: 0.5,
        fixed: false,
        maxmin: true, //开启最大化最小化按钮
        area: ['600px','450px'],//弹出层宽度
        content: url,
        offset:'40px',//弹出层位置离顶100px
        success:function(index, layero){
        },
        cancel: function(index, layero){
            layer.close(index);//需要手动关闭窗口
        },
        end:function(index, layero){
            layer.close(index);//需要手动关闭窗口
        }
    });
}
//关闭iframe
function fnCloseIframe(){
    let index = parent.layer.getFrameIndex(window.name); //获取窗口索引
    parent.layer.close(index);
};

/**
 * 删除菜单
 */
function fnDeleteRole(type, code){
    let url = '/common/role/'+type+'/'+code;
    layer.confirm('确定要删除？', {
          btn: ['确定','取消'] //按钮
        }, function(){
            $.ajax({
            type: 'get',
            url: url,
            async: true,
            dataType: "JOSN",
            success: function(rdata) {

            },
            error:function (rdata){
                layer.msg('提示：删除失败', {icon: 5});
            },
            complete:function (rdata){
                if(rdata.status==200){
                    layer.msg('提示：删除成功', {icon: 1});
                    window.parent.location.reload();
                }else{
                    layer.msg('提示：删除失败', {icon: 5});
                }
            }
        });
        }, function(){
          //取消操作
        });
}