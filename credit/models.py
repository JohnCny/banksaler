#coding:utf8
import datetime,settings
import Authenticate.models
import MySQLdb
import tools.pagination

pager=tools.pagination.pager()
db=settings.db
users=Authenticate.models.users()

class credit:
    customer_id=''
    balance_sheet=''
    gl_sheet=''
    company_img=''
    warehouse_img=''
    stock_relationship=''
    amount_of_credit=''
    year_of_credit=''
    voice_record=''
    guarantee=''
    GPS=''
    credit_type=''
    status=''
    create_date=''
    create_user=''

    def get_credit_list_paged(self,credit_type,page_num,per_page):
        credit_type=MySQLdb.escape_string(credit_type)
        query_string="""
                    SELECT cg.id AS id,c.company_name AS company_name,c.customer_number AS customer_number,
                           cg.customer_id AS customer_id
                    FROM credit AS cg
                        INNER JOIN customer as c
                            ON cg.customer_id=c.id
                                WHERE cg.credit_type=%s
                """%credit_type

        result=pager.query_result_paged(query_string,page_num,per_page)

        return result

    def get_credit_list_query_paged(self,page_num,per_page,
                                    create_user,customer_number,credit_type,beg_date,end_date):
        customer_number=MySQLdb.escape_string(customer_number)
        beg_date=MySQLdb.escape_string(beg_date)
        end_date=MySQLdb.escape_string(end_date)

        where=''
        if create_user!=0:
            where+='cg.create_user=%s and '%create_user
        if customer_number!='0':
            where+='c.customer_number=%s and '%customer_number
        if credit_type!=0:
            where+='cg.credit_type=%s and '%credit_type
        if beg_date!='0' and end_date!='0':
            where+="cg.create_date between '%s' and '%s' and "%(beg_date,end_date)
        elif end_date=='0':
            where+="cg.create_date>='%s' and "%beg_date
        elif beg_date=='0':
            where+="cg.create_date<='%s' and "%end_date

        where+='1=1'

        query_string="""
                    SELECT cg.id AS id,c.company_name AS company_name,c.customer_number AS customer_number,
                           cg.customer_id AS customer_id,u.real_name AS create_user,
                           cg.credit_type AS credit_type,cg.status AS status,cg.create_date AS create_date
                    FROM credit AS cg
                        INNER JOIN customer as c ON cg.customer_id=c.id
                         INNER JOIN users AS u  on c.create_user=u.id
                         WHERE
                    """+where
        result=pager.query_result_paged(query_string,page_num,per_page)

        return result

    def get_credit_by_id(self,id):
        return db.select('credit', where='id=$id', vars=locals()).list()

    def create_credit(self,credit):
        return db.insert('credit',customer_id=credit.customer_id,
                balance_sheet=credit.balance_sheet,gl_sheet=credit.gl_sheet,
                warehouse_img=credit.warehouse_img,company_img=credit.company_img,
                stock_relationship=credit.stock_relationship,amount_of_credit=credit.amount_of_credit,
                year_of_credit=credit.year_of_credit,voice_record=credit.voice_record,
                guarantee=credit.guarantee,GPS=credit.GPS,
                credit_type=credit.credit_type,status=0,
                create_user=credit.create_user,create_date=datetime.datetime.utcnow()
                )

    def del_credit(self,id):
        return db.delete('credit', where="id=$id", vars=locals())

    def update_credit(self,id,credit):
        return db.update('credit', where="id=$id",customer_id=credit.customer_id,
                balance_sheet=credit.balance_sheet,gl_sheet=credit.gl_sheet,
                warehouse_img=credit.warehouse_img,company_img=credit.company_img,
                stock_relationship=credit.stock_relationship,amount_of_credit=credit.amount_of_credit,
                year_of_credit=credit.year_of_credit,voice_record=credit.voice_record,
                guarantee=credit.guarantee,GPS=credit.GPS,
                status=credit.status,vars=locals())

    def set_data(self,data):
        credit.customer_id=data['customer_id']
        credit.balance_sheet=data['balance_sheet']
        credit.gl_sheet=data['gl_sheet']
        credit.warehouse_img=data['warehouse_img']
        credit.company_img=data['company_img']
        credit.stock_relationship=data['stock_relationship']
        credit.amount_of_credit=data['amount_of_credit']
        credit.year_of_credit=data['year_of_credit']
        credit.voice_record=data['voice_record']
        credit.guarantee=data['guarantee']
        credit.GPS=data['GPS']
        credit.credit_type=data['credit_type']
        credit.status=data['status']
        credit.create_user=data['create_user']

        return credit

class credit_grant:
    customer_id=''
    amount_of_credit=''
    year_of_credit=''
    usage_of_credit=''
    voice_record_of_interview=''
    voice_record_of_guarantee=''
    video_record_of_interview=''
    img_record_of_interview=''
    img_record_of_guarantee=''
    video_record_of_guarantee=''
    credit_type=''
    create_user=''
    create_date=''

    def get_credit_grant_list_query_paged(self,page_num,per_page,
                                    create_user,customer_number,credit_type,beg_date,end_date):
        customer_number=MySQLdb.escape_string(customer_number)
        beg_date=MySQLdb.escape_string(beg_date)
        end_date=MySQLdb.escape_string(end_date)

        where=''
        if create_user!=0:
            where+='cg.create_user=%s and '%create_user
        if customer_number!='0':
            where+='c.customer_number=%s and '%customer_number
        if credit_type!=0:
            where+='cg.credit_type=%s and '%credit_type
        if beg_date!='0' and end_date!='0':
            where+='cg.create_date between %s and %s and '%(beg_date,end_date)
        elif end_date=='0':
            where+='cg.create_date>=%s and '%beg_date
        elif beg_date=='0':
            where+='cg.create_date<=%s and '%end_date

        where+='1=1'

        query_string="""
                    SELECT cg.id AS id,c.company_name AS company_name,c.customer_number AS customer_number,
                           cg.customer_id AS customer_id,u.real_name AS create_user,
                           cg.credit_type AS credit_type,cg.status AS status,cg.create_date AS create_date
                    FROM credit_grant AS cg
                        INNER JOIN customer as c ON cg.customer_id=c.id
                         INNER JOIN users AS u  on c.create_user=u.id
                          WHERE
                    """+where
        result=pager.query_result_paged(query_string,page_num,per_page)

        return result

    def get_credit_grant_list_paged(self,credit_type,page_num,per_page):
        credit_type=MySQLdb.escape_string(credit_type)
        query_string="""
                    SELECT cg.id AS id,c.company_name AS company_name,c.customer_number AS customer_number
                           ,cg.customer_id AS customer_id
                    FROM credit_grant AS cg
                        INNER JOIN customer as c
                            ON cg.customer_id=c.id
                                WHERE cg.credit_type=%s
                """%credit_type

        result=pager.query_result_paged(query_string,page_num,per_page)

        return result

    def get_credit_grant_by_id(self,id):
        return db.select('credit_grant', where='id=$id', vars=locals()).list()

    def create_credit_grant(self,credit_grant):
        return db.insert('credit_grant',customer_id=credit_grant.customer_id,
                amount_of_credit=credit_grant.amount_of_credit,year_of_credit=credit_grant.year_of_credit,
                usage_of_credit=credit_grant.usage_of_credit,voice_record_of_interview=credit_grant.voice_record_of_interview,
                video_record_of_interview=credit_grant.video_record_of_interview,voice_record_of_guarantee=credit_grant.voice_record_of_guarantee,
                img_record_of_interview=credit_grant.img_record_of_interview,img_record_of_guarantee=credit_grant.img_record_of_guarantee,
                video_record_of_guarantee=credit_grant.video_record_of_guarantee,credit_type=credit_grant.credit_type,
                create_user=credit_grant.create_user,create_date=datetime.datetime.utcnow()
                )

    def del_credit_grant(self,id):
        return db.delete('credit_grant', where="id=$id", vars=locals())

    def update_credit_grant(self,id,credit_grant):
        return db.update('credit_grant', where="id=$id",
                amount_of_credit=credit_grant.amount_of_credit,year_of_credit=credit_grant.year_of_credit,
                usage_of_credit=credit_grant.usage_of_credit,voice_record_of_interview=credit_grant.voice_record_of_interview,
                video_record_of_interview=credit_grant.video_record_of_interview,voice_record_of_guarantee=credit_grant.voice_record_of_guarantee,
                img_record_of_interview=credit_grant.img_record_of_interview,img_record_of_guarantee=credit_grant.img_record_of_guarantee,
                video_record_of_guarantee=credit_grant.video_record_of_guarantee,vars=locals())

    def set_data(self,data):
        credit_grant.customer_id=data['customer_id']
        credit_grant.amount_of_credit=data['amount_of_credit']
        credit_grant.year_of_credit=data['year_of_credit']
        credit_grant.usage_of_credit=data['usage_of_credit']
        credit_grant.voice_record_of_interview=data['voice_record_of_interview']
        credit_grant.video_record_of_interview=data['video_record_of_interview']
        credit_grant.voice_record_of_guarantee=data['voice_record_of_guarantee']
        credit_grant.img_record_of_interview=data['img_record_of_interview']
        credit_grant.img_record_of_guarantee=data['img_record_of_guarantee']
        credit_grant.video_record_of_guarantee=data['video_record_of_guarantee']
        credit_grant.credit_type=data['credit_type']
        credit_grant.create_user=data['create_user']
        
        return credit_grant

class credit_manage:
    customer_id=''
    capital_verification_report=''
    usage_of_credit=''
    is_meet_credit_requirements=''
    operation=''
    operation_img=''
    guarantee_status=''
    GPS=''
    credit_type=''
    status=''
    create_user=''
    create_date=''
    modify_date=''
    modify_user=''

    def get_credit_manage_list_query_paged(self,page_num,per_page,
                                          create_user,customer_number,credit_type,beg_date,end_date):
        customer_number=MySQLdb.escape_string(customer_number)
        beg_date=MySQLdb.escape_string(beg_date)
        end_date=MySQLdb.escape_string(end_date)

        where=''
        if create_user!=0:
            where+='cg.create_user=%s and '%create_user
        if customer_number!='0':
            where+='c.customer_number=%s and '%customer_number
        if credit_type!=0:
            where+='cg.credit_type=%s and '%credit_type
        if beg_date!='0' and end_date!='0':
            where+='cg.create_date between %s and %s and '%(beg_date,end_date)
        elif end_date=='0':
            where+='cg.create_date>=%s and '%beg_date
        elif beg_date=='0':
            where+='cg.create_date<=%s and '%end_date

        where+='1=1'

        query_string="""
                        SELECT cg.id AS id,c.company_name AS company_name,c.customer_number AS customer_number,
                               cg.customer_id AS customer_id,u.real_name AS create_user,
                               cg.credit_type AS credit_type,cg.status AS status,cg.create_date AS create_date
                        FROM credit_manage AS cg
                         INNER JOIN customer as c ON cg.customer_id=c.id
                          INNER JOIN users AS u  on c.create_user=u.id
                           WHERE
                        """+where
        result=pager.query_result_paged(query_string,page_num,per_page)

        return result


    def get_credit_manage_list_paged(self,credit_type,page_num,per_page):
        credit_type=MySQLdb.escape_string(credit_type)
        query_string="""
                    SELECT cg.id AS id,c.company_name AS company_name,c.customer_number AS customer_number,
                            cg.customer_id AS customer_id
                    FROM credit_manage AS cg
                        INNER JOIN customer as c
                            ON cg.customer_id=c.id
                                WHERE cg.credit_type=%s
                """%credit_type

        result=pager.query_result_paged(query_string,page_num,per_page)

        return result

    def get_credit_manage_by_id(self,id):
        return db.select('credit_manage', where='id=$id', vars=locals()).list()

    def create_credit_manage(self,credit_manage):
        return db.insert('credit_manage',customer_id=credit_manage.customer_id,
                capital_verification_report=credit_manage.capital_verification_report,
                usage_of_credit=credit_manage.usage_of_credit,is_meet_credit_requirements=credit_manage.is_meet_credit_requirements,
                operation=credit_manage.operation,operation_img=credit_manage.operation_img,
                guarantee_status=credit_manage.guarantee_status,GPS=credit_manage.GPS,
                credit_type=credit_manage.credit_type,status=0,
                create_user=credit_manage.create_user,create_date=datetime.datetime.utcnow(),
                modify_user=credit_manage.modify_user,modify_date=datetime.datetime.utcnow()
                )

    def del_credit_manage(self,id):
        return db.delete('credit_manage', where="id=$id", vars=locals())

    def update_credit_manage(self,id,credit):
        return db.update('credit_manage', where="id=$id",customer_id=credit_manage.customer_id,
                capital_verification_report=credit_manage.capital_verification_report,
                usage_of_credit=credit_manage.usage_of_credit,is_meet_credit_requirements=credit_manage.is_meet_credit_requirements,
                operation=credit_manage.operation,operation_img=credit_manage.operation_img,
                guarantee_status=credit_manage.guarantee_status,GPS=credit_manage.GPS,
                status=credit_manage.status,modify_user=credit_manage.modify_user,
                modify_date=datetime.datetime.utcnow(),vars=locals())

    def set_data(self,data):
        credit_manage.customer_id=data['customer_id']
        credit_manage.capital_verification_report=data['capital_verification_report']
        credit_manage.usage_of_credit=data['usage_of_credit']
        credit_manage.is_meet_credit_requirements=data['is_meet_credit_requirements']
        credit_manage.operation=data['operation']
        credit_manage.operation_img=data['operation_img']
        credit_manage.guarantee_status=data['guarantee_status']
        credit_manage.GPS=data['GPS']
        credit_manage.credit_type=data['credit_type']
        credit_manage.status=data['status']
        credit_manage.create_user=data['create_user']
        credit_manage.modify_user=data['modify_user']

        return credit_manage


class search:
    def get_all_work_by_users_id(self,users_id):
        query="""select c.id,c.customer_number,c.company_name,c.create_user
                from credit as c where c.create_user=1 union
                select cg.id,cg.customer_number,cg.company_name,cg.create_user
                from credit_grant as cg  where cg.create_user=1 union
                select cm.id,cm.customer_number,cm.company_name,cm.create_user
                from credit_manage as cm where cm.create_user=1 union
                select st.id,st.customer_number,st.company_name,st.create_user
                from saler_target as st
            """


