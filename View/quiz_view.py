from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QRadioButton, QButtonGroup , QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt


class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuizMaster")
        self.resize(400, 300)
        self.question_label = QLabel("Quelle est la capitale de la France ?", self)
        self.question_label.setAlignment(Qt.AlignCenter) # Centrer le texte
        self.question_label.move(50, 100)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.question_label)
        self.setLayout(self.main_layout) # Application du layout à la fenêtre
        # ----- Style -----
        self.setStyleSheet("background-color: lightblue; font-size:16px; font-style:bold;")

        self.answers_layout = QVBoxLayout()
        self.answers_layout.setSpacing(20)
        
        self.radio1 = QRadioButton("paris")
        self.radio2 = QRadioButton("Lyon")
        self.radio3 = QRadioButton("Marseille")
        self.radio4 = QRadioButton("Bordeaux")

        self.answers_layout.addWidget(self.radio1)
        self.answers_layout.addWidget(self.radio2)
        self.answers_layout.addWidget(self.radio3)
        self.answers_layout.addWidget(self.radio4)

        self.main_layout.addLayout(self.answers_layout)

        # Layout suivant / précédent 
        self.navigation_layout = QHBoxLayout()
        self.navigation_layout.setSpacing(30)
        
        self.box1 = QPushButton('Précédant')
        self.box2 = QPushButton('Suivant')
        
        self.navigation_layout.addWidget(self.box1)
        self.navigation_layout.addWidget(self.box2)
        
        self.main_layout.addLayout(self.navigation_layout)
        


