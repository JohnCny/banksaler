#coding:utf8

import web
import models
import auth
import tools.show_result as sr
import json

org_users=models.org_users()


urls=(
    'get_org_users','get_org_users',
)

class get_org_users:
    def GET(self):
        users_id=str(auth.get_users_id()[0]['users_id'])
        if users_id:
            try:
                org_id=str(org_users.get_org_by_users(users_id)[0]['org_id'])
                return json.dumps(org_users.get_users_by_org(org_id))
            except:
                return sr.show_result_fail()
        else:
            return sr.show_result_fail()


app_org_users = web.application(urls, locals())