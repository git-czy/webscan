from Ui.ui_main import UiMainWindow
from Web_scan.dsxs import init_options, scan_page


def xss_get_input(main_window: UiMainWindow):
    url = main_window.xss_url.text()
    data = main_window.xss_data.text()
    result = "not valid input"
    if url:
        # init_options()
        result = scan_page(url if url.startswith("http") else "http://%s" % url, data)
    main_window.xss_scan_res.setPlainText(result)
