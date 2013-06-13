#coding:utf8

import web
import settings
import datetime
import MySQLdb
import tools.pagination

pager=tools.pagination.pager()
db=settings.db

class customer_users:
    customer_id=''
    users_id=''
    create_user=''
    create_date=''
    modify_user=''
    modify_date=''

    def get_customer_users_list_paged(self,page_num,per_page,users_id=0,customer_number=0,company_name='0'):
        company_name=MySQLdb.escape_string(company_name)

        where=''
        if users_id!=0:
            where+='cu.users_id=%s and '%users_id
        if customer_number!=0:
            where+='cu.customer_id=%s and '%customer_number
        if company_name!='0':
            where+='c.company_name=%s and '%company_name

        where+='1=1'

        query_string="""
                    SELECT cu.id AS id,c.company_name AS company_name,c.customer_number AS customer_number,
                           u.real_name AS real_name,cu.customer_id AS customer_id
                    FROM
                        customer_users AS cu
                    INNER JOIN customer AS c ON cu.customer_id=c.id
                    INNER JOIN users AS u ON cu.users_id=u.id
                    WHERE
                    """+where

        return pager.query_result_paged(query_string,page_num,per_page)

    def get_customer_users_by_id(self,id):
        return db.select('customer_users', where='id=$id', vars=locals()).list()

    def create_customer_users(self,customer_users):
        return db.insert('customer_users',
                         customer_id=customer_users.customer_id,users_id=customer_users.users_id,
                         modify_user=customer_users.modify_user,modify_date=datetime.datetime.utcnow(),
                         create_user=customer_users.create_user,create_date=datetime.datetime.utcnow(),
        )

    def del_customer_users(self,id):
        return db.delete('customer_users', where="id=$id", vars=locals())

    def update_customer_users(self,id,customer_users):
        return db.update('customer_users', where="id=$id",
                         customer_id=customer_users.customer_id,users_id=customer_users.users_id,
                         modify_user=customer_users.modify_user,modify_date=datetime.datetime.utcnow(),vars=locals())

    def set_data(self,data):
        customer_users.customer_id=data['customer_id']
        customer_users.users_id=data['users_id']
        customer_users.create_user=data['create_user']
        customer_users.create_date=data['create_date']
        customer_users.modify_user=data['modify_user']
        customer_users.modify_date=data['modify_date']

        return customer_users