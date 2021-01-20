import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="root",
auth_plugin='mysql_native_password',
database='main',
autocommit=True
)

def mysql_val(cpf_v, nome_v, senha_v):
    c = mydb.cursor()
    c.execute("""select cpf, nome, senha from users where 
    cpf = '{}' and
    nome = '{}' and
    senha = '{}'""".format(cpf_v, nome_v, senha_v))
    data = c.fetchall()

    if len(data) == 0:
        return None
    else:
        c.execute("select `id`, `setor` from `users` where cpf = '{}'".format(cpf_v))
        user_id = c.fetchone()
        return user_id

def mysql_files(cpf_v):
    e = mydb.cursor()
    e.execute("select `id` from `users` where cpf = '{}'".format(cpf_v))
    var_id = e.fetchone()
    e.execute("select * from files where id <= {} order by id desc".format(var_id[0]))
    file_data = e.fetchall()
    mydb.close()
    return file_data