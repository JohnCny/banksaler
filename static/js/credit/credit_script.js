function getAllCredit(){
    var get = crud.dom.factory("GET");
    var url = "/credit/list?credit_type=1";
    get.doGet(url,getAllUserCallback,"获取贷款信息列表失败！");
    
    function getAllUserCallback(json){
        var objs = $.evalJSON(json);
        objs.pop();
        for(var i = 0;i<objs.length;i++){
            var content = '<div>'+
                '<a class="btn btn-info" href="javascript:void(0);" onclick="gotoBjCredit('+objs[i].id+','+objs[i].customer_id+');">'+
                    '<i class="icon-edit icon-white"></i>编辑'+
                '</a>&nbsp;'+
                '<a class="btn btn-danger" href="javascript:void(0);" onclick="deleteCredit('+objs[i].id+');">'+
                    '<i class="icon-trash icon-white"></i>删除'+
                '</a>'+ 
            '</div>';
            $('#yhTable').dataTable().fnAddData( [
              '<input type="checkbox" name="credit_checkbox" onclick="changeColor(this)"/>',
              objs[i].customer_number,
              objs[i].company_name,
              content
              ]
            );
            
            window.parent.resizeFrame();
        }
    }
}

function gotoBjCredit(id,customer_id){
    var param = {
        "id":id,
        "customer_id":customer_id
    }
    var jsonparam = $.toJSON(param);
    $("#jsonparam",window.parent.document).attr("value",jsonparam);
    
    window.location.href = "bj_credit";
}

function initCreditContent(){
    var param = $.evalJSON($("#jsonparam",window.parent.document).val());
    
    var get = crud.dom.factory("GET");
    var url = "/credit/" + param.id;
    get.doGet(url,initSalerContentCallback,"加载贷款信息失败！");
    
    function initSalerContentCallback(json){
        var objs = $.evalJSON(json);
        
        for(var i = 0;i<objs.length;i++){
            $("#balance_sheet_url").attr("value",objs[i].balance_sheet);
            if(objs[i].balance_sheet != ""){
                $("#balance_sheet_information").text("图片已上传");
                $("#balance_sheet_information").attr("class","label label-success");
            }
            else{
                $("#balance_sheet_information").text("图片未上传");
                $("#balance_sheet_information").attr("class","label label-important"); 
            }
            $("#gl_sheet_url").attr("value",objs[i].gl_sheet);
            if(objs[i].gl_sheet != ""){
                $("#gl_sheet_information").text("图片已上传");
                $("#gl_sheet_information").attr("class","label label-success");
            }
            else{
                $("#gl_sheet_information").text("图片未上传");
                $("#gl_sheet_information").attr("class","label label-important"); 
            }
            $("#company_img_url").attr("value",objs[i].company_img);
            if(objs[i].company_img != ""){
                $("#company_img_information").text("图片已上传");
                $("#company_img_information").attr("class","label label-success");
            }
            else{
                $("#company_img_information").text("图片未上传");
                $("#company_img_information").attr("class","label label-important"); 
            }
            $("#warehouse_img_url").attr("value", objs[i].warehouse_img);
            if(objs[i].warehouse_img != ""){
                $("#warehouse_img_information").text("图片已上传");
                $("#warehouse_img_information").attr("class","label label-success");
            }
            else{
                $("#warehouse_img_information").text("图片未上传");
                $("#warehouse_img_information").attr("class","label label-important"); 
            }
            $("#stock_relationship").attr("value",objs[i].stock_relationship);
            $("#amount_of_credit").attr("value",objs[i].amount_of_credit);
            $("#year_of_credit").attr("value",objs[i].year_of_credit);
            $("#voice_record_url").attr("value",objs[i].voice_record);
            if(objs[i].voice_record != ""){
                $("#voice_record_information").text("图片已上传");
                $("#voice_record_information").attr("class","label label-success");
            }
            else{
                $("#voice_record_information").text("图片未上传");
                $("#voice_record_information").attr("class","label label-important"); 
            }
            $("#guarantee").attr("value",objs[i].guarantee);
        }
    }
    
    var get2 = crud.dom.factory("GET");
    var url2 = "/customer/list";
    get2.doGet(url2,getAllCustomerCallback,"获取商户列表失败！");
    
    function getAllCustomerCallback(json){
        var objs = $.evalJSON(json);
        objs.pop();
        for(var i=0;i<objs.length;i++){
            if(param.customer_id == objs[i].id){
                $("#customer_number").append('<option value='+objs[i].id+' selected>'+objs[i].customer_number+'</option>');
            }
            else{
                $("#customer_number").append('<option value='+objs[i].id+'>'+objs[i].customer_number+'</option>');
            }
        }
        $("#customer_number").trigger("liszt:updated");
    }
    
    var get3 = crud.dom.factory("GET");
    var url3 = "/customer/" + param.customer_id;
    get3.doGet(url3,initCustomerCallback,"加载客户信息失败！");
    
    function initCustomerCallback(json){
        var objs = $.evalJSON(json);
        
        for(var i = 0;i<objs.length;i++){
            $("#company_name").text(objs[i].company_name);
            $("#company_manager").text(objs[i].company_manager);
            $("#manager_id_card").attr("src",wsHost+filePath+objs[i].manager_id_card);
            $("#id_card_name").text(objs[i].id_card_name);
            $("#id_card_sex").text(objs[i].id_card_sex=="1"?"男":"女");
            $("#id_card_birthday").text(objs[i].id_card_birthday);
            $("#id_card_address").text(objs[i].id_card_address);
            $("#id_card_num").text(objs[i].id_card_num);
            $("#id_card_photo").attr("src",wsHost+filePath+objs[i].id_card_photo);
            $("#business_license").attr("src",wsHost+filePath+objs[i].business_license);
            $("#organization_code_certificate").attr("src",wsHost+filePath+objs[i].organization_code_certificate);
            $("#tax_certificate").text(objs[i].tax_certificate);
            $("#credit_card_number").text(objs[i].credit_card_number);
            $("#credit_card_img").attr("src",wsHost+filePath+objs[i].credit_card_img);
            $("#company_articles").attr("src",wsHost+filePath+objs[i].company_articles);
            $("#report_of_assets").attr("src",wsHost+filePath+objs[i].report_of_assets);
            $("#shareholder").text(objs[i].shareholder);
            $("#mobile_phone").text(objs[i].mobile_phone);
            $("#telephone").text(objs[i].telephone);
        }
    }
}

