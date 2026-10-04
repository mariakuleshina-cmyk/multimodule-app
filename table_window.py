import csv
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from ui_table_window import Ui_TableWindow
from data_reader import get_data


class TableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableWindow()
        self.ui.setupUi(self)

        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels([
            "Температура",
            "Влажность",
            "Освещение"
        ])

        self.ui.readButton.clicked.connect(self.read_data)
        self.ui.saveButton.clicked.connect(self.save_data)

    def read_data(self):
        data = get_data()

        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)

        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(data[0])))
        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(data[1])))
        self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(data[2])))

    def save_data(self):
        with open("data.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Температура", "Влажность", "Освещение"])

            for row in range(self.ui.tableWidget.rowCount()):
                values = []
                for col in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(row, col)
                    values.append(item.text() if item else "")
                writer.writerow(values)