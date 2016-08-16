# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lista_clientes.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setAccessibleName("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pesquisa_entrada = QtWidgets.QLineEdit(self.centralwidget)
        self.pesquisa_entrada.setGeometry(QtCore.QRect(30, 40, 441, 31))
        self.pesquisa_entrada.setObjectName("pesquisa_entrada")
        self.pushButton_pesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pesquisar.setGeometry(QtCore.QRect(500, 40, 115, 32))
        self.pushButton_pesquisar.setObjectName("pushButton_pesquisar")

        self.listWidget_clientes = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_clientes.setGeometry(QtCore.QRect(30, 141, 441, 221))
        self.listWidget_clientes.setObjectName("listWidget_clientes")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_clientes.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_clientes.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_clientes.addItem(item)


        self.pushButton_adicionar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_adicionar.setGeometry(QtCore.QRect(200, 380, 115, 32))
        self.pushButton_adicionar.setObjectName("pushButton_adicionar")
        self.pushButton_alterar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_alterar.setGeometry(QtCore.QRect(500, 190, 115, 32))
        self.pushButton_alterar.setObjectName("pushButton_alterar")
        self.pushButton_excluir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_excluir.setGeometry(QtCore.QRect(500, 270, 115, 32))
        self.pushButton_excluir.setObjectName("pushButton_excluir")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_pesquisar.setText(_translate("MainWindow", "Pesquisar"))
        __sortingEnabled = self.listWidget_clientes.isSortingEnabled()
        self.listWidget_clientes.setSortingEnabled(False)

        item = self.listWidget_clientes.item(0)
        item.setText(_translate("MainWindow", "levy"))
        item = self.listWidget_clientes.item(1)
        item.setText(_translate("MainWindow", "eline"))
        item = self.listWidget_clientes.item(2)
        item.setText(_translate("MainWindow", "nico"))

        
        self.listWidget_clientes.setSortingEnabled(__sortingEnabled)
        self.pushButton_adicionar.setText(_translate("MainWindow", "Novo Cliente"))
        self.pushButton_alterar.setText(_translate("MainWindow", "Alterar"))
        self.pushButton_excluir.setText(_translate("MainWindow", "Excluir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

