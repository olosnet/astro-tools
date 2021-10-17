from PyQt5.QtCore import QObject


class CalcCCDWidgetTranslate:

    @staticmethod
    def GROUP_CCD(parent: QObject) -> str:
        return parent.tr("CCD")

    @staticmethod
    def GROUP_CCD_RESOLUTION(parent: QObject) -> str:
        return parent.tr("Resolution")

    @staticmethod
    def GROUP_CCD_FOCAL_LENGHT(parent: QObject) -> str:
        return parent.tr("Focal length")

    @staticmethod
    def GROUP_CCD_PIXEL_SIZE(parent: QObject) -> str:
        return parent.tr("Pixel size")

    @staticmethod
    def GROUP_CCD_CHIP_SIZE(parent: QObject) -> str:
        return parent.tr("Chip size")

    @staticmethod
    def LABEL_PIXEL_SIZE(parent: QObject) -> str:
        return parent.tr("Pixel size") + " (µm):"

    @staticmethod
    def LABEL_FOCAL_LENGHT(parent: QObject) -> str:
        return parent.tr("Focal length") + " (mm):"

    @staticmethod
    def LABEL_RESOLUTION_PIXEL(parent: QObject) -> str:
        return parent.tr("Resolution") + " (\"/pixel):"

    @staticmethod
    def LABEL_RESULT_PIXEL(parent: QObject) -> str:
        return parent.tr("Result") + " (\"/pixel):"

    @staticmethod
    def LABEL_RESULT_MM(parent: QObject) -> str:
        return parent.tr("Result") + " (mm):"

    @staticmethod
    def LABEL_HORIZONTAL_SIZE(parent: QObject) -> str:
        return parent.tr("Horizontal size") + " (mm):"

    @staticmethod
    def LABEL_VERTICAL_SIZE(parent: QObject) -> str:
        return parent.tr("Vertical size") + " (mm):"

    @staticmethod
    def LABEL_HORIZONTAL_RESOLUTION(parent: QObject) -> str:
        return parent.tr("Horizontal resolution") + " (px):"

    @staticmethod
    def LABEL_VERTICAL_RESOLUTION(parent: QObject) -> str:
        return parent.tr("Vertical resolution") + " (px):"

    @staticmethod
    def LABEL_HORIZONTAL_PIXEL_SIZE(parent: QObject) -> str:
        return parent.tr("Horizontal pixel size") + " (µm):"

    @staticmethod
    def LABEL_VERTICAL_PIXEL_SIZE(parent: QObject) -> str:
        return parent.tr("Vertical pixel size") + " (µm):"

    @staticmethod
    def LABEL_DIAGONALLY(parent: QObject) -> str:
        return parent.tr("Diagonally") + " (mm):"

    @staticmethod
    def TOOLTIP_CCD_RESOLUTION(parent: QObject) -> str:
        return parent.tr("(Pixel size / Focal Lenght)") + " * 206.265"

    @staticmethod
    def TOOLTIP_CCD_FOCAL_LENGHT(parent: QObject) -> str:
        return parent.tr("(Pixel size * 206.265) / Resolution")

    @staticmethod
    def TOOLTIP_CCD_PIXEL_SIZE(parent: QObject) -> str:
        return parent.tr("Size / Resolution")

    @staticmethod
    def TOOLTIP_CCD_CHIP_SIZE(parent: QObject) -> str:
        return parent.tr("Pixel Size / Resolution")

    @staticmethod
    def TOOLTIP_COPY_TO_CLIPBOARD(parent: QObject) -> str:
        return parent.tr("Copy to clipboard")
