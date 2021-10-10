
from PyQt5.QtCore import QObject


class Translate(QObject):

    def MENU_FILE_S(self) -> str:
        return self.tr("&File")

    def MENU_HELP_S(self) -> str:
        return self.tr("&Help")

    def ACTION_EXIT_S(self) -> str:
        return self.tr("&Exit")

    def ACTION_ABOUT_S(self) -> str:
        return self.tr("About")

    def TIP_EXIT_S(self) -> str:
        return self.tr("Close the application.")

    def TAB_TITLE_CALC(self) -> str:
        return self.tr("Calculators")

    def TAB_TITLE_PS(self) -> str:
        return self.tr("Plate solving")

    def GROUP_CCD(self) -> str:
        return self.tr("CCD")

    def GROUP_CCD_RESOLUTION(self) -> str:
        return self.tr("Resolution")

    def GROUP_CCD_FOCAL_LENGHT(self) -> str:
        return self.tr("Focal length")

    def GROUP_CCD_PIXEL_SIZE(self) -> str:
        return self.tr("Pixel size")

    def GROUP_CCD_CHIP_SIZE(self) -> str:
        return self.tr("Chip size")

    def LABEL_PIXEL_SIZE(self) -> str:
        return self.tr("Pixel size (µm):")

    def LABEL_FOCAL_LENGHT(self) -> str:
        return self.tr("Focal length (mm):")

    def LABEL_RESOLUTION_PIXEL(self) -> str:
        return self.tr("Resolution (\"/pixel):")

    def LABEL_RESULT_PIXEL(self) -> str:
        return self.tr("Result (\"/pixel):")

    def LABEL_RESULT_MM(self) -> str:
        return self.tr("Result (mm):")

    def LABEL_HORIZONTAL_SIZE(self) -> str:
        return self.tr("Horizontal size (mm):")

    def LABEL_VERTICAL_SIZE(self) -> str:
        return self.tr("Vertical size (mm):")

    def LABEL_HORIZONTAL_RESOLUTION(self) -> str:
        return self.tr("Horizontal resolution (px):")

    def LABEL_VERTICAL_RESOLUTION(self) -> str:
        return self.tr("Vertical resolution (px):")

    def LABEL_HORIZONTAL_PIXEL_SIZE(self) -> str:
        return self.tr("Horizontal pixel size (µm):")

    def LABEL_VERTICAL_PIXEL_SIZE(self) -> str:
        return self.tr("Vertical pixel size (µm):")

    def CALC_SELECTOR(self) -> str:
        return self.tr("Calculation type:")

    def TOOLTIP_CCD_RESOLUTION(self) -> str:
        return self.tr("(Pixel size / Focal Lenght) * 206.265")

    def TOOLTIP_CCD_FOCAL_LENGHT(self) -> str:
        return self.tr("(Pixel size * 206.265) / Resolution")

    def TOOLTIP_CCD_PIXEL_SIZE(self) -> str:
        return self.tr("Size / Resolution")

    def TOOLTIP_CCD_CHIP_SIZE(self) -> str:
        return self.tr("Pixel Size / Resolution")

    def TOOLTIP_COPY_TO_CLIPBOARD(self) -> str:
        return self.tr("Copy to clipboard")