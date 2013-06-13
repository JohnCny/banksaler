function initTree(){
    var nodeId = 1;
    initTreeData();
    initGridData(nodeId);
}

function initTreeData(){
    function zTreeOnClick(event, treeId, treeNode) {
        var param = {
            "id":treeNode.id
        }
        var jsonparam = $.toJSON(param);
        $("#jsonparam",window.parent.document).attr("value",jsonparam);
            
        initGridData(treeNode.id);
    };
    
    var setting = {
        data: {
            simpleData: {
                enable: true
            }
        },
        callback: {
            onClick: zTreeOnClick
        }
    };
    
    var get = crud.dom.factory("GET");
    var url = "/orgnization/list";
    get.doGet(url,initTreeDataCallback,"机构树加载失败！");
    
    function initTreeDataCallback(json){
        var objs = $.evalJSON(json);
        objs.pop();
        var zNodes =[];
        
        for(var i in objs){
            zNodes.push({ id:objs[i].id, pId:objs[i].org_parent, name:objs[i].org_name,open:true}); 
        }
        $.fn.zTree.init($("#treeDemo"), setting, zNodes);
    }
}

function initGridData(id){
    $('#jgglTable').dataTable().fnClearTable();
    
    var get = crud.dom.factory("GET");
    var url = "/orgnization/" + id;
    get.doGet(url,initGridDataCallback,"获取机构列表失败！");
    
    function initGridDataCallback(json){
        var objs = $.evalJSON(json);
        var content;
        for(var i = 0;i<objs.length;i++){
            content  = '<div>'+
                '<a class="btn btn-info" href="javascript:void(0);" onclick="gotoBjgroup('+objs[i].id+','+objs[i].org_parent+')">'+
                    '<i class="icon-edit icon-white"></i>'+
                    '编辑'+                                            
                '</a>&nbsp;'+
                '<a class="btn btn-danger" href="javascript:void(0);" onclick="deleteGroup('+objs[i].id+')">'+
                    '<i class="icon-trash icon-white"></i>'+ 
                        '删除'+
                '</a>'+
            '</div>';
            
            $('#jgglTable').dataTable().fnAddData( [
                '<input type="checkbox" name="group_checkbox" onclick="changeColor(this)"/>',
                objs[i].id,
                objs[i].org_name,
                '类型未知',
                content
                ]
              );
        }
        window.parent.resizeFrame();
    }
}

function gotoNewgroup(){
    window.location.href = "new_group";
}

function gotoBjgroup(id,org_parent){
    var param = {
        "id":id,
        "org_parent":org_parent
    }
    var jsonparam = $.toJSON(param);
    $("#jsonparam",window.parent.document).attr("value",jsonparam);
    
    window.location.href = "bj_group";
}

function deleteGroup(id){
    var del = crud.dom.factory("DELETE");
    var url = "/orgnization/"+ id;
    del.doDelete(url,deleteGroupCallback,"删除失败！");
    
    function deleteGroupCallback(json){
        window.location.href = "jggl";
    }
}

function initGroupContent(){
    var param = $.evalJSON($("#jsonparam",window.parent.document).val());
    
    var get = crud.dom.factory("GET");
    var url = "/orgnization/"+ param.id;
    get.doGet(url,initGroupContentCallback,"加载机构信息失败！");
    
    function initGroupContentCallback(json){
        var objs = $.evalJSON(json);
        
        for(var i = 0;i<objs.length;i++){
          //$("#group-id").attr("value",obj.id);
            $("#org_name").attr("value",objs[i].org_name);
            //$("#group_level option[@value='"+obj.bs_group_level+"']").attr("selected","true");
            //$("#group_parent option[@value='"+obj.bs_group_level+"']").attr("selected","true");
        }
    }
}