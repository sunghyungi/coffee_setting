from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from DB_connection.coffee_backup import BackupRestore
from DB_connection.coffee_init_service import DbInit


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Database_setting/coffee.ui")
        self.db = DbInit()
        self.ui.init.clicked.connect(self.db.service)
        self.backup = BackupRestore()
        self.ui.backup.clicked.connect(self.backup.data_backup)
        self.ui.restore.clicked.connect(self.backup.data_restore)
        self.ui.show()