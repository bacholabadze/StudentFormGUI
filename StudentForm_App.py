from PyQt5 import QtWidgets
import sys
from StudentForm import Ui_MainWindow
import random

import time
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://homework:hw12345678@studentform.sqapw0j.mongodb.net/?retryWrites=true&w=majority')


class Student:
    def __init__(self, lname="", fname="", sub1="", scr1="", sub2="", scr2="", sub3="", scr3="", sub4="", scr4="",
                 sub5="", scr5="", sub6="", scr6="", sub7="", scr7="", sub8="", scr8="", sub9="", scr9="", sub10="",
                 scr10=""):
        self.id = str(random.randrange(0, 999999999)).zfill(9)

        self.lname = lname  # სტუდენტის სახელი
        self.fname = fname  # გვარი

        self.sub1 = sub1  # საგნების დასახელება
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.sub5 = sub5
        self.sub6 = sub6
        self.sub7 = sub7
        self.sub8 = sub8
        self.sub9 = sub9
        self.sub10 = sub10

        self.scr1 = scr1  # ქულების რაოდენობა
        self.scr2 = scr2
        self.scr3 = scr3
        self.scr4 = scr4
        self.scr5 = scr5
        self.scr6 = scr6
        self.scr7 = scr7
        self.scr8 = scr8
        self.scr9 = scr9
        self.scr10 = scr10

        # print(f"{self.scr1} [][] {type(self.scr1)}")

    def __str__(self):
        printStudent = f"""
        --------------------------------
        ID: {self.id}
        Saxeli: {self.fname}
        Gvari: {self.lname}
        Sagani1: {self.sub1}
        Sagani1-is Qula: {self.scr1}
        Sagani2: {self.sub2}
        Sagani2-is Qula: {self.scr2}
        Sagani3: {self.sub3}
        Sagani3-is Qula: {self.scr3}
        Sagani4: {self.sub4}
        Sagani4-is Qula: {self.scr4}
        Sagani5: {self.sub5}
        Sagani5-is Qula: {self.scr5}
        Sagani6: {self.sub6}
        Sagani6-is Qula: {self.scr6}
        Sagani7: {self.sub7}
        Sagani7-is Qula: {self.scr7}
        Sagani8: {self.sub8}
        Sagani8-is Qula: {self.scr8}
        Sagani9: {self.sub9}
        Sagani9-is Qula: {self.scr9}
        Sagani10: {self.sub10}
        Sagani10-is Qula: {self.scr10}
        ------------------------------"""
        return printStudent


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.combobox_changes()
        self.ui.comboBox.activated.connect(self.combobox_changes)
        self.ui.butt_record.clicked.connect(self.make_record)  # ჩაწერა ღილაკი
        self.ui.butt_all_record.clicked.connect(self.fill_all_student)  # ფაილიდან ჩაწერის ღილაკი
        self.ui.butt_find.clicked.connect(self.find_students)  # ძებნის ღილაკი
        self.ui.butt_delete.clicked.connect(self.delete_student)  # წაშლის ღილაკი
        self.ui.butt_update.clicked.connect(self.update_student)  # განახლების ღილაკი
        # მონაცემთა ბაზა
        self.__conn = cluster
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
            self.ui.record_grp_names.setEnabled(True)
            self.ui.record_subjects.setEnabled(True)
            self.ui.record_te_num.setEnabled(False)

            self.ui.butt_update.setEnabled(True)
            self.ui.butt_delete.setEnabled(True)
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

    # მონაცემების დამატება მონაცემთა ბაზაში, სათითაოდ ან ბაზიდან, თუ სახელი და გვარი არ არსებობს უკვე.
    def insert_to_data_base(self, newStud):
        name = newStud.fname
        lname = newStud.lname
        # print(f"Sadzebneli {name}{lname}")
        results = self.mycoll.find({"fname": name, "lname": lname})
        check = True
        for x in results:
            if name in x["fname"] and lname in x["lname"]:
                # print(f"results ----------- {x}")
                check = False
        if check:
            print("[!] Axali Daemata")
            self.mycoll.insert_one(newStud.__dict__)

    def delete_student(self):
        del_id = self.ui.record_te_num.toPlainText()
        del_lname = self.ui.record_te_lname_2.toPlainText()
        del_fname = self.ui.record_te_fname_2.toPlainText()

        results = self.mycoll.delete_one({"id": del_id, "lname": del_lname, "fname": del_fname})
        self.clear_fields()
        print("[!] Caishala")
    def update_student(self):
        update_id = self.ui.record_te_num.toPlainText()

        new_lname = self.ui.record_te_lname_2.toPlainText().strip()
        new_fname = self.ui.record_te_fname_2.toPlainText().strip()

        new_sub1 = self.ui.te_subj_name1.toPlainText().strip()
        new_sub2 = self.ui.te_subj_name2.toPlainText().strip()
        new_sub3 = self.ui.te_subj_name3.toPlainText().strip()
        new_sub4 = self.ui.te_subj_name4.toPlainText().strip()
        new_sub5 = self.ui.te_subj_name5.toPlainText().strip()
        new_sub6 = self.ui.te_subj_name6.toPlainText().strip()
        new_sub7 = self.ui.te_subj_name7.toPlainText().strip()
        new_sub8 = self.ui.te_subj_name8.toPlainText().strip()
        new_sub9 = self.ui.te_subj_name9.toPlainText().strip()
        new_sub10 = self.ui.te_subj_name10.toPlainText().strip()

        new_scr1 = self.ui.te_subj_score1.toPlainText().strip()
        new_scr2 = self.ui.te_subj_score2.toPlainText().strip()
        new_scr3 = self.ui.te_subj_score3.toPlainText().strip()
        new_scr4 = self.ui.te_subj_score4.toPlainText().strip()
        new_scr5 = self.ui.te_subj_score5.toPlainText().strip()
        new_scr6 = self.ui.te_subj_score6.toPlainText().strip()
        new_scr7 = self.ui.te_subj_score7.toPlainText().strip()
        new_scr8 = self.ui.te_subj_score8.toPlainText().strip()
        new_scr9 = self.ui.te_subj_score9.toPlainText().strip()
        new_scr10 = self.ui.te_subj_score10.toPlainText().strip()

        results = self.mycoll.update_one({"id": update_id}, {"$set": {"lname": new_lname, "fname": new_fname,
                                                                      "sub1": new_sub1, "sub2": new_sub2,
                                                                      "sub3": new_sub3, "sub4": new_sub4,
                                                                      "sub5": new_sub5, "sub6": new_sub6,
                                                                      "sub7": new_sub7, "sub8": new_sub8,
                                                                      "sub9": new_sub9, "sub10": new_sub10,
                                                                      "scr1": new_scr1, "scr2": new_scr2,
                                                                      "scr3": new_scr3, "scr4": new_scr4,
                                                                      "scr5": new_scr5, "scr6": new_scr6,
                                                                      "scr7": new_scr7, "scr8": new_scr8,
                                                                      "scr9": new_scr9, "scr10": new_scr10, }})
        print("[!] Ganaxlda")

    # ასუფთავებს ყველაფერს
    def clear_fields(self):
        self.ui.record_te_num.setText("")  # N
        self.ui.record_te_lname_2.setText("")  # გვარი
        self.ui.record_te_fname_2.setText("")  # სახელი

        self.ui.te_subj_name1.setText("")  # საგნის დასახელება 1
        self.ui.te_subj_name2.setText("")  # საგნის დასახელება 2
        self.ui.te_subj_name3.setText("")  # საგნის დასახელება 3
        self.ui.te_subj_name4.setText("")  # საგნის დასახელება 4
        self.ui.te_subj_name5.setText("")  # საგნის დასახელება 5
        self.ui.te_subj_name6.setText("")  # საგნის დასახელება 6
        self.ui.te_subj_name7.setText("")  # საგნის დასახელება 7
        self.ui.te_subj_name8.setText("")  # საგნის დასახელება 8
        self.ui.te_subj_name9.setText("")  # საგნის დასახელება 9
        self.ui.te_subj_name10.setText("")  # საგნის დასახელება 10

        self.ui.te_subj_score1.setText("")  # საგნის შეფასება 1
        self.ui.te_subj_score2.setText("")  # საგნის შეფასება 2
        self.ui.te_subj_score3.setText("")  # საგნის შეფასება 3
        self.ui.te_subj_score4.setText("")  # საგნის შეფასება 4
        self.ui.te_subj_score5.setText("")  # საგნის შეფასება 5
        self.ui.te_subj_score6.setText("")  # საგნის შეფასება 6
        self.ui.te_subj_score7.setText("")  # საგნის შეფასება 7
        self.ui.te_subj_score8.setText("")  # საგნის შეფასება 8
        self.ui.te_subj_score9.setText("")  # საგნის შეფასება 9
        self.ui.te_subj_score10.setText("")  # საგნის შეფასება 10

        self.ui.delete_te_num.setText("")  # N ძებნა
        self.ui.delete_te_lname.setText("")  # გვარი ძებნა
        self.ui.delete_te_fname.setText("")  # სახელი ძებნა

    def find_students(self):
        searchN = self.ui.delete_te_num.toPlainText().strip()
        searchLname = self.ui.delete_te_lname.toPlainText().strip()
        searchFname = self.ui.delete_te_fname.toPlainText().strip()

        # print(f"\n\n&&&&&&&&searchN: {searchN}, searchL: {searchLname}, searchF: {searchFname}")
        results = self.mycoll.find({})
        for x in results:
            try:
                if searchN in x["id"] and searchFname in x["fname"] and searchLname in x["lname"]:
                    # print(f"\t\tNapovnia------------{x}")
                    self.ui.record_te_num.setText(x["id"])
                    self.ui.record_te_lname_2.setText(x["lname"])
                    self.ui.record_te_fname_2.setText(x["fname"])

                    self.ui.te_subj_name1.setText("".join(x["sub1"]))
                    self.ui.te_subj_name2.setText("".join(x["sub2"]))
                    self.ui.te_subj_name3.setText("".join(x["sub3"]))
                    self.ui.te_subj_name4.setText("".join(x["sub4"]))
                    self.ui.te_subj_name5.setText("".join(x["sub5"]))
                    self.ui.te_subj_name6.setText("".join(x["sub6"]))
                    self.ui.te_subj_name7.setText("".join(x["sub7"]))
                    self.ui.te_subj_name8.setText("".join(x["sub8"]))
                    self.ui.te_subj_name9.setText("".join(x["sub9"]))
                    self.ui.te_subj_name10.setText("".join(x["sub10"]))

                    self.ui.te_subj_score1.setText("".join(x["scr1"]))
                    self.ui.te_subj_score2.setText("".join(x["scr2"]))
                    self.ui.te_subj_score3.setText("".join(x["scr3"]))
                    self.ui.te_subj_score4.setText("".join(x["scr4"]))
                    self.ui.te_subj_score5.setText("".join(x["scr5"]))
                    self.ui.te_subj_score6.setText("".join(x["scr6"]))
                    self.ui.te_subj_score7.setText("".join(x["scr7"]))
                    self.ui.te_subj_score8.setText("".join(x["scr8"]))
                    self.ui.te_subj_score9.setText("".join(x["scr9"]))
                    self.ui.te_subj_score10.setText("".join(x["scr10"]))
                    break
            except KeyError:
                print("Key Error")
                print(x)
                pass

    # ფუნქცია პარსავს სტუდენტების ფაილს და შეყავს 10-10 მონაცემი გრაფებში
    def fill_all_student(self):
        print("დაიწყო ფაილიდან ჩამატება")
        with open("student_data.in", "r", encoding="utf8") as f:
            contents = f.readlines()
            for student in contents:
                # Shevqmnat Student Class mogvianebti Dasaediteblad
                newStudent = Student()

                # Davxlichot Data
                student = student.split("#")
                # print(f"{student[0]}----{student[1]} || {student}")
                # New Line movashorot
                student[len(student) - 1] = student[len(student) - 1].strip()
                # print(student)
                try:
                    # Studentis Saxeli Gvari Savaldebuloa
                    newStudent.lname = student[0].strip()
                    newStudent.fname = student[1].strip()
                except IndexError:
                    continue
                try:
                    # Arasavaldebulo Fields
                    newStudent.sub1 = student[2].strip()
                    newStudent.scr1 = student[3].strip()
                    newStudent.sub2 = student[4].strip()
                    newStudent.scr2 = student[5].strip()
                    newStudent.sub3 = student[6].strip()
                    newStudent.scr3 = student[7].strip()
                    newStudent.sub4 = student[8].strip()
                    newStudent.scr4 = student[9].strip()
                    newStudent.sub5 = student[10].strip()
                    newStudent.scr5 = student[11].strip()
                    newStudent.sub6 = student[12].strip()
                    newStudent.scr6 = student[13].strip()
                    newStudent.sub7 = student[14].strip()
                    newStudent.scr7 = student[15].strip()
                    newStudent.sub8 = student[16].strip()
                    newStudent.scr8 = student[17].strip()
                    newStudent.scr9 = student[18].strip()
                    newStudent.scr9 = student[19].strip()
                    newStudent.scr10 = student[20].strip()
                    newStudent.scr10 = student[21].strip()
                except IndexError:
                    # Kvela Sagnis Monacemi Ar Moidzebna
                    pass
                print(f"{newStudent}")
                self.insert_to_data_base(newStudent)

    # ჩაწერა ღილაკზე დაჭერის შემთხვევაში ვქმნით დიქშენარის
    def make_record(self):
        # სავალდებულო გრაფები
        dct = {
            "N": self.ui.record_te_num.toPlainText(),
            "Lname": self.ui.record_te_lname_2.toPlainText(),
            "Fname": self.ui.record_te_fname_2.toPlainText(),
        }

        if dct["N"] and dct["Lname"] and dct["Fname"]:
            # print(dct["N"], dct["Lname"], dct["Fname"])
            newSt = Student()

            newSt.id = str(dct["N"]).replace("\n", "")
            newSt.fname = dct["Fname"]
            newSt.lname = dct["Lname"]
            changeSubType = "".join(str(self.ui.te_subj_name1.toPlainText()))
            newSt.sub1 = changeSubType,
            newSt.scr1 = str(self.ui.te_subj_score1.toPlainText()).strip(),
            newSt.sub2 = str(self.ui.te_subj_name2.toPlainText()).strip(),
            newSt.scr2 = str(self.ui.te_subj_score2.toPlainText()).strip(),
            newSt.sub3 = str(self.ui.te_subj_name3.toPlainText()).strip(),
            newSt.scr3 = str(self.ui.te_subj_score3.toPlainText()).strip(),
            newSt.sub4 = str(self.ui.te_subj_name4.toPlainText()).strip(),
            newSt.scr4 = str(self.ui.te_subj_score4.toPlainText()).strip(),
            newSt.sub5 = str(self.ui.te_subj_name5.toPlainText()).strip(),
            newSt.scr5 = str(self.ui.te_subj_score5.toPlainText()).strip(),
            newSt.sub6 = str(self.ui.te_subj_name6.toPlainText()).strip(),
            newSt.scr6 = str(self.ui.te_subj_score6.toPlainText()).strip(),
            newSt.sub7 = str(self.ui.te_subj_name7.toPlainText()),
            newSt.scr7 = str(self.ui.te_subj_score7.toPlainText()).strip(),
            newSt.sub8 = str(self.ui.te_subj_name8.toPlainText()).strip(),
            newSt.scr8 = str(self.ui.te_subj_score8.toPlainText()).strip(),
            newSt.sub9 = str(self.ui.te_subj_name9.toPlainText()).strip(),
            newSt.scr9 = str(self.ui.te_subj_score9.toPlainText()).strip(),
            newSt.sub10 = str(self.ui.te_subj_name10.toPlainText()).strip(),
            newSt.scr10 = str(self.ui.te_subj_score10.toPlainText()).strip(),
            print(newSt)
            # ბაზაში დამატება
            self.insert_to_data_base(newSt)
        self.clear_fields()
        time.sleep(3)


app = QtWidgets.QApplication([])
application = myApp()
application.show()
sys.exit(app.exec())
