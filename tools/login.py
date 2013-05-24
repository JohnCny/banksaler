#coding:utf8

import web
import json
import settings
import Authenticate.models

urls=(
    '/','login'
)
"""登陆''"""
class login:

    def POST(self):
        json_data=json.loads(web.data())
        login_name=json_data['login_name']
        login_password=json_data['login_password']
        myvar=dict(login_name=login_name,login_password=login_password)
        result=settings.db.select('users',myvar,where="login_name=$login_name and login_password=$login_password")
        

        if len(result):
            web.ctx.status = '200 Success'
            result_list=result.list()
            org_users=Authenticate.models.org_users()
            org_result=org_users.get_org_by_users(result_list[0].id)
            if len(org_result):
                return json.dumps({'result':'Success','userid':result_list[0].id,
                    'username':result_list[0].real_name,'org_id':org_result[0].id},separators=(',', ': '),ensure_ascii=False)
        else :
            web.ctx.status = '401 UnAuthorized'
            return json.dumps({'result':'UnAuthorized'},separators=(',', ': '))

app_login = web.application(urls, locals())
