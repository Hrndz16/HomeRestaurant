import sys
from PySide6.QtWidgets import QApplication
from controllers.MainWindow import MainWindowForm

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindowForm()
    Window.show()
    sys.exit(app.exec())

