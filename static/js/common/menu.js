/**
 * 菜单操作相关模块
 */
$(document).ready(function(){
    $("#saveMenuForm").click(function(){
        $.ajax({
            type: 'post',
            url: '/common/menu/save/',
            data: $("#menuForm").serialize(),
            async: true,
            dataType: "JOSN",
            success: function(rdata) {

            },
            error:function (rdata){

            },
            complete:function (rdata){
                if(rdata.status==200){
                    fnCloseMenuIframe();
                    window.parent.location.reload();
                }else{
                    alert(rdata.error);
                }
            }
        });
    });
});
function fngotomenupage(){
    layer.open({
        id:1,
        type: 2,//iframe
        title: ['菜单添加', 'font-size:14px;font-weight:bold;'],
        shadeClose: false,
        shade: false,
        fixed: false,
        maxmin: true, //开启最大化最小化按钮
        area: ['600px','600px'],//弹出层宽度
        content: "/common/menu/save/",
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
function fnCloseMenuIframe(){
    let index = parent.layer.getFrameIndex(window.name); //获取窗口索引
    parent.layer.close(index);
};
