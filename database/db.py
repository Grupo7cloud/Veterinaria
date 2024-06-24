import pymysql

db_host = 'instance-veterinaria.c18as8u80819.us-east-1.rds.amazonaws.com'
db_user = 'siete'
db_password = '987654321'
db_database = 'db_cym'
db_table = 'users'

def connectionSQL():
    try:
        connection_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_database
            )
        print("Successfull connection to the database")
        return connection_sql
    except Exception as err:
        print("Error connecting to the database")
        print(err)
        return None
        
def add_user(id, Nombre, Apellido, Telefono, Correo, Nombre_Mascota):
    instruction_sql = "INSERT INTO " + db_table + " (id, Nombre, Apellido, Telefono, Correo, Nombre_Mascota) VALUES ("+id+", '"+Nombre+"', '"+Apellido+"', '"+Telefono+"', '"+Correo+"', '"+Nombre_Mascota+"')"
    connection_sql = connectionSQL()
    try:
        if connection_sql != None:
            cursor = connection_sql.cursor()
            cursor.execute(instruction_sql)
            connection_sql.commit() 
            print("User added")
            return True
        else:
            print("Error connecting to th database")
            return False
    except Exception as err:
        print("Error creating the user")
        print(err)
        return False
        
def consult_user(id):
    instruction_sql = "SELECT * FROM users WHERE id = " +id
    connection_sql = connectionSQL()
    try:
        cursor = connection_sql.cursor()
        cursor.execute(instruction_sql)
        result_data = cursor.fetchall()
        print(result_data)
    except Exception as err:
        print("Error", err)
        
        
