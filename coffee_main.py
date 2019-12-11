from PyQt5.QtWidgets import QApplication

from Database_setting.widget_coffee_setting import MyApp

if __name__ == "__main__":
    app = QApplication([])
    w = MyApp()
    app.exec_()
