# -*- coding:UTF-8 -*-

from Tkinter import *
import ttk, MySQLdb

class Programa(Frame):
	def __init__(self, master):
		self.master = master
		master.title("Eh design")
		self.login()
		self.conexaoBanco()
		self.barraTop()




	def conexaoBanco(self):
		BANCO = 'ehdesign'
		USER ='root'
		PASSWD=''
		HOST='127.0.0.1'

		try:
			conexao = MySQLdb.connect(db=BANCO,user=USER,passwd=PASSWD,host=HOST)
			cursor = conexao.cursor()
			usuario = self.usuario_entrada.get()
			senha = self.senha_entrada.get()
			sql = "select * from usuarios where usuario like '"+usuario+"' and senha like '"+senha+"'"
			cursor.execute(sql)
			valido = cursor.fetchall()
			#print 'conectou essa caralha'
			#print("Numero de usuarios validos:  "+str(len(valido)))

			if str(len(valido)) == '1':
				self.frame_logo.destroy()
				self.frame_login.destroy()
				self.barraTop()
				self.inicio()


		except MySQLdb as erro:
			print ('Deu merda',erro)
		return conexao

	def barraTop(self):
		menubar = Menu(self.master)
		self.master.config(menu=menubar)
		self.filemenu = Menu(self.master, tearoff=0)

		self.filemenu.add_command(label="Cadastro Pessoas/Empresas", command=self.cadastroPessoasClientes)
		self.filemenu.add_command(label="Cadastro Matéria-Prima", command=self.representantes)
		self.filemenu.add_command(label="Cadastro de Produtos", command=self.fornecedores)

		self.filemenu.add_command(label="Exit", command=self.fechar)
		menubar.add_cascade(label="Cadastro", menu=self.filemenu)

	def login(self):


		self.frame_logo = Frame(self.master)
		self.frame_logo.grid(row=1,columnspan=10,padx=315,pady=100)
		self.photo = PhotoImage(file='img/logo.gif')
		self.logo_eh = Label(self.frame_logo)
		self.logo_eh['image'] = self.photo
		self.logo_eh.grid()


		self.frame_login = Frame(self.master)
		self.frame_login.grid(row=2,column=4,padx=340)


		self.usuario = Label(self.frame_login, text='Usuário')
		self.usuario.grid(row=1,column=1)
		self.usuario_entrada = Entry(self.frame_login)
		self.usuario_entrada.grid(row=1,column=2)

		self.senha = Label(self.frame_login, text='Senha')
		self.senha.grid(row=2,column=1)
		self.senha_entrada = Entry(self.frame_login,show='*')
		self.senha_entrada.grid(row=2,column=2)

		self.botao_login = Button(self.frame_login,text="Login",command=self.conexaoBanco)


		self.botao_login.grid(row=3,column=2)

	def fornecedores(self):
		pass

	def clientes(self):
		pass

	def cadastroPessoasClientes(self):
		self.frame_inicio.destroy()

		self.frame_cadastro = Frame(self.master)
		self.frame_cadastro.grid()

		self.entry_pesquisa = Entry(self.frame_cadastro)
		self.entry_pesquisa.grid(row=1,column=1,padx=30,pady=15)

		self.btn_pesquisa = Button(self.frame_cadastro, text='Pesquisar')
		self.btn_pesquisa.grid(row=1,column=2,sticky=W)

		self.separador = Frame(self.frame_cadastro, height=2,bd=3,relief=SUNKEN,width=900)
		self.separador.grid(row=2,columnspan=20) #divisao da tela em 20 partes

		self.labelTipo = Label(self.frame_cadastro, text='Tipo :')
		self.labelTipo.grid(row=3,column=1,pady=15,sticky=W)

		self.lbl_tipo = Label(self.frame_cadastro, text='Tipo')
		self.lbl_tipo.grid(row=3,column=1,pady=15,sticky=E)



		self.combobox_tipo = ttk.Combobox(self.lbl_tipo, values=['Pessoa','Empresa','Representante'],state='readonly',width=20)
		self.combobox_tipo.current(1)
		self.combobox_tipo.grid()

		self.codigo = Label(self.frame_cadastro, text='Código :')
		self.codigo.grid(row=3,column=2,sticky=W)
		self.codigo_entrada = Entry(self.frame_cadastro,width=4)
		self.codigo_entrada.grid(row=3,column=2,sticky=E)

		self.cpf_cnpj = Label(self.frame_cadastro, text='Cpf/Cnpj :')
		self.cpf_cnpj.grid(row=3,column=3)
		self.cpf_cnpj_entrada = Entry(self.frame_cadastro)
		self.cpf_cnpj_entrada.grid(row=3,column=4)

		self.nome = Label(self.frame_cadastro, text='Nome :')
		self.nome.grid(row=4,column=1,sticky=W)
		self.nome_entrada = Entry(self.frame_cadastro, width=32)
		self.nome_entrada.grid(row=4,columnspan=3,sticky=E)

		self.telefone = Label(self.frame_cadastro, text='Telefone :')
		self.telefone.grid(row=4,column=3)
		self.telefone_entrada = Entry(self.frame_cadastro, width=13)
		self.telefone_entrada.grid(row=4,column=4)

		self.endereco = Label(self.frame_cadastro, text='Endereço :')
		self.endereco.grid(row=5,column=1,sticky=W)
		self.endereco_entrada = Entry(self.frame_cadastro, width=32)
		self.endereco_entrada.grid(row=5,columnspan=3,sticky=E)

		self.complemento = Label(self.frame_cadastro, text='Complemento :')
		self.complemento.grid(row=5,column=3)
		self.complemento_entrada = Entry(self.frame_cadastro, width=13)
		self.complemento_entrada.grid(row=5,column=4)

		self.bairro = Label(self.frame_cadastro, text='Bairro :')
		self.bairro.grid(row=6,column=1,sticky=W)
		self.bairro_entrada = Entry(self.frame_cadastro, width=12)
		self.bairro_entrada.grid(row=6,column=1)

		self.cep = Label(self.frame_cadastro, text='CEP :')
		self.cep.grid(row=6,column=2)
		self.cep_entrada = Entry(self.frame_cadastro, width=13)
		self.cep_entrada.grid(row=6,columnspan=4,sticky=E)

		self.cidade = Label(self.frame_cadastro, text='Cidade :')
		self.cidade.grid(row=7,column=1,sticky=W)
		self.cidade_entrada = Entry(self.frame_cadastro, width=12)
		self.cidade_entrada.grid(row=7,column=1)

		self.estado = Label(self.frame_cadastro, text='Estado :')
		self.estado.grid(row=7,column=2)
		self.estado_entrada = Entry(self.frame_cadastro, width=13)
		self.estado_entrada.grid(row=7,columnspan=4,sticky=E)

		self.email = Label(self.frame_cadastro, text='Email :')
		self.email.grid(row=8,column=1,sticky=W)
		self.email_entrada = Entry(self.frame_cadastro, width=45)
		self.email_entrada.grid(row=8,columnspan=4,sticky=E)

		self.contato = Label(self.frame_cadastro, text='Contato :')
		self.contato.grid(row=9,column=1,sticky=W)
		self.contato_entrada = Entry(self.frame_cadastro, width=32)
		self.contato_entrada.grid(row=9,columnspan=3,sticky=E)

		self.observacao = Label(self.frame_cadastro, text='Observação :')
		self.observacao.grid(row=10,column=1,sticky=W)
		self.observacao_entrada = Entry(self.frame_cadastro, width=65)
		self.observacao_entrada.grid(row=10,columnspan=8,sticky=E)

		self.btn_salvar = Button(self.frame_cadastro, text="Salvar")
		self.btn_salvar.grid(row=15,column=8)

		self.btn_alterar = Button(self.frame_cadastro, text="Alterar")
		self.btn_alterar.grid(row=15, column=9)

		self.btn_excluir = Button(self.frame_cadastro, text="Excluir")
		self.btn_excluir.grid(row=15,column=10)


	def representantes(self):
		pass

	def situacao(self):
		pass

	def fechar(self):
		self.master.destroy()


	def inicio(self):
		self.frame_inicio = Frame(self.master)
		self.label_inicio = Label(self.frame_inicio)
		self.frame_inicio.grid()
		self.image = PhotoImage(file='img/logo.gif')
		self.label_inicio['image'] = self.image
		self.label_inicio.grid(row=1,column=1,padx=350,pady=250)






tela = Tk()
eh_program = Programa(tela)
tela.geometry("900x600+200+100")
tela.mainloop()
