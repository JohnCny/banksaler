#coding:utf8
import web
import os
import datetime
import show_result as sr
import base64

urls=(
    '/img','upload_img',
    '/file','upload_file',
    '/video','upload_video',
    '/voice','upload_voice'
)

class upload_img:
    def POST(self):
        files = web.input(file={})

        if 'file' in files:
            """设置服务器端目录"""
            homedir = os.getcwd()
            filedir = '%s/static/upload/img' %homedir
            
            """获取文件后缀，并以时间更改文件名"""
            filepath=files.file_path.replace('\\','/')
            ext=filepath.split('.', 1)[1]

            now=datetime.datetime.now()
            t ="%d%d%d%d%d%d" %(now.year,now.month,now.day,now.hour,now.minute,now.second)
            
            file_name = t+'.'+ext
            """从本地读取文件二进制流并传输至服务端"""            
             
            data=files['file'].file.read()
            try:
                with open(filedir+'/'+file_name, 'wb') as f_out:
                    f_out.write(data)
                f_out.close()
            except:
                return sr.show_result_fail()
            
            return '/static/upload/img/'+file_name

class upload_file:
    def POST(self):
        files = web.input(file_path={})

        if 'file_path' in files:
            """设置服务器端目录"""
            homedir = os.getcwd()
            filedir = '%s/static/upload/file' %homedir
            
            """获取文件后缀，并以时间更改文件名"""
            filepath=files.file_path.replace('\\','/')
            ext=filepath.split('.', 1)[1]

            now=datetime.datetime.now()
            t ="%d%d%d%d%d%d" %(now.year,now.month,now.day,now.hour,now.minute,now.second)
            
            file_name = t+'.'+ext
            """从本地读取文件二进制流并传输至服务端"""
            
            try:
                with open(files.file_path) as f_in:
                    data = f_in.read()
                f_in.close()

                with open(filedir+'/'+file_name, 'w') as f_out:
                    f_out.write(data)
                f_out.close()
            except:
                return sr.show_result_fail() 
            
            return '/static/upload/file/'+file_name

class upload_video:
    def POST(self):
        files = web.input(file_path={})

        if 'file_path' in files:
            """设置服务器端目录"""
            homedir = os.getcwd()
            filedir = '%s/static/upload/video' %homedir
            
            """获取文件后缀，并以时间更改文件名"""
            filepath=files.file_path.replace('\\','/')
            ext=filepath.split('.', 1)[1]

            now=datetime.datetime.now()
            t ="%d%d%d%d%d%d" %(now.year,now.month,now.day,now.hour,now.minute,now.second)
            
            file_name = t+'.'+ext
            """从本地读取文件二进制流并传输至服务端"""
            
            try:
                with open(files.file_path,'rb') as f_in:
                    data = f_in.read()
                f_in.close()

                with open(filedir+'/'+file_name, 'wb') as f_out:
                    f_out.write(data)
                f_out.close()
            except:
                return sr.show_result_fail() 
            
            return '/static/upload/video/'+file_name

class upload_voice:
    def POST(self):
        files = web.input(file_path={})

        if 'file_path' in files:
            """设置服务器端目录"""
            homedir = os.getcwd()
            filedir = '%s/static/upload/voice' %homedir
            
            """获取文件后缀，并以时间更改文件名"""
            filepath=files.file_path.replace('\\','/')
            ext=filepath.split('.', 1)[1]

            now=datetime.datetime.now()
            t ="%d%d%d%d%d%d" %(now.year,now.month,now.day,now.hour,now.minute,now.second)
            
            file_name = t+'.'+ext
            """从本地读取文件二进制流并传输至服务端"""
            
            try:
                with open(files.file_path, 'rb') as f_in:
                    data = f_in.read()
                f_in.close()

                with open(filedir+'/'+file_name, 'wb') as f_out:
                    f_out.write(data)
                f_out.close()
            except:
                return sr.show_result_fail() 
            
            return '/static/upload/voice/'+file_name
        
app_file_upload = web.application(urls, locals())
