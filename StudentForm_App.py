from PyQt5 import QtWidgets
import sys
from StudentForm import Ui_MainWindow

import time
from pymongo import MongoClient


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.combobox_changes()
        self.ui.comboBox.activated.connect(self.combobox_changes)
        self.ui.butt_record.clicked.connect(self.make_record)  # ჩაწერა ღილაკი

        # მონაცემთა ბაზა
        self.__conn = MongoClient()
        self.myBase = self.__conn["studentsDB"]
        self.mycoll = self.myBase["studentsCol"]

    def combobox_changes(self):
        text = self.ui.comboBox.currentText()
        if text == "ჩანაწერის გაკეთება":
            self.ui.record_grp_names.setEnabled(True)
            self.ui.record_subjects.setEnabled(True)
            self.ui.record_te_num.setEnabled(True)

            self.ui.butt_update.setEnabled(False)
            self.ui.butt_delete.setEnabled(False)
            self.ui.butt_all_record.setEnabled(True)
            self.ui.butt_record.setEnabled(True)

            self.ui.fing_grp.setEnabled(False)

        elif text == "ჩანაწერის განახლება":
            self.ui.record_grp_names.setEnabled(False)
            self.ui.record_subjects.setEnabled(False)
            self.ui.record_te_num.setEnabled(False)

            self.ui.butt_update.setEnabled(False)
            self.ui.butt_delete.setEnabled(False)
            self.ui.butt_all_record.setEnabled(False)
            self.ui.butt_record.setEnabled(False)
            self.ui.fing_grp.setEnabled(True)

        elif text == "ჩანაწერის ძებნა":
            self.ui.record_grp_names.setEnabled(False)
            self.ui.record_subjects.setEnabled(False)

            self.ui.butt_all_record.setEnabled(False)
            self.ui.butt_record.setEnabled(False)
            self.ui.butt_update.setEnabled(False)
            self.ui.butt_delete.setEnabled(True)

            self.ui.fing_grp.setEnabled(True)

    # ასუფთავებს N, სახელს და გვარს
    def clear_fields(self):
        self.ui.label_15.setPlainText("")
        self.ui.label_16.setPlainText("")
        self.ui.label_17.setPlainText("")

    # ჩაწერა ღილაკზე დაჭერის შემთხვევაში ვქმნით დიქშენარის
    def make_record(self):
        dct = {
            "N": int(self.ui.label_15.toPlainText()),
            "Lname": self.ui.label_16.toPlainText(),
            "Fname": self.ui.label_16.toPlainText(),
        }
        # წესით უნდა დაბეჭდოს N მაგრამ პროგრამა ითიშება. ????????
        print(dct["N"])
        print("გაეშვიიიი")
        time.sleep(5)
        # გასუფთავების გამოძახება
        self.clear_fields()
        # ბაზაში ჩვენი დიქშენარის დამატება
        self.mycoll.insert_one(dct)
        time.sleep(10)


app = QtWidgets.QApplication([])
application = myApp()
application.show()
sys.exit(app.exec())


