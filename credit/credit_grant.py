#coding:utf8

import web
import models
import json
import tools.show_result as sr
import tools.json_encoding as encoder

urls=(
    'list','get_credit_grant_list',
    'create','create_credit_grant',
    '(\d+)','manage_credit_grant'
)

credit_grant=models.credit_grant()

"""只返回id,公司名称，公司法人"""
class get_credit_grant_list:

    def GET(self):
        try:
            params=web.input()
            credit_type=params.credit_type
            page=params.page if hasattr(params, 'page') else 1
            perpage = params.perpage if hasattr(params, 'perpage') else 10

            
            return json.dumps(credit_grant.get_credit_grant_list_paged(credit_type,page,perpage),
                              cls=encoder.DateEncoder,ensure_ascii=False)
        except:
            return sr.show_result_fail()
        
"""新增贷前调查表"""
class create_credit_grant:
    
    def POST(self):
        json_data=json.loads(web.data())
        my_credit_grant=credit_grant.set_data(json_data)
        result=credit_grant.create_credit_grant(my_credit_grant)

        return sr.show_result(result)

"""管理贷前调查表"""
class manage_credit_grant:
    
    def GET(self,id):
        return json.dumps(credit_grant.get_credit_grant_by_id(id),cls=encoder.DateEncoder,ensure_ascii=False)

    def PUT(self,id):
        json_data=json.loads(web.data())
        my_credit_grant=credit_grant.set_data(json_data)
        result=credit_grant.update_credit_grant(id,my_credit_grant)
        
        return sr.show_result(result)

    def DELETE(self,id):
        result=credit_grant.del_credit_grant(id)

        return sr.show_result(result)

        
app_credit_grant = web.application(urls, locals())
