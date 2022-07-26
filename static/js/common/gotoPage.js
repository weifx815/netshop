/**
 * 根据地址进入页面
 */
let titles = [
    '菜单信息',
    '角色信息',
    '系统码表信息'
]
function fnGotoPage(url,num){
    layer.open({
        id:num,
        type: 2,//iframe
        title: [titles[num], 'font-size:14px;font-weight:bold;'],
        shadeClose: false,
        shade: 0.5,
        fixed: false,
        maxmin: true, //开启最大化最小化按钮
        area: ['600px','400px'],//弹出层宽度
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
 * 删除操作
 */
let confirms = [
    '该删除会级联删除下级菜单，确定要删除？',
    '确定要删除？',
    '该删除会级联删除码表子项，确定要删除?'
]
function fnDelete(url,num){
    layer.confirm(confirms[num], {
          btn: ['确定','取消'] //按钮
        }, function(){
            $.ajax({
            type: 'get',
            url: url,
            async: true,
            dataType: "json",
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