import sqlite3
from sqlite3 import Error
# Criando conexão com o banco de dados
def conexaobanco():

    local = 'D:\\usuario\\Documents\\projetof-_final_05\\cadastros.db'
    con= None
    try:
        con = sqlite3.connect(local)

    except Error as ex:
        print(ex)
    return con
#------------------------------------------------
conex = conexaobanco() 

# Criando tabela no banco
t_sql = """CREATE TABLE tb_cadastrados(
                    id_cadastrado integer primary key,
                    login_ varchar(30),
                    senha varchar(30),
                    login_2 varchar(30),
                    senha_2 varchar(30)               
                    );"""


def criandoTabela(conexao,sql):
    try:
        i = conexao.cursor()
        i.execute(sql)

    
    except Error as ex:
        print(ex)

criandoTabela(conex, t_sql)


conex.close()
