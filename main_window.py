from PyQt5.QtWidgets import QMainWindow
from ui_main_window import Ui_MainWindow
from table_window import TableWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.table_window = None

        self.ui.tableButton.clicked.connect(self.open_table)

    def open_table(self):
        if self.table_window is None:
            self.table_window = TableWindow()
        self.table_window.show()