#coding:utf8
import datetime,settings
import Authenticate.models
import MySQLdb
import tools.pagination

db=settings.db
users=Authenticate.models.users()
pager=tools.pagination.pager()

class saler_target:
    company_name=''
    company_manager=''
    company_addr=''
    main_operating_range=''
    staff_amount=''
    last_year_operating=''
    main_bank=''
    have_credit=''
    is_customer=''
    is_credit_customer=''
    saler_opinion=''
    create_user=''
    create_date=''
    modify_date=''
    modify_user=''

class saler_target:

    def get_saler_target(self):
        return db.select('saler_target', order='create_date DESC').list()
    """返回id,公司名称,负责人，地址"""
    def get_saler_target_list(self):
        return db.select('saler_target',what='id,company_name,company_manager,company_addr',group="company_manager").list()

    def get_saler_target_list_by_condition(self,page_num,per_page,create_user,beg_date,end_date):
        where=''

        """SQL防注入"""
        create_user=MySQLdb.escape_string(create_user)
        beg_date=MySQLdb.escape_string(beg_date)
        end_date=MySQLdb.escape_string(end_date)

        if create_user!=0:
            where+='create_user=%s and '%create_user
        if beg_date!='0' and end_date!='0':
            where+='create_date between %s and %s and '%(beg_date,end_date)
        elif end_date=='0':
            where+='create_date>=%s and '%beg_date
        elif beg_date=='0':
            where+='create_date<=%s and '%end_date

        where+='1=1'

        result=pager.result_paged('product',where=where,
                                order="product_create_date DESC",page_num=page_num,per_page=per_page)

        """替换结果集中的人员id"""
        for item in result:
            id=item.create_user
            item.create_user=users.get_users_by_id(id)[0]['real_name']

        return result


    def get_saler_target_list_paged(self,offset,limit):
        result=db.select('saler_target',what='id,company_name,company_manager,company_addr',order="create_date DESC",
                offset=offset,limit=limit).list()
        counts = settings.db.query("SELECT COUNT(*) AS count FROM saler_target")[0]
        pages = counts.count / limit
        
        if counts.count % limit > 0:
                pages += 1

        result.extend([{'pages':pages}])
        return result

    def get_saler_target_by_id(self,id):
        return db.select('saler_target', where='id=$id', vars=locals()).list()

    def create_saler_target(self,saler_target):
        return db.insert('saler_target',company_name=saler_target.company_name,company_manager=saler_target.company_manager,
                company_addr=saler_target.company_addr,main_operating_range=saler_target.main_operating_range,
                staff_amount=saler_target.staff_amount,last_year_operating=saler_target.last_year_operating,
                main_bank=saler_target.main_bank,have_credit=saler_target.have_credit,is_customer=saler_target.is_customer,
                is_credit_customer=saler_target.is_credit_customer,saler_opinion=saler_target.saler_opinion,
                create_user=saler_target.create_user,create_date=datetime.datetime.utcnow(),
                modify_date=datetime.datetime.utcnow(),modify_user=saler_target.modify_user)

    def del_saler_target(self,id):
        return db.delete('saler_target', where="id=$id", vars=locals())

    def update_saler_target(self,id,saler_target):
        return db.update('saler_target', where="id=$id",company_name=saler_target.company_name,company_manager=saler_target.company_manager,
                company_addr=saler_target.company_addr,main_operating_range=saler_target.main_operating_range,
                staff_amount=saler_target.staff_amount,last_year_operating=saler_target.last_year_operating,
                main_bank=saler_target.main_bank,have_credit=saler_target.have_credit,is_customer=saler_target.is_customer,
                is_credit_customer=saler_target.is_credit_customer,saler_opinion=saler_target.saler_opinion,
                modify_date=datetime.datetime.utcnow(),
                modify_user=saler_target.modify_user,vars=locals())

    def set_data(self,data):
        saler_target.company_name=data['company_name']
        saler_target.company_manager=data['company_manager']
        saler_target.company_addr=data['company_addr']
        saler_target.main_operating_range=data['main_operating_range']
        saler_target.staff_amount=data['staff_amount']
        saler_target.last_year_operating=data['last_year_operating']
        saler_target.main_bank=data['main_bank']
        saler_target.have_credit=data['have_credit']
        saler_target.is_customer=data['is_customer']
        saler_target.is_credit_customer=data['is_credit_customer']
        saler_target.saler_opinion=data['saler_opinion']
        saler_target.create_user=data['create_user']
        saler_target.modify_user=data['modify_user']

        return saler_target

class operating_range:
    def get_operating_range_list_paged(self,offset,limit):
        result=db.select('operating_range',offset=offset,limit=limit).list()
        counts = settings.db.query("SELECT COUNT(*) AS count FROM operating_range")[0]
        pages = counts.count / limit
        
        if counts.count % limit > 0:
                pages += 1

        result.extend([{'pages':pages}])
        return result
    
    def get_operating_range_by_id(self,id):
        return db.select('operating_range',where="id=$id", vars=locals()).list()

    def create_operating_range(self,range_name):
        return db.insert('operating_range',range_name=range_name)

    def del_operating_range(self,id):
        return db.delete('operating_range',where="id=$id", vars=locals())

    def update_operating_range(self,id,range_name):
        return db.update('operating_range',where="id=$id", vars=locals(),range_name=range_name)    


       
