#coding:utf8
import datetime,settings
import tools.pagination
import MySQLdb

pager=tools.pagination.pager()

db = settings.db
"""构造product类 简化传参"""
class my_product:
    product_name=''
    product_type=''
    product_describe=''
    product_img=''
    product_beg_date=''
    product_end_date=''


class product:
        def get_product(self):
            return db.select('product', order='product_create_date DESC').list()

        def get_product_by_type(self,product_type_id):
            return db.select('product',where='product_type=$product_type_id',vars=locals()).list()

        def get_product_by_id(self,id):
            return db.select('product', where='id=$id', vars=locals()).list()
        
        def get_product_by_type_with_page(self,product_type_id,page_num=1,per_page=10):
            product_type_id=MySQLdb.escape_string(product_type_id)

            where="product_type='%s'"%product_type_id

            return pager.result_paged('product',where=where,
                                      order="product_create_date DESC",page_num=page_num,per_page=per_page)

        def create_product(self,product):
            return db.insert('product',product_name=product.product_name,product_type=product.product_type,product_describe=product.product_describe,
                    product_img=product.product_img,product_beg_date=product.product_beg_date,product_end_date=product.product_end_date,
                    product_create_date=datetime.datetime.utcnow())

        def del_product(self,id):
            return db.delete('product', where="id=$id", vars=locals())

        def update_product(self,id,product):
            return db.update('product', where="id=$id", vars=locals(),product_name=product.product_name,product_type=product.product_type,
                    product_describe=product.product_describe,product_img=product.product_img,product_beg_date=product.product_beg_date,
                    product_end_date=product.product_end_date,)
        
        def init(self,data):
            my_product.product_name=data['product_name']
            my_product.product_type=data['product_type']
            my_product.product_describe=data['product_describe']
            my_product.product_img=data['product_img']
            my_product.product_beg_date=data['product_beg_date']
            my_product.product_end_date=data['product_end_date']

            return my_product

class product_type:
        def get_product_type(self):
            return db.select('product_type').list()
        
        def get_product_type_by_id(self,id):
            return db.select('product_type',where="id=$id", vars=locals()).list()

        def create_product_type(self,type_name):
            return db.insert('product_type',type_name=type_name)

        def del_product_type(self,id):
            return db.delete('product_type',where="id=$id", vars=locals())

        def update_product_type(self,id,type_name):
            return db.update('product_type',where="id=$id", vars=locals(),type_name=type_name)





