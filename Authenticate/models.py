#coding:utf8
import settings
import md5

db=settings.db

class users:
    login_name=''
    login_password=''
    real_name=''
    mobile=''
    user_code=''
    is_active='' 

    def set_data(self,data):
        users.login_name=data['login_name']
        users.login_password=data['login_password']
        users.real_name=data['real_name']
        users.mobile=data['mobile']
        users.user_code=data['user_code']
        users.is_active=data['is_active']

        return users

    def get_users_by_id(self,id):
        return db.select('users', where='id=$id', vars=locals()).list()
    
    def users_login(self,login_name,login_password):
        myvar=dict(login_name=login_name,login_password=login_password)
        result=db.select('users',myvar,where="login_name=$login_name and login_password=$login_password")
        
        return result

    def get_users_name_by_org(self,org_id):
        result=db.select('users',where="id in (select users_id from org_users where org_id=$org_id)",
                         what="id,real_name",vars=locals()).list()
        return result

    def get_users_list_paged(self,offset,limit):
        result=db.select('users',what='id,real_name,user_code',offset=offset,limit=limit,vars=locals()).list()
        counts = db.query("SELECT COUNT(*) AS count FROM users")[0]
        pages = counts.count / limit
            
        if counts.count % limit > 0:
            pages += 1
            
        result.extend([{'pages':pages}])
        return result

    def create_users(self,users):
        login_password=md5.new(users.login_password).hexdigest()
        return db.insert('users',login_name=users.login_name,login_password=login_password,real_name=users.real_name,
                    mobile=users.mobile,user_code=users.user_code,is_active=users.is_active)

    def update_users(self,id,users):
        login_password=md5.new(users.login_password).hexdigest()
        return db.update('users',where="id=$id",login_password=login_password,
                real_name=users.real_name,mobile=users.mobile,
                user_code=users.user_code,is_active=users.is_active,vars=locals())

    def del_users(self,id):
        return db.delete('users',where="id=$id",vars=locals())


class role:
    role_name='' 

    def set_data(self,data):
        role.role_name=data['role_name']

        return role

    def get_role_by_id(self,id):
        return db.select('role', where='id=$id', vars=locals()).list()
     
    def get_role(self):
        return db.select('role').list()

    def get_role_list_paged(self,offset,limit):
        result=db.select('role',offset=offset,limit=limit,vars=locals()).list()
        counts = db.query("SELECT COUNT(*) AS count FROM role")[0]
        pages = counts.count / limit
            
        if counts.count % limit > 0:
            pages += 1
            
        result.extend([{'pages':pages}])
        return result

    def create_role(self,role):
        return db.insert('role',role_name=role.role_name)

    def update_role(self,id,role):
        return db.update('role',where="id=$id",role_name=role.role_name,vars=locals())

    def del_role(self,id):
        return db.delete('role',where="id=$id",vars=locals())

class operate:
    operate_name=''
    code_name=''
    parent_operate=''

    def set_data(self,data):
        operate.operate_name=data['operate_name']
        operate.code_name=data['code_name']
        operate.parent_operate=data['parent_operate']

        return operate

    def get_operate_by_id(self,id):
        return db.select('operate', where='id=$id', vars=locals()).list()
     
    def get_operate(self):
        return db.select('operate').list()

    def get_operate_list_paged(self,offset,limit):
        result=db.select('operate',offset=offset,limit=limit,vars=locals()).list()
        counts = db.query("SELECT COUNT(*) AS count FROM operate")[0]
        pages = counts.count / limit
            
        if counts.count % limit > 0:
            pages += 1
            
        result.extend([{'pages':pages}])
        return result

    def create_operate(self,operate):
        return db.insert('operate',operate_name=operate.operate_name,code_name=operate.code_name,
                parent_operate=operate.parent_operate)

    def update_operate(self,id,operate):
        return db.update('operate',where="id=$id",operate_name=operate.operate_name,code_name=operate.code_name,
                parent_operate=operate.parent_operate,vars=locals())

    def del_role(self,id):
        return db.delete('role',where="id=$id",vars=locals())

class orgnization:
    org_name=''
    org_parent='' 

    def set_data(self,data):
        orgnization.org_name=data['org_name']
        orgnization.org_parent=data['org_parent']
    
        return orgnization

    def get_orgnization_by_id(self,id):
        return db.select('orgnization', where='id=$id', vars=locals()).list()
     
    def get_orgnization(self):
        return db.select('orgnization').list()

    def get_orgnization_list_paged(self,offset,limit):
        result=db.select('orgnization',offset=offset,limit=limit,vars=locals()).list()
        counts = db.query("SELECT COUNT(*) AS count FROM orgnization")[0]
        pages = counts.count / limit
            
        if counts.count % limit > 0:
            pages += 1
            
        result.extend([{'pages':pages}])
        return result

    def create_orgnization(self,orgnization):
        return db.insert('orgnization',org_name=orgnization.org_name,org_parent=orgnization.org_parent)

    def update_orgnization(self,id,orgnization):
        return db.update('orgnization',where="id=$id",org_name=orgnization.org_name,
                org_parent=orgnization.org_parent,vars=locals())

    def del_orgnization(self,id):
        return db.delete('orgnization',where="id=$id",vars=locals())

class org_users:
    org_id=''
    users_id='' 

    def set_data(self,data):
        org_users.org_id=data['org_id']
        org_users.users_id=data['users_id']
    
        return org_users
    
    def check_users_in_org(self,org_id,users_id):
        result=db.select('org_users',where="org_id=$org_id",vars=locals()).list()
        return len(result)
    
    def get_org_by_users(self,users_id):
        return db.select('org_users',where="users_id=$users_id",vars=locals()).list()

    def get_users_by_org(self,org_id):
        return  db.select('org_users',where="org_id=$org_id",vars=locals()).list()


    def get_users_by_org_paged(self,offset,limit,org_id):
        result=db.select('org_users',where="org_id=$org_id",
                offset=offset,limit=limit,vars=locals()).list()
        counts = db.query("SELECT COUNT(*) AS count FROM org_users where org_id=$org_id",vars=locals())[0]
        pages = counts.count / limit
            
        if counts.count % limit > 0:
            pages += 1
            
        result.extend([{'pages':pages}])
        return result

    def create_org_users(self,org_users):
        return db.insert('org_users',org_id=org_users.org_id,users_id=org_users.users_id)

    def update_org_users(self,id,org_users):
        return db.update('org_users',where="id=$id",org_id=org_users.org_id,
                users_id=org_users.users_id,vars=locals())

    def del_org_users(self,id):
        return db.delete('org_users',where="id=$id",vars=locals())

class org_role:
    org_id=''
    role_id='' 

    def set_data(self,data):
        org_role.org_id=data['org_id']
        org_role.role_id=data['role_id']
    
        return org_role
    
    def get_role_by_org(self,org_id):
        return db.select('org_role',where="org_id=$org_id",vars=locals()).list()
        
        

    def get_role_by_org_paged(self,offset,limit,org_id):
        result=db.select('org_role',where="org_id=$org_id",
                offset=offset,limit=limit,vars=locals()).list()
        counts = db.query("SELECT COUNT(*) AS count FROM org_role where org_id=$org_id",vars=locals())[0]
        pages = counts.count / limit
            
        if counts.count % limit > 0:
            pages += 1
            
        result.extend([{'pages':pages}])
        return result

    def create_org_role(self,org_role):
        return db.insert('org_role',org_id=org_role.org_id,role_id=org_role.role_id)

    def update_org_role(self,id,org_role):
        return db.update('org_role',where="id=$id",org_id=org_role.org_id,
                role_id=org_role.role_id,vars=locals())

    def del_org_role(self,id):
        return db.delete('org_role',where="id=$id",vars=locals())

class users_role:
    users_id=''
    role_id='' 

    def set_data(self,data):
        users_role.users_id=data['users_id']
        users_role.role_id=data['role_id']
    
        return users_role
    
    def get_role_by_users(self,users_id):
        return db.select('users_role',where="users_id=$users_id",vars=locals()).list()
        
        

    def get_role_by_users_paged(self,offset,limit,users_id):
        result=db.select('users_role',where="users_id=$users_id",
                offset=offset,limit=limit,vars=locals()).list()
        counts = db.query("SELECT COUNT(*) AS count FROM users_role where users_id=$users_id",vars=locals())[0]
        pages = counts.count / limit
            
        if counts.count % limit > 0:
            pages += 1
            
        result.extend([{'pages':pages}])
        return result

    def create_users_role(self,users_role):
        return db.insert('users_role',users_id=users_role.users_id,role_id=users_role.role_id)

    def update_users_role(self,id,users_role):
        return db.update('users_role',where="id=$id",users_id=users_role.users_id,
                role_id=users_role.role_id,vars=locals())

    def del_users_role(self,id):
        return db.delete('users_role',where="id=$id",vars=locals())

