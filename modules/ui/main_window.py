
from PyQt5.QtCore import QLocale, QSize
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, \
    QAction, QVBoxLayout, QTabWidget, QWidget
from modules.ui.translate import MainWindowTranslate as tr

from modules.ui.widgets.calc_widget import CalcWidget
from modules.ui.widgets.plate_solve_widget import PlateSolveWidget
from modules.ui.widgets.status_bar_widget import StatusBarWidget


class MainWindow(QMainWindow):

    __app = None

    __action_quit = None
    __action_about = None

    __main_tab = None

    __layout_main = None
    __locale =  QLocale(QLocale.system().name())


    def __init__(self, app: QApplication, w_width=800, w_height=600) -> None:
        super().__init__()

        self.__app = app

        # Main Window Settings
        self.setWindowTitle("Astro-tools")
        self.resize(QSize(w_width, w_height))
        self.setStatusBar(StatusBarWidget(self))

        # Main menu
        self.__make_actions()
        self.setMenuBar(self.__make_main_menu())

        # Central widget
        self.setCentralWidget(QWidget(self))
        central_widget = self.centralWidget()
        self.__layout_main = QVBoxLayout(central_widget)
        central_widget.setLayout(self.__layout_main)

        self.__make_main_tab()

    def __make_main_tab(self) -> None:
        self.__main_tab = QTabWidget(self)

        self.__main_tab.addTab(CalcWidget(self, self.__locale), tr.TAB_TITLE_CALC(self))
        self.__main_tab.addTab(PlateSolveWidget(self, self.__locale), tr.TAB_TITLE_PS(self))

        self.__layout_main.addWidget(self.__main_tab)

    def __make_actions(self) -> None:
        self.__action_quit = QAction(tr.ACTION_EXIT_S(self), self)
        self.__action_quit.setShortcut(QKeySequence("Alt+F4"))
        self.__action_quit.setStatusTip(tr.TIP_EXIT_S(self))
        self.__action_quit.triggered.connect(self.close_app)

        self.__action_about = QAction(tr.ACTION_ABOUT_S(self), self)

    def __make_main_menu(self) -> QMenuBar:
        menu_bar = QMenuBar(self)

        file_menu = QMenu(tr.MENU_FILE_S(self), self)
        file_menu.addAction(self.__action_quit)

        help_menu = QMenu(tr.MENU_HELP_S(self), self)
        help_menu.addAction(self.__action_about)

        menu_bar.addMenu(file_menu)
        menu_bar.addMenu(help_menu)

        return menu_bar

    def run(self) -> None:
        self.show()

    def close_app(self) -> None:
        self.__app.exit(0)



