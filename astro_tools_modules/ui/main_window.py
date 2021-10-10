
from PyQt5.QtCore import QSize, pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QDoubleSpinBox, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QMenuBar, QMenu, \
    QAction, QStatusBar, QVBoxLayout, QTabWidget, QWidget, QGroupBox

from astro_tools_modules.share.calc import Calc \

from .translate import Translate


class MainWindow(QMainWindow):

    __app = None
    __tr = None

    __action_quit = None
    __action_about = None

    __main_tab = None

    __layout_main = None

    __ccd_resolution_pixel_size = None
    __ccd_resolution_focal_length = None
    __ccd_resolution_result = None

    __ccd_focal_length_pixel_size = None
    __ccd_focal_length_resolution = None
    __ccd_focal_length_result = None

    def __init__(self, app: QApplication, w_width=800, w_height=600) -> None:
        super().__init__()
        self.__app = app
        self.__tr = Translate()

        # Main Window Settings
        self.setWindowTitle("Astro-tools")
        self.resize(QSize(w_width, w_height))
        self.setStatusBar(QStatusBar())

        # Main menu
        self.__make_actions()
        self.setMenuBar(self.__make_main_menu())

        # Central widget
        self.setCentralWidget(QWidget(self))
        central_widget = self.centralWidget()
        self.__layout_main = QVBoxLayout(central_widget)
        central_widget.setLayout(self.__layout_main)

        self.__make_main_tab()

    def __make_calc_widget(self) -> QWidget:
        widget = QWidget(self)
        layout = QVBoxLayout(widget)

        ccd_group_box = QGroupBox(self.__tr.GROUP_CCD(), widget)
        ccd_group_box_layout = QGridLayout(ccd_group_box)

        # Resolution
        resolution_group_box = QGroupBox(
            self.__tr.GROUP_CCD_RESOLUTION(), ccd_group_box)
        resolution_group_box_layout = QHBoxLayout(resolution_group_box)
        resolution_group_box.setLayout(resolution_group_box_layout)
        resolution_group_box_layout.addWidget(
            QLabel(self.__tr.LABEL_PIXEL_SIZE()))
        self.__ccd_resolution_pixel_size = QDoubleSpinBox()
        self.__ccd_resolution_pixel_size.valueChanged.connect(
            self.on_resolution_change)
        resolution_group_box_layout.addWidget(self.__ccd_resolution_pixel_size)
        resolution_group_box_layout.addWidget(
            QLabel(self.__tr.LABEL_FOCAL_LENGHT()))
        self.__ccd_resolution_focal_length = QDoubleSpinBox()
        self.__ccd_resolution_focal_length.valueChanged.connect(
            self.on_resolution_change)
        self.__ccd_resolution_focal_length.setMaximum(10000.0)
        resolution_group_box_layout.addWidget(
            self.__ccd_resolution_focal_length)
        resolution_group_box_layout.addWidget(
            QLabel(self.__tr.LABEL_RESULT_PIXEL()))
        self.__ccd_resolution_result = QDoubleSpinBox()
        self.__ccd_resolution_result.setReadOnly(True)
        self.__ccd_resolution_result
        resolution_group_box_layout.addWidget(self.__ccd_resolution_result)
        ccd_group_box_layout.addWidget(resolution_group_box, 0, 0)

        # Focal lenght
        focal_lenght_group_box = QGroupBox(
            self.__tr.GROUP_CCD_FOCAL_LENGHT(), ccd_group_box)
        focal_lenght_group_box_layout = QHBoxLayout(focal_lenght_group_box)
        focal_lenght_group_box_layout.addWidget(
            QLabel(self.__tr.LABEL_PIXEL_SIZE()))
        self.__ccd_focal_length_pixel_size = QDoubleSpinBox()
        self.__ccd_focal_length_pixel_size.valueChanged.connect(
            self.on_focal_lenght_change)
        focal_lenght_group_box_layout.addWidget(
            self.__ccd_focal_length_pixel_size)
        focal_lenght_group_box_layout.addWidget(
            QLabel(self.__tr.LABEL_RESOLUTION_PIXEL()))
        self.__ccd_focal_length_resolution = QDoubleSpinBox()
        self.__ccd_focal_length_resolution.setDecimals(3)
        self.__ccd_focal_length_resolution.valueChanged.connect(
            self.on_focal_lenght_change)
        focal_lenght_group_box_layout.addWidget(
            self.__ccd_focal_length_resolution)
        focal_lenght_group_box_layout.addWidget(
            QLabel(self.__tr.LABEL_RESULT_MM()))
        self.__ccd_focal_length_result = QLineEdit()
        self.__ccd_focal_length_result.setReadOnly(True)
        focal_lenght_group_box_layout.addWidget(self.__ccd_focal_length_result)
        ccd_group_box_layout.addWidget(focal_lenght_group_box, 0, 1)

        # Pixel size
        pixel_size_group_box = QGroupBox(
            self.__tr.GROUP_CCD_PIXEL_SIZE(), ccd_group_box)
        ccd_group_box_layout.addWidget(pixel_size_group_box, 1, 0)

        # Chip size
        chip_size_group_box = QGroupBox(
            self.__tr.GROUP_CCD_CHIP_SIZE(), ccd_group_box)
        ccd_group_box_layout.addWidget(chip_size_group_box, 1, 1)

        ccd_group_box.setLayout(ccd_group_box_layout)
        layout.addWidget(ccd_group_box)
        widget.setLayout(layout)
        return widget

    def __make_platesolve_widget(self) -> QWidget:
        widget = QWidget(self)
        layout = QVBoxLayout(widget)

        widget.setLayout(layout)
        return widget

    def __make_main_tab(self) -> None:
        self.__main_tab = QTabWidget(self)

        self.__main_tab.addTab(self.__make_calc_widget(),
                               self.__tr.TAB_TITLE_CALC())
        self.__main_tab.addTab(
            self.__make_platesolve_widget(), self.__tr.TAB_TITLE_PS())

        self.__layout_main.addWidget(self.__main_tab)

    def __make_actions(self) -> None:
        self.__action_quit = QAction(self.__tr.ACTION_EXIT_S(), self)
        self.__action_quit.setShortcut(QKeySequence("Alt+F4"))
        self.__action_quit.setStatusTip(self.__tr.TIP_EXIT_S())
        self.__action_quit.triggered.connect(self.close_app)

        self.__action_about = QAction(self.__tr.ACTION_ABOUT_S(), self)

    def __make_main_menu(self) -> QMenuBar:
        menu_bar = QMenuBar(self)

        file_menu = QMenu(self.__tr.MENU_FILE_S(), self)
        file_menu.addAction(self.__action_quit)

        help_menu = QMenu(self.__tr.MENU_HELP_S(), self)
        help_menu.addAction(self.__action_about)

        menu_bar.addMenu(file_menu)
        menu_bar.addMenu(help_menu)

        return menu_bar

    def run(self) -> None:
        self.show()

    @pyqtSlot()
    def close_app(self) -> None:
        self.__app.exit(0)

    @pyqtSlot()
    def on_resolution_change(self) -> None:
        pixel_size = self.__ccd_resolution_pixel_size.value()
        focal_length = self.__ccd_resolution_focal_length.value()

        if pixel_size > 0 and focal_length > 0:
            result = Calc.ccd_resolution(pixel_size, focal_length)
            self.__ccd_resolution_result.setText(str(result))

    @pyqtSlot()
    def on_focal_lenght_change(self) -> None:
        pixel_size = self.__ccd_focal_length_pixel_size.value()
        resolution = self.__ccd_focal_length_resolution.value()

        if pixel_size > 0 and resolution > 0:
            result = Calc.ccd_focal_lenght(pixel_size, resolution)
            self.__ccd_focal_length_result.setText(str(result))
