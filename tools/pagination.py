import settings
import tools.show_result as sr

db=settings.db

class pager:

    def result_paged(self,tb_name,where='1=1',what='*',order=None,page_num=1,per_page=10):
        page_num=int(page_num)
        count_query="""
                    SELECT COUNT(*) as count FROM %s WHERE %s
                    """%(tb_name,where)

        counts=db.query(count_query)[0]

        pages = counts.count / per_page

        if counts.count % per_page >= 0:
            pages += 1

        if page_num>pages:
            return None

        offset=(int(page_num) - 1) * per_page

        result=db.select(tb_name,what=what,where=where,order=order,limit=per_page,offset=offset).list()

        result.extend([{'pages':pages}])

        return result


    def query_result_paged(self,query,page_num=1,per_page=10):
        page_num=int(page_num)

        query_result=db.query(query).list()

        counts=len(query_result)

        pages = counts / per_page

        if counts % per_page >= 0:
            pages += 1

        if page_num>pages:
            return None

        offset=(int(page_num) - 1) * per_page

        page_string=" LIMIT %s OFFSET %s"%(per_page,offset)
        query+=page_string

        result=db.query(query).list()

        result.extend([{'pages':pages}])

        return result
