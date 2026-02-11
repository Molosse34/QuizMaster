import sys
# Classe principale pour l'application PyQt5
from PyQt5.QtWidgets import QApplication
# Import de la fenêtre principale de l'application
from View.quiz_view import QuizView
from PyQt5.QtGui import QIcon
app = QApplication(sys.argv) # Crée l'application
app.setWindowIcon(QIcon("resources/quizicon.png"))

window = QuizView() # Crée la fenêtre
window.show() # Affiche la fenêtre
sys.exit(app.exec_()) # Lance la boucle de l'application et quitte proprement           