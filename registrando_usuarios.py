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

t_sql = """INSERT INTO tb_cadastrados
            (login_, senha, login_2, senha_2)
            VALUES('felipesilva@gmail.com','silva12', 'silvasantiago@gmail.com', 'flamengo_horrivel')"""
def inserindo(conexao, sql):
    try: 
        i = conexao.cursor()
        i.execute(sql)
        conexao.commit() # para fazer a persistênica do registro
    except Error as ex:
        print(ex)

inserindo(conex, t_sql)
