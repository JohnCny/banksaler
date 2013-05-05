import web
import json

def show_result(result):
    if result:
            web.ctx.status = '200 Success'
            return json.dumps({'result':'Success'})
    else:
            web.ctx.status = '500 Failed'
            return json.dumps({'result':'Failed'})

def show_result_message(message):
    web.ctx.status = '500 Failed'
    return json.dumps(message,ensure_ascii=False)

def show_result_false():
    web.ctx.status = '500 Failed'
    return json.dumps({'result':'Failed'})
    
