
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDoubleSpinBox, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QMenuBar, QMenu, \
    QPushButton, QSpinBox, QVBoxLayout, QWidget, QGroupBox

from modules.share.calc import Calc
from modules.ui.translate import CalcCCDWidgetTranslate as tr

import modules.ui.res


class CalcCCDWidget(QGroupBox):

    __ccd_resolution_pixel_size = None
    __ccd_resolution_focal_length = None
    __ccd_resolution_result = None

    __ccd_focal_length_pixel_size = None
    __ccd_focal_length_resolution = None
    __ccd_focal_length_result = None

    __ccd_pixel_size_vsize = None
    __ccd_pixel_size_hsize = None
    __ccd_pixel_size_vresolution = None
    __ccd_pixel_size_hresolution = None
    __ccd_pixel_size_vresult = None
    __ccd_pixel_size_hresult = None

    __ccd_chip_pixel_size = None
    __ccd_chip_hresolution = None
    __ccd_chip_vresolution = None
    __ccd_chip_result_h = None
    __ccd_chip_result_v = None
    __ccd_chip_result_diagonally = None

    __locale = None

    __icon_clipboard = None

    __CLIPBOARD_RESOLUTION = 1
    __CLIPBOARD_FOCAL_LENGTH = 2
    __CLIPBOARD_PIXEL_RESULT_H = 3
    __CLIPBOARD_PIXEL_RESULT_V = 4
    __CLIPBOARD_CHIP_RESULT_H = 5
    __CLIPBOARD_CHIP_RESULT_V = 6
    __CLIPBOARD_CHIP_RESULT_D = 7

    def __init__(self, parent, locale):
        super().__init__(parent)

        self.setTitle(tr.GROUP_CCD(self))

        self.__locale = locale
        self.__icon_clipboard = QtGui.QIcon(":/icons/clipboard")
        ccd_group_box_layout = QVBoxLayout(self)

        ccd_group_box_layout.addWidget(self.__make_resolution_group())
        ccd_group_box_layout.addWidget(self.__make_focal_lenght_group())
        ccd_group_box_layout.addWidget(self.__make_pixel_size_group())
        ccd_group_box_layout.addWidget(self.__make_chips_size_group())
        self.setLayout(ccd_group_box_layout)

    def __make_resolution_group(self) -> QWidget:

        resolution_group_box = QGroupBox(tr.GROUP_CCD_RESOLUTION(self), self)
        resolution_group_box_layout = QHBoxLayout(resolution_group_box)
        resolution_group_box.setLayout(resolution_group_box_layout)
        resolution_group_box.setToolTip(tr.TOOLTIP_CCD_RESOLUTION(self))

        # Pixel size
        resolution_group_box_layout.addWidget(
            QLabel(tr.LABEL_PIXEL_SIZE(self)))
        self.__ccd_resolution_pixel_size = QDoubleSpinBox()
        self.__ccd_resolution_pixel_size.valueChanged.connect(
            self.__on_resolution_change)
        resolution_group_box_layout.addWidget(self.__ccd_resolution_pixel_size)

        # Focal lenght
        resolution_group_box_layout.addWidget(
            QLabel(tr.LABEL_FOCAL_LENGHT(self)))
        self.__ccd_resolution_focal_length = QDoubleSpinBox()
        self.__ccd_resolution_focal_length.valueChanged.connect(
            self.__on_resolution_change)
        self.__ccd_resolution_focal_length.setMaximum(10000.0)
        resolution_group_box_layout.addWidget(
            self.__ccd_resolution_focal_length)

        # Result
        resolution_group_box_layout.addWidget(
            QLabel(tr.LABEL_RESULT_PIXEL(self)))
        self.__ccd_resolution_result = QLineEdit()
        self.__ccd_resolution_result.setReadOnly(True)
        resolution_group_box_layout.addWidget(self.__ccd_resolution_result)

        # Clipboard
        clipboard_button = QPushButton()
        clipboard_button.setIcon(self.__icon_clipboard)
        clipboard_button.setToolTip(tr.TOOLTIP_COPY_TO_CLIPBOARD(self))
        clipboard_button.clicked.connect(lambda: self.__copy_to_clipboard(1))
        resolution_group_box_layout.addWidget(clipboard_button)

        return resolution_group_box

    def __make_focal_lenght_group(self) -> QWidget:

        focal_lenght_group_box = QGroupBox(
            tr.GROUP_CCD_FOCAL_LENGHT(self), self)
        focal_lenght_group_box_layout = QHBoxLayout(focal_lenght_group_box)
        focal_lenght_group_box.setToolTip(tr.TOOLTIP_CCD_FOCAL_LENGHT(self))

        # Pixel size
        focal_lenght_group_box_layout.addWidget(
            QLabel(tr.LABEL_PIXEL_SIZE(self)))
        self.__ccd_focal_length_pixel_size = QDoubleSpinBox()
        self.__ccd_focal_length_pixel_size.valueChanged.connect(
            self.__on_focal_lenght_change)

        # Resolution
        focal_lenght_group_box_layout.addWidget(
            self.__ccd_focal_length_pixel_size)
        focal_lenght_group_box_layout.addWidget(
            QLabel(tr.LABEL_RESOLUTION_PIXEL(self)))
        self.__ccd_focal_length_resolution = QDoubleSpinBox()
        self.__ccd_focal_length_resolution.setDecimals(3)
        self.__ccd_focal_length_resolution.setMaximum(10000.0)
        self.__ccd_focal_length_resolution.valueChanged.connect(
            self.__on_focal_lenght_change)

        # Result
        focal_lenght_group_box_layout.addWidget(
            self.__ccd_focal_length_resolution)
        focal_lenght_group_box_layout.addWidget(
            QLabel(tr.LABEL_RESULT_MM(self)))
        self.__ccd_focal_length_result = QLineEdit()
        self.__ccd_focal_length_result.setReadOnly(True)
        focal_lenght_group_box_layout.addWidget(self.__ccd_focal_length_result)

        # Clipboard
        clipboard_button = QPushButton()
        clipboard_button.setIcon(self.__icon_clipboard)
        clipboard_button.setToolTip(tr.TOOLTIP_COPY_TO_CLIPBOARD(self))
        clipboard_button.clicked.connect(lambda: self.__copy_to_clipboard(2))
        focal_lenght_group_box_layout.addWidget(clipboard_button)

        return focal_lenght_group_box

    def __make_pixel_size_group(self) -> QWidget:

        pixel_size_group_box = QGroupBox(tr.GROUP_CCD_PIXEL_SIZE(self), self)
        pixel_size_group_box_layout = QGridLayout(pixel_size_group_box)
        pixel_size_group_box.setToolTip(tr.TOOLTIP_CCD_PIXEL_SIZE(self))

        # Horizontal size
        pixel_size_group_box_layout.addWidget(
            QLabel(tr.LABEL_HORIZONTAL_SIZE(self)), 0, 0)
        self.__ccd_pixel_size_hsize = QDoubleSpinBox()
        self.__ccd_pixel_size_hsize.setDecimals(3)
        self.__ccd_pixel_size_hsize.setMaximum(10000.0)
        self.__ccd_pixel_size_hsize.valueChanged.connect(
            self.__on_pixel_size_change)
        pixel_size_group_box_layout.addWidget(
            self.__ccd_pixel_size_hsize, 0, 1)

        # Vertical size
        pixel_size_group_box_layout.addWidget(
            QLabel(tr.LABEL_VERTICAL_SIZE(self)), 1, 0)
        self.__ccd_pixel_size_vsize = QDoubleSpinBox()
        self.__ccd_pixel_size_vsize.setDecimals(3)
        self.__ccd_pixel_size_vsize.setMaximum(10000.0)
        self.__ccd_pixel_size_vsize.valueChanged.connect(
            self.__on_pixel_size_change)
        pixel_size_group_box_layout.addWidget(
            self.__ccd_pixel_size_vsize, 1, 1)

        # Horizontal resolution
        pixel_size_group_box_layout.addWidget(
            QLabel(tr.LABEL_HORIZONTAL_RESOLUTION(self)), 0, 2)
        self.__ccd_pixel_size_hresolution = QSpinBox()
        self.__ccd_pixel_size_hresolution.setMaximum(10000)
        self.__ccd_pixel_size_hresolution.valueChanged.connect(
            self.__on_pixel_size_change)
        pixel_size_group_box_layout.addWidget(
            self.__ccd_pixel_size_hresolution, 0, 3)

        # Vertical resolution
        pixel_size_group_box_layout.addWidget(
            QLabel(tr.LABEL_VERTICAL_RESOLUTION(self)), 1, 2)
        self.__ccd_pixel_size_vresolution = QSpinBox()
        self.__ccd_pixel_size_vresolution.setMaximum(10000)
        self.__ccd_pixel_size_vresolution.valueChanged.connect(
            self.__on_pixel_size_change)
        pixel_size_group_box_layout.addWidget(
            self.__ccd_pixel_size_vresolution, 1, 3)

        # Horizontal pixel size result
        pixel_size_group_box_layout.addWidget(
            QLabel(tr.LABEL_HORIZONTAL_PIXEL_SIZE(self)), 0, 4)
        self.__ccd_pixel_size_hresult = QLineEdit()
        self.__ccd_pixel_size_hresult.setReadOnly(True)
        pixel_size_group_box_layout.addWidget(
            self.__ccd_pixel_size_hresult, 0, 5)

        # Clipboard
        h_clipboard_button = QPushButton()
        h_clipboard_button.setIcon(self.__icon_clipboard)
        h_clipboard_button.setToolTip(tr.TOOLTIP_COPY_TO_CLIPBOARD(self))
        h_clipboard_button.clicked.connect(lambda: self.__copy_to_clipboard(3))
        pixel_size_group_box_layout.addWidget(h_clipboard_button, 0, 6)

        # Vertical pixel size result
        pixel_size_group_box_layout.addWidget(
            QLabel(tr.LABEL_VERTICAL_PIXEL_SIZE(self)), 1, 4)
        self.__ccd_pixel_size_vresult = QLineEdit()
        self.__ccd_pixel_size_vresult.setReadOnly(True)
        pixel_size_group_box_layout.addWidget(
            self.__ccd_pixel_size_vresult, 1, 5)

        # Clipboard
        v_clipboard_button = QPushButton()
        v_clipboard_button.setIcon(self.__icon_clipboard)
        v_clipboard_button.setToolTip(tr.TOOLTIP_COPY_TO_CLIPBOARD(self))
        v_clipboard_button.clicked.connect(lambda: self.__copy_to_clipboard(4))
        pixel_size_group_box_layout.addWidget(v_clipboard_button, 1, 6)

        return pixel_size_group_box

    def __make_chips_size_group(self) -> QWidget:

        # Chip size
        chip_size_group_box = QGroupBox(tr.GROUP_CCD_CHIP_SIZE(self), self)
        chip_size_group_box_layout = QGridLayout(chip_size_group_box)
        chip_size_group_box.setLayout(chip_size_group_box_layout)
        chip_size_group_box.setToolTip(tr.TOOLTIP_CCD_CHIP_SIZE(self))

        # Horizontal resolution
        chip_size_group_box_layout.addWidget(
            QLabel(tr.LABEL_HORIZONTAL_RESOLUTION(self)), 0, 0)
        self.__ccd_chip_hresolution = QSpinBox()
        self.__ccd_chip_hresolution.setMaximum(10000)
        self.__ccd_chip_hresolution.valueChanged.connect(
            self.__on_chip_size_change)
        chip_size_group_box_layout.addWidget(
            self.__ccd_chip_hresolution, 0, 1)

        # Vertical resolution
        chip_size_group_box_layout.addWidget(
            QLabel(tr.LABEL_VERTICAL_RESOLUTION(self)), 1, 0)
        self.__ccd_chip_vresolution = QSpinBox()
        self.__ccd_chip_vresolution.setMaximum(10000)
        self.__ccd_chip_vresolution.valueChanged.connect(
            self.__on_chip_size_change)
        chip_size_group_box_layout.addWidget(
            self.__ccd_chip_vresolution, 1, 1)

        # Pixel size
        chip_size_group_box_layout.addWidget(
            QLabel(tr.LABEL_PIXEL_SIZE(self)), 2, 0)
        self.__ccd_chip_pixel_size = QDoubleSpinBox()
        self.__ccd_chip_pixel_size.valueChanged.connect(
            self.__on_chip_size_change)
        chip_size_group_box_layout.addWidget(
            self.__ccd_chip_pixel_size, 2, 1)

        # Result Horizontal Size
        chip_size_group_box_layout.addWidget(
            QLabel(tr.LABEL_HORIZONTAL_SIZE(self)), 0, 2)
        self.__ccd_chip_result_h = QLineEdit()
        self.__ccd_chip_result_h.setReadOnly(True)
        chip_size_group_box_layout.addWidget(self.__ccd_chip_result_h, 0, 3)

        # Clipboard
        h_clipboard_button = QPushButton()
        h_clipboard_button.setIcon(self.__icon_clipboard)
        h_clipboard_button.setToolTip(tr.TOOLTIP_COPY_TO_CLIPBOARD(self))
        h_clipboard_button.clicked.connect(lambda: self.__copy_to_clipboard(5))
        chip_size_group_box_layout.addWidget(h_clipboard_button, 0, 4)

        # Result Vertical size
        chip_size_group_box_layout.addWidget(
            QLabel(tr.LABEL_VERTICAL_SIZE(self)), 1, 2)
        self.__ccd_chip_result_v = QLineEdit()
        self.__ccd_chip_result_v.setReadOnly(True)
        chip_size_group_box_layout.addWidget(self.__ccd_chip_result_v, 1, 3)

        # Clipboard
        v_clipboard_button = QPushButton()
        v_clipboard_button.setIcon(self.__icon_clipboard)
        v_clipboard_button.setToolTip(tr.TOOLTIP_COPY_TO_CLIPBOARD(self))
        v_clipboard_button.clicked.connect(lambda: self.__copy_to_clipboard(6))
        chip_size_group_box_layout.addWidget(v_clipboard_button, 1, 4)

        # Result diagonally
        chip_size_group_box_layout.addWidget(
            QLabel(tr.LABEL_DIAGONALLY(self)), 2, 2)
        self.__ccd_chip_result_diagonally = QLineEdit()
        self.__ccd_chip_result_diagonally.setReadOnly(True)
        chip_size_group_box_layout.addWidget(
            self.__ccd_chip_result_diagonally, 2, 3)

        # Clipboard
        d_clipboard_button = QPushButton()
        d_clipboard_button.setIcon(self.__icon_clipboard)
        d_clipboard_button.setToolTip(tr.TOOLTIP_COPY_TO_CLIPBOARD(self))
        d_clipboard_button.clicked.connect(lambda: self.__copy_to_clipboard(7))
        chip_size_group_box_layout.addWidget(d_clipboard_button, 2, 4)

        return chip_size_group_box

    def __on_resolution_change(self) -> None:
        pixel_size = self.__ccd_resolution_pixel_size.value()
        focal_length = self.__ccd_resolution_focal_length.value()

        if pixel_size > 0 and focal_length > 0:
            result = Calc.ccd_resolution(pixel_size, focal_length)

            self.__ccd_resolution_result.setText(
                self.__locale.toString(result, precision=4)
            )

    def __on_focal_lenght_change(self) -> None:
        pixel_size = self.__ccd_focal_length_pixel_size.value()
        resolution = self.__ccd_focal_length_resolution.value()

        if pixel_size > 0 and resolution > 0:
            result = Calc.ccd_focal_lenght(pixel_size, resolution)

            self.__ccd_focal_length_result.setText(
                self.__locale.toString(result, precision=1))

    def __on_pixel_size_change(self) -> None:
        h_size = self.__ccd_pixel_size_hsize.value()
        v_size = self.__ccd_pixel_size_vsize.value()
        h_resolution = self.__ccd_pixel_size_hresolution.value()
        v_resolution = self.__ccd_pixel_size_vresolution.value()

        if h_size > 0 and v_size > 0 and h_resolution > 0 and v_resolution > 0:
            hpixel_size, vpixelsize = Calc.ccd_pixel_size(
                h_size, v_size, h_resolution, v_resolution)

            self.__ccd_pixel_size_hresult.setText(
                self.__locale.toString(hpixel_size, precision=3))
            self.__ccd_pixel_size_vresult.setText(
                self.__locale.toString(vpixelsize, precision=3))

    def __on_chip_size_change(self) -> None:
        h_res = self.__ccd_chip_hresolution.value()
        v_res = self.__ccd_chip_vresolution.value()
        p_size = self.__ccd_chip_pixel_size.value()

        if h_res > 0 and v_res > 0 and p_size > 0:
            h_size, v_size, diagonally = Calc.ccd_chip_size(
                p_size, h_res, v_res)

            self.__ccd_chip_result_h.setText(
                self.__locale.toString(h_size, precision=3))
            self.__ccd_chip_result_v.setText(
                self.__locale.toString(v_size, precision=3))
            self.__ccd_chip_result_diagonally.setText(
                self.__locale.toString(diagonally, precision=3))

    def __copy_to_clipboard(self, mode):
        text = ''

        if mode == self.__CLIPBOARD_RESOLUTION:
            text = self.__ccd_resolution_result.text()
        elif mode == self.__CLIPBOARD_FOCAL_LENGTH:
            text = self.__ccd_focal_length_resolution.text()
        elif mode == self.__CLIPBOARD_PIXEL_RESULT_H:
            text = self.__ccd_pixel_size_hresult.text()
        elif mode == self.__CLIPBOARD_PIXEL_RESULT_V:
            text = self.__ccd_pixel_size_vresult.text()
        elif mode == self.__CLIPBOARD_CHIP_RESULT_H:
            text = self.__ccd_chip_result_h.text()
        elif mode == self.__CLIPBOARD_CHIP_RESULT_V:
            text = self.__ccd_chip_result_v.text()
        elif mode == self.__CLIPBOARD_CHIP_RESULT_D:
            text = self.__ccd_chip_result_diagonally.text()

        QApplication.clipboard().setText(text)
