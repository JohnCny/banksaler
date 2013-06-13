function getAllSaler(){
    var get = crud.dom.factory("GET");
    var url = "/saler/list";
    get.doGet(url,getAllSalerCallback,"获取商户列表失败！");
    
    function getAllSalerCallback(json){
        var objs = $.evalJSON(json);
        objs.pop();
        for(var i=0;i<objs.length;i++){
            //var jdata = {id:objs[i].id,company_name:objs[i].company_name,company_addr:objs[i].company_addr};
            var content = '<div>'+
            '<a class="btn btn-info" href="javascript:void(0);" onclick="gotoBjsaler('+objs[i].id+');">'+
            '<i class="icon-edit icon-white"></i>'+  
            '编辑'+                                            
            '</a>&nbsp;'+
            '<a class="btn btn-danger" href="javascript:void(0);" onclick="deleteSaler('+objs[i].id+');">'+
            '<i class="icon-trash icon-white"></i>'+ 
            '删除'+
            '</a>'+
            '</div>';
            
            $('#shTable').dataTable().fnAddData( [
              '<input type="checkbox" name="saler_checkbox" onclick="changeColor(this)"/>',
              objs[i].id,
              objs[i].company_name,
              objs[i].company_addr,
              objs[i].company_manager,
              content
              ]
            );
            
            window.parent.resizeFrame();
        }
    }
}

function gotoNewSaler(){
    window.location.href = "new_sale";
}

function gotoBjsaler(id){
    var param = {
        "id":id
    }
    var jsonparam = $.toJSON(param);
    $("#jsonparam",window.parent.document).attr("value",jsonparam);
    
    window.location.href = "bj_sale";
}

function deleteSaler(id){
    var del = crud.dom.factory("DELETE");
    var url = "/saler/" + id;
    del.doDelete(url,deleteSalerCallback,"删除失败！");
    
    function deleteSalerCallback(json){
        window.location.href = "shgl";
    }
}

function initSalerContent(){
    var param = $.evalJSON($("#jsonparam",window.parent.document).val());
    var get = crud.dom.factory("GET");
    var url = "/saler/" + param.id;
    get.doGet(url,initSalerContentCallback,"加载商户信息失败！");
    
    function initSalerContentCallback(json){
        var obj = $.evalJSON(json);
        
        for(var i = 0;i<obj.length;i++){
            $("#company_name").attr("value",obj[i].company_name);
            $("#company_manager").attr("value",obj[i].company_manager);
            $("#company_addr").attr("value",obj[i].company_addr);
            $("#main_operating_range_id").attr("value",obj[i].main_operating_range_id);
            $("#main_operating_range_id").trigger("liszt:updated");
            $("#staff_amount").attr("value",obj[i].staff_amount);
            $("#last_year_operating").attr("value",obj[i].last_year_operating);
            $("#main_bank").attr("value",obj[i].main_bank);
            $("#saler_opinion").attr("value",obj[i].saler_opinion);
            if(obj[i].is_customer == false){
                $("#no1").click();
            }
            if(obj[i].is_credit_customer == false){
                $("#no2").click();
            }
            
        }
    }
}

//customer
function getAllCustomer(){
    var get = crud.dom.factory("GET");
    var url = "/customer/list";
    get.doGet(url,getAllCustomerCallback,"获取商户列表失败！");
    
    function getAllCustomerCallback(json){
        var objs = $.evalJSON(json);
        objs.pop();
        for(var i=0;i<objs.length;i++){
            //var jdata = {id:objs[i].id,company_name:objs[i].company_name,company_addr:objs[i].company_addr};
            var content = '<div>'+
            '<a class="btn btn-info" href="javascript:void(0);" onclick="gotoBjCustomer('+objs[i].id+');">'+
            '<i class="icon-edit icon-white"></i>'+  
            '编辑'+                                            
            '</a>&nbsp;'+
            '<a class="btn btn-danger" href="javascript:void(0);" onclick="deleteCustomer('+objs[i].id+');">'+
            '<i class="icon-trash icon-white"></i>'+ 
            '删除'+
            '</a>'+
            '</div>';
            
            $('#shTable').dataTable().fnAddData( [
              '<input type="checkbox" name="customer_checkbox" onclick="changeColor(this)"/>',
              objs[i].customer_number,
              objs[i].company_name,
              objs[i].company_manager,
              content
              ]
            );
            
            window.parent.resizeFrame();
        }
    }
}

