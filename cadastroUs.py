# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastroUs.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class cadastroUs(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 386)
        self.conexao_banco = self.conexao_bd()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(130, 10, 111, 16))
        self.titulo.setObjectName("titulo")
        self.label_usuario = QtWidgets.QLabel(self.centralwidget)
        self.label_usuario.setGeometry(QtCore.QRect(20, 60, 59, 16))
        self.label_usuario.setObjectName("label_usuario")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 140, 59, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 121, 16))
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 230, 115, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.requisicao)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 59, 16))
        self.label_3.setObjectName("label_3")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 60, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 100, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 140, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)



        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 180, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 300, 171, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "cadastro Eh!"))
        self.titulo.setText(_translate("MainWindow", "Cadastro Usuário"))
        self.label_usuario.setText(_translate("MainWindow", "Usuário:"))
        self.label.setText(_translate("MainWindow", "Senha:"))
        self.label_2.setText(_translate("MainWindow", "Confirmar Senha:"))
        self.pushButton.setText(_translate("MainWindow", "Cadastrar"))
        self.label_3.setText(_translate("MainWindow", "Telefone:"))
        self.label_4.setText(_translate("MainWindow", ""))

    def conexao_bd(self):
        self.conexao = sqlite3.connect('eh.db')
        self.cursor = self.conexao.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                   nome CHAR(50),
                                                                   telefone CHAR(15),
                                                                   senha CHAR(20))""")

        self.conexao.commit()

    def requisicao(self):
        self.nome = self.lineEdit.text()
        self.telefone = self.lineEdit_2.text()
        self.senha = self.lineEdit_3.text()
        self.con_senha = self.lineEdit_4.text()
        
        print (self.nome,self.telefone,self.senha,self.con_senha)
        

        if self.senha == self.con_senha:
            self.dados =[[self.nome,self.telefone,self.senha]]
            self.cursor.executemany("""INSERT INTO usuarios(nome,telefone,senha) VALUES (?,?,?)""", self.dados)
            self.conexao.commit()
            self.cursor.close()
            self.conexao.close()


            self.label_4.setText("Cadastrado com sucesso")

        else:    
            self.label_4.setText("A senha não confere")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = cadastroUs()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


