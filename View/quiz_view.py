from PyQt5.QtWidgets import QWidget
class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuizMaster - Bienvenue !")
        self.resize(400, 300)
        self.setStyleSheet("background-color: lightblue;")
        self.setFixedSize(400, 300)
