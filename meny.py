import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, 
    QMessageBox, QLineEdit, QLabel
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Finans-programmet")
        self.resize(400, 300)

        self.startup_window()

    def startup_window(self):

        startup_window_widget = QWidget()
        layout = QVBoxLayout()
        startup_window_widget.setLayout(layout)

        label = QLabel("Finans-programmet")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        login_button = QPushButton("Logga in")
        create_account_button = QPushButton("Skapa konto")
        exit_button = QPushButton("Avsluta")

        login_button.clicked.connect(self.login_window)
        create_account_button.clicked.connect(self.create_account_window)
        exit_button.clicked.connect(self.close)

        layout.addWidget(label)
        layout.addWidget(login_button)
        layout.addWidget(create_account_button)
        layout.addWidget(exit_button)

        self.setCentralWidget(startup_window_widget)


    def login_window(self):

        login_widget = QWidget()
        layout = QVBoxLayout()
        login_widget.setLayout(layout)

        title = QLabel("Logga in")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Användarnamn")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Lösenord")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password) # Med echomode kan man välja hur input sr ut vid inmatning, här blir det ***

        login_button = QPushButton("Logga in")
        back_button = QPushButton("Tillbaka")
        back_button.clicked.connect(self.startup_window)
        login_button.clicked.connect(self.log_in)



        layout.addWidget(title)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)
        layout.addWidget(back_button)

        self.setCentralWidget(login_widget)

    def create_account_window(self):

        create_account_widget = QWidget()
        layout = QVBoxLayout()
        create_account_widget.setLayout(layout)

        title = QLabel("Skapa konto")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)


        back_button = QPushButton("Tillbaka")
        back_button.clicked.connect(self.startup_window)

        layout.addWidget(title)
        layout.addWidget(back_button)

        self.setCentralWidget(create_account_widget)

    def log_in(self):

        username = self.username_input.text()
        password = self.password_input.text()

        if username == "user" and password == "password":
            QMessageBox.information(self, "Inloggning lyckades", "Välkommen!")
            
        else:
            QMessageBox.warning(self, "Inloggning misslyckades", "Fel användarnamn eller lösenord.")

           
# ---- Starta appen ----
app = QApplication(sys.argv)
app.setStyle("Fusion")  # Stabilare på Windows
window = MainWindow()
window.show()
sys.exit(app.exec())
