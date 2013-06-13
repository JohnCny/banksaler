#coding:utf8
import os
import web
from web.contrib.template import render_mako

BASE_PATH=os.path.join(os.path.dirname(__file__),'../templates').replace('\\','/')

render = render_mako(
    directories=[BASE_PATH,],
    input_encoding='utf-8',
    output_encoding='utf-8',
    )

render_products=render_mako(
    directories=[os.path.join(BASE_PATH,'products').replace('\\','/'),],
    input_encoding='utf-8',
    output_encoding='utf-8',
    )

render_users=render_mako(
    directories=[os.path.join(BASE_PATH,'users').replace('\\','/'),],
    input_encoding='utf-8',
    output_encoding='utf-8',
    )

render_groups=render_mako(
    directories=[os.path.join(BASE_PATH,'groups').replace('\\','/'),],
    input_encoding='utf-8',
    output_encoding='utf-8',
    )

render_salers=render_mako(
    directories=[os.path.join(BASE_PATH,'salers').replace('\\','/'),],
    input_encoding='utf-8',
    output_encoding='utf-8',
    )

render_credit=render_mako(
    directories=[os.path.join(BASE_PATH,'credit').replace('\\','/'),],
    input_encoding='utf-8',
    output_encoding='utf-8',
    )

render_companycredit=render_mako(
    directories=[os.path.join(BASE_PATH,'company_credit').replace('\\','/'),],
    input_encoding='utf-8',
    output_encoding='utf-8',
    )

render_devices=render_mako(
    directories=[os.path.join(BASE_PATH,'devices').replace('\\','/'),],
    input_encoding='utf-8',
    output_encoding='utf-8',
    )

render_bk=render_mako(
    directories=[os.path.join(BASE_PATH,'bk').replace('\\','/'),],
    input_encoding='utf-8',
    output_encoding='utf-8',
    )

urls=(
    '','login_view',
    'index','index_view',
    'welcome','welcome_view',
    'menu','menu_view',
    'lccp','lccp_view',
    'cpzs','cpzs_view',
    'bksqb','bksqb_view',
    'new_product','newproduct_view',
    'cpbj','cpbj_view',
    'bj_product','bjproduct_view',
    'yhgl','yhgl_view',
    'new_use','newuse_view',
    'bj_use','bjuse_view',
    'jggl','jggl_view',
    'new_group','newgroup_view',
    'bj_group','bjgroup_view',
    'sbgl','sbgl_view',
    'new_device','newdevice_view',
    'bj_device','bjdevice_view',
    'customer','customer_view',
    #'new_customer','newcustomer_view',
    'bj_customer','bjcustomer_view',
    'shgl','shgl_view',
    #'new_sale','newsaler_view',
    'bj_sale','bjsaler_view',
    'logout','logout_view',
    'changepwd','changepwd_view',

    'credit','credit_view',
    #'new_credit','newcredit_view',
    'bj_credit','bjcredit_view',

    'creditgrant','creditgrant_view',
    #'new_creditgant','newcreditgrant_view',
    'bj_creditgant','bjcreditgrant_view',

    'creditmanage','creditmanage_view',
    #'new_creditmanage','newcreditmanage_view',
    'bj_creditmanage','bjcreditmanage_view',
    
    'company_credit','company_credit_view',
    'bj_company_credit','bjcompany_credit_view',

    'company_creditgrant','company_creditgrant_view',
    'bj_company_creditgant','bjcompany_creditgrant_view',

    'company_creditmanage','company_creditmanage_view',
    'bj_company_creditmanage','bjcompany_creditmanage_view',

    'custom_manage','custom_manage_view',

    'daily_search','daily_search_view',
    'daily_manage','daily_manage_view',
    
    'customer_relation_search','customer_relation_search_view',
    'customer_relation','customer_relation_view',
    'new_customer_relation','new_customer_relation_view',
)

class login_view:
    def GET(self):
       return render.login()

class logout_view:
    def GET(self):
        return render.login()

class index_view:
    def GET(self):
        return render.index()
    def POST(self):
        return render.index()

class welcome_view:
    def GET(self):
        return render.welcome()

class menu_view:
    def GET(self):
        return render.menu()

class lccp_view:
    def GET(self):
        return render_products.lccp()

class cpzs_view:
    def GET(self):
        return render_products.cpzs()

class bksqb_view:
    def GET(self):
        return render_bk.bksqb()

class newproduct_view:
    def GET(self):
        return render_products.new_product()

class cpbj_view:
    def GET(self):
        return render_products.cpbj()

class bjproduct_view:
    def GET(self):
        return render_products.bj_product()

class yhgl_view:
    def GET(self):
        return render_users.yhgl()

class newuser_view:
    def GET(self):
        return render_users.new_user()

class bjuser_view:
    def GET(self):
        return render_users.bj_user()

class jggl_view:
    def GET(self):
        return render_groups.jggl()

class newgroup_view:
    def GET(self):
        return render_groups.new_group()

class bjgroup_view:
    def GET(self):
        return render_groups.bj_group()

class sbgl_view:
    def GET(self):
        return render_devices.sbgl()

class newdevice_view:
    def GET(self):
        return render_devices.new_device()

class bjdevice_view:
    def GET(self):
        return render_devices.bj_device()

class customer_view:
    def GET(self):
        return render_salers.customer()

class bjcustomer_view:
    def GET(self):
        return render_salers.bj_customer()
    
class shgl_view:
    def GET(self):
        return render_salers.shgl()

class newsaler_view:
    def GET(self):
        return render_salers.new_saler()

class bjsaler_view:
    def GET(self):
        return render_salers.bj_saler()

class changepwd_view:
    def GET(self):
        return render.change_password()

class credit_view:
    def GET(self):
        return render_credit.credit()

class creditgrant_view:
    def GET(self):
        return render_credit.credit_grant()

class creditmanage_view:
    def GET(self):
        return render_credit.credit_manage()

#class newcredit_view:
#    def GET(self):
#        return render_credit.new_credit()

class bjcredit_view:
    def GET(self):
        return render_credit.bj_credit()

#class newcreditgrant_view:
#    def GET(self):
#        return render_credit.new_creditgant()

class bjcreditgrant_view:
    def GET(self):
        return render_credit.bj_creditgant()

#class newcreditmanage_view:
#        def GET(self):
#            return render_credit.new_creditmanage()

class bjcreditmanage_view:
    def GET(self):
        return render_credit.bj_creditmanage()

class company_credit_view:
    def GET(self):
        return render_companycredit.company_credit()
    
class bjcompany_credit_view:
    def GET(self):
        return render_companycredit.bj_company_credit()
    
class company_creditgrant_view:
    def GET(self):
        return render_companycredit.company_credit_grant()
    
class bjcompany_creditgrant_view:
    def GET(self):
        return render_companycredit.bj_company_credit_grant()
    
class company_creditmanage_view:
    def GET(self):
        return render_companycredit.company_credit_manage()
    
class bjcompany_creditmanage_view:
    def GET(self):
        return render_companycredit.bj_company_credit_manage()
    
class daily_search_view:
    def GET(self):
        return render_salers.daily_search()

class daily_manage_view:
    def GET(self):
        return render_salers.daily_manage()
    
class customer_relation_search_view:
    def GET(self):
        return render_salers.customer_relation_search()
 
class customer_relation_view:
    def GET(self):
        return render_salers.customer_relation()   

class new_customer_relation_view:
    def GET(self):
        return render_salers.new_customer_relation()  

app_pc = web.application(urls, locals())
