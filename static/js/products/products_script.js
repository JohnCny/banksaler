//function GetQueryString(name) {
//    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)","i");
//    var r = window.location.search.substr(1).match(reg);
//    if (r!=null) return unescape(r[2]); return null;
//}
 
function getCpList(){
    var param = $.evalJSON($("#jsonparam",window.parent.document).val());
    $("#productTypeNameHref").html(param.productTypeName);
    $("#productTypeNameH2").html('<i class="icon-info-sign" ></i>'+param.productTypeName);
    
    var get = crud.dom.factory("GET");
    var url = wsProduct + "/?product_type="+param.productType;
    get.doGet(url,getCpListCallback,"加载产品列表信息失败！");
    
    function getCpListCallback(json){
        var objs = $.evalJSON(json);
        objs.pop();//删除json中最后一项:页数{pages:5}
        for(var i = 0;i<objs.length;i++){
            var content = '<div class="img_box">'+
                                    '<a href="javascript:void(0);" onclick="gotoCpzs('+objs[i].id+')" class="thumbnail">'+
                                '<img src="'+wsHost + filePath + objs[i].product_img+'" />'+
                                    '<h3>'+objs[i].product_name+'</h3>'+
                            '</a>'+
                        '</div>';
            $(content).appendTo("#cpzsul");
        }
        window.parent.resizeFrame();
    }
}

function gotoCpzs(id){
    var param = {
        "id":id
    }
    var jsonparam = $.toJSON(param);
    $("#jsonparam",window.parent.document).attr("value",jsonparam);
    window.location.href = "cpzs";
}

function getCpDetail(){
    var param = $.evalJSON($("#jsonparam",window.parent.document).val());
    
    var get = crud.dom.factory("GET");
    var url = wsProduct + "/" + param.id;
    get.doGet(url,getCpDetailCallback,"加载产品信息失败！");
    
    function getCpDetailCallback(json){
        var objs = $.evalJSON(json);
        for(var i = 0;i<objs.length;i++){
            if(objs[i].product_img != ''){
                var content = "<div style='width:30%;'>"+
                "<img id='img-text' src='"+wsHost + filePath + objs[i].product_img+"' style='width:100%;height:100%;'/>"+
                "</div>"+
                "<div style='width:68%'>"+
                    "<h4 class='help'><strong>产品描述：</strong></h4>"+
                    "<span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+objs[i].product_describe+"<span>"+
                "</div>"+
                "<div style='width:99%;'>"+    
                    "<h4 class='help'><strong>产品特点：</strong></h4>"+
                    "<ul>"+
                    "<li>收益固定、保本保息</li>"+
                    "<li>稳健型配置必选 收益率高，是银行同期定存的数倍</li>"+
                    "<li>运作期限明确，便于安排资金使用计划 </li>"+
                    "<li>信托财产独立，不受信托公司影响，可用于抵押保管银行开设专户、专款专用 保管银行开设专户、专款专用 </li>"+
                "</ul>"+
                "</div>";
                $(content).appendTo("#cpzsContent");
            }
            else{
                var content = "<div style='width:99%'>"+
                    "<h4 class='help'><strong>产品描述：</strong></h4>"+
                    "<span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+objs[i].product_describe+"<span>"+
                "</div>"+
                "<div style='width:99%;'>"+    
                    "<h4 class='help'><strong>产品特点：</strong></h4>"+
                    "<ul>"+
                        "<li>收益固定、保本保息</li>"+
                        "<li>稳健型配置必选 收益率高，是银行同期定存的数倍</li>"+
                        "<li>运作期限明确，便于安排资金使用计划 </li>"+
                        "<li>信托财产独立，不受信托公司影响，可用于抵押保管银行开设专户、专款专用 保管银行开设专户、专款专用 </li>"+
                    "</ul>"+
                "</div>";
                $(content).appendTo("#cpzsContent");
            }
        }
        window.parent.resizeFrame();
    }
}

function getAllCp(){
    $.ajax({
        url:wsHost + wsProductType,
        type: "GET",
        timeout: 5000,
        dataType:'text',
        success: function (json) {
            var objCplx = $.evalJSON(json);
            for(var i = 0;i<objCplx.length;i++){
                $.ajax({
                    url:wsHost + wsProduct + "/?product_type="+objCplx[i].id,
                    type: "GET",
                    timeout: 5000,
                    dataType:'text',
                    success: function (json1) {
                        var objs = $.evalJSON(json1);
                        objs.pop();
                        for(var j = 0;j<objs.length;j++){
                            var content = "<div>"+
                                "<a class='btn btn-success' href='javascript:void(0);' onclick='gotoCpzs("+objs[j].id+");'>"+
                                    "<i class='icon-zoom-in icon-white'></i>  "+
                                        "查看"+                                       
                                "</a>&nbsp;"+
                                "<a class='btn btn-info' href='javascript:void(0);' onclick='gotoBjproduct("+objs[j].id+");'>"+
                                    "<i class='icon-edit icon-white'></i>"+  
                                        "编辑"+                                            
                                "</a>&nbsp;"+
                                "<a class='btn btn-danger' href='javascript:void(0);' onclick='deleteCP("+objs[j].id+")'>"+
                                    "<i class='icon-trash icon-white'></i>"+ 
                                        "删除"+
                                "</a>"+
                            "</div>";
                            $('#cpTable').dataTable().fnAddData( [
                              '<input type="checkbox" name="product_checkbox" onclick="changeColor(this)"/>',
                              objs[j].product_name,
                              '111',
                              objs[j].product_create_date,
                              '222',
                              //$("#cpbjTr").tmpl(jdata).html()
                              content
                              ]
                            );
                            
                            window.parent.resizeFrame();
                        }
                    },
                    error: function(xhr){
                        
                    }
                 });
            }
        },
        error: function(xhr){
        }
    });
}

function gotoNewproduct(){
    window.location.href = "new_product";
}

function gotoBjproduct(id){
    var param = {
        "id":id
    }
    var jsonparam = $.toJSON(param);
    $("#jsonparam",window.parent.document).attr("value",jsonparam);
    
    window.location.href = "bj_product";
}

function initProductContent(){
    var param = $.evalJSON($("#jsonparam",window.parent.document).val());
    
    var get = crud.dom.factory("GET");
    var url = wsProduct + "/" + param.id;
    get.doGet(url,initProductContentCallback,"加载产品信息失败！");
    
    function initProductContentCallback(json){
        var objs = $.evalJSON(json);
        for(var i = 0;i<objs.length;i++){
            $("#product_name").attr("value",objs[i].product_name);
            $("#product_type_id").val(objs[i].product_type);
            $("#product_type_id").trigger("liszt:updated");
            $("#product_img_url").attr("value",objs[i].product_img);
            if(objs[i].product_img != ""){
                $("#product_img_information").text("图片已上传");
                $("#product_img_information").attr("class","label label-success");
            }
            else{
                $("#product_img_information").text("图片未上传");
                $("#product_img_information").attr("class","label label-important"); 
            }
            $("#product_beg_date").attr("value",objs[i].product_beg_date);
            $("#product_end_date").attr("value",objs[i].product_end_date);
            
            var o = $("#product_describe").cleditor()[0];
            $("#product_describe").val(objs[i].product_describe);
            o.updateFrame();
        }
     
    }
}


function deleteCP(id){
    var del = crud.dom.factory("DELETE");
    var url = wsProduct + "/" + id;
    del.doDelete(url,deleteCPCallback,"删除失败！");
    
    function deleteCPCallback(json){
        window.location.href = "cpbj";
    }
}