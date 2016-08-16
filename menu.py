# -*- coding: utf-8 -*-

import time
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from cadastro_cliente import *


class menu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(330, 200, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label1.setFont(font)
        self.label1.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuCadastro = QtWidgets.QMenu(self.menubar)
        self.menuCadastro.setObjectName("menuCadastro")
        self.menuEstoque = QtWidgets.QMenu(self.menubar)
        self.menuEstoque.setObjectName("menuEstoque")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionCliente = QtWidgets.QAction(MainWindow)
        self.actionCliente.setObjectName("actionCliente")
        self.actionCliente.setShortcut("Ctrl+C")

        self.actionCliente.triggered.connect(self.cadastro_lista)

        self.actionProtudos = QtWidgets.QAction(MainWindow)
        self.actionProtudos.setObjectName("actionProtudos")
        self.actionProtudos.setShortcut("Ctrl+P")
        self.actionProtudos.triggered.connect(self.form_produto)


        self.actionSitua_ao = QtWidgets.QAction(MainWindow)
        self.actionSitua_ao.setObjectName("actionSitua_ao")


        self.actionAviamentos = QtWidgets.QAction(MainWindow)
        self.actionAviamentos.setObjectName("actionAviamentos")
        self.actionAviamentos.setShortcut("Ctrl+A")
        self.actionAviamentos.triggered.connect(self.form_aviamentos)

        self.menuCadastro.addAction(self.actionCliente)

        self.menuCadastro.addAction(self.actionProtudos)
        self.menuCadastro.addAction(self.actionAviamentos)
        self.menuEstoque.addAction(self.actionSitua_ao)
        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuEstoque.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def bd_conexao(self):
        self.conexao = sqlite3.connect('eh.db')
        self.cursor = self.conexao.cursor()

    def clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.comboBox.clear()
        self.lineEdit_3.clear()
        self.lineEdit_6.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_7.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.lineEdit_id_cliente.clear()
        self.textEdit.clear()


    def cadastro_lista(self, MainWindow):
        self.dialog_lista_cliente = QtWidgets.QDialog()
        self.dialog_lista_cliente.setObjectName("Lista_clientes")
        self.dialog_lista_cliente.setWindowTitle("Lista clientes")
        self.dialog_lista_cliente.resize(640, 480)

        self.pesquisa_entrada = QtWidgets.QLineEdit(self.dialog_lista_cliente)
        self.pesquisa_entrada.setGeometry(QtCore.QRect(30, 40, 441, 31))
        self.pesquisa_entrada.setObjectName("pesquisa_entrada")


        self.pushButton_pesquisar = QtWidgets.QPushButton(self.dialog_lista_cliente)
        self.pushButton_pesquisar.setGeometry(QtCore.QRect(500, 40, 115, 32))
        self.pushButton_pesquisar.setObjectName("pushButton_pesquisar")
        self.pushButton_pesquisar.setText("Pesquisar")

        self.listWidget_clientes = QtWidgets.QListWidget(self.dialog_lista_cliente)
        self.listWidget_clientes.setGeometry(QtCore.QRect(30, 141, 441, 221))
        self.listWidget_clientes.setObjectName("listWidget_clientes")

        self.listagem = self.cursor.execute("SELECT nome FROM clientes").fetchall()

        for i in self.listagem:
            print (i)
            self.listWidget_clientes.addItem("%s" % (i))


        self.pushButton_adicionar = QtWidgets.QPushButton(self.dialog_lista_cliente)
        self.pushButton_adicionar.setGeometry(QtCore.QRect(200, 380, 115, 32))
        self.pushButton_adicionar.setObjectName("pushButton_adicionar")
        self.pushButton_adicionar.setText("Novo Cliente")
        self.pushButton_adicionar.clicked.connect(self.form_cadastro)


        self.pushButton_alterar = QtWidgets.QPushButton(self.dialog_lista_cliente)
        self.pushButton_alterar.setGeometry(QtCore.QRect(500, 190, 115, 32))
        self.pushButton_alterar.setObjectName("pushButton_alterar")
        self.pushButton_alterar.setText("Alterar")
        self.pushButton_alterar.clicked.connect(self.pesquisando_cliente)

        self.pushButton_excluir = QtWidgets.QPushButton(self.dialog_lista_cliente)
        self.pushButton_excluir.setGeometry(QtCore.QRect(500, 270, 115, 32))
        self.pushButton_excluir.setObjectName("pushButton_excluir")
        self.pushButton_excluir.setText("Excluir")
        self.pushButton_excluir.clicked.connect(self.excluir)

        self.dialog_lista_cliente.show()


    def form_cadastro(self, MainWindow):

        self.dialog = QtWidgets.QDialog()
        self.dialog.setObjectName("Dialog")
        self.dialog.setWindowTitle('Cadastro de cliente')
        self.dialog.resize(832, 532)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.dialog)

        # label do nome
        self.label = QtWidgets.QLabel(self.dialog)
        self.label.setGeometry(QtCore.QRect(20, 80, 59, 16))
        self.label.setObjectName("label")
        self.label.setText('Nome:')

        # label do cpf e cnpj
        self.label_2 = QtWidgets.QLabel(self.dialog)
        self.label_2.setGeometry(QtCore.QRect(420, 80, 59, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Cpf/Cnpj:")

        # label do tipo
        self.label_3 = QtWidgets.QLabel(self.dialog)
        self.label_3.setGeometry(QtCore.QRect(560, 80, 59, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Tipo:")

        # entrada do nome
        self.lineEdit = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 100, 331, 21))
        self.lineEdit.setObjectName("lineEdit_nome")

        # entrada do cpf ou cnpj
        self.lineEdit_2 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 100, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_cpf")

        # caixa de escolha
        self.comboBox = QtWidgets.QComboBox(self.dialog)
        self.comboBox.setGeometry(QtCore.QRect(560, 100, 131, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Pessoa")
        self.comboBox.addItem("Empresa")
        self.comboBox.addItem("Representante")

        # label do email
        self.label_4 = QtWidgets.QLabel(self.dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 59, 16))
        self.label_4.setObjectName("label_email")
        self.label_4.setText('Email:')

        # entrada do email
        self.lineEdit_3 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 150, 331, 21))
        self.lineEdit_3.setObjectName("lineEdit_email")

        # label do endereco
        self.label_5 = QtWidgets.QLabel(self.dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 71, 16))
        self.label_5.setObjectName("label_endereco")
        self.label_5.setText('Endereço:')

        # label do complemento
        self.label_6 = QtWidgets.QLabel(self.dialog)
        self.label_6.setGeometry(QtCore.QRect(420, 180, 101, 16))
        self.label_6.setObjectName("label_complemento")
        self.label_6.setText('Complemento:')

        # entrada do endereco
        self.lineEdit_4 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 200, 331, 21))
        self.lineEdit_4.setObjectName("lineEdit_endereco")


        # entrada do complemento
        self.lineEdit_5 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(420, 200, 121, 21))
        self.lineEdit_5.setObjectName("lineEdit_complemento")


        # label do telefone
        self.label_7 = QtWidgets.QLabel(self.dialog)
        self.label_7.setGeometry(QtCore.QRect(420, 130, 59, 16))
        self.label_7.setObjectName("label_telefone")
        self.label_7.setText('Telefone:')


        # entrada do telefone
        self.lineEdit_6 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(420, 150, 141, 21))
        self.lineEdit_6.setObjectName("lineEdit_telefone")

        # label do bairro
        self.label_8 = QtWidgets.QLabel(self.dialog)
        self.label_8.setGeometry(QtCore.QRect(570, 180, 59, 16))
        self.label_8.setObjectName("label_8")
        self.label_8.setText('Bairro:')

        # entrada do bairro
        self.lineEdit_7 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(570, 200, 171, 21))
        self.lineEdit_7.setObjectName("lineEdit_bairro")

        '''# linha de divisao
        self.line_2 = QtWidgets.QFrame(self.dialog)
        self.line_2.setGeometry(QtCore.QRect(-10, 60, 851, 16))
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")'''


        # botao de pesquisa
        '''self.pushButton = QtWidgets.QPushButton(self.dialog)
        self.pushButton.setGeometry(QtCore.QRect(650, 20, 115, 32))
        self.pushButton.setObjectName("Pesquisa")
        self.pushButton.setText('Pesquisar')
        self.pushButton.clicked.connect(self.pesquisando_cliente)'''



        # entrada da pesquisa
        '''self.lineEdit_8 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(52, 20, 571, 31))
        self.lineEdit_8.setObjectName("lineEdit_pesquisa")'''

        # label da cidade
        self.label_9 = QtWidgets.QLabel(self.dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 230, 59, 16))
        self.label_9.setObjectName("label_cidade")
        self.label_9.setText('Cidade:')

        # label do estado
        self.label_10 = QtWidgets.QLabel(self.dialog)
        self.label_10.setGeometry(QtCore.QRect(210, 230, 59, 16))
        self.label_10.setObjectName("label_Estado")
        self.label_10.setText('Estado:')

        # label do cep
        self.label_11 = QtWidgets.QLabel(self.dialog)
        self.label_11.setGeometry(QtCore.QRect(420, 230, 59, 16))
        self.label_11.setObjectName("label_cep")
        self.label_11.setText('Cep:')

        # entrada da cidade
        self.lineEdit_9 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(20, 250, 113, 21))
        self.lineEdit_9.setObjectName("lineEdit_cidade")

        # entrada do estado
        self.lineEdit_10 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(210, 250, 113, 21))
        self.lineEdit_10.setObjectName("lineEdit_estado")

        # entrada do cep
        self.lineEdit_11 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(420, 250, 113, 21))
        self.lineEdit_11.setObjectName("lineEdit_cep")

        # label do contato
        self.label_12 = QtWidgets.QLabel(self.dialog)
        self.label_12.setGeometry(QtCore.QRect(20, 290, 59, 16))
        self.label_12.setObjectName("label_contato")
        self.label_12.setText('Contato:')

        # entrada do contato
        self.lineEdit_12 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_12.setGeometry(QtCore.QRect(20, 310, 113, 21))
        self.lineEdit_12.setObjectName("lineEdit_contato")

        # label dos comentarios
        self.label_13 = QtWidgets.QLabel(self.dialog)
        self.label_13.setGeometry(QtCore.QRect(20, 340, 101, 16))
        self.label_13.setObjectName("label_comentarios")
        self.label_13.setText('Comentarios:')

        # entrada dos comentatios
        self.textEdit = QtWidgets.QTextEdit(self.dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 360, 601, 78))
        self.textEdit.setObjectName("textEdit_comentarios")

        # botao para adicionar no banco
        self.pushButton_2 = QtWidgets.QPushButton(self.dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 450, 115, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText('Adicionar')
        self.pushButton_2.clicked.connect(self.adicionar)

        # botao para fazer alteracao
        self.pushButton_3 = QtWidgets.QPushButton(self.dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 450, 115, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText('Alterar')
        self.pushButton_3.clicked.connect(self.alterar)

        # botao para excluir cliente
        self.pushButton_4 = QtWidgets.QPushButton(self.dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 450, 115, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setText('Excluir')
        self.pushButton_4.clicked.connect(self.excluir)

        # id numero de identificacao
        self.label_id = QtWidgets.QLabel(self.dialog)
        self.label_id.setGeometry(QtCore.QRect(710,80,59,16))
        self.label_id.setObjectName("Label_id")
        self.label_id.setText("Id:")

        # entrada do id
        self.lineEdit_id_cliente = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_id_cliente.setGeometry(QtCore.QRect(710,100,61,21))
        self.lineEdit_id_cliente.setObjectName("lineEdit_id_cliente")




        self.dialog.show()




        print("chamando")

    def adicionar(self):
        self.nome_cliente = self.lineEdit.text()
        self.cpf_cnpj_cliente = self.lineEdit_2.text()
        self.tipo_cliente = self.comboBox.currentText()
        self.email_cliente = self.lineEdit_3.text()
        self.telefone_cliente = self.lineEdit_6.text()
        self.endereco_cliente = self.lineEdit_4.text()
        self.complemento_cliente = self.lineEdit_5.text()
        self.bairro_cliente = self.lineEdit_7.text()
        self.cidade_cliente = self.lineEdit_9.text()
        self.estado_cliente = self.lineEdit_10.text()
        self.cep_cliente = self.lineEdit_11.text()
        self.contato_cliente = self.lineEdit_12.text()
        self.comentarios_cliente = self.textEdit.toPlainText()


        self.dados_clientes = [[self.nome_cliente, self.cpf_cnpj_cliente, self.tipo_cliente, self.telefone_cliente,  self.endereco_cliente, self.complemento_cliente, self.bairro_cliente, self.cidade_cliente, self.estado_cliente, self.cep_cliente, self.contato_cliente,self.comentarios_cliente ,self.email_cliente]]

        self.cursor.executemany("""INSERT INTO clientes (nome, cpf_cnpj, tipo, telefone, endereco, complemento, bairro, cidade, estado, cep, contato, comentarios, email) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""", self.dados_clientes)
        self.conexao.commit()


        print('Nome: %s , Cpf/Cnpj: %s ,Tipo: %s , Email: %s , Telefone: %s , Endereço: %s , Complemento: %s , Bairro: %s , Cidade: %s , Estado: %s , Cep: %s , Contato: %s , Comentarios: %s ' % (self.nome_cliente, self.cpf_cnpj_cliente,self.tipo_cliente, self.email_cliente, self.telefone_cliente, self.endereco_cliente, self.complemento_cliente, self.bairro_cliente, self.cidade_cliente, self.estado_cliente, self.cep_cliente, self.contato_cliente, self.comentarios_cliente))

        print('adicionar')

        time.sleep(2)
        self.clear()


    def alterar(self):
        print('alterado')

    def pesquisando_cliente(self):
        self.form_cadastro(MainWindow)

        #self.dialog.show()

        self.valor = self.listWidget_clientes.currentItem().text()

        self.pesquisa = self.cursor.execute("SELECT nome from clientes WHERE nome='%s' " % (self.valor)).fetchone()

        if self.pesquisa != None:



            self.filtro = self.cursor.execute("""SELECT nome, cpf_cnpj, tipo, telefone, endereco, complemento, bairro, cidade, estado, cep, contato, comentarios, email FROM clientes where nome='%s' """ %(self.valor)).fetchall()

            self.filtro_nome = self.cursor.execute("""SELECT nome FROM clientes WHERE nome='%s' """ %(self.valor)).fetchone()
            self.filtro_cpf_cnpj = self.cursor.execute("""SELECT cpf_cnpj FROM clientes WHERE nome='%s' """ %(self.valor)).fetchone()
            self.filtro_id = self.cursor.execute("""SELECT cliente_id FROM clientes WHERE nome='%s' """ % (self.valor)).fetchone()
            self.filtro_tipo = self.cursor.execute("""SELECT tipo FROM clientes WHERE nome='%s' """ % (self.valor)).fetchone()
            self.filtro_email = self.cursor.execute("""SELECT email FROM clientes WHERE nome='%s' """ % (self.valor)).fetchone()
            self.filtro_telefone = self.cursor.execute("""SELECT telefone FROM clientes WHERE nome='%s' """ % (self.valor)).fetchone()
            self.filtro_endereco = self.cursor.execute("""SELECT endereco FROM clientes WHERE nome='%s' """ % (self.valor)).fetchone()
            self.filtro_complemento = self.cursor.execute("""SELECT complemento FROM clientes WHERE nome='%s' """ %(self.valor)).fetchone()
            self.filtro_bairro = self.cursor.execute("""SELECT bairro FROM clientes WHERE nome='%s' """ %(self.valor)).fetchone()
            self.filtro_cidade = self.cursor.execute("""SELECT cidade FROM clientes WHERE nome='%s' """ %(self.valor)).fetchone()
            self.filtro_estado = self.cursor.execute("""SELECT estado FROM clientes WHERE nome='%s' """ %(self.valor)).fetchone()
            self.filtro_cep = self.cursor.execute("""SELECT cep FROM clientes WHERE nome='%s' """ %(self.valor)).fetchone()
            self.filtro_contato = self.cursor.execute("""SELECT contato FROM clientes WHERE nome='%s' """ % (self.valor)).fetchone()
            self.filtro_comentarios = self.cursor.execute(""" SELECT comentarios FROM clientes WHERE nome='%s' """ % (self.valor)).fetchone()





            self.lineEdit.setText("%s" % (self.filtro_nome))
            self.lineEdit_2.setText("%s" %(self.filtro_cpf_cnpj))
            self.lineEdit_id_cliente.setText("%d" %(self.filtro_id))
            self.comboBox.setCurrentText("%s" %(self.filtro_tipo))
            self.lineEdit_3.setText("%s" % (self.filtro_email))
            self.lineEdit_6.setText("%s" % (self.filtro_telefone))
            self.lineEdit_4.setText("%s" % (self.filtro_endereco))
            self.lineEdit_5.setText("%s" % (self.filtro_complemento))
            self.lineEdit_7.setText("%s" % (self.filtro_bairro))
            self.lineEdit_9.setText("%s" % (self.filtro_cidade))
            self.lineEdit_10.setText("%s" % (self.filtro_estado))
            self.lineEdit_11.setText("%s" % (self.filtro_cep))
            self.lineEdit_12.setText("%s" % (self.filtro_contato))
            self.textEdit.setPlainText("%s" % (self.filtro_comentarios))




            print (self.filtro)
            print (self.filtro_nome)


        else:
            print ('nada encontrado')

        #print ('pesquisando')
        #print (self.pesquisa)

    def excluir(self):
        self.selecionado = self.listWidget_clientes.currentItem().text()
        print(self.selecionado)

        self.filtro_id = self.cursor.execute("""SELECT cliente_id FROM clientes WHERE nome='%s' """ % (self.selecionado)).fetchone()

        self.cursor.execute("""DELETE from clientes WHERE cliente_id='%s' """ % (self.filtro_id))

        #print (self.filtro_id)
        self.conexao.commit()
        #print('Excluido')
        #self.clear()





    def form_produto(self, MainWindow):
        self.dialog_produto = QtWidgets.QDialog()
        self.dialog_produto.setObjectName("Dialog")
        self.dialog_produto.setWindowTitle('Cadastro de Produtos')
        self.dialog_produto.resize(832, 532)

        self.dialog_produto.show()

    def form_aviamentos(self, MainWindow):
        self.dialog_aviamentos = QtWidgets.QDialog()
        self.dialog_aviamentos.setObjectName("Dialog")
        self.dialog_aviamentos.setWindowTitle('Cadastro_de_Aviamentos')
        self.dialog_aviamentos.resize(768, 427)

        self.label_codigo = QtWidgets.QLabel(self.dialog_aviamentos)
        self.label_codigo.setGeometry(QtCore.QRect(80, 30, 59, 16))
        self.label_codigo.setObjectName("label_codigo")
        self.label_codigo.setText('Codigo:')

        self.lineEdit = QtWidgets.QLineEdit(self.dialog_aviamentos)
        self.lineEdit.setGeometry(QtCore.QRect(80, 60, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.labe_aviamento = QtWidgets.QLabel(self.dialog_aviamentos)
        self.labe_aviamento.setGeometry(QtCore.QRect(250, 30, 121, 16))
        self.labe_aviamento.setObjectName("labe_aviamento")
        self.labe_aviamento.setText("Nome Aviamento:")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.dialog_aviamentos)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 60, 401, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_fornecedor = QtWidgets.QLabel(self.dialog_aviamentos)
        self.label_fornecedor.setGeometry(QtCore.QRect(80, 100, 81, 16))
        self.label_fornecedor.setObjectName("label_fornecedor")
        self.label_fornecedor.setText("Fornecedor:")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.dialog_aviamentos)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 130, 571, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_valor = QtWidgets.QLabel(self.dialog_aviamentos)
        self.label_valor.setGeometry(QtCore.QRect(80, 170, 41, 16))
        self.label_valor.setObjectName("label_valor")
        self.label_valor.setText("Valor:")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.dialog_aviamentos)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 190, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_unidade = QtWidgets.QLabel(self.dialog_aviamentos)
        self.label_unidade.setGeometry(QtCore.QRect(530, 190, 61, 21))
        self.label_unidade.setObjectName("label_unidade")
        self.label_unidade.setText("Unidade:")

        self.comboBox = QtWidgets.QComboBox(self.dialog_aviamentos)
        self.comboBox.setGeometry(QtCore.QRect(600, 190, 121, 21))
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Unitaria")
        self.comboBox.addItem("Metrica")

        self.label_observacoes = QtWidgets.QLabel(self.dialog_aviamentos)
        self.label_observacoes.setGeometry(QtCore.QRect(80, 230, 91, 16))
        self.label_observacoes.setObjectName("label_observacoes")
        self.label_observacoes.setText('Observações:')

        self.Button_adicionar_fornecedor = QtWidgets.QPushButton(self.dialog_aviamentos)
        self.Button_adicionar_fornecedor.setGeometry(QtCore.QRect(680, 130, 21, 21))
        self.Button_adicionar_fornecedor.setObjectName("Button_adicionar_fornecedor")
        self.Button_adicionar_fornecedor.setText("+")

        self.textEdit = QtWidgets.QTextEdit(self.dialog_aviamentos)
        self.textEdit.setGeometry(QtCore.QRect(80, 260, 381, 91))
        self.textEdit.setObjectName("textEdit")

        self.pushButton_salvar = QtWidgets.QPushButton(self.dialog_aviamentos)
        self.pushButton_salvar.setGeometry(QtCore.QRect(590, 280, 115, 32))
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        self.pushButton_salvar.setText("Salvar")


        self.dialog_aviamentos.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eh design!"))
        self.label1.setText(_translate("MainWindow", "Eh design!"))
        self.menuCadastro.setTitle(_translate("MainWindow", "Cadastro"))
        self.menuEstoque.setTitle(_translate("MainWindow", "Estoque"))
        self.actionCliente.setText(_translate("MainWindow", "Cliente"))

        self.actionProtudos.setText(_translate("MainWindow", "Protudos"))
        self.actionSitua_ao.setText(_translate("MainWindow", "Situaçao"))
        self.actionAviamentos.setText(_translate("MainWindow", "Aviamentos"))









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = menu()

    ui.setupUi(MainWindow)
    ui.bd_conexao()
    MainWindow.show()
    sys.exit(app.exec_())