function changeCustomerForCredit(obj){
    var id = obj.value;
    
    var get = crud.dom.factory("GET");
    var url = "/customer/" + id;
    get.doGet(url,initCustomerCallback,"加载客户信息失败！");
    
    function initCustomerCallback(json){
        var objs = $.evalJSON(json);
        
        for(var i = 0;i<objs.length;i++){
            $("#company_name").text(objs[i].company_name);
            $("#company_manager").text(objs[i].company_manager);
            $("#manager_id_card").attr("src",wsHost+filePath+objs[i].manager_id_card);
            $("#id_card_name").text(objs[i].id_card_name);
            $("#id_card_sex").text(objs[i].id_card_sex=="1"?"男":"女");
            $("#id_card_birthday").text(objs[i].id_card_birthday);
            $("#id_card_address").text(objs[i].id_card_address);
            $("#id_card_num").text(objs[i].id_card_num);
            $("#id_card_photo").attr("src",wsHost+filePath+objs[i].id_card_photo);
            $("#business_license").attr("src",wsHost+filePath+objs[i].business_license);
            $("#organization_code_certificate").attr("src",wsHost+filePath+objs[i].organization_code_certificate);
            $("#tax_certificate").text(objs[i].tax_certificate);
            $("#credit_card_number").text(objs[i].credit_card_number);
            $("#credit_card_img").attr("src",wsHost+filePath+objs[i].credit_card_img);
            $("#company_articles").attr("src",wsHost+filePath+objs[i].company_articles);
            $("#report_of_assets").attr("src",wsHost+filePath+objs[i].report_of_assets);
            $("#shareholder").text(objs[i].shareholder);
            $("#mobile_phone").text(objs[i].mobile_phone);
            $("#telephone").text(objs[i].telephone);
        }
    }
}

function deleteCredit(id){
    var del = crud.dom.factory("DELETE");
    var url = "/credit/" + id;
    del.doDelete(url,initSalerContentCallback,"删除失败！");
    
    function initSalerContentCallback(json){
        window.location.href = "credit";
    }
}

function getAllCreditGrant(){
    var get = crud.dom.factory("GET");
    var url = "/grantcredit/list?credit_type=1";
    get.doGet(url,getAllUserCallback,"获取贷款信息列表失败！");
    
    function getAllUserCallback(json){
        var objs = $.evalJSON(json);
        objs.pop();
        for(var i = 0;i<objs.length;i++){
            var content = '<div>'+
                '<a class="btn btn-info" href="javascript:void(0);" onclick="gotoBjCreditGrant('+objs[i].id+','+objs[i].customer_id+');">'+
                    '<i class="icon-edit icon-white"></i>编辑'+
                '</a>&nbsp;'+
                '<a class="btn btn-danger" href="javascript:void(0);" onclick="deleteCreditGrant('+objs[i].id+');">'+
                    '<i class="icon-trash icon-white"></i>删除'+
                '</a>'+ 
            '</div>';
            $('#yhTable').dataTable().fnAddData( [
              '<input type="checkbox" name="credit_grant_checkbox" onclick="changeColor(this)"/>',
              objs[i].customer_number,
              objs[i].company_name,
              content
              ]
            );
            
            window.parent.resizeFrame();
        }
    }
}

