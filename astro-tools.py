#!/usr/bin/env python3
from PyQt5.QtWidgets import QApplication
from astro_tools_modules.ui import MainWindow





def main():

    app = QApplication([])

    main_ui = MainWindow(app)
    main_ui.run()

    #window = QWidget()
    #layout = QVBoxLayout()

    # layout.addWidget(QPushButton('Top'))
    # layout.addWidget(QPushButton('Bottom'))
    # window.setLayout(layout)
    # window.show()

    app.exec()


if __name__ == "__main__":
    main()
