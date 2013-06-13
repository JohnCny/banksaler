/**
 * 显示时间
 */
function showdate()
{
    var date=new Date();
    var month=creattime(date.getMonth()+1);
    var da=creattime(date.getDate());
    var day=date.getDay();
    var nian=date.getFullYear();
    var txt;
    function creattime(i)
    {
        if(i<10)
        {i="0"+i}
        return i
    }
    switch(day)
    {
        case 1:
            txt="一"
            break
        case 2:
            txt="二"
            break
        case 3:
            txt="三"
            break
        case 4:
            txt="四"
            break
        case 5:
            txt="五"
            break
        case 6:
            txt="六"
            break
        case 0:
            txt="日"
            break
        default:
            sj.innerHTML="出错了"
    }
    document.getElementById('date').innerHTML="<font color='gray'>今天是：</font><font color='#3f9fd9'>"+nian+"年"+month+"月"+da+"日&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;星期"+txt+"</font>"
}

/**
 * 获取cookie
 * @param c_name
 * @returns
 */
function getCookie(c_name)
{
    if (document.cookie.length>0)
    { 
        c_start=document.cookie.indexOf(c_name + "=")
        if (c_start!=-1)
        { 
            c_start=c_start + c_name.length+1 
            c_end=document.cookie.indexOf(";",c_start)
            if (c_end==-1) 
                c_end=document.cookie.length

            return unescape(document.cookie.substring(c_start,c_end))
        } 
    }
    return ""
}

/**
 * 设置cookie
 * @param c_name
 * @param value
 * @param expireTimes
 */
function setCookie(c_name,value,expireTimes)
{
    var exdate=new Date();
    exdate.setTime(exdate.getTime()+expireTimes)
    document.cookie=c_name+ "=" +escape(value)+
    ((expireTimes==null) ? "" : "; expires="+exdate.toGMTString());
}

/**
 * 删除cookie
 * @param c_name
 */
function delCookie(c_name)
{
    var exdate=new Date();
    exdate.setTime(exdate.getTime() - 1);
    var cval=getCookie(c_name);
    if(cval!=null) document.cookie= c_name + "="+cval+";expires="+exdate.toGMTString();
}

/**
 * 动态构建form
 * @param action
 * @param jsonparam
 * @param parent
 */
function formSubmit(action,jsonparam,parent) {
    var turnForm = document.createElement("form");
    if(parent != null){
        parent.document.body.appendChild(turnForm);
    }
    else{
        document.body.appendChild(turnForm);
    }
    
    //var csrftoken = '<div style="display:none"><input type="hidden" name="csrfmiddlewaretoken" value="'+getCookie("csrftoken")+'"/></div>';
    var csrftokenDIV = document.createElement("div");
    csrftokenDIV.style.display="none";
    var csrftokenINPUT = document.createElement("input"); 
    csrftokenINPUT.setAttribute("type","hidden"); 
    csrftokenINPUT.setAttribute("name","csrfmiddlewaretoken"); 
    csrftokenINPUT.setAttribute("value",getCookie("csrftoken")); 
    csrftokenDIV.appendChild(csrftokenINPUT);
    turnForm.appendChild(csrftokenDIV);
    
    turnForm.method = 'post';
    turnForm.action = action;
    //turnForm.target = '_blank';
    
    var newElement = document.createElement("input");
    newElement.setAttribute("name","jsonparam");
    newElement.setAttribute("type","hidden");
    newElement.setAttribute("value",jsonparam);
    turnForm.appendChild(newElement);
    turnForm.submit();
}

/**
 * 改变表格行背景色
 * @param obj
 */
function changeColor(obj){
    if(obj.checked==true)
        obj.parentElement.parentElement.style.background="#def0d8"
    else
        obj.parentElement.parentElement.style.background="white"
}
/**
 * 改变图片大小
 * @param obj
 * @param label
 */
