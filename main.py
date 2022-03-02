# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets

from Ui.ui_main import UiMainWindow
from thread_part.xss_ui_method import xss_get_input

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    main_window.show()

    main_window.xss_start_button.clicked.connect(lambda: xss_get_input(main_window))
    sys.exit(app.exec_())
