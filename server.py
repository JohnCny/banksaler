#coding:utf8

import web
import tools.login as login,tools.file_upload as file_upload
import product.product as product,product.product_type as product_type
import saler.saler as saler,saler.operating_range as operating_range
import credit.credit as credit,credit.credit_grant as credit_grant,credit.credit_manage as credit_manage
import Authenticate.users as users
### Url mappings
urls=(
    '/login', login.app_login,
    '/product/', product.app_product,
    '/product_type', product_type.app_product_type,
    '/saler',saler.app_saler_target,
    '/operating_range',operating_range.app_operating_range,
    '/credit',credit.app_credit,
    '/grantcredit',credit_grant.app_credit_grant,
    '/managecredit',credit_manage.app_credit_manage,
    '/upload',file_upload.app_file_upload,
    '/users',users.app_users,
)

app = web.application(urls, locals())

if __name__ == "__main__":
	app.run()