//function gotoNewCustomer(){
//    window.location.href = "new_sale";
//}

function gotoBjCustomer(id){
    var param = {
        "id":id
    }
    var jsonparam = $.toJSON(param);
    $("#jsonparam",window.parent.document).attr("value",jsonparam);
    
    window.location.href = "bj_customer";
}

function deleteCustomer(id){
    var del = crud.dom.factory("DELETE");
    var url = "/customer/" + id;
    del.doDelete(url,deleteSalerCallback,"删除失败！");
    
    function deleteSalerCallback(json){
        window.location.href = "customer";
    }
}

function initCustomerContent(){
    var param = $.evalJSON($("#jsonparam",window.parent.document).val());
    var get = crud.dom.factory("GET");
    var url = "/customer/" + param.id;
    get.doGet(url,initCustomerContentCallback,"加载商户信息失败！");
    
    function initCustomerContentCallback(json){
        var objs = $.evalJSON(json);
        
        for(var i = 0;i<objs.length;i++){
            $("#customer_number").attr("value",objs[i].customer_number);
            $("#company_name").attr("value",objs[i].company_name);
            $("#company_manager").attr("value",objs[i].company_manager);
            $("#manager_id_card_url").attr("value",objs[i].manager_id_card);
            if(objs[i].manager_id_card != ""){
                $("#manager_id_card_information").text("图片已上传");
                $("#manager_id_card_information").attr("class","label label-success");
            }
            else{
                $("#manager_id_card_information").text("图片未上传");
                $("#manager_id_card_information").attr("class","label label-important"); 
            }
            $("#id_card_name").attr("value",objs[i].id_card_name);
            $("input:radio[name='id_card_sex']").eq(objs[i].id_card_sex).attr("checked",'checked');
            $("input:radio[name='id_card_sex']").uniform();//radio渲染
            $("#id_card_birthday").attr("value",objs[i].id_card_birthday);
            $("#id_card_address").attr("value",objs[i].id_card_address);
            $("#id_card_num").attr("value",objs[i].id_card_num);
            $("#id_card_photo_url").attr("value",objs[i].id_card_photo);
            if(objs[i].id_card_photo != ""){
                $("#id_card_photo_information").text("图片已上传");
                $("#id_card_photo_information").attr("class","label label-success");
            }
            else{
                $("#id_card_photo_information").text("图片未上传");
                $("#id_card_photo_information").attr("class","label label-important"); 
            }
            $("#business_license_url").attr("value",objs[i].business_license);
            if(objs[i].business_license != ""){
                $("#business_license_information").text("图片已上传");
                $("#business_license_information").attr("class","label label-success");
            }
            else{
                $("#business_license_information").text("图片未上传");
                $("#business_license_information").attr("class","label label-important"); 
            }
            $("#organization_code_certificate_url").attr("value",objs[i].organization_code_certificate);
            if(objs[i].organization_code_certificate != ""){
                $("#organization_code_certificate_information").text("图片已上传");
                $("#organization_code_certificate_information").attr("class","label label-success");
            }
            else{
                $("#organization_code_certificate_information").text("图片未上传");
                $("#organization_code_certificate_information").attr("class","label label-important"); 
            }
            $("#tax_certificate").attr("value",objs[i].tax_certificate);
            $("#credit_card_number").attr("value",objs[i].credit_card_number);
            $("#credit_card_img_url").attr("value",objs[i].credit_card_img);
            if(objs[i].credit_card_img != ""){
                $("#credit_card_img_information").text("图片已上传");
                $("#credit_card_img_information").attr("class","label label-success");
            }
            else{
                $("#credit_card_img_information").text("图片未上传");
                $("#credit_card_img_information").attr("class","label label-important"); 
            }
            $("#company_articles_url").attr("value",objs[i].company_articles);
            if(objs[i].company_articles != ""){
                $("#company_articles_information").text("图片已上传");
                $("#company_articles_information").attr("class","label label-success");
            }
            else{
                $("#company_articles_information").text("图片未上传");
                $("#company_articles_information").attr("class","label label-important"); 
            }
            $("#report_of_assets_url").attr("value",objs[i].report_of_assets);
            if(objs[i].report_of_assets != ""){
                $("#report_of_assets_information").text("图片已上传");
                $("#report_of_assets_information").attr("class","label label-success");
            }
            else{
                $("#report_of_assets_information").text("图片未上传");
                $("#report_of_assets_information").attr("class","label label-important"); 
            }
            $("#shareholder").attr("value",objs[i].shareholder);
            $("#mobile_phone").attr("value",objs[i].mobile_phone);
            $("#telephone").attr("value",objs[i].telephone);
        }
    }
}

