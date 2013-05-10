#coding:utf8

import web
import json
import settings

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
            return json.dumps({'result':'Success','username':result[0].real_name},separators=(',', ': '))
        else :
            web.ctx.status = '401 UnAuthorized'
            return json.dumps({'result':'UnAuthorized'},separators=(',', ': '))

app_login = web.application(urls, locals())
