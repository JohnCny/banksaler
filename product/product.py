#coding:utf8
import web
import json
import models
import tools.show_result as sr
import tools.json_encoding as encoder
import traceback

urls = (
    '(\d+)', 'product_by_id',
    'create', 'create_product',
    '','show_product'
)


product=models.product()

"""产品管理"""
class product_by_id:

    def GET(self,id):
        return json.dumps(product.get_product_by_id(id),cls=encoder.DateEncoder,ensure_ascii=False)

    def PUT(self,id):
        json_data=json.loads(web.data())
        my_product=product.init(json_data)
        result=product.update_product(id,my_product)
        
        return sr.show_result(result)

    def DELETE(self,id):
        result=product.del_product(id)
        return sr.show_result(result)

"""新增产品"""
class create_product:
    def POST(self):
        json_data=json.loads(web.data())
        my_product=product.init(json_data)
        result=product.create_product(my_product)

        return sr.show_result(result)
"""展示产品 
url param:product_type
"""
class show_product:

    def GET(self):
        try:
            params=web.input()
            product_type=params.product_type
            page=params.page if hasattr(params, 'page') else 1
            per_page=params.per_page if hasattr(params, 'per_page') else 10

            result= product.get_product_by_type_with_page(product_type,page_num=page,per_page=per_page)

            if result:
                return json.dumps(result,
                        cls=encoder.DateEncoder,ensure_ascii=False)
            else:
                return sr.show_result_fail()
        except:
            return sr.show_result_fail()+traceback.print_exc()

app_product = web.application(urls, locals())        

