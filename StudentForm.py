# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 500)
        MainWindow.setMinimumSize(QtCore.QSize(727, 500))
        MainWindow.setMaximumSize(QtCore.QSize(727, 500))
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 221, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.fing_grp = QtWidgets.QGroupBox(self.centralwidget)
        self.fing_grp.setEnabled(True)
        self.fing_grp.setGeometry(QtCore.QRect(10, 350, 701, 91))
        self.fing_grp.setTitle("")
        self.fing_grp.setObjectName("fing_grp")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fing_grp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.fing_grp)
        self.label_6.setMinimumSize(QtCore.QSize(50, 22))
        self.label_6.setMaximumSize(QtCore.QSize(65, 22))
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.fing_grp)
        self.label_5.setMinimumSize(QtCore.QSize(180, 22))
        self.label_5.setMaximumSize(QtCore.QSize(150, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.fing_grp)
        self.label_2.setMinimumSize(QtCore.QSize(130, 22))
        self.label_2.setMaximumSize(QtCore.QSize(130, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.fing_grp)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delete_te_num = QtWidgets.QTextEdit(self.fing_grp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_te_num.sizePolicy().hasHeightForWidth())
        self.delete_te_num.setSizePolicy(sizePolicy)
        self.delete_te_num.setMinimumSize(QtCore.QSize(60, 30))
        self.delete_te_num.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.delete_te_num.setFont(font)
        self.delete_te_num.setLineWidth(15)
        self.delete_te_num.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.delete_te_num.setLineWrapColumnOrWidth(0)
        self.delete_te_num.setObjectName("delete_te_num")
        self.horizontalLayout.addWidget(self.delete_te_num)
        self.delete_te_lname = QtWidgets.QTextEdit(self.fing_grp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_te_lname.sizePolicy().hasHeightForWidth())
        self.delete_te_lname.setSizePolicy(sizePolicy)
        self.delete_te_lname.setMinimumSize(QtCore.QSize(150, 30))
        self.delete_te_lname.setMaximumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.delete_te_lname.setFont(font)
        self.delete_te_lname.setLineWidth(15)
        self.delete_te_lname.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.delete_te_lname.setLineWrapColumnOrWidth(0)
        self.delete_te_lname.setObjectName("delete_te_lname")
        self.horizontalLayout.addWidget(self.delete_te_lname)
        self.delete_te_fname = QtWidgets.QTextEdit(self.fing_grp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_te_fname.sizePolicy().hasHeightForWidth())
        self.delete_te_fname.setSizePolicy(sizePolicy)
        self.delete_te_fname.setMinimumSize(QtCore.QSize(150, 30))
        self.delete_te_fname.setMaximumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.delete_te_fname.setFont(font)
        self.delete_te_fname.setLineWidth(15)
        self.delete_te_fname.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.delete_te_fname.setLineWrapColumnOrWidth(0)
        self.delete_te_fname.setObjectName("delete_te_fname")
        self.horizontalLayout.addWidget(self.delete_te_fname)
        self.butt_find = QtWidgets.QPushButton(self.fing_grp)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.butt_find.setFont(font)
        self.butt_find.setObjectName("butt_find")
        self.horizontalLayout.addWidget(self.butt_find)
        self.label_14 = QtWidgets.QLabel(self.fing_grp)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.label_13 = QtWidgets.QLabel(self.fing_grp)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.record_subjects = QtWidgets.QGroupBox(self.centralwidget)
        self.record_subjects.setGeometry(QtCore.QRect(10, 100, 701, 201))
        self.record_subjects.setTitle("")
        self.record_subjects.setObjectName("record_subjects")
        self.widget = QtWidgets.QWidget(self.record_subjects)
        self.widget.setGeometry(QtCore.QRect(0, 0, 699, 197))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.te_subj_name2 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_name2.setMinimumSize(QtCore.QSize(250, 30))
        self.te_subj_name2.setMaximumSize(QtCore.QSize(250, 30))
        self.te_subj_name2.setObjectName("te_subj_name2")
        self.gridLayout.addWidget(self.te_subj_name2, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.te_subj_name1 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_name1.setMinimumSize(QtCore.QSize(250, 30))
        self.te_subj_name1.setMaximumSize(QtCore.QSize(250, 30))
        self.te_subj_name1.setTabChangesFocus(True)
        self.te_subj_name1.setObjectName("te_subj_name1")
        self.gridLayout.addWidget(self.te_subj_name1, 1, 0, 1, 1)
        self.te_subj_score1 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_score1.setMinimumSize(QtCore.QSize(65, 30))
        self.te_subj_score1.setMaximumSize(QtCore.QSize(65, 30))
        self.te_subj_score1.setLineWidth(15)
        self.te_subj_score1.setTabChangesFocus(True)
        self.te_subj_score1.setDocumentTitle("")
        self.te_subj_score1.setObjectName("te_subj_score1")
        self.gridLayout.addWidget(self.te_subj_score1, 1, 1, 1, 1)
        self.te_subj_score4 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_score4.setMinimumSize(QtCore.QSize(65, 30))
        self.te_subj_score4.setMaximumSize(QtCore.QSize(65, 30))
        self.te_subj_score4.setLineWidth(15)
        self.te_subj_score4.setDocumentTitle("")
        self.te_subj_score4.setObjectName("te_subj_score4")
        self.gridLayout.addWidget(self.te_subj_score4, 4, 1, 1, 1)
        self.te_subj_name4 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_name4.setMinimumSize(QtCore.QSize(250, 30))
        self.te_subj_name4.setMaximumSize(QtCore.QSize(250, 30))
        self.te_subj_name4.setObjectName("te_subj_name4")
        self.gridLayout.addWidget(self.te_subj_name4, 4, 0, 1, 1)
        self.te_subj_name3 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_name3.setMinimumSize(QtCore.QSize(250, 30))
        self.te_subj_name3.setMaximumSize(QtCore.QSize(250, 30))
        self.te_subj_name3.setObjectName("te_subj_name3")
        self.gridLayout.addWidget(self.te_subj_name3, 3, 0, 1, 1)
        self.te_subj_name5 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_name5.setMinimumSize(QtCore.QSize(250, 30))
        self.te_subj_name5.setMaximumSize(QtCore.QSize(250, 30))
        self.te_subj_name5.setObjectName("te_subj_name5")
        self.gridLayout.addWidget(self.te_subj_name5, 5, 0, 1, 1)
        self.te_subj_score3 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_score3.setMinimumSize(QtCore.QSize(50, 30))
        self.te_subj_score3.setMaximumSize(QtCore.QSize(65, 30))
        self.te_subj_score3.setLineWidth(15)
        self.te_subj_score3.setDocumentTitle("")
        self.te_subj_score3.setObjectName("te_subj_score3")
        self.gridLayout.addWidget(self.te_subj_score3, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 2, 1, 1)
        self.te_subj_score2 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_score2.setMinimumSize(QtCore.QSize(65, 30))
        self.te_subj_score2.setMaximumSize(QtCore.QSize(65, 30))
        self.te_subj_score2.setLineWidth(15)
        self.te_subj_score2.setDocumentTitle("")
        self.te_subj_score2.setObjectName("te_subj_score2")
        self.gridLayout.addWidget(self.te_subj_score2, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.te_subj_score5 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_score5.setMinimumSize(QtCore.QSize(65, 30))
        self.te_subj_score5.setMaximumSize(QtCore.QSize(65, 30))
        self.te_subj_score5.setLineWidth(15)
        self.te_subj_score5.setDocumentTitle("")
        self.te_subj_score5.setObjectName("te_subj_score5")
        self.gridLayout.addWidget(self.te_subj_score5, 5, 1, 1, 1)
        self.te_subj_name7 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_name7.setMinimumSize(QtCore.QSize(250, 30))
        self.te_subj_name7.setMaximumSize(QtCore.QSize(250, 30))
        self.te_subj_name7.setObjectName("te_subj_name7")
        self.gridLayout.addWidget(self.te_subj_name7, 2, 2, 1, 1)
        self.te_subj_name10 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_name10.setMinimumSize(QtCore.QSize(250, 30))
        self.te_subj_name10.setMaximumSize(QtCore.QSize(250, 30))
        self.te_subj_name10.setObjectName("te_subj_name10")
        self.gridLayout.addWidget(self.te_subj_name10, 5, 2, 1, 1)
        self.te_subj_name6 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_name6.setMinimumSize(QtCore.QSize(250, 30))
        self.te_subj_name6.setMaximumSize(QtCore.QSize(250, 30))
        self.te_subj_name6.setObjectName("te_subj_name6")
        self.gridLayout.addWidget(self.te_subj_name6, 1, 2, 1, 1)
        self.te_subj_name9 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_name9.setMinimumSize(QtCore.QSize(250, 30))
        self.te_subj_name9.setMaximumSize(QtCore.QSize(250, 30))
        self.te_subj_name9.setObjectName("te_subj_name9")
        self.gridLayout.addWidget(self.te_subj_name9, 4, 2, 1, 1)
        self.te_subj_name8 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_name8.setMinimumSize(QtCore.QSize(250, 30))
        self.te_subj_name8.setMaximumSize(QtCore.QSize(250, 30))
        self.te_subj_name8.setObjectName("te_subj_name8")
        self.gridLayout.addWidget(self.te_subj_name8, 3, 2, 1, 1)
        self.te_subj_score6 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_score6.setMinimumSize(QtCore.QSize(50, 30))
        self.te_subj_score6.setMaximumSize(QtCore.QSize(65, 30))
        self.te_subj_score6.setLineWidth(15)
        self.te_subj_score6.setDocumentTitle("")
        self.te_subj_score6.setObjectName("te_subj_score6")
        self.gridLayout.addWidget(self.te_subj_score6, 1, 3, 1, 1)
        self.te_subj_score8 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_score8.setMinimumSize(QtCore.QSize(50, 30))
        self.te_subj_score8.setMaximumSize(QtCore.QSize(65, 30))
        self.te_subj_score8.setLineWidth(15)
        self.te_subj_score8.setDocumentTitle("")
        self.te_subj_score8.setObjectName("te_subj_score8")
        self.gridLayout.addWidget(self.te_subj_score8, 3, 3, 1, 1)
        self.te_subj_score7 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_score7.setMinimumSize(QtCore.QSize(65, 30))
        self.te_subj_score7.setMaximumSize(QtCore.QSize(65, 30))
        self.te_subj_score7.setLineWidth(15)
        self.te_subj_score7.setDocumentTitle("")
        self.te_subj_score7.setObjectName("te_subj_score7")
        self.gridLayout.addWidget(self.te_subj_score7, 2, 3, 1, 1)
        self.te_subj_score9 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_score9.setMinimumSize(QtCore.QSize(65, 30))
        self.te_subj_score9.setMaximumSize(QtCore.QSize(65, 30))
        self.te_subj_score9.setLineWidth(15)
        self.te_subj_score9.setDocumentTitle("")
        self.te_subj_score9.setObjectName("te_subj_score9")
        self.gridLayout.addWidget(self.te_subj_score9, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.te_subj_score10 = QtWidgets.QTextEdit(self.widget)
        self.te_subj_score10.setMinimumSize(QtCore.QSize(65, 30))
        self.te_subj_score10.setMaximumSize(QtCore.QSize(65, 30))
        self.te_subj_score10.setLineWidth(15)
        self.te_subj_score10.setDocumentTitle("")
        self.te_subj_score10.setObjectName("te_subj_score10")
        self.gridLayout.addWidget(self.te_subj_score10, 5, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.butt_record = QtWidgets.QPushButton(self.centralwidget)
        self.butt_record.setGeometry(QtCore.QRect(330, 310, 120, 30))
        self.butt_record.setMinimumSize(QtCore.QSize(120, 30))
        self.butt_record.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.butt_record.setFont(font)
        self.butt_record.setObjectName("butt_record")
        self.butt_update = QtWidgets.QPushButton(self.centralwidget)
        self.butt_update.setGeometry(QtCore.QRect(460, 310, 120, 30))
        self.butt_update.setMinimumSize(QtCore.QSize(120, 30))
        self.butt_update.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.butt_update.setFont(font)
        self.butt_update.setObjectName("butt_update")
        self.butt_delete = QtWidgets.QPushButton(self.centralwidget)
        self.butt_delete.setGeometry(QtCore.QRect(590, 310, 120, 30))
        self.butt_delete.setMinimumSize(QtCore.QSize(120, 30))
        self.butt_delete.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.butt_delete.setFont(font)
        self.butt_delete.setObjectName("butt_delete")
        self.label_find = QtWidgets.QLabel(self.centralwidget)
        self.label_find.setGeometry(QtCore.QRect(10, 440, 701, 41))
        self.label_find.setText("")
        self.label_find.setAlignment(QtCore.Qt.AlignCenter)
        self.label_find.setObjectName("label_find")
        self.butt_all_record = QtWidgets.QPushButton(self.centralwidget)
        self.butt_all_record.setGeometry(QtCore.QRect(10, 310, 310, 30))
        self.butt_all_record.setMinimumSize(QtCore.QSize(310, 30))
        self.butt_all_record.setMaximumSize(QtCore.QSize(310, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.butt_all_record.setFont(font)
        self.butt_all_record.setObjectName("butt_all_record")
        self.record_grp_names = QtWidgets.QGroupBox(self.centralwidget)
        self.record_grp_names.setGeometry(QtCore.QRect(10, 50, 691, 41))
        self.record_grp_names.setTitle("")
        self.record_grp_names.setObjectName("record_grp_names")
        self.layoutWidget_3 = QtWidgets.QWidget(self.record_grp_names)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 0, 691, 42))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.record_names = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.record_names.setContentsMargins(0, 0, 0, 0)
        self.record_names.setSpacing(4)
        self.record_names.setObjectName("record_names")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_15.setMinimumSize(QtCore.QSize(30, 22))
        self.label_15.setMaximumSize(QtCore.QSize(30, 22))
        self.label_15.setTextFormat(QtCore.Qt.PlainText)
        self.label_15.setObjectName("label_15")
        self.record_names.addWidget(self.label_15)
        self.record_te_num = QtWidgets.QTextEdit(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.record_te_num.sizePolicy().hasHeightForWidth())
        self.record_te_num.setSizePolicy(sizePolicy)
        self.record_te_num.setMinimumSize(QtCore.QSize(60, 30))
        self.record_te_num.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.record_te_num.setFont(font)
        self.record_te_num.setLineWidth(15)
        self.record_te_num.setTabChangesFocus(True)
        self.record_te_num.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.record_te_num.setLineWrapColumnOrWidth(0)
        self.record_te_num.setObjectName("record_te_num")
        self.record_names.addWidget(self.record_te_num)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_16.setMinimumSize(QtCore.QSize(0, 40))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.record_names.addWidget(self.label_16)
        self.record_te_lname_2 = QtWidgets.QTextEdit(self.layoutWidget_3)
        self.record_te_lname_2.setMinimumSize(QtCore.QSize(220, 30))
        self.record_te_lname_2.setMaximumSize(QtCore.QSize(230, 30))
        self.record_te_lname_2.setTabChangesFocus(True)
        self.record_te_lname_2.setObjectName("record_te_lname_2")
        self.record_names.addWidget(self.record_te_lname_2)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_17.setMinimumSize(QtCore.QSize(0, 40))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.record_names.addWidget(self.label_17)
        self.record_te_fname_2 = QtWidgets.QTextEdit(self.layoutWidget_3)
        self.record_te_fname_2.setMinimumSize(QtCore.QSize(215, 30))
        self.record_te_fname_2.setMaximumSize(QtCore.QSize(215, 30))
        self.record_te_fname_2.setTabChangesFocus(True)
        self.record_te_fname_2.setObjectName("record_te_fname_2")
        self.record_names.addWidget(self.record_te_fname_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Form"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ჩანაწერის გაკეთება"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ჩანაწერის განახლება"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ჩანაწერის ძებნა"))
        self.label_6.setText(_translate("MainWindow", "  N"))
        self.label_5.setText(_translate("MainWindow", "  გვარი"))
        self.label_2.setText(_translate("MainWindow", "  სახელი"))
        self.delete_te_num.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                              "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                              "type=\"text/css\">\n "
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; "
                                              "font-size:14pt; font-weight:400; font-style:normal;\">\n "
                                              "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                              "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                              "-qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.butt_find.setText(_translate("MainWindow", "ძებნა"))
        self.label_8.setText(_translate("MainWindow", "საგნის დასახელება"))
        self.te_subj_score1.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                               "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                               "type=\"text/css\">\n "
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; "
                                               "font-size:16pt; font-weight:400; font-style:normal;\">\n "
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                               "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                               "-qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.te_subj_score4.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.te_subj_score3.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "საგნის დასახელება"))
        self.te_subj_score2.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "შეფასება"))
        self.te_subj_score5.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.te_subj_score6.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                               "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.te_subj_score8.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.te_subj_score7.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.te_subj_score9.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "შეფასება"))
        self.te_subj_score10.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" style=\"-qt-paragraph-type:empty; "
                                                "margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                                "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br "
                                                "/></p></body></html>"))
        self.butt_record.setText(_translate("MainWindow", "ჩაწერა"))
        self.butt_update.setText(_translate("MainWindow", "განახლება"))
        self.butt_delete.setText(_translate("MainWindow", "წაშლა"))
        self.butt_all_record.setText(_translate("MainWindow", "ყველა ჩაწერის გაკეთება"))
        self.label_15.setText(_translate("MainWindow", "  N"))
        self.record_te_num.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                            "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" "
                                                            "/><style type=\"text/css\">\n "
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:\'MS Shell Dlg "
                                                            "2\'; font-size:14pt; font-weight:400; "
                                                            "font-style:normal;\">\n "
                                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; "
                                                            "margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                                            "margin-right:0px; -qt-block-indent:0; "
                                                            "text-indent:0px;\"><br /></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "  გვარი: "))
        self.label_17.setText(_translate("MainWindow", "  სახელი: "))
