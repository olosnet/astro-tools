from datetime import datetime
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QStatusBar, QWidget
from modules.share.calc import Calc
from modules.ui.translate import StatusBarWidgetTranslate as tr

class StatusBarWidget(QStatusBar):

    __utc_time_label = None
    __julian_date_label = None
    __current_julian_datetime = None
    __now_copied = False

    def __init__(self, parent):
        super().__init__(parent)

        status_bar_widgets = QWidget(self)
        widgets_layout = QHBoxLayout(status_bar_widgets)

        self.__utc_time_label = QLabel(self)
        self.__utc_time_label.setStyleSheet("QLabel {color: blue; font-weight: bold;}")
        self.__julian_date_label = QLabel(self)
        self.__julian_date_label.setStyleSheet("QLabel {color: red; font-weight: bold; text-decoration: underline;}")
        self.__julian_date_label.setCursor(Qt.PointingHandCursor)
        self.__julian_date_label.setToolTip(tr.TIP_COPY_JD_TO_CLIPBOARD(self))
        self.__julian_date_label.mousePressEvent = self.__copy_to_clipboard

        widgets_layout.addStretch()
        widgets_layout.addWidget(self.__utc_time_label)
        widgets_layout.addWidget(QLabel("|", self))
        widgets_layout.addWidget(self.__julian_date_label)

        self.addWidget(status_bar_widgets, Qt.AlignRight)
        self.setStyleSheet("QStatusBar::item { border: 0px solid black };") # No status bar widget border

        # First update
        self.__update_datetime()

        timer = QTimer(self)
        timer.timeout.connect(self.__update_datetime)
        timer.start(1000)

    def __update_datetime(self):
        dt = datetime.utcnow()
        self.__utc_time_label.setText("UTC: " + dt.strftime("%m/%d/%Y, %H:%M:%S"))
        self.__current_julian_datetime = str(Calc.time_to_jd_dt(dt))
        self.__julian_date_label.setText("JD: " + self.__current_julian_datetime)

        if self.__now_copied:
            self.showMessage('')
            self.__now_copied = False

    def __copy_to_clipboard(self, event):
        QApplication.clipboard().setText(self.__current_julian_datetime)
        self.showMessage(tr.STATUS_COPIED(self))
        self.__now_copied = True
