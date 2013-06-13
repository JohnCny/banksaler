#coding:utf8

import web
import models
import json
import tools.show_result as sr
import traceback

urls=(
    '/list','get_orgnization_list',
    '/create','create_orgnization',
    '/(\d+)','manage_orgnization',
)

orgnization=models.orgnization()

"""获取用户真实姓名，用户编码列表"""
class get_orgnization_list:

    def GET(self):
        try:
            params=web.input()
            page=params.page if hasattr(params, 'page') else 1
            perpage = 10
            offset = (int(page) - 1) * perpage

            return json.dumps(orgnization.get_orgnization_list_paged(offset,perpage),ensure_ascii=False)
        except:
            return sr.show_result_fail()+traceback.print_exc()
"""新增机构"""
class create_orgnization:

    def POST(self):
        json_data=json.loads(web.data())
        my_orgnization=orgnization.set_data(json_data)
        result=orgnization.create_orgnization(my_orgnization)

        return sr.show_result(result)

"""管理机构"""
class manage_orgnization:

    def GET(self,id):
        return json.dumps(orgnization.get_orgnization_by_id(id),ensure_ascii=False)

    def PUT(self,id):
        json_data=json.loads(web.data())
        my_orgnization=orgnization.set_data(json_data)
        result=orgnization.update_orgnization(id,my_orgnization)

        return sr.show_result(result)

    def DELETE(self,id):
        result=orgnization.del_orgnization(id)

        return sr.show_result(result)



app_orgnization = web.application(urls, locals())
