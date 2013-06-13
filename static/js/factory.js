/**
 * 工厂模式
 */
var crud = crud || {};
crud.dom = crud.dom || {};

//带auth的GET
crud.dom.GETAuth = function() {
    this.doGetAuth = function(url,auth,callback,errorMsg) {
        $.ajax({
            url : wsHost + url,
            type : "GET",
            timeout : 5000,
            dataType : 'text',
            beforeSend : function(req) {
                req.setRequestHeader('Authorization', auth);
            },
            success : function(json) {
                //回调
                callback(json);
            },
            error : function(e,xhr,opt) {
                // 请求出错处理
                //alert("请求出错(请检查网络连接.)");
                alert(errorMsg);
            }
        });
    };
};

// 子函数1：GET--获取
crud.dom.GET = function() {
    this.doGet = function(url, callback,errorMsg) {
        $.ajax({
            url : wsHost + url,
            type : "GET",
            timeout : 5000,
            dataType : 'text',
            success : function(json) {
                //回调
                callback(json);
            },
            error : function(xhr) {
                // 请求出错处理
                //alert("请求出错(请检查网络连接.)");
                alert(errorMsg);
            }
        });
    };
};

// 子函数2：POST--添加
crud.dom.POST = function() {
    this.doPost = function(url,data,callback,errorMsg) {
        $.ajax({
            url : wsHost + url,
            type : "POST",
            timeout : 5000,
            data: data,
            dataType : 'text',
            success : function(json) {
                //回调
                callback(json);
            },
            error : function(xhr) {
                // 请求出错处理
                //alert("请求出错(请检查网络连接.)");
                alert(errorMsg);
            }
        });
    };
};

// 子函数3：PUT--更新
crud.dom.PUT = function() {
    this.doPut = function(url,data,callback,errorMsg) {
        $.ajax({
            url : wsHost + url,
            type : "PUT",
            timeout : 5000,
            data: data,
            dataType : 'text',
            success : function(json) {
                //回调
                callback(json);
            },
            error : function(xhr) {
                // 请求出错处理
                //alert("请求出错(请检查网络连接.)");
                alert(errorMsg);
            }
        });
    };
};

//子函数4：DELETE--删除
crud.dom.DELETE = function() {
    this.doDelete = function(url,callback,errorMsg) {
        $.ajax({
            url : wsHost + url,
            type : "DELETE",
            timeout : 5000,
            dataType : 'text',
            success : function(json) {
                //回调
                callback(json);
            },
            error : function(xhr) {
                // 请求出错处理
                //alert("请求出错(请检查网络连接.)");
                alert(errorMsg);
            }
        });
    };
};

//上传方法
crud.dom.UPLOAD = function() {
    this.doUpload = function(type,obj,callback,errorMsg) {
        var url;
        if(type == "img"){
            url = wsHost + wsImg + "?file_path=" + obj.value;
        }
        else if(type == "file"){
            url = wsHost + wsFile + "?file_path=" + obj.value;
        }
        else if(type == "Video"){
            url = wsHost + wsVideo + "?file_path=" + obj.value;
        }
        else if(type == "Voice"){
            url = wsHost + wsVoice + "?file_path=" + obj.value;
        }
        
        $.ajaxFileUpload
        ({
            url:url, 
            secureuri:false,
            fileElementId:obj.id,
            dataType: 'xml',
            success: function (data)
            {
                callback($(data).text());
            },
            error: function (data, status, e)
            {
                alert(errorMsg);
            }
        });
        
    };
};

// 工厂方法接口
// [javascript]
crud.dom.factory = function(operation) {
    return new crud.dom[operation];
}