function bigger(obj,label){
    if(obj.style.height!="200px"){
        obj.style.height="200px";
        document.getElementById(label).style.paddingTop="100px";
        document.getElementById(label).style.paddingBottom="100px";
    }
    else{
        obj.style.height="50px";
        document.getElementById(label).style.paddingTop="22px";
        document.getElementById(label).style.paddingBottom="22px";
    }
     window.parent.resizeFrame();
}
/**
 * 列表全选
 * @param obj
 * @param checkbox
 */
function ChkAllClick(obj,checkbox){
    var arrSon = document.getElementsByName(checkbox);
    for(i=0;i<arrSon.length;i++) {
        if(arrSon[i].checked!=true){
            arrSon[i].click();
           
          }
        else{
            arrSon[i].click();
          }
    }
    
}

/**
 * disable的checkbox
 * @param obj
 */
function disableChk(obj){
    //if(obj.checked == tr)
    return obj.checked;
}

/**
 * 上传单个文件
 * @param obj
 */
function doupload(type,obj){
    var id = obj.id;
    //上传文件
    var upload = crud.dom.factory("UPLOAD");
    upload.doUpload(type,obj,uploadCallback,"选择的文件上传失败，请稍后重试！");
    
    function uploadCallback(data){
        $("#"+id + "_url").attr("value",data);
        $("#"+id + "_information").text("文件上传成功");
        $("#"+id + "_information").attr("class","label label-info");
    }
}

//以下为index.html的菜单控制
/**
 * 修改密码
 */
function gotoChangePwd(){
    document.getElementById("content_frame").src = "changepwd";
}

/**
 * 产品展示
 */
function gotoLccp(productType,productTypeName,limit,offset){
    var param = {
        "productType":productType,
        "productTypeName":productTypeName,
        "limit":limit,
        "offset":offset
    }
    var jsonparam = $.toJSON(param);
    $("#jsonparam").attr("value",jsonparam);
    var iframe = document.getElementById("content_frame");
    iframe.src = "lccp";
}

/**
 * 客户拓展
 */
function gotoShgl(){
    document.getElementById("content_frame").src = "shgl";
}

/**
 * 客户管理
 */
function gotoCustomer(){
    document.getElementById("content_frame").src = "customer";
}

/**
 * 日常行为管理
 */
function gotoDaily(){
    document.getElementById("content_frame").src = "daily_search";
}

/**
 * 客户关系维护
 */
function gotoCustomerRelationSearch(){
    document.getElementById("content_frame").src = "customer_relation_search";
}

/**
 * 贷前信息采集
 */
function gotoCredit(){
    document.getElementById("content_frame").src = "credit";
}

/**
 * 贷款发放项目采集
 */
function gotoCreditgrant(){
    document.getElementById("content_frame").src = "creditgrant";
}

/**
 * 贷后管理
 */
function gotoCreditmanage(){
    document.getElementById("content_frame").src = "creditmanage";
}

/**
 * 贷前信息采集
 */
function gotoCompanyCredit(){
    document.getElementById("content_frame").src = "company_credit";
}

/**
 * 贷款发放项目采集
 */
function gotoCompanyCreditgrant(){
    document.getElementById("content_frame").src = "company_creditgrant";
}

/**
 * 贷后管理
 */
function gotoCompanyCreditmanage(){
    document.getElementById("content_frame").src = "company_creditmanage";
}

/**
 * 办卡申请表
 */
function gotoBksqb(){
    document.getElementById("content_frame").src = "bksqb";
}

/**
 * 产品管理
 */
function gotoCpbj(){
    document.getElementById("content_frame").src = "cpbj";
}

/**
 * 用户管理
 */
function gotoYhgl(){
    document.getElementById("content_frame").src = "yhgl";
}

/**
 * 机构管理
 */
function gotoJggl(){
    $("#jsonparam").attr("value","");
    $("#treeDemo").css("display","block");
    document.getElementById("content_frame").src = "jggl";
}

/**
 * 设备管理
 */
function gotoSbgl(){
    document.getElementById("content_frame").src = "sbgl";
}