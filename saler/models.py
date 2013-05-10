#coding:utf8
import datetime,settings

db=settings.db

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
    entry_user=''
    create_date=''
    modify_date=''
    modify_user=''

class saler_target:

    def get_saler_target(self):
        return db.select('saler_target', order='create_date DESC').list()
    """返回id与公司名称"""
    def get_saler_target_list(self):
        return db.select('saler_target',what='id,company_name,company_manager',group="company_manager").list()
    
    def get_saler_target_list_paged(self,offset,limit):
        result=db.select('saler_target',what='id,company_name,company_manager',order="create_date DESC",
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
                entry_user=saler_target.entry_user,create_date=datetime.datetime.utcnow(),
                modify_date=datetime.datetime.utcnow(),modify_user=saler_target.modify_user)

    def del_saler_target(self,id):
        return db.delete('saler_target', where="id=$id", vars=locals())

    def update_saler_target(self,id,product):
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
        saler_target.entry_user=data['entry_user']
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


       
