from PyQt5.QtCore import QDir, QLocale, QSize, QStandardPaths
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, \
    QAction, QVBoxLayout, QTabWidget, QWidget

from modules.base.db import ProfileSettingsDB
from .tr import MainWindowTranslate as tr

from modules.calc.ui import CalcWidget
from modules.plate_solve.ui import PlateSolveWidget
from modules.locations.ui import LocationsDialog

from .status_bar.ui import StatusBarWidget


class MainWindow(QMainWindow):

    __app = None
    __profile_db : ProfileSettingsDB = None

    __action_quit = None
    __action_about = None
    __action_settings_locations = None

    __main_tab = None

    __layout_main = None
    __locale =  QLocale(QLocale.system().name())


    __location_settings_dialog = None


    def __init__(self, app: QApplication, w_width=800, w_height=600) -> None:

        super().__init__()
        self.__app = app

        # Get configuration path
        config_path = QDir(QStandardPaths.writableLocation(QStandardPaths.ConfigLocation))
        config_path.mkpath("astro-tools")
        config_path.cd("astro-tools")

        # Init profile settings DB
        self.__profile_db = ProfileSettingsDB(config_path.path())

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

        self.__action_settings_locations = QAction(tr.ACTION_LOCATIONS_S(self), self)
        self.__action_settings_locations.setStatusTip(tr.TIP_SETTINGS_S(self))
        self.__action_settings_locations.triggered.connect(self.locations_settings_dialog)

    def __make_main_menu(self) -> QMenuBar:
        menu_bar = QMenuBar(self)

        file_menu = QMenu(tr.MENU_FILE_S(self), self)
        file_menu.addAction(self.__action_quit)
        file_menu.addAction

        settings_menu = QMenu(tr.MENU_SETTINGS_S(self), self)
        settings_menu.addAction(self.__action_settings_locations)


        help_menu = QMenu(tr.MENU_HELP_S(self), self)
        help_menu.addAction(self.__action_about)

        menu_bar.addMenu(file_menu)
        menu_bar.addMenu(settings_menu)
        menu_bar.addMenu(help_menu)

        return menu_bar

    def run(self) -> None:
        self.show()

    def close_app(self) -> None:
        self.close()

    def locations_settings_dialog(self) -> None:
        if not self.__location_settings_dialog:
            self.__location_settings_dialog = LocationsDialog(self, self.__locale, self.__profile_db)

        self.__location_settings_dialog.exec_()

    def closeEvent(self, event):
        self.__profile_db.close()

