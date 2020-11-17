import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QMessageBox

from bloc1 import Notepad



import bloc1


class menu(QMainWindow):

    def __init__(self):
        super().__init__()

         #creamos el menu
        self.bloc=Notepad()
        self.form_widget=self.bloc
        self.setCentralWidget(self.form_widget)
        barra=self.menuBar()

        archivo=barra.addMenu('Archivo')
        

        guardar_accion=QAction('Guardar',self)
        guardar_accion.setShortcut('Ctrl+G')

        nuevo_accion=QAction('Nuevo',self)
        nuevo_accion.setShortcut('Ctrl+N')

        salir_accion=QAction('Salir',self)
        salir_accion.setShortcut('Ctrl+S')

        abrir_accion=QAction('Abrir',self)
        abrir_accion.setShortcut('Ctrl+A')

       

        archivo.addAction(guardar_accion)
        archivo.addAction(nuevo_accion)
        archivo.addAction(salir_accion)
        archivo.addAction(abrir_accion)

        

        salir_accion.triggered.connect(self.salir_trigger)
        archivo.triggered.connect(self.seleccionar)

        self.setWindowTitle('App Desktop')
        self.resize(600,400)

        self.show()


    def salir_trigger(self):
        if self.bloc.texto.toPlainText()=='':
            qApp.quit()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("¿ Salir ?")
            msg.setInformativeText("Desea salir sin guardar el archivo")
            msg.setWindowTitle("¿ salir ?")
            msg.setDetailedText("Si sale no se guardar nada de lo que se encuentra en pantalla")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
	
            if msg.exec_()==1024:
                qApp.quit()
            else:
                self.bloc.texto_guardar()
            
            
            

    def seleccionar(self, q):
        if q.text() =='Guardar':
           self.bloc.texto_guardar()
        
        elif q.text()=='Abrir':
            self.bloc.texto_abrir()



app=QApplication(sys.argv)
menu=menu()
sys.exit(app.exec_())



        





