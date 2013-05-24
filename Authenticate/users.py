#coding:utf8

import web
import models
import json
import tools.show_result as sr

urls=(
    '/list','get_users_list',
    '/create','create_users',
    '/(\d+)','manage_users',
    '/login','users_login',
    '/get_user_name/(\d+)','get_user_name',
)

users=models.users()

"""获取用户真实姓名，用户编码列表"""
class get_users_list:

    def GET(self):
        try:
            params=web.input()
            page=params.page if hasattr(params, 'page') else 1
            perpage = 10
            offset = (int(page) - 1) * perpage
            
            return json.dumps(users.get_users_list_paged(offset,perpage),ensure_ascii=False)
        except:
            return sr.show_result_fail()

"""新增用户"""
class create_users:
    
    def POST(self): 
        json_data=json.loads(web.data())
        my_users=users.set_data(json_data)
        result=users.create_users(my_users)

        return sr.show_result(result)

"""管理用户"""
class manage_users:
    
    def GET(self,id):
        return json.dumps(users.get_users_by_id(id),ensure_ascii=False)

    def PUT(self,id):
        json_data=json.loads(web.data())
        my_users=users.set_data(json_data)
        result=users.update_users(id,my_users)
        
        return sr.show_result(result)

    def DELETE(self,id):
        result=users.del_users(id)

        return sr.show_result(result)


class users_login:

    def POST(self):
        json_data=json.loads(web.data())
        login_name=json_data['login_name']
        login_password=json_data['login_password']
        result=users.users_login(login_name,login_password)
        

        if len(result):
            web.ctx.status = '200 Success'
            result_list=result.list()
            return json.dumps({'result':'Success','userid':result_list[0].id,
                'username':result_list[0].real_name,},separators=(',', ': '),ensure_ascii=False)
        else :
            web.ctx.status = '401 UnAuthorized'
            return json.dumps({'result':'UnAuthorized'},separators=(',', ': '))

class get_user_name:
    def GET(self,org_id):
        return json.dumps(users.get_users_name_by_org(org_id),ensure_ascii=False)

                
app_users = web.application(urls, locals())