function getAllManager(){
    var get = crud.dom.factory("GET");
    var url = "/users/get_user_name/2";//要改！！！
    get.doGet(url,getAllSalerCallback,"获取客户经理列表失败！");
    
    function getAllSalerCallback(json){
        var objs = $.evalJSON(json);
        var content;
        for(var i=0;i<objs.length;i++){
            $("#saler_manager").append("<option value="+objs[i].id+">"+objs[i].real_name+"</option>");
        }
        $("#saler_manager").trigger("liszt:updated");
    }
}

function changeManeger(obj){
    $("#customer_number").empty();
    $("#customer_number").append("<option value='0'>---------------</option>");
    
    var value = obj.value;
    
    var get = crud.dom.factory("GET");
    var url = "/customer/list";//要改！！！
    get.doGet(url,getAllCustomerCallback,"获取客户列表失败！");
    
    function getAllCustomerCallback(json){
        var objs = $.evalJSON(json);
        objs.pop();
        for(var i=0;i<objs.length;i++){
            $("#customer_number").append("<option value="+objs[i].id+">"+objs[i].customer_number+"</option>");
        }
        $("#customer_number").trigger("liszt:updated");
    }
}

function initDailyManage(){
    //bug
    var get = crud.dom.factory("GET");
    var url =  $("#jsonparam",window.parent.document).val();
    
    $('#downloadForm').attr("action",url);
    $('#downloadForm').attr("target",'_blank');
    
    get.doGet(url,submitCallback,"查询失败");
    
    function submitCallback(json){
        var objs = $.evalJSON(json);
        objs.pop();
        for(var i = 0;i<objs.length;i++){
            var content = '<div>'+
                '<a class="btn btn-info" href="javascript:void(0);" onclick="gotoBjDailyManege('+objs[i].id+','+objs[i].customer_id+','+objs[i].credit_type+','+objs[i].status+');">'+
                    '<i class="icon-edit icon-white"></i>编辑'+
                '</a>&nbsp;'+
                '<a class="btn btn-danger" href="javascript:void(0);" onclick="deleteDailyManege('+objs[i].id+','+objs[i].customer_id+','+objs[i].credit_type+','+objs[i].status+');">'+
                    '<i class="icon-trash icon-white"></i>删除'+
                '</a>'+ 
            '</div>';
            
            $('#dailyTable').dataTable().fnAddData( [
              '<input type="checkbox" name="daily_checkbox" onclick="changeColor(this)"/>',
              objs[i].customer_number,
              objs[i].company_name,
              objs[i].create_user,
              objs[i].create_date,
              content
              ]
            );
            
            window.parent.resizeFrame();
        }
    }
}

function downloadDailyManage(){
    $('#downloadForm').submit();
}

