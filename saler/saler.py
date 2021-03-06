#coding:utf8

import web
import models
import json
import tools.show_result as sr
import tools.json_encoding as encoder

urls=(
    '/list','get_saler_target_list',
    '/create','create_saler_target',
    '/(\d+)','manage_saler_target'
)

saler_target=models.saler_target()
"""只返回id,公司名称，公司法人"""
class get_saler_target_list:

    def GET(self):
        try:
            params=web.input()
            page=params.page if hasattr(params, 'page') else 1
            perpage = 10
            offset = (int(page) - 1) * perpage
            
            return json.dumps(saler_target.get_saler_target_list_paged(offset,perpage)
                                ,cls=encoder.DateEncoder,ensure_ascii=False)
        except:
            return sr.show_result_fail()
        
"""新增目标客户表"""
class create_saler_target:
    
    def POST(self): 
        json_data=json.loads(web.data())
        my_saler_target=saler_target.set_data(json_data)
        result=saler_target.create_saler_target(my_saler_target)

        return sr.show_result(result)
"""管理目标客户"""
class manage_saler_target:
    
    def GET(self,id):
        return json.dumps(saler_target.get_saler_target_by_id(id),cls=encoder.DateEncoder,ensure_ascii=False)

    def PUT(self,id):
        json_data=json.loads(web.data())
        my_saler_target=saler_target.set_data(json_data)
        result=saler_target.update_saler_target(id,my_saler_target)
        
        return sr.show_result(result)

    def DELETE(self,id):
        result=saler_target.del_saler_target(id)

        return sr.show_result(result)

        
app_saler_target = web.application(urls, locals())
