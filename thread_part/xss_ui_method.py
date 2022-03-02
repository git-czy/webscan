from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal

from Web_scan.dsxs import xss_main


def xss_get_input(main_window):
    url = main_window.xss_url.text()
    data = main_window.xss_data.text()
    proxy = main_window.xss_proxy.text()
    cookie = main_window.xss_cookie.text()
    ua = main_window.xss_user_agent.text()
    referer = main_window.xss_referer.text()
    if url:
        # init_options()
        main_window.start_xss_thread(url, data=data, proxy=proxy, cookie=cookie, ua=ua, referer=referer)


class XssThread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    res_signal = pyqtSignal(str)

    end_signal = pyqtSignal(bool)

    def __init__(self, url, **kwargs):
        super(XssThread, self).__init__()
        self.url = url
        self.options = kwargs

    def __del__(self):
        self.wait()

    def run(self):
        self.end_signal.emit(False)
        xss_main(self.url if self.url.startswith("http") else "http://%s" % self.url, self.res_signal, **self.options)
        self.end_signal.emit(True)
