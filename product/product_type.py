#coding:utf8

import web
import json
import models
import tools.show_result as sr

urls=(
	'/', 'get_product_type',
	"/(\d+)", "product_type_by_id",
    "/create", "create_product_type"
)

product_type=models.product_type()

"""管理产品类型"""
class product_type_by_id:
        
    def GET(self,product_type_id):
        return json.dumps(product_type.get_product_type_by_id(product_type_id), ensure_ascii=False)

    def PUT(self,product_type_id):
        json_data=json.loads(web.data())
        type_name=json_data['type_name']
        result=product_type.update_product_type(product_type_id,type_name)

        return sr.show_result(result)

    def DELETE(self,product_type_id):
        result=product_type.del_product_type(product_type_id)
        return sr.show_result(result)

"""获取产品类型"""
class get_product_type:

    def GET(self):
		return json.dumps(product_type.get_product_type(),ensure_ascii=False)

"""新增产品类型"""
class create_product_type:

    def POST(self):
        json_data=json.loads(web.data())
        type_name=json_data['type_name']
        result=product_type.create_product_type(type_name)

        return sr.show_result(result)


app_product_type = web.application(urls, locals())        

