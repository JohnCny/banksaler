function getAllUser(){
    var get = crud.dom.factory("GET");
    var url = "http://127.0.0.1:8000/ws/user/?format=json&username=test&api_key=1234567890test";
    get.doGet(url,getAllUserCallback,"获取用户列表失败！");
    
    function getAllUserCallback(json){
        var objs = $.evalJSON(json).objects;
        for(var i in objs){
            var jdata = {id:objs[i].id,mobile:objs[i].mobile,user_code:objs[i].user_code,resource_uri:objs[i].resource_uri};
            
            $('#yhTable').dataTable().fnAddData( [
              '<input type="checkbox" name="user_checkbox" onclick="changeColor(this)"/>',
              objs[i].user_code,
              '111',
              '222',
              '333',
              
              $("#yhglTr").tmpl(jdata).html()
              ]
            );
            
            window.parent.resizeFrame();
        }
    }
}

function gotoNewuser(){
    window.location.href = "new-user";
}

function gotoBjuser(id){
    var param = {
        "id":id
    }
    var jsonparam = $.toJSON(param);
    $("#jsonparam",window.parent.document).attr("value",jsonparam);
    
    window.location.href = "bj-user";
}

function initUserContent(){
    var param = $.evalJSON($("#jsonparam",window.parent.document).val());
    var get = crud.dom.factory("GET");
    var url = "http://127.0.0.1:8000/ws/user/"+param.id+"/?format=json&username=test&api_key=1234567890test";
    get.doGet(url,initUserContentCallback,"加载用户信息失败！");
    
    function initUserContentCallback(json){
        var obj = $.evalJSON(json);
        
        $("#id").attr("value",obj.id);
        $("#mobile").attr("value",obj.mobile);
    }
}

function deleteUser(id){
    var data = JSON.stringify({
        "user_id": id,
    });
    var del = crud.dom.factory("DELETE");
    var url = "http://127.0.0.1:8000/ws/user/?format=json&username=test&api_key=1234567890test";
    del.doDelete(url,deleteUserCallback,"删除失败！");
    
    function deleteUserCallback(json){
        window.location.href = "yhgl";
    }
}

function resetPwd(id){
    
}