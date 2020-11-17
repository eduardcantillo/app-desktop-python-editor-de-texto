import sys
import os


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import  QWidget
from PyQt5.QtWidgets import  QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import  QHBoxLayout
from PyQt5.QtWidgets import  QFileDialog
from PyQt5.QtWidgets import  QMainWindow
from PyQt5.QtWidgets import  QAction
from PyQt5.QtWidgets import  qApp



class Notepad(QWidget):
    def __init__(self):
        super(Notepad,self).__init__()
        self.texto=QTextEdit(self)
        self.borrar_boton=QPushButton('Borrar')
        self.guardar_boton=QPushButton('Guardar')
        self.abrir_boton=QPushButton('Abrir')
       

        self.init_ui()

    
    def init_ui(self):
        v_formato=QVBoxLayout()
        h_formato=QHBoxLayout()
        
        
        h_formato.addWidget(self.borrar_boton)
        h_formato.addWidget(self.guardar_boton)
        h_formato.addWidget(self.abrir_boton)

        v_formato.addWidget(self.texto)
        v_formato.addLayout(h_formato)

        self.guardar_boton.clicked.connect(self.texto_guardar)
        self.borrar_boton.clicked.connect(self.texto_borrar)
        self.abrir_boton.clicked.connect(self.texto_abrir)

        self.setLayout(v_formato)
        self.setWindowTitle('app Arquitectura')

        self.show()

    
    def texto_guardar(self):
        filename=QFileDialog.getSaveFileName(self, 'Guardar Archivo', os.getenv('HOME'))

        try:
            with open (filename[0],'w') as g:
                 mi_texto=self.texto.toPlainText()
                 g.write(mi_texto)
        except :
            print('No ha guardado el archivo')

    def texto_abrir(self):
        filename=QFileDialog.getOpenFileName(self, 'Abrir Archivo', os.getenv('HOME'))
        
        try:
            with open(filename[0],'r') as l:
                mi_archivo=l.read()
                self.texto.setText(mi_archivo)
            
        except:
            print('No se ha seleccionado ningun archivo para abrir')

    def texto_borrar(self):
        self.texto.clear()


class menu(QMainWindow):

    def __init__(self):
        super().__init__()

        self.form_widget=Notepad()
        self.setCentralWidget(self.form_widget)
        
        self.init.ui()

    def init_ui(self):
        bar=self.menuBar()
        File = bar.addMenu('Archivo')

        new_action=QAction('Nuevo',self)
        new_action.setShortcut('Ctrl+N')

        



#app=QApplication(sys.argv)
#editor=Notepad()
#sys.exit(app.exec_())
