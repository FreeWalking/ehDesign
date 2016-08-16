# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aviamentos.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_janela_aviamentos(object):
    def setupUi(self, janela_aviamentos):
        janela_aviamentos.setObjectName("janela_aviamentos")
        janela_aviamentos.resize(768, 427)
        self.centralwidget = QtWidgets.QWidget(janela_aviamentos)
        self.centralwidget.setObjectName("centralwidget")
        self.label_codigo = QtWidgets.QLabel(self.centralwidget)
        self.label_codigo.setGeometry(QtCore.QRect(80, 30, 59, 16))
        self.label_codigo.setObjectName("label_codigo")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 60, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.labe_aviamento = QtWidgets.QLabel(self.centralwidget)
        self.labe_aviamento.setGeometry(QtCore.QRect(250, 30, 121, 16))
        self.labe_aviamento.setObjectName("labe_aviamento")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 60, 401, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_fornecedor = QtWidgets.QLabel(self.centralwidget)
        self.label_fornecedor.setGeometry(QtCore.QRect(80, 100, 81, 16))
        self.label_fornecedor.setObjectName("label_fornecedor")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 130, 571, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_valor = QtWidgets.QLabel(self.centralwidget)
        self.label_valor.setGeometry(QtCore.QRect(80, 170, 41, 16))
        self.label_valor.setObjectName("label_valor")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 190, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_unidade = QtWidgets.QLabel(self.centralwidget)
        self.label_unidade.setGeometry(QtCore.QRect(530, 190, 61, 21))
        self.label_unidade.setObjectName("label_unidade")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(600, 190, 121, 21))
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_observacoes = QtWidgets.QLabel(self.centralwidget)
        self.label_observacoes.setGeometry(QtCore.QRect(80, 230, 91, 16))
        self.label_observacoes.setObjectName("label_observacoes")
        self.Button_adicionar_fornecedor = QtWidgets.QPushButton(self.centralwidget)
        self.Button_adicionar_fornecedor.setGeometry(QtCore.QRect(680, 130, 21, 21))
        self.Button_adicionar_fornecedor.setObjectName("Button_adicionar_fornecedor")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 260, 381, 91))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setGeometry(QtCore.QRect(590, 280, 115, 32))
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        janela_aviamentos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(janela_aviamentos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 22))
        self.menubar.setObjectName("menubar")
        janela_aviamentos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(janela_aviamentos)
        self.statusbar.setObjectName("statusbar")
        janela_aviamentos.setStatusBar(self.statusbar)

        self.retranslateUi(janela_aviamentos)
        QtCore.QMetaObject.connectSlotsByName(janela_aviamentos)

    def retranslateUi(self, janela_aviamentos):
        _translate = QtCore.QCoreApplication.translate
        janela_aviamentos.setWindowTitle(_translate("janela_aviamentos", "MainWindow"))
        self.label_codigo.setText(_translate("janela_aviamentos", "Codigo:"))
        self.labe_aviamento.setText(_translate("janela_aviamentos", "Nome Aviamento:"))
        self.label_fornecedor.setText(_translate("janela_aviamentos", "Fornecedor:"))
        self.label_valor.setText(_translate("janela_aviamentos", "Valor:"))
        self.label_unidade.setText(_translate("janela_aviamentos", "Unidade:"))
        self.comboBox.setItemText(0, _translate("janela_aviamentos", "Unitaria "))
        self.comboBox.setItemText(1, _translate("janela_aviamentos", "Metrica"))
        self.label_observacoes.setText(_translate("janela_aviamentos", "Observações:"))
        self.Button_adicionar_fornecedor.setText(_translate("janela_aviamentos", "+"))
        self.pushButton_salvar.setText(_translate("janela_aviamentos", "Salvar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janela_aviamentos = QtWidgets.QMainWindow()
    ui = Ui_janela_aviamentos()
    ui.setupUi(janela_aviamentos)
    janela_aviamentos.show()
    sys.exit(app.exec_())

