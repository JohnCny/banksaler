#coding:utf8

import web
import tools.login as login
import product.product as product,product.product_type as product_type
import saler.saler as saler

### Url mappings
urls=(
    '/login', login.app_login,
    '/product/', product.app_product,
    '/product_type', product_type.app_product_type,
    '/saler',saler.app_saler_target
)

app = web.application(urls, locals())

if __name__ == "__main__":
	app.run()
