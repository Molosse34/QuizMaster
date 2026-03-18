from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
class StartView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.title = QLabel("Bienvenue dans le Quiz")
        self.start_button = QPushButton("Commencer")
        layout.addWidget(self.title)
        layout.addWidget(self.start_button)
        self.setLayout(layout)