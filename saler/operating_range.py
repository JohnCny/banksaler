#coding:utf8

import web
import json
import models
import tools.show_result as sr

urls=(
	'/list', 'get_operating_range',
	"/(\d+)", "operating_range_by_id",
    "/create", "create_operating_range"
)

operating_range=models.operating_range()

"""管理产品类型"""
class operating_range_by_id:
        
    def GET(self,operating_range_id):
        return json.dumps(operating_range.get_operating_range_by_id(operating_range_id), ensure_ascii=False)

    def PUT(self,operating_range_id):
        json_data=json.loads(web.data())
        range_name=json_data['range_name']
        result=operating_range.update_operating_range(operating_range_id,range_name)

        return sr.show_result(result)

    def DELETE(self,operating_range_id):
        result=operating_range.del_operating_range(operating_range_id)
        return sr.show_result(result)

"""获取产品类型"""
class get_operating_range:

    def GET(self):
        try:
            params=web.input()
            page=params.page if hasattr(params, 'page') else 1
            perpage = 10
            offset = (int(page) - 1) * perpage

            return json.dumps(operating_range.get_operating_range_list_paged(offset,perpage),ensure_ascii=False)
        except:
            return sr.show_result_fail()

"""新增产品类型"""
class create_operating_range:

    def POST(self):
        json_data=json.loads(web.data())
        range_name=json_data['range_name']
        result=operating_range.create_operating_range(range_name)

        return sr.show_result(result)


app_operating_range = web.application(urls, locals()) 
