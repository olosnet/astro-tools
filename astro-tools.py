#!/usr/bin/env python3
from PyQt5.QtWidgets import QApplication
from modules.base.ui import MainWindow

def main():

    app = QApplication([])

    main_ui = MainWindow(app)
    main_ui.run()

    app.exec()

if __name__ == "__main__":
    main()
