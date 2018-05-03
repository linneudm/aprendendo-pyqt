from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class FrmVideoAula(QWidget):

	def __init__(self, parent = None):
		super(FrmVideoAula,self).__init__(parent)

		left_spacer = QWidget()
		left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		right_spacer = QWidget()
		right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


		layoutPrincipal = QVBoxLayout()

		txtNome = QLineEdit(self)
		txtSobreNome = QLineEdit(self)

		flayout = QFormLayout()
		flayout.addRow('Informe o nome', txtNome)
		flayout.addRow('Informe o sobrenome', txtSobreNome)

		layoutPrincipal.addLayout(flayout)

		btnOk = QPushButton('Ok', self)
		btnCancelar = QPushButton('Cancelar', self)
		btnCancelar.clicked.connect(self.close)

		hboxBotoes = QHBoxLayout()
		
		hboxBotoes.addWidget(left_spacer)
		hboxBotoes.addWidget(btnOk)
		hboxBotoes.addWidget(btnCancelar)
		hboxBotoes.addWidget(right_spacer)

		layoutPrincipal.addLayout(hboxBotoes)

		self.setLayout(layoutPrincipal)

#if __name__ == __main__:
import sys
root = QApplication(sys.argv)
root.setWindowIcon(QIcon('Koala.jpg'))
#root.setWindowTitle("Aprendendo PyQt5")
app = FrmVideoAula(None)
app.setWindowTitle("Aprendendo PyQt5")
app.show()
root.exec_()