class role_permission:
    permission_id=''
    role_id='' 

    def set_data(self,data):
        role_permission.permission_id=data['permission_id']
        role_permission.role_id=data['role_id']
    
        return role_permission
    
    def get_permission_by_role(self,role_id):
        return db.select('role_permission',where="role_id=$role_id",vars=locals()).list()

    def get_permission_by_role_paged(self,offset,limit,role_id):
        result=db.select('role_permission',where="role_id=$role_id",
                offset=offset,limit=limit,vars=locals()).list()
        counts = db.query("SELECT COUNT(*) AS count FROM role_permission where role_id=$role_id",vars=locals())[0]
        pages = counts.count / limit
            
        if counts.count % limit > 0:
            pages += 1
            
        result.extend([{'pages':pages}])
        return result

    def create_role_permission(self,role_permission):
        return db.insert('role_permission',permission_id=role_permission.permission_id,role_id=role_permission.role_id)

    def update_role_permission(self,id,role_permission):
        return db.update('role_permission',where="id=$id",permission_id=role_permission.permission_id,
                role_id=role_permission.role_id,vars=locals())

    def del_role_permission(self,id):
        return db.delete('role_permission',where="id=$id",vars=locals())

class auth_key:
    user_id=''
    auth_key='' 

    def set_data(self,data):
        auth_key.user_id=data['user_id']
        auth_key.auth_key=data['auth_key']
    
        return auth_key 
    
    def get_users_id(self,auth_key):
        return db.select('auth_key',where="auth_key=$auth_key",vars=locals()).list()
        

    def check_auth_key(self,auth_key):
        result=db.select('auth_key',where="auth_key=$auth_key",vars=locals()).list()
        return len(result)

    def create_auth_key(self,auth_key):
        return db.insert('auth_key',user_id=auth_key.user_id,auth_key=auth_key.auth_key)

    def update_auth_key(self,id,auth_key):
        return db.update('auth_key',where="id=$id",user_id=auth_key.user_id,
                auth_key=auth_key.auth_key,vars=locals())

    def del_auth_key(self,id):
        return db.delete('auth_key',where="id=$id",vars=locals())

class operate_permission:
    permission_id=''
    operate_id='' 

    def set_data(self,data):
        operate_permission.permission_id=data['permission_id']
        operate_permission.operate_id=data['operate_id']
    
        return operate_permission
    
    def get_operate_by_permission(self,permission_id):
        return db.select('operate_permission',where="permission_id=$permission_id",vars=locals()).list()

    def check_operate_in_permission(self,operate_id,permission_id):
        result=db.select('operate_permission',
                where="permission_id=$permission_id and operate_id=$operate_id",vars=locals()).list()
        return len(result)

    def get_permission_by_role_paged(self,offset,limit,role_id):
        result=db.select('operate_permission',where="permission_id=$permission_id",
                offset=offset,limit=limit,vars=locals()).list()
        counts = db.query("SELECT COUNT(*) AS count FROM operate_permission where permission_id=$permission_id",vars=locals())[0]
        pages = counts.count / limit
            
        if counts.count % limit > 0:
            pages += 1
            
        result.extend([{'pages':pages}])
        return result

    def create_operate_permission(self,operate_permission):
        return db.insert('operate_permission',permission_id=operate_permission.permission_id,operate_id=operate_permission.operate_id)

    def update_operate_permission(self,id,operate_permission):
        return db.update('operate_permission',where="id=$id",permission_id=operate_permission.permission_id,
                operate_id=operate_permission.operate_id,vars=locals())

    def del_operate_permission(self,id):
        return db.delete('operate_permission',where="id=$id",vars=locals())

