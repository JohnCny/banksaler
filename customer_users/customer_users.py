#coding:utf8

import web
import models
import json
import tools.show_result as sr
import tools.json_encoding as encoder
import Authenticate.auth
import traceback


urls=(
    'list','get_customer_users_list',
    'create','create_customer_users',
    '(\d+)','manage_customer_users',
)

customer_users=models.customer_users()


"""只返回id,公司名称，客户号,客户经理名称"""
class get_customer_users_list:

    def GET(self):
        try:
            params=web.input()
            page=params.page if hasattr(params, 'page') else 1
            perpage =params.perpage if hasattr(params, 'perpage') else 10
            customer_number=params.customer_number
            users_id=params.users_id
            company_name=params.company_name

            return json.dumps(customer_users.get_customer_users_list_paged(page,perpage,users_id,customer_number,company_name)
                ,cls=encoder.DateEncoder,ensure_ascii=False)
        except:
            return sr.show_result_fail()+traceback.print_exc()


"""新增客户关系管理"""
class create_customer_users:

    def POST(self):
        json_data=json.loads(web.data())
        my_customer_users=customer_users.set_data(json_data)
        result=customer_users.create_customer_users(my_customer_users)

        return sr.show_result(result)

"""管理客户关系表"""
class manage_customer_users:

    def GET(self,id):
        return json.dumps(customer_users.get_customer_users_by_id(id),cls=encoder.DateEncoder,ensure_ascii=False)

    def PUT(self,id):
        json_data=json.loads(web.data())
        my_customer_users=customer_users.set_data(json_data)
        result=customer_users.update_customer_users(id,my_customer_users)

        return sr.show_result(result)

    def DELETE(self,id):
        result=customer_users.del_customer_users(id)

        return sr.show_result(result)


app_customer_users = web.application(urls, locals())
