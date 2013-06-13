#coding:utf8

import web
import settings
import datetime
import tools.pagination

pager=tools.pagination.pager()
db=settings.db

class customer:
    customer_number=''
    company_name=''
    company_manager=''
    mobile_phone=''
    telephone=''
    manager_id_card=''
    business_license=''
    organization_code_certificate=''
    tax_certificate=''
    credit_card_number=''
    credit_card_img=''
    company_articles=''
    report_of_assets=''
    shareholder=''
    id_card_name=''
    id_card_sex=''
    id_card_birthday=''
    id_card_address=''
    id_card_num=''
    id_card_photo=''
    create_user=''
    create_date=''
    modify_user=''
    modify_date=''

    def get_customer_list_paged(self,page_num,per_page):
        return pager.result_paged('customer',
                                  order="create_date DESC",page_num=page_num,per_page=per_page)

    def get_customer_by_id(self,id):
        return db.select('customer', where='id=$id', vars=locals()).list()

    def create_customer(self,customer):
        return db.insert('customer',customer_number=customer.customer_number,company_name=customer.company_name,
                         company_manager=customer.company_manager,manager_id_card=customer.manager_id_card,
                         mobile_phone=customer.mobile_phone,telephone=customer.telephone,
                         business_license=customer.business_license,organization_code_certificate=customer.organization_code_certificate,
                         tax_certificate=customer.tax_certificate,credit_card_number=customer.credit_card_number,
                         credit_card_img=customer.credit_card_img,company_articles=customer.company_articles,
                         report_of_assets=customer.report_of_assets,shareholder=customer.shareholder,
                         id_card_name=customer.id_card_name,id_card_sex=customer.id_card_sex,
                         id_card_birthday=customer.id_card_birthday,
                         id_card_address=customer.id_card_address,id_card_num=customer.id_card_num,
                         id_card_photo=customer.id_card_photo,
                         modify_user=customer.modify_user,modify_date=datetime.datetime.utcnow(),
                         create_user=customer.create_user,create_date=datetime.datetime.utcnow(),
                         )

    def del_customer(self,id):
        return db.delete('customer', where="id=$id", vars=locals())

    def update_customer(self,id,customer):
        return db.update('customer', where="id=$id",customer_number=customer.customer_number,company_name=customer.company_name,
                         company_manager=customer.company_manager,manager_id_card=customer.manager_id_card,
                         mobile_phone=customer.mobile_phone,telephone=customer.telephone,
                         business_license=customer.business_license,organization_code_certificate=customer.organization_code_certificate,
                         tax_certificate=customer.tax_certificate,credit_card_number=customer.credit_card_number,
                         credit_card_img=customer.credit_card_img,company_articles=customer.company_articles,
                         report_of_assets=customer.report_of_assets,shareholder=customer.shareholder,
                         id_card_name=customer.id_card_name,id_card_sex=customer.id_card_sex,
                         id_card_birthday=customer.id_card_birthday,
                         id_card_address=customer.id_card_address,id_card_num=customer.id_card_num,
                         id_card_photo=customer.id_card_photo,
                         modify_user=customer.modify_user,modify_date=datetime.datetime.utcnow(),vars=locals())

    def set_data(self,data):
        customer.customer_number=data['customer_number']
        customer.company_name=data['company_name']
        customer.company_manager=data['company_manager']
        customer.mobile_phone=data['mobile_phone']
        customer.telephone=data['telephone']
        customer.manager_id_card=data['manager_id_card']
        customer.business_license=data['business_license']
        customer.organization_code_certificate=data['organization_code_certificate']
        customer.tax_certificate=data['tax_certificate']
        customer.credit_card_number=data['credit_card_number']
        customer.credit_card_img=data['credit_card_img']
        customer.company_articles=data['company_articles']
        customer.report_of_assets=data['report_of_assets']
        customer.shareholder=data['shareholder']
        customer.id_card_name=data['id_card_name']
        customer.id_card_sex=data['id_card_sex']
        customer.id_card_birthday=data['id_card_birthday']
        customer.id_card_address=data['id_card_address']
        customer.id_card_num=data['id_card_num']
        customer.id_card_photo=data['id_card_photo']
        customer.create_user=data['create_user']
        customer.modify_user=data['modify_user']

        return customer
