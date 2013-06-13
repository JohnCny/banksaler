function getAllDevice(){
    var get = crud.dom.factory("GET");
    var url = "http://127.0.0.1:8000/ws/device/?format=json&username=test&api_key=1234567890test";
    get.doGet(url,getAllDeviceCallback,"获取设备列表失败！");
    
    function getAllDeviceCallback(json){
        var objs = $.evalJSON(json).objects;
        for(var i in objs){
            var jdata = {id:objs[i].id,mobile:objs[i].mobile,user_code:objs[i].user_code,resource_uri:objs[i].resource_uri};
            
            $('#sbglTable').dataTable().fnAddData( [
              '<input type="checkbox" name="device_checkbox" onclick="changeColor(this)"/>',
              objs[i].id,
              '123',
              $("#sbglTr").tmpl(jdata).html()
              ]
            );
            
            window.parent.resizeFrame();
        }
    }
}

function gotoNewdevice(){
    window.location.href = "new-device";
}

function gotoBjdevice(id){
    var param = {
        "id":id
    }
    var jsonparam = $.toJSON(param);
    $("#jsonparam",window.parent.document).attr("value",jsonparam);
    
    window.location.href = "bj-device";
}

function initDeviceContent(){
    var param = $.evalJSON($("#jsonparam",window.parent.document).val());
    var get = crud.dom.factory("GET");
    var url = "http://127.0.0.1:8000/ws/device/"+param.id+"/?format=json&username=test&api_key=1234567890test";
    get.doGet(url,initDeviceContentCallback,"加载设备信息失败！");
    
    function initDeviceContentCallback(json){
        var obj = $.evalJSON(json);
        
        $("#device_code").attr("value",obj.device_code);
    }
}

function deleteDevice(id){
    var data = JSON.stringify({
        "id": id,
    });
    var del = crud.dom.factory("DELETE");
    var url = "http://127.0.0.1:8000/ws/device/?format=json&username=test&api_key=1234567890test";
    del.doDelete(url,deleteDeviceCallback,"删除失败！");
    
    function deleteDeviceCallback(json){
        window.location.href = "sbgl";
    }
}