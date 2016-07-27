# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from menu import *
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usuario_label = QtWidgets.QLabel(self.centralwidget)
        self.usuario_label.setGeometry(QtCore.QRect(370, 220, 59, 16))
        self.usuario_label.setObjectName("usuario_label")
        self.senha_label = QtWidgets.QLabel(self.centralwidget)
        self.senha_label.setGeometry(QtCore.QRect(370, 270, 59, 16))
        self.senha_label.setObjectName("senha_label")

        self.usuario_entrada = QtWidgets.QLineEdit(self.centralwidget)
        self.usuario_entrada.setGeometry(QtCore.QRect(340, 240, 113, 21))
        self.usuario_entrada.setText("")
        self.usuario_entrada.setObjectName("usuario_entrada")
        self.senha_entrada = QtWidgets.QLineEdit(self.centralwidget)
        self.senha_entrada.setGeometry(QtCore.QRect(340, 290, 113, 21))
        self.senha_entrada.setObjectName("senha_entrada")
        self.senha_entrada.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(290, 70, 221, 111))
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")

        
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(360, 340, 61, 32))
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.InputSenha)


        MainWindow.setCentralWidget(self.centralwidget)
        

       

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def InputSenha(self):
        login_us = self.usuario_entrada.text()
        senhaUs = self.senha_entrada.text()
        verificador = False


        conexao = sqlite3.connect('eh.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT nome FROM usuarios WHERE nome="%s"   ' %login_us )
        resultado1 = cursor.fetchone()

        '''
        x = print('Resultado da busca: %s' %resultado1)
        y = print('Nome usuario: %s' % login_us)
        #print('Senha usuario: %s' % senhaUs)


        if x == y :
            print('resultado dos nomes iguais')
            
        else:
            print('Resultado dos nomes diferentes ')
            

        cursor.execute('SELECT senha FROM usuarios WHERE senha="%s" ' %senhaUs)
        resultado2 = cursor.fetchone()

        w = print('Resultado da senha: %s' %resultado2)
        z = print('Senha campo: %s' %senhaUs)

        if w == z:
            print('Senhas iguais')
            
        else:
            print('Senhas diferentes')
            
        '''
        
        ui = menu()
        ui.setupUi(MainWindow)
        
  
       
        
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eh! Design"))
        self.usuario_label.setText(_translate("MainWindow", "Usuário"))
        self.senha_label.setText(_translate("MainWindow", "Senha"))
        self.label_logo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/logo.png\"/></p></body></html>"))
        self.login_btn.setText(_translate("MainWindow", "Login"))



    def conexao():
        pass




#import img_rc


import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

