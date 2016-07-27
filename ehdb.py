import sqlite3


conexao = sqlite3.connect('eh.db')
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                      nome CHAR(50),
                                                      telefone CHAR(15),
                                                      senha CHAR(20))""")

cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
														nome VARCHAR(100),
														cpf_cnpj VARCHAR(50),
														tipo VARCHAR(20),
														telefone VARCHAR(15),
														endereco VARCHAR(255),
														complemento VARCHAR(100),
														bairro VARCHAR(50),
														cidade VARCHAR(50),
														estado varchar(50),
														cep VARCHAR(15),
														contato varchar(50),
														comentarios varchar(255))""")

conexao.commit()
cursor.close()
conexao.close()