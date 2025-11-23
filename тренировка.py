import math
import sys

try:
    from PyQt5 import QtWidgets, QtCore
    from PyQt5.QtWidgets import (
        QMainWindow,
        QWidget,
        QGridLayout,
        QTextEdit,
        QPushButton,
        QApplication,
    )

    PYQT_AVAILABLE = True
except ImportError:
    PYQT_AVAILABLE = False
    print("PyQt5 не установлен. Установите: pip install PyQt5")


class CalculatorWindow(QMainWindow):

    def __init__(self):
        if not PYQT_AVAILABLE:
            print("PyQt5 недоступен. Приложение не может быть запущено.")
            return

        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 500)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QGridLayout()
        central_widget.setLayout(layout)

        # Display
        self.text_edit = QTextEdit()
        self.text_edit.setMaximumHeight(50)
        self.text_edit.setAlignment(QtCore.Qt.AlignRight)
        layout.addWidget(self.text_edit, 0, 0, 1, 5)

        # Create buttons
        self._create_buttons(layout)

        # State variables
        self.block_digits = False
        self.block_operators = True

    def _create_buttons(self, layout):
        # Number buttons
        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("0", 4, 0),
        ]

        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(self._on_digit_btn_clicked)
            layout.addWidget(btn, row, col)
            setattr(self, f"btn_{text}", btn)

        # Operation buttons
        operations = [("+", 1, 3), ("-", 2, 3), ("×", 3, 3), ("÷", 4, 3)]

        for text, row, col in operations:
            btn = QPushButton(text)
            if text == "+":
                btn.clicked.connect(self._on_button_plus_clicked)
            elif text == "-":
                btn.clicked.connect(self._on_button_minus_clicked)
            elif text == "×":
                btn.clicked.connect(self._on_button_multiply_clicked)
            elif text == "÷":
                btn.clicked.connect(self._on_button_divide_clicked)
            layout.addWidget(btn, row, col)
            setattr(
                self,
                f'btn_{"plus" if text == "+" else "minus" if text == "-" else "multiply" if text == "×" else "divide"}',
                btn,
            )

        # Function buttons
        functions = [
            ("√", 1, 4, self._on_button_sqrt_clicked),
            ("sin", 2, 4, self._on_button_trigonometric_clicked),
            ("cos", 3, 4, self._on_button_trigonometric_clicked),
            ("tg", 4, 4, self._on_button_trigonometric_clicked),
            ("ctg", 5, 0, self._on_button_trigonometric_clicked),
            ("π", 5, 1, self._on_button_pi_clicked),
            ("e", 5, 2, self._on_button_e_clicked),
            ("(", 5, 3, self._on_start_group_clicked),
            (")", 5, 4, self._on_close_group_clicked),
        ]

        for text, row, col, handler in functions:
            btn = QPushButton(text)
            btn.clicked.connect(handler)
            layout.addWidget(btn, row, col)
            if text in ["√", "sin", "cos", "tg", "ctg", "π", "e"]:
                setattr(self, f"btn_{text}", btn)
            elif text == "(":
                self.btn_start_group = btn
            elif text == ")":
                self.btn_close_group = btn

        # Control buttons
        self.btn_exec = QPushButton("=")
        self.btn_exec.clicked.connect(self._on_exec_clicked)
        layout.addWidget(self.btn_exec, 6, 0, 1, 2)

        self.btn_clear = QPushButton("C")
        self.btn_clear.clicked.connect(self._on_button_clear_clicked)
        layout.addWidget(self.btn_clear, 6, 2, 1, 3)

    def _on_digit_btn_clicked(self):
        clicked_btn = self.sender()
        digit_value = clicked_btn.text()
        current_text = self.text_edit.toPlainText()

        if digit_value == "0":
            if current_text == "" or not current_text[-1].isdigit():
                self.text_edit.setPlainText(current_text + digit_value)
                self.block_digits = True
            else:
                self.text_edit.setPlainText(current_text + digit_value)
        else:
            if not self.block_digits:
                self.text_edit.setPlainText(current_text + digit_value)
            else:
                self.text_edit.setPlainText(current_text + "." + digit_value)
                self.block_digits = False

    def _on_button_trigonometric_clicked(self):
        clicked_btn = self.sender()
        func_name = clicked_btn.text()
        text = self.text_edit.toPlainText()

        if text != "" and text[-1] != ",":
            self.text_edit.setPlainText(text + f"{func_name}(")

    def _on_button_plus_clicked(self):
        if not self.block_operators:
            self.text_edit.setPlainText(self.text_edit.toPlainText() + "+")
            self.block_operators = True

    def _on_button_minus_clicked(self):
        if not self.block_operators:
            self.text_edit.setPlainText(self.text_edit.toPlainText() + "-")
            self.block_operators = True

    def _on_button_multiply_clicked(self):
        if not self.block_operators:
            self.text_edit.setPlainText(self.text_edit.toPlainText() + "×")
            self.block_operators = True

    def _on_button_divide_clicked(self):
        if not self.block_operators:
            self.text_edit.setPlainText(self.text_edit.toPlainText() + "÷")
            self.block_operators = True

    def _on_button_sqrt_clicked(self):
        text = self.text_edit.toPlainText()
        if text != "" and text[-1] not in ["+", "-", "×", "÷"]:
            self.text_edit.setPlainText(text + "√")
        else:
            self.text_edit.setPlainText(text + "√")

    def _on_start_group_clicked(self):
        self.text_edit.setPlainText(self.text_edit.toPlainText() + "(")

    def _on_close_group_clicked(self):
        self.text_edit.setPlainText(self.text_edit.toPlainText() + ")")

    def _on_exec_clicked(self):
        expression = self.text_edit.toPlainText()
        try:
            # Заменяем операторы на Python-эквиваленты
            expression = expression.replace("×", "*")
            expression = expression.replace("÷", "/")
            expression = expression.replace("√", "math.sqrt")
            expression = expression.replace("π", str(math.pi))
            expression = expression.replace("e", str(math.e))

            # Добавляем math. для тригонометрических функций
            expression = expression.replace("sin(", "math.sin(")
            expression = expression.replace("cos(", "math.cos(")
            expression = expression.replace("tg(", "math.tan(")
            expression = expression.replace("ctg(", "1/math.tan(")

            result = eval(expression)
            result = round(result, 4)
            if result == int(result):
                result = int(result)
            self.text_edit.setPlainText(str(result))
        except Exception as e:
            self.text_edit.setPlainText(f"Error: {str(e)}")

    def _on_button_clear_clicked(self):
        self.text_edit.setPlainText("")

    def _on_button_pi_clicked(self):
        current_text = self.text_edit.toPlainText()
        if current_text != "":
            if current_text[-1].isdigit() or current_text[-1].isalpha():
                self.text_edit.setPlainText(current_text + "×π")
            else:
                self.text_edit.setPlainText(current_text + "π")
        else:
            self.text_edit.setPlainText(current_text + "π")

    def _on_button_e_clicked(self):
        current_text = self.text_edit.toPlainText()
        if current_text != "":
            if current_text[-1].isdigit() or current_text[-1].isalpha():
                self.text_edit.setPlainText(current_text + "×e")
            else:
                self.text_edit.setPlainText(current_text + "e")
        else:
            self.text_edit.setPlainText(current_text + "e")


def main():
    if not PYQT_AVAILABLE:
        print("PyQt5 не установлен. Установите: pip install PyQt5")
        return

    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
