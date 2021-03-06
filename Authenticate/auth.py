#coding:utf8

import web
import models
import settings

db=settings.db

def check_auth_key():
    auth_head=web.ctx.env.get('Authorization')
    if models.auth_key.check_auth_key(auth_head):
        return True
    else:
        return False

def validate_key(fn):
    """
    验证auth_key 是否合法
    """
    def new(*args):
        if not check_auth_key():
            web.badrequest()
        return fn(*args)
    return new
 
def get_operate_by_user(users_id):
    query_string= """select opr.code_name from operate opr
                        inner join operate_permission as opr_per on opr.id=opr_per.operate_id
                        inner join role_permission as r_per on opr_per.id=r_per.permission_id
                        inner join org_role as org on r_per.id=org.role_id
                        inner join org_users as org_u on org.id=org_u.org_id"""
    result=db.query(query_string).list()
    
    return result
    
def get_users_id():
    auth_head=web.ctx.env.get('HTTP_AUTHORIZATION')
    auth_key=models.auth_key()
    users_id=auth_key.get_users_id(auth_head)
    if len(users_id) :
        return users_id
    else:
        return False
   