function gotoBjDailyManege(id,customer_id,credit_type,status){
    var param = {
        "id":id,
        "customer_id":customer_id
    }
    var jsonparam = $.toJSON(param);
    $("#jsonparam",window.parent.document).attr("value",jsonparam);
        
    if(credit_type == 1){//小微
        switch(status){
            case 1://贷前
                window.location.href = "bj_credit";
                break;
            case 2://贷中
                window.location.href = "bj_creditgant";
                break;
            case 3://贷后
                window.location.href = "bj_creditmanage";
                break;
        }
    }
    else if(credit_type == 2){//公司
        switch(status){
            case 1://贷前
                window.location.href = "bj_company_credit";
                break;
            case 2://贷中
                window.location.href = "bj_company_creditgant";
                break;
            case 3://贷后
                window.location.href = "bj_company_creditmanage";
                break;
        }
    }
    else if(credit_type == 3){//拓展
        
    }
}

function deleteDailyManege(id,customer_id,credit_type,status){
    
}

var selectValue;
var selectText;
var dynSelect;
function getAllManageForCustomer(){
    dynSelect = '<select  style="width:100px;" onchange="getChoose(this);">'+
                                '<option value="0">----</option>';
   
    var get = crud.dom.factory("GET");
    var url = "/users/get_user_name/2";//要改！！！
    get.doGet(url,getAllManageForCustomerCallback,"获取客户经理列表失败！");
    
    function getAllManageForCustomerCallback(json){
        var objs = $.evalJSON(json);
        for(var i=0;i<objs.length;i++){
            dynSelect += '<option value='+objs[i].id+'>'+objs[i].real_name+'</option>';
        }
        dynSelect +=  '</select>';
    }
}

function getChoose(obj){
    selectValue=obj.value;
    selectText=obj.options[obj.selectedIndex].text;
}

function initCustomerRelation(){
    var objs = $.evalJSON($("#jsonparam",window.parent.document).val());
    objs.pop();
    for(var i = 0;i<objs.length;i++){
        var content = '<div>'+
            '<a class="btn btn-info" href="javascript:void(0);" onclick="changeCell('+objs[i].id+','+objs[i].customer_id+');">'+
                '<i class="icon-edit icon-white"></i>编辑'+
            '</a>&nbsp;'+
            '<a class="btn btn-danger" href="javascript:void(0);" onclick="deleteCreditGrant('+objs[i].id+');">'+
                '<i class="icon-trash icon-white"></i>删除'+
            '</a>'+ 
        '</div>';
        
        $('#shTable').dataTable().fnAddData( [
          '<input type="checkbox" name="cu_checkbox" onclick="changeColor(this)"/>',
          objs[i].customer_number,
          objs[i].company_name,
          objs[i].real_name,
          content
          ]
        );
        
        window.parent.resizeFrame();
    }
}

function changeCell(id,customer_id){
    var obj = window.event.srcElement;
    var aRow  =  obj.parentElement.parentElement.parentElement;     //   alert(aRow);
    if(obj.innerText == "编辑"){
        var oldValue  =  aRow.cells[3].innerHTML;
        //var obj = $(dynSelect);
        //obj.find("option[text='"+oldValue+"']").attr("selected",true);
        aRow.cells[3].innerHTML = dynSelect;
        obj.innerText = "保存";
    }
    else{
        var data = JSON.stringify({
            "users_id": selectValue,
            "customer_id":customer_id,
            "create_user":1,
            "create_date":"",
            "modify_user":1,
            "modify_date":"",
        });
        
        //工厂模式
        var put = crud.dom.factory("PUT");
        var url = "/cu/" + id;
        put.doPut(url,data,submitCallback,"保存失败！");
        //回调
        function submitCallback(){
            aRow.cells[3].innerHTML = selectText;
            obj.innerText = "编辑";
        }
    }
}
//function gotoNewCustomerRelation(){
//    window.location.href = "new_customer_relation";
//}