/**
 * 菜单操作相关模块
 */
$(document).ready(function(){
    $("#saveMenuForm").click(function(){
        let url = '/common/menu/'+$("#form_type").val()+'/'+$("#obj").val()+"";
        $.ajax({
            type: 'post',
            url: url,
            data: $("#menuForm").serialize(),
            async: true,
            dataType: "json",
            success: function(rdata) {

            },
            error:function (rdata){

            },
            complete:function (rdata){
                if(rdata.status==200){
                    fnCloseIframe();
                    window.parent.location.reload();
                }else{
                    layer.msg('提示：操作失败', {icon: 5});
                }
            }
        });
    });
});
