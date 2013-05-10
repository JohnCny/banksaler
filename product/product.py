#coding:utf8
import web
import json
import models
import tools.show_result as sr
import tools.json_encoding as encoder

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
            perpage = 10
            offset = (int(page) - 1) * perpage

            result= product.get_product_by_type_with_page(offset,perpage,product_type)
            
            return json.dumps(result,
                    cls=encoder.DateEncoder,ensure_ascii=False)
        except:
            return sr.show_result_fail()

app_product = web.application(urls, locals())        

