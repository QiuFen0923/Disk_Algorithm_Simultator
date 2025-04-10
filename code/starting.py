# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QStringListModel
from PyQt6.QtWidgets import QWidget, QMessageBox
from main import test
from FCFS import fcfs
from SSTF import sstf
from C_SCAN import c_scan
from LOOK import look
from mydraw import Matplotlibwidget_2D



class Ui_Form(QWidget):
    Flag = False
    start = 0
    list_generate = []
    list_plot = []
    total_movement = 0
    average_movement = 0

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.move(90, 60)
        Form.resize(1550, 860)
        self.graphicsView = QtWidgets.QGraphicsView(parent=Form)
        self.graphicsView.setGeometry(QtCore.QRect(5, 1, 1021, 661))
        self.graphicsView.setObjectName("graphicsView")
        self.Generation = QtWidgets.QPushButton(parent=Form)
        self.Generation.setGeometry(QtCore.QRect(100, 770, 121, 71))
        self.Generation.setObjectName("Generation")

        self.draw_widdget = Matplotlibwidget_2D()

        self.graphicsView_layout = QtWidgets.QHBoxLayout(self.graphicsView)
        self.graphicsView_layout.addWidget(self.draw_widdget)


        self.Generation.clicked.connect(self.generate)

        self.gridLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(350, 710, 281, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.LOOK = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.LOOK.setObjectName("LOOK")
        self.gridLayout.addWidget(self.LOOK, 1, 0, 1, 1)

        self.LOOK.clicked.connect(self.look_integration)

        self.SSTF = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.SSTF.setObjectName("SSTF")
        self.gridLayout.addWidget(self.SSTF, 0, 1, 1, 1)

        self.SSTF.clicked.connect(self.sstf_integration)

        self.FCFS = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.FCFS.setObjectName("FCFS")
        self.gridLayout.addWidget(self.FCFS, 0, 0, 1, 1)

        self.FCFS.clicked.connect(self.fcfs_integration)

        self.C_SCAN = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.C_SCAN.setObjectName("C_SCAN")
        self.gridLayout.addWidget(self.C_SCAN, 1, 1, 1, 1)

        self.C_SCAN.clicked.connect(self.c_scan_integration)

        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(350, 680, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(680, 680, 121, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(680, 740, 121, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(680, 800, 121, 51))
        self.label_5.setObjectName("label_5")
        self.first_head = QtWidgets.QLineEdit(parent=Form)
        self.first_head.setGeometry(QtCore.QRect(140, 710, 113, 20))
        self.first_head.setObjectName("first_head")
        self.first_head.setPlaceholderText("范围为0~1499")

        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(20, 710, 121, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.current_algorithm = QtWidgets.QLineEdit(parent=Form)
        self.current_algorithm.setGeometry(QtCore.QRect(800, 689, 113, 31))
        self.current_algorithm.setObjectName("current_algorithm")
        self.movement = QtWidgets.QLineEdit(parent=Form)
        self.movement.setGeometry(QtCore.QRect(800, 750, 113, 31))
        self.movement.setObjectName("movement")
        self.average = QtWidgets.QLineEdit(parent=Form)
        self.average.setGeometry(QtCore.QRect(800, 810, 113, 31))
        self.average.setObjectName("average")
        self.clear = QtWidgets.QPushButton(parent=Form)
        self.clear.setGeometry(QtCore.QRect(270, 710, 51, 21))
        self.clear.setObjectName("clear")

        self.clear.clicked.connect(self.input_clear)

        self.listView_origin = QtWidgets.QListView(parent=Form)
        self.listView_origin.setGeometry(QtCore.QRect(1028, 25, 171, 830))
        self.listView_origin.setObjectName("listView_origin")

        self.listView_fcfs = QtWidgets.QListView(parent=Form)
        self.listView_fcfs.setGeometry(QtCore.QRect(1210, 25, 150, 400))
        self.listView_fcfs.setObjectName("listView_fcfs")

        self.listView_sstf = QtWidgets.QListView(parent=Form)
        self.listView_sstf.setGeometry(QtCore.QRect(1380, 25, 150, 400))
        self.listView_sstf.setObjectName("listView_sstf")

        self.listView_look = QtWidgets.QListView(parent=Form)
        self.listView_look.setGeometry(QtCore.QRect(1210, 455, 150, 400))
        self.listView_look.setObjectName("listView_look")

        self.listView_cscan = QtWidgets.QListView(parent=Form)
        self.listView_cscan.setGeometry(QtCore.QRect(1380, 455, 150, 400))
        self.listView_cscan.setObjectName("listView_cscan")

        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(454, 705, 75, 24))
        self.pushButton.setObjectName("ALL")

        self.pushButton.clicked.connect(self.all_integration)

        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(1060, 5, 121, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(1210, 5, 170, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(parent=Form)
        self.label_9.setGeometry(QtCore.QRect(1380, 5, 170, 16))
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(parent=Form)
        self.label_10.setGeometry(QtCore.QRect(1210, 440, 170, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(parent=Form)
        self.label_11.setGeometry(QtCore.QRect(1380, 440, 170, 16))
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "磁盘调度算法模拟程序"))
        self.Generation.setText(_translate("Form", "生成随机序列"))
        self.LOOK.setText(_translate("Form", "LOOK"))
        self.SSTF.setText(_translate("Form", "SSTF"))
        self.FCFS.setText(_translate("Form", "FCFS"))
        self.C_SCAN.setText(_translate("Form", "C_SCAN"))
        self.pushButton.setText(_translate("Form", "ALL"))
        self.label_2.setText(_translate("Form", "请选择磁盘调度算法："))
        self.label_3.setText(_translate("Form", "当前磁盘调度算法："))
        self.label_4.setText(_translate("Form", "磁头移动数："))
        self.label_5.setText(_translate("Form", "平均寻道长度："))
        self.label_6.setText(_translate("Form", "请输入初始磁头位置："))
        self.label_7.setText(_translate("Form", "初始随机磁道号序列："))
        self.label_8.setText(_translate("Form", "FCFS："))
        self.label_9.setText(_translate("Form", "SSTF："))
        self.label_10.setText(_translate("Form", "LOOK："))
        self.label_11.setText(_translate("Form", "C-SCAN："))
        self.clear.setText(_translate("Form", "重置"))

    def input_clear(self):
        self.first_head.setText("")
        self.current_algorithm.setText("")
        self.movement.setText("")
        self.average.setText("")
        self.start = None
        self.list_generate = []
        self.list_plot = []
        self.listView_origin.setModel(QStringListModel([]))  # 清空原始数据列表
        self.listView_fcfs.setModel(QStringListModel([]))  # 清空 FCFS 列表
        self.listView_sstf.setModel(QStringListModel([]))  # 清空 SSTF 列表
        self.listView_look.setModel(QStringListModel([]))  # 清空 LOOK 列表
        self.listView_cscan.setModel(QStringListModel([]))  # 清空 C_SCAN 列表
        self.Flag = False



    def input(self):
        start_text = self.first_head.text()
        if not start_text.isdigit():
            self.warning_window_NAN()
            return False

        self.start = int(start_text)
        if self.start >= 1500 or self.start < 0:
            self.warning_window_OutOfRange()
            return False
        return True



    def generate(self):
        if self.input() == True:
            self.current_algorithm.setText("")
            self.movement.setText("")
            self.average.setText("")
            self.list_generate = test.generate_track_numbers(self.start)


            # 更新原始数据列表视图
            self.list_generate_str_origin = [str(num) for num in self.list_generate]
            self.listView_origin.setModel(QStringListModel(self.list_generate_str_origin))

            # 更新 FCFS 数据列表视图
            self.total_movement_fcfs, self.list_plot_fcfs, self.average_movement_fcfs = fcfs(self.start, self.list_generate)
            self.listView_fcfs.setModel(QStringListModel([str(num) for num in self.list_plot_fcfs]))

            # 更新 SSTF 数据列表视图
            self.total_movement_sstf, self.list_plot_sstf, self.average_movement_sstf = sstf(self.start, self.list_generate)
            self.listView_sstf.setModel(QStringListModel([str(num) for num in self.list_plot_sstf]))

            # 更新 LOOK 数据列表视图
            self.total_movement_look, self.list_plot_look, self.average_movement_look = look(self.start, self.list_generate, 400)
            self.listView_look.setModel(QStringListModel([str(num) for num in self.list_plot_look]))

            self.total_movement_cscan, self.list_plot_cscan, self.average_movement_cscan = c_scan(self.start, self.list_generate, 400)
            self.listView_cscan.setModel(QStringListModel([str(num) for num in self.list_plot_cscan]))

            self.Flag = True



    def fcfs_integration(self):
        if self.Flag == True:
            self.current_algorithm.setText("FCFS")
            self.average.setText(str(self.average_movement_fcfs))
            self.movement.setText(str(self.total_movement_fcfs))
            self.draw_widdget.start_fcfs(self.list_plot_fcfs)
        else:
            self.warning_window_not_generation()


    def sstf_integration(self):
        if self.Flag == True:
            self.current_algorithm.setText("SSTF")
            self.average.setText(str(self.average_movement_sstf))
            self.movement.setText(str(self.total_movement_sstf))
            self.draw_widdget.start_sstf(self.list_plot_sstf)
        else:
            self.warning_window_not_generation()

    def look_integration(self):
        if self.Flag == True:
            self.current_algorithm.setText("LOOK")
            self.average.setText(str(self.average_movement_look))
            self.movement.setText(str(self.total_movement_look))
            self.draw_widdget.start_look(self.list_plot_look)
        else:
            self.warning_window_not_generation()


    def c_scan_integration(self):
        if self.Flag == True:
            self.current_algorithm.setText("C_SCAN")
            self.average.setText(str(self.average_movement_cscan))
            self.movement.setText(str(self.total_movement_cscan))
            self.draw_widdget.start_cscan(self.list_plot_cscan)
        else:
            self.warning_window_not_generation()

    def all_integration(self):
        if self.Flag == True:
            self.current_algorithm.setText("ALL")
            self.average.setText("")
            self.movement.setText("")
            self.draw_widdget.plot_all_lists(self.list_plot_fcfs, self.list_plot_sstf, self.list_plot_look, self.list_plot_cscan)
        else:
            self.warning_window_not_generation()

    def warning_window_OutOfRange(self):
        QMessageBox.information(self, 'Warning', '请输入范围在0~1499的数字!')

    def warning_window_NAN(self):
        QMessageBox.information(self, 'Warning', '请输入数字!')

    def warning_window_not_generation(self):
        QMessageBox.information(self, 'Warning', '请先生成随机序列!')




if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication, QWidget

    app = QApplication(sys.argv)

    ui = Ui_Form()

    ui.show()

    sys.exit(app.exec())
