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
                    layer.msg('提示：操作失败', {icon: 5});
                }
            }
        });
    });
});

/**
 * 进入菜单信息页面
 */
function fngotomenupage(type,code){
    let url = '/common/menu/'+type+'/'+code;
    layer.open({
        id:1,
        type: 2,//iframe
        title: ['菜单信息', 'font-size:14px;font-weight:bold;'],
        shadeClose: false,
        shade: 0.5,
        fixed: false,
        maxmin: true, //开启最大化最小化按钮
        area: ['600px','600px'],//弹出层宽度
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
function fnCloseMenuIframe(){
    let index = parent.layer.getFrameIndex(window.name); //获取窗口索引
    parent.layer.close(index);
};

/**
 * 删除菜单
 */
function fnDeleteMenu(type, code){
    let url = '/common/menu/'+type+'/'+code;
    layer.confirm('该删除会级联删除下级菜单，确定要删除？', {
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