#coding:utf8
import web
import Authenticate.auth
import settings
import json

db=settings.db

urls=(
    '/get_menu','get_menu'        
)

class get_menu:

    def GET(self):
        users_id=str(Authenticate.auth.get_users_id()[0]['users_id'])
        if users_id:
            query_string="""
                            select m.menu_name,m.menu_code_name from menu as m
                                inner join menu_role mr on m.id=mr.menu_id
                                inner join users_role ur on mr.role_id=ur.role_id where ur.users_id=
                         """
            query=query_string+users_id
            result=db.query(query).list()

            return json.dumps(result,ensure_ascii=False)
        else:
            return None

app_menu = web.application(urls, locals())

