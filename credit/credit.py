#coding:utf8

import web
import models
import json
import tools.show_result as sr
import tools.json_encoding as encoder
import traceback


urls=(
    '/list','get_credit_list',
    '/create','create_credit',
    '/(\d+)','manage_credit'
)

credit=models.credit()

"""只返回id,公司名称，公司法人"""
class get_credit_list:

    def GET(self):
        try:
            params=web.input()
            credit_type=params.credit_type
            page=params.page if hasattr(params, 'page') else 1
            perpage =params.perpage if hasattr(params, 'perpage') else 10

            
            return json.dumps(credit.get_credit_list_paged(credit_type,page,perpage),
                              cls=encoder.DateEncoder,ensure_ascii=False)
        except:
            return sr.show_result_fail()
        
"""新增贷前调查表"""
class create_credit:
    
    def POST(self):        
        json_data=json.loads(web.data())
        my_credit=credit.set_data(json_data)
        result=credit.create_credit(my_credit)

        return sr.show_result(result)

"""管理贷前调查表"""
class manage_credit:
    
    def GET(self,id):
        return json.dumps(credit.get_credit_by_id(id),cls=encoder.DateEncoder,ensure_ascii=False)

    def PUT(self,id):
        json_data=json.loads(web.data())
        my_credit=credit.set_data(json_data)
        result=credit.update_credit(id,my_credit)
        
        return sr.show_result(result)

    def DELETE(self,id):
        result=credit.del_credit(id)

        return sr.show_result(result)

        
app_credit = web.application(urls, locals())
