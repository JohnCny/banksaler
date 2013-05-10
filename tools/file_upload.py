import web
import os


HERE = os.path.dirname(__file__)
BASE_PATH= os.path.join(HERE,'..')
IMG_PATH= os.path.join(BASE_PATH,'img')

urls=(
    '/img','upload_img',
    '/file','create_credit',
    '/video','manage_credit'
)

class upload_img:
    def POST(self):
        files = web.input(file_path={})
        filedir = IMG_PATH
        if 'file_path' in files:
            filepath=files.file_path.replace('\\','/')
            file_name=filepath.split('/')[-1]
            with open(files.file_path, 'rb') as f_in:
                data = f_in.read()
            f_in.close()
            
            with open(filedir+'/'+file_name, 'wb') as f_out:
                f_out.write(data)
            f_out.close()

            return r'img/'+file_name
            
        
        
app_file_upload = web.application(urls, locals())