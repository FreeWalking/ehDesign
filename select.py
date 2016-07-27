import sqlite3

conexao = sqlite3.connect("eh.db")
cursor = conexao.cursor()
pesquisa = cursor.execute("""SELECT * FROM clientes""")
resultado = cursor.fetchall()
print ('%s' %(resultado))