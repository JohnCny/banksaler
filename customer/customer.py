#coding:utf8

import web
import models
import json
import tools.show_result as sr
import tools.json_encoding as encoder
import traceback

urls=(
    '/list','get_customer_list',
    '/create','create_customer',
    '/(\d+)','manage_customer',
)

customer=models.customer()


"""只返回id,公司名称，客户号"""
class get_customer_list:

    def GET(self):
        try:
            params=web.input()
            page=params.page if hasattr(params, 'page') else 1
            per_page=params.per_page if hasattr(params, 'per_page') else 10

            return json.dumps(customer.get_customer_list_paged(page_num=page,per_page=per_page),
                              cls=encoder.DateEncoder,ensure_ascii=False)
        except:
            return sr.show_result_fail()+traceback.print_exc()


"""新增客户"""
class create_customer:

    def POST(self):
        json_data=json.loads(web.data())
        my_customer=customer.set_data(json_data)
        result=customer.create_customer(my_customer)

        return sr.show_result(result)

"""管理客户"""
class manage_customer:

    def GET(self,id):
        return json.dumps(customer.get_customer_by_id(id),cls=encoder.DateEncoder,ensure_ascii=False)

    def PUT(self,id):
        json_data=json.loads(web.data())
        my_customer=customer.set_data(json_data)
        result=customer.update_customer(id,my_customer)

        return sr.show_result(result)

    def DELETE(self,id):
        result=customer.del_customer(id)

        return sr.show_result(result)


app_customer = web.application(urls, locals())