function gotoBjCreditGrant(id,customer_id){
    var param = {
        "id":id,
        "customer_id":customer_id
    }
    var jsonparam = $.toJSON(param);
    $("#jsonparam",window.parent.document).attr("value",jsonparam);
    
    window.location.href = "bj_creditgant";
}

function initCreditGrantContent(){
    var param = $.evalJSON($("#jsonparam",window.parent.document).val());
    
    var get = crud.dom.factory("GET");
    var url = "/grantcredit/" + param.id;
    get.doGet(url,initSalerContentCallback,"加载贷款信息失败！");
    
    function initSalerContentCallback(json){
        var objs = $.evalJSON(json);
        
        for(var i = 0;i<objs.length;i++){
            $("#amount_of_credit").attr("value",objs[i].amount_of_credit);
            $("#year_of_credit").attr("value",objs[i].year_of_credit);
            $("#usage_of_credit").attr("value",objs[i].usage_of_credit);
            $("#voice_record_of_interview_url").attr("value",objs[i].voice_record_of_interview);
            if(objs[i].voice_record_of_interview != ""){
                $("#voice_record_of_interview_information").text("语音已上传");
                $("#voice_record_of_interview_information").attr("class","label label-success");
            }
            else{
                $("#voice_record_of_interview_information").text("语音未上传");
                $("#voice_record_of_interview_information").attr("class","label label-important"); 
            }
            $("#voice_record_of_guarantee_url").attr("value",objs[i].voice_record_of_guarantee);
            if(objs[i].voice_record_of_guarantee != ""){
                $("#voice_record_of_guarantee_information").text("语音已上传");
                $("#voice_record_of_guarantee_information").attr("class","label label-success");
            }
            else{
                $("#voice_record_of_guarantee_information").text("语音未上传");
                $("#voice_record_of_guarantee_information").attr("class","label label-important"); 
            }
            $("#video_record_of_interview_url").attr("value",objs[i].video_record_of_interview);
            if(objs[i].video_record_of_interview != ""){
                $("#video_record_of_interview_information").text("视频已上传");
                $("#video_record_of_interview_information").attr("class","label label-success");
            }
            else{
                $("#video_record_of_interview_information").text("视频未上传");
                $("#video_record_of_interview_information").attr("class","label label-important"); 
            }
            $("#img_record_of_interview_url").attr("value",objs[i].img_record_of_interview);
            if(objs[i].img_record_of_interview != ""){
                $("#img_record_of_interview_information").text("图片已上传");
                $("#img_record_of_interview_information").attr("class","label label-success");
            }
            else{
                $("#img_record_of_interview_information").text("图片未上传");
                $("#img_record_of_interview_information").attr("class","label label-important"); 
            }
            $("#img_record_of_guarantee_url").attr("value",objs[i].img_record_of_guarantee);
            if(objs[i].img_record_of_guarantee != ""){
                $("#img_record_of_guarantee_information").text("图片已上传");
                $("#img_record_of_guarantee_information").attr("class","label label-success");
            }
            else{
                $("#img_record_of_guarantee_information").text("图片未上传");
                $("#img_record_of_guarantee_information").attr("class","label label-important"); 
            }
            $("#video_record_of_guarantee_url").attr("value",objs[i].video_record_of_guarantee);
            if(objs[i].video_record_of_guarantee != ""){
                $("#video_record_of_guarantee_information").text("视频已上传");
                $("#video_record_of_guarantee_information").attr("class","label label-success");
            }
            else{
                $("#video_record_of_guarantee_information").text("视频未上传");
                $("#video_record_of_guarantee_information").attr("class","label label-important"); 
            }
        }
    }
    
    var get2 = crud.dom.factory("GET");
    var url2 = "/customer/list";
    get2.doGet(url2,getAllCustomerCallback,"获取商户列表失败！");
    
    function getAllCustomerCallback(json){
        var objs = $.evalJSON(json);
        objs.pop();
        for(var i=0;i<objs.length;i++){
            if(param.customer_id == objs[i].id){
                $("#customer_number").append('<option value='+objs[i].id+' selected>'+objs[i].customer_number+'</option>');
            }
            else{
                $("#customer_number").append('<option value='+objs[i].id+'>'+objs[i].customer_number+'</option>');
            }
        }
        $("#customer_number").trigger("liszt:updated");
    }
}

