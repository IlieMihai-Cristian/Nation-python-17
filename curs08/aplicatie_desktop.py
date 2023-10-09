from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton
import sys


class CalculatorApp(QMainWindow):

    def __init__(self):
        super(CalculatorApp, self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        # self.central_widget.setFixedSize(400, 300)
        self.setCentralWidget(self.central_widget)
        self.result_display = QLineEdit()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.result_display)

        buttons_layout = QVBoxLayout()
        button_rows = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "7"),
            ("1", "2", "3", "4"),
            ("0", ".", "=", "+")
        ]

        for row in button_rows:
            row_widget = QWidget()
            row_layout = QHBoxLayout()

            for button_text, width, height in zip(row, [80, 80, 80, 80], [80, 80, 80, 80]):
                button = self.create_button(button_text, width, height)
                row_layout.addWidget(row_widget)

        self.layout.addLayout(buttons_layout)

        self.central_widget.setLayout(self.layout)

        self.current_input = ""
        self.result_display.setText(self.current_input)

    def create_button(self, text, width, height):
        button = QPushButton(text)
        button.setFixedSize(width, height)
        button.clicked.connect(self.handle_button_click)
        return button

    def handle_button_click(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == '=':
            try:
                result = str(eval(self.current_input))
                self.current_input = result
            except Exception:
                self.current_input = "Error"
        else:
            self.current_input += button_text

        self.result_display.setText(self.current_input)



def main():
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
