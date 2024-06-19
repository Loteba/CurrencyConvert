import sys
import os
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic

class Dialogo (QMainWindow):
    GBP=4.85
    SOL=1


    def __init__(self):
        ruta = os.path.join(os.path.dirname(__file__), '..', 'vista', 'CurrencyConvert.ui')
        QMainWindow.__init__(self)
        uic.loadUi(ruta,self)

        self.pbTipoCambio.clicked.connect(self.calcularConversion)

    def calcularConversion( self ):
        convertido=0.0
        inicial=0.0

        inicial=float(self.leImporte.text())
        convertido=inicial

        if self.rbDeUK.isChecked():
            convertido=inicial/self.SOL
        elif self.rbDeAUS.isChecked():
            convertido = inicial / self.GBP

        if self.rbAUK.isChecked():
            convertido=inicial*self.SOL
        elif self.rbAAUS.isChecked():
            convertido = inicial * self.GBP

        self.lblCambio.setText(convertido.__str__())

if __name__ == '__main__':
    app=QApplication(sys.argv)
    dialogo=Dialogo()
    dialogo.show()
    app.exec_()