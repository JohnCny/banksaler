import settings

class Authorization:

    def authenticate(auth_key):
        myvar=dict(auth_key=auth_key)
        result=settings.db.select('auth_key',myvar,where="auth_key=$auth_key")
        
        if len(result):
            return True
        else :
            return False

    
    def get_user_id(auth_key):
        myvar=dict(auth_key=auth_key)
        result=settings.db.select('auth_key',myvar,where="auth_key=$auth_key")
        
        if len(result):
            return result[0].user_id
        else :
            return None

    

    def get_permission_id(permission_name):
        myvar=dict(permission_name=permission_name)
        result=settings.db.select('permissions',myvar,where="permission_name=$permission_name")

        if len(result):
            return result[0].permission_id
        else :
            return None

    def authorization(auth_key,permission_name):
        user_id=get_user_id(auth_key)
        permission_id=get_permission_id(permission_name)

        if user_id is not None and permission_id is not None:
            myvar=dict(permission_name=permission_name,user_id=user_id)
            result=settings.db.select('user_permission',myvar,where="user_id=$user_id and permission_id=$permission_id")

            if len(result):
                return True
            else:
                return False
        else:
            return False
