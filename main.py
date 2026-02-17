import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QTextEdit, QLineEdit
)
from PyQt6.QtCore import Qt


class CommandWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Robo App")
        self.resize(700, 500)

        layout = QVBoxLayout()

        # Output display
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background:black;color:red;")
        layout.addWidget(self.output)

        # Command input
        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText("Type a command and press Enter...")
        self.input_line.returnPressed.connect(self.run_command)
        layout.addWidget(self.input_line)

        self.setLayout(layout)

        self.print_output("Robo App at your service.")

    def print_output(self, text):
        self.output.append(text)

    def run_command(self):
        command = self.input_line.text()
        self.print_output(f"> {command}")
        self.input_line.clear()

        # --- Example commands ---
        if command == "help":
            self.print_output("Commands: help, clear, hello")
        elif command == "clear":
            self.output.clear()
        elif command == "hello":
            self.print_output("Hello, Minal 👋")
        else:
            self.print_output("Unknown command")


app = QApplication(sys.argv)
window = CommandWindow()
window.show()
sys.exit(app.exec())
