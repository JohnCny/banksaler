#coding:utf8
import datetime,settings

db=settings.db

class credit:
    customer_number=''
    company_name=''
    company_manager=''
    manager_id_card=''
    business_license=''
    organization_code_certificate=''
    tax_certificate=''
    credit_card_nuber=''
    credit_card_img=''
    company_articles=''
    report_of_assets=''
    shareholder=''
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

    def get_credit_list_paged(self,offset,limit):
        result=db.select('credit',what='id,company_name,customer_number',order="create_date DESC",
                offset=offset,limit=limit).list()
        counts = settings.db.query("SELECT COUNT(*) AS count FROM credit")[0]
        pages = counts.count / limit
        
        if counts.count % limit > 0:
                pages += 1

        result.extend([{'pages':pages}])
        return result

    def get_credit_by_id(self,id):
        return db.select('credit', where='id=$id', vars=locals()).list()

    def create_credit(self,credit):
        return db.insert('credit',customer_number=credit.customer_number,company_name=credit.company_name,
                company_manager=credit.company_manager,manager_id_card=credit.manager_id_card,
                business_license=credit.business_license,organization_code_certificate=credit.organization_code_certificate,
                tax_certificate=credit.tax_certificate,credit_card_nuber=credit.credit_card_nuber,
                credit_card_img=credit.credit_card_img,company_articles=credit.company_articles,
                report_of_assets=credit.report_of_assets,shareholder=credit.shareholder,
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
        return db.update('credit', where="id=$id",customer_number=credit.customer_number,company_name=credit.company_name,
                company_manager=credit.company_manager,manager_id_card=credit.manager_id_card,
                business_license=credit.business_license,organization_code_certificate=credit.organization_code_certificate,
                tax_certificate=credit.tax_certificate,credit_card_nuber=credit.credit_card_nuber,
                credit_card_img=credit.credit_card_img,company_articles=credit.company_articles,
                report_of_assets=credit.report_of_assets,shareholder=credit.shareholder,
                balance_sheet=credit.balance_sheet,gl_sheet=credit.gl_sheet,
                warehouse_img=credit.warehouse_img,company_img=credit.company_img,
                stock_relationship=credit.stock_relationship,amount_of_credit=credit.amount_of_credit,
                year_of_credit=credit.year_of_credit,voice_record=credit.voice_record,
                guarantee=credit.guarantee,GPS=credit.GPS,
                status=credit.status,vars=locals())

    def set_data(self,data):
        credit.customer_number=data['customer_number']
        credit.company_name=data['company_name']
        credit.company_manager=data['company_manager']
        credit.manager_id_card=data['manager_id_card']
        credit.business_license=data['business_license']
        credit.organization_code_certificate=data['organization_code_certificate']
        credit.tax_certificate=data['tax_certificate']
        credit.credit_card_nuber=data['credit_card_nuber']
        credit.credit_card_img=data['credit_card_img']
        credit.company_articles=data['company_articles']
        credit.report_of_assets=data['report_of_assets']
        credit.shareholder=data['shareholder']
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
        credit.create_date=data['create_date']

        return credit

class credit_grant:
    customer_number=''
    company_name=''
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

    def get_credit_grant_list_paged(self,offset,limit):
        result=db.select('credit_grant',what='id,company_name,customer_number',order="create_date DESC",
                offset=offset,limit=limit).list()
        counts = settings.db.query("SELECT COUNT(*) AS count FROM credit_grant")[0]
        pages = counts.count / limit
        
        if counts.count % limit > 0:
                pages += 1

        result.extend([{'pages':pages}])
        return result

    def get_credit_grant_by_id(self,id):
        return db.select('credit_grant', where='id=$id', vars=locals()).list()

    def create_credit_grant(self,credit_grant):
        return db.insert('credit_grant',customer_number=credit_grant.customer_number,company_name=credit_grant.company_name,
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
        return db.update('credit_grant', where="id=$id",customer_number=credit_grant.customer_number,company_name=credit_grant.company_name,
                amount_of_credit=credit_grant.amount_of_credit,year_of_credit=credit_grant.year_of_credit,
                usage_of_credit=credit_grant.usage_of_credit,voice_record_of_interview=credit_grant.voice_record_of_interview,
                video_record_of_interview=credit_grant.video_record_of_interview,voice_record_of_guarantee=credit_grant.voice_record_of_guarantee,
                img_record_of_interview=credit_grant.img_record_of_interview,img_record_of_guarantee=credit_grant.img_record_of_guarantee,
                video_record_of_guarantee=credit_grant.video_record_of_guarantee,vars=locals())

    def set_data(self,data):
        credit_grant.customer_number=data['customer_number']
        credit_grant.company_name=data['company_name']
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
    customer_number=''
    company_name=''
    manager_id_card=''
    business_license=''
    organization_code_certificate=''
    tax_certificate=''
    credit_card_nuber=''
    credit_card_img=''
    company_articles=''
    capital_verification_report=''
    shareholder=''
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

    def get_credit_manage_list_paged(self,offset,limit):
        result=db.select('credit_manage',what='id,company_name,customer_number',order="create_date DESC",
                offset=offset,limit=limit).list()
        counts = settings.db.query("SELECT COUNT(*) AS count FROM credit_manage")[0]
        pages = counts.count / limit
        
        if counts.count % limit > 0:
                pages += 1

        result.extend([{'pages':pages}])
        return result

    def get_credit_manage_by_id(self,id):
        return db.select('credit_manage', where='id=$id', vars=locals()).list()

    def create_credit_manage(self,credit_manage):
        return db.insert('credit_manage',customer_number=credit_manage.customer_number,company_name=credit_manage.company_name,
                manager_id_card=credit_manage.manager_id_card,tax_certificate=credit_manage.tax_certificate,
                business_license=credit_manage.business_license,organization_code_certificate=credit_manage.organization_code_certificate,
                credit_card_img=credit_manage.credit_card_img,company_articles=credit_manage.company_articles,
                capital_verification_report=credit_manage.capital_verification_report,shareholder=credit_manage.shareholder,
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
        return db.update('credit_manage', where="id=$id",customer_number=credit_manage.customer_number,company_name=credit_manage.company_name,
                manager_id_card=credit_manage.manager_id_card,tax_certificate=credit_manage.tax_certificate,
                business_license=credit_manage.business_license,organization_code_certificate=credit_manage.organization_code_certificate,
                credit_card_img=credit_manage.credit_card_img,company_articles=credit_manage.company_articles,
                capital_verification_report=credit_manage.capital_verification_report,shareholder=credit_manage.shareholder,
                usage_of_credit=credit_manage.usage_of_credit,is_meet_credit_requirements=credit_manage.is_meet_credit_requirements,
                operation=credit_manage.operation,operation_img=credit_manage.operation_img,
                guarantee_status=credit_manage.guarantee_status,GPS=credit_manage.GPS,
                status=credit_manage.status,modify_user=credit_manage.modify_user,
                modify_date=datetime.datetime.utcnow(),vars=locals())

    def set_data(self,data):
        credit_manage.customer_number=data['customer_number']
        credit_manage.company_name=data['company_name']
        credit_manage.manager_id_card=data['manager_id_card']
        credit_manage.business_license=data['business_license']
        credit_manage.organization_code_certificate=data['organization_code_certificate']
        credit_manage.tax_certificate=data['tax_certificate']
        credit_manage.credit_card_img=data['credit_card_img']
        credit_manage.company_articles=data['company_articles']
        credit_manage.capital_verification_report=data['capital_verification_report']
        credit_manage.shareholder=data['shareholder']
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



