# Authenticate User
def authenticate(username, password):
    
    db = database()
    
    try:
        with db.cursor() as cursor:
          sql = "SELECT username FROM users WHERE username ='{0}' AND password ='{1}'".format(username, password)
          cursor.execute(sql)
          result = cursor.fetchone()
          
    except Exception as e:
        print("auth: {}".format(e))
        
    finally:
        db.close()
        
    return result
    