function deleteCreditGrant(id){
    var del = crud.dom.factory("DELETE");
    var url = "/grantcredit/" + id;
    del.doDelete(url,initSalerContentCallback,"删除失败！");
    
    function initSalerContentCallback(json){
        window.location.href = "creditgrant";
    }
}

function getAllCreditManage(){
    var get = crud.dom.factory("GET");
    var url = "/managecredit/list?credit_type=1";
    get.doGet(url,getAllUserCallback,"获取贷款信息列表失败！");
    
    function getAllUserCallback(json){
        var objs = $.evalJSON(json);
        objs.pop();
        for(var i = 0;i<objs.length;i++){
            var content = '<div>'+
                '<a class="btn btn-info" href="javascript:void(0);" onclick="gotoBjCreditmanage('+objs[i].id+','+objs[i].customer_id+');">'+
                    '<i class="icon-edit icon-white"></i>编辑'+
                '</a>&nbsp;'+
                '<a class="btn btn-danger" href="javascript:void(0);" onclick="deleteCreditmanage('+objs[i].id+');">'+
                    '<i class="icon-trash icon-white"></i>删除'+
                '</a>'+ 
            '</div>';
            $('#yhTable').dataTable().fnAddData( [
              '<input type="checkbox" name="credit_manage_checkbox" onclick="changeColor(this)"/>',
              objs[i].customer_number,
              objs[i].company_name,
              content
              ]
            );
            
            window.parent.resizeFrame();
        }
    }
}

function gotoBjCreditmanage(id,customer_id){
    var param = {
        "id":id,
        "customer_id":customer_id
    }
    var jsonparam = $.toJSON(param);
    $("#jsonparam",window.parent.document).attr("value",jsonparam);
    
    window.location.href = "bj_creditmanage";
}

function initCreditManegeContent(){
    var param = $.evalJSON($("#jsonparam",window.parent.document).val());
    
    var get = crud.dom.factory("GET");
    var url = "/managecredit/" + param.id;
    get.doGet(url,initSalerContentCallback,"加载贷款信息失败！");
    
    function initSalerContentCallback(json){
        var objs = $.evalJSON(json);
        
        for(var i = 0;i<objs.length;i++){
            $("#capital_verification_report_url").attr("value",objs[i].capital_verification_report);
            if(objs[i].capital_verification_report != ""){
                $("#capital_verification_report_information").text("图片已上传");
                $("#capital_verification_report_information").attr("class","label label-success");
            }
            else{
                $("#capital_verification_report_information").text("图片未上传");
                $("#capital_verification_report_information").attr("class","label label-important"); 
            }
            $("#usage_of_credit").attr("value",objs[i].usage_of_credit);
            $("input:radio[name='is_meet_credit_requirements']").eq(objs[i].is_meet_credit_requirements).attr("checked",'checked');
            $("input:radio[name='is_meet_credit_requirements']").uniform();//radio渲染
            $("#operation").attr("value",objs[i].operation);
            $("#operation_img_url").attr("value",objs[i].operation_img);
            if(objs[i].capital_verification_report != ""){
                $("#operation_img_information").text("图片已上传");
                $("#operation_img_information").attr("class","label label-success");
            }
            else{
                $("#operation_img_information").text("图片未上传");
                $("#operation_img_information").attr("class","label label-important"); 
            }
            $("#guarantee_status").attr("value",objs[i].guarantee_status);
        }
    }
    
    var get2 = crud.dom.factory("GET");
    var url2 = "/customer/list";
    get2.doGet(url2,getAllCustomerCallback,"获取商户列表失败！");
    
    function getAllCustomerCallback(json){
        var objs = $.evalJSON(json);
        objs.pop();
        for(var i=0;i<objs.length;i++){
            if(param.customer_id == objs[i].id){
                $("#customer_number").append('<option value='+objs[i].id+' selected>'+objs[i].customer_number+'</option>');
            }
            else{
                $("#customer_number").append('<option value='+objs[i].id+'>'+objs[i].customer_number+'</option>');
            }
        }
        $("#customer_number").trigger("liszt:updated");
    }
}

function deleteCreditmanage(id){
    var del = crud.dom.factory("DELETE");
    var url = "/managecredit/" + id;
    del.doDelete(url,initSalerContentCallback,"删除失败！");
    
    function initSalerContentCallback(json){
        window.location.href = "creditmanage";
    }
}