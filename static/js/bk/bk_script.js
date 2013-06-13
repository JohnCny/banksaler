//省市区三级联动
function initAddress(){
    var provinceSelector = JQuery("#provinceSelector");
    var citySelector = JQuery("#citySelector");
    var areaSelector=JQuery("#areaSelector");
    GetProvince();
    provinceSelector.change(function () {
        var provinceName = provinceSelector.val();
        if (provinceName != '') {
            GetCity(provinceName);
            areaSelector.empty();
        }
        else{
            citySelector.empty();
            areaSelector.empty();
        }
    });
    citySelector.change(function () {
        var provinceName = provinceSelector.val();
        var cityName = citySelector.val();
        if(cityName!=''){
            GetArea(provinceName, cityName);
        }
        else{
            areaSelector.empty();
        }
    });
}

// 获取省份(直辖市)信息
function GetProvince() {
    var provSelector = JQuery("#provinceSelector");
    provSelector.empty();
    provSelector.append("<option value=''>--请选择--</option>");
    var arrProvince = provinceInfo;
    for (var provinceIndex in arrProvince) {
        provSelector.append("<option value='" + arrProvince[provinceIndex]["name"] + "'>" + arrProvince[provinceIndex]["name"] + "</option>")
    }
}

// 获取指定省份(直辖市)的城市(辖区或县)信息
function GetCity(provinceName) {
    var citySelector = JQuery("#citySelector");
    var arrCity;
    for (var provinceIndex in provinceInfo) {
        if (provinceInfo[provinceIndex]["name"] == provinceName) {
            arrCity = provinceInfo[provinceIndex]["sub"];
            break;
        }
    }
    citySelector.empty();
    citySelector.append("<option value=''>--请选择--</option>")
    for (var cityIndex in arrCity) {
        citySelector.append("<option value='" + arrCity[cityIndex]["name"] + "'>" + arrCity[cityIndex]["name"] + "</option>")
    }
}

// 获取指定城市(辖区或县)的地区信息
function GetArea(provinceName, cityName) {
    var areaSelector = JQuery("#areaSelector");
    var arrCity, arrArea;
    for (var provinceIndex in provinceInfo) {
        if (provinceInfo[provinceIndex]["name"] == provinceName) {
            arrCity = provinceInfo[provinceIndex]["sub"];
            for (var cityIndex in arrCity) {
                if (arrCity[cityIndex]["name"] == cityName) {
                    arrArea = arrCity[cityIndex]["sub"];
                    break;
                }
            }
        }
    }
    areaSelector.empty();
    areaSelector.append("<option value=''>--请选择--</option>")
    for (var areaIndex in arrArea) {
        areaSelector.append("<option value='" + arrArea[areaIndex]["name"] + "'>" + arrArea[areaIndex]["name"] + "</option>")
    }
}