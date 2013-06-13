#coding:utf8

import web
import settings
import models
import json
import tools.show_result as sr
import traceback
import saler.models as saler
import report.daily_manager
import tools.json_encoding as encoder

db=settings.db
dm=report.daily_manager.report_daily_manage()

urls=(
    '/list','list_result'
)

class list_result:
    def GET(self):
        params=web.input()
        try:
            type=params.type
            saler_manager=int(params.saler_manager)
            customer_number=str(params.customer_number)
            credit_type=int(params.credit_type)
            beg_date=str(params.beg_date)
            end_date=str(params.end_date)
            page_num=params.page if hasattr(params, 'page') else 1
            per_page =params.per_page if hasattr(params, 'per_page') else 10



            if type=='1':
                credit=models.credit()
                result=credit.get_credit_list_query_paged(page_num,per_page,saler_manager,
                                                          customer_number,credit_type,
                                                          beg_date,end_date)
                return json.dumps(result,cls=encoder.DateEncoder,ensure_ascii=False)
            elif type=='2':
                credit_grant=models.credit_grant()
                result=credit_grant.get_credit_grant_list_query_paged(page_num,per_page,saler_manager,
                                                          customer_number,credit_type,
                                                          beg_date,end_date)

                return json.dumps(result,cls=encoder.DateEncoder,ensure_ascii=False)
            elif type=='3':
                credit_manage=models.credit_manage()
                result=credit_manage.get_credit_manage_list_query_paged(page_num,per_page,saler_manager,
                                                                      customer_number,credit_type,
                                                                      beg_date,end_date)

                return json.dumps(result,cls=encoder.DateEncoder,ensure_ascii=False)
            elif type=='4':
                saler_target=saler.saler_target
                result=saler_target.get_saler_target_list_by_condition(self,page_num,per_page,saler_manager,beg_date,end_date)
                return json.dumps(result,cls=encoder.DateEncoder,ensure_ascii=False)


        except:
            return sr.show_result_fail()+traceback.print_exc()


    def POST(self):
        params=web.input()
        try:
            type=params.type
            saler_manager=int(params.saler_manager)
            customer_number=str(params.customer_number)
            credit_type=int(params.credit_type)
            beg_date=str(params.beg_date)
            end_date=str(params.end_date)
            page_num=params.page if hasattr(params, 'page') else 1
            per_page =params.per_page if hasattr(params, 'per_page') else 10



            if type=='1':
                credit=models.credit()
                result=credit.get_credit_list_query_paged(page_num,per_page,saler_manager,
                                                          customer_number,credit_type,
                                                          beg_date,end_date)
                return dm.download_report(1,result)
            elif type=='2':
                credit_grant=models.credit_grant()
                result=credit_grant.get_credit_grant_list_query_paged(page_num,per_page,saler_manager,
                                                                      customer_number,credit_type,
                                                                      beg_date,end_date)

                return dm.download_report(2,result)
            elif type=='3':
                credit_manage=models.credit_manage()
                result=credit_manage.get_credit_manage_list_query_paged(page_num,per_page,saler_manager,
                                                                        customer_number,credit_type,
                                                                        beg_date,end_date)

                return dm.download_report(3,result)
            elif type=='4':
                saler_target=saler.saler_target
                result=saler_target.get_saler_target_list_by_condition(self,page_num,per_page,saler_manager,beg_date,end_date)
                return dm.download_report(4,result)


        except:
            return sr.show_result_fail()+traceback.print_exc()


app_search_credit = web.application(urls, locals())





