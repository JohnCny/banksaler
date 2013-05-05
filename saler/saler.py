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
        return json.dumps(saler_target.get_saler_target_list().list(),cls=encoder.DateEncoder,ensure_ascii=False)
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
        return json.dumps(saler_target.get_saler_target_list().list(),cls=encoder.DateEncoder,ensure_ascii=False)

    def PUT(self,id):
        json_data=json.loads(web.data())
        my_saler_target=saler_target.set_data(json_data)
        result=saler_target.update_saler_target(id,my_saler_target)

        return sr.show_result(result)

    def DELETE(self,id):
        result=saler_target.del_saler_target(id)

        return sr.show_result(result)

        
app_saler_target = web.application(urls, locals())
