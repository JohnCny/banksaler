#coding:utf8
import xlwt
import StringIO
import web
import datetime

class report_daily_manage:
    def download_report(self,type,query_set):
        """使用文件流传输文件至本地"""

        type_name=''
        """生成文件名"""
        if type==1:
            type_name=u'贷前调查'
        elif type==2:
            type_name=u'贷中调查'
        elif type==2:
            type_name=u'贷后调查'
        elif type==2:
            type_name=u'商户拓展'

        now=datetime.datetime.now()
        t ="%d-%d-%d" %(now.year,now.month,now.day)
        file_name=u'截止至'+t+u'日'+type_name+u'统计表'+'.xls'
        """设置web header"""
        web.header('Content-type','application/vnd.ms-excel')  #指定返回的类型
        web.header('Transfer-Encoding','chunked')
        web.header('Content-Disposition','attachment;filename="%s"'%file_name) #设定用户浏览器显示的保存文件名
        """开始制作表格"""
        wb=xlwt.Workbook()
        wb.encoding='utf8'
        ws=wb.add_sheet('1')
        """表头开始"""
        ws.write(0,0,u'序号')
        ws.write(0,1,u'客户经理名称')
        ws.write(0,2,u'公司名称')
        ws.write(0,3,u'客户号')
        ws.write(0,4,u'拜访日期')

        col_saler=ws.col(1)
        col_saler.width=256*15

        col_company=ws.col(2)
        col_company.width=256*20

        col_cn=ws.col(3)
        col_cn.width=256*15

        col_date=ws.col(4)
        col_date.width=256*20
        """表体开始"""
        count=1
        for item in query_set:
            if item.get('create_user') is not None:
                ws.write(count,0,count)
                ws.write(count,1,item.get('create_user'))
                ws.write(count,2,item.get('company_name'))
                ws.write(count,3,item.get('customer_number'))
                ws.write(count,4,str(item.get('create_date')))
                count+=1

        sio=StringIO.StringIO()
        wb.save(sio)
        return sio.getvalue()




