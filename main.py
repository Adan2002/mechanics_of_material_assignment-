from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
import pyqtgraph as pg
import numpy as np
# from main_ui import Ui_Form
# from VForce_ui import *
# from HForce_ui import *
# from ForceZai_ui import *
# from ForceOther_ui import *
# from Yueshu1_ui import *
# from Yueshu2_ui import *
# from Yueshu3_ui import *
import sys
import os
os.environ['QT_MAC_WANTS_LAYER'] = '1'


# class WindowVForce(QWidget):
#     force = 0
#     dist = 0
#
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_VForce()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.return_main)
#
#     def return_main(self):
#         self.force = self.ui.lineEdit.text()
#         self.dist = self.ui.lineEdit_2.text()
#         if self.force.isdigit() and self.dist.isdigit():
#             self.close()
#         else:
#             self.force = 0
#             self.dist = 0
#             QMessageBox.information(None, '注意！', '请输入数字！')
#
#
# class WindowHForce(QWidget):
#     force = 0
#     dist = 0
#
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_HForce()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.return_main)
#
#     def return_main(self):
#         self.force = self.ui.lineEdit.text()
#         self.dist = self.ui.lineEdit_2.text()
#         if self.force.isdigit() and self.dist.isdigit():
#             self.close()
#         else:
#             self.force = 0
#             self.dist = 0
#             QMessageBox.information(None, '注意！', '请输入数字！')
#
#
# class WindowForceOther(QWidget):
#     force = 0
#     dist = 0
#
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_ForceOther()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.return_main)
#
#     def return_main(self):
#         self.force = self.ui.lineEdit.text()
#         self.dist = self.ui.lineEdit_2.text()
#         if self.force.isdigit() and self.dist.isdigit():
#             self.close()
#         else:
#             self.force = 0
#             self.dist = 0
#             QMessageBox.information(None, '注意！', '请输入数字！')
#
#
# class WindowForceZai(QWidget):
#     force = 0
#     dist1 = 0
#     dist2 = 0
#
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_ForceZai()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.return_main)
#
#     def return_main(self):
#         self.force = self.ui.lineEdit.text()
#         self.dist1 = self.ui.lineEdit_2.text()
#         self.dist2 = self.ui.lineEdit_3.text()
#         if self.force.isdigit() and self.dist1.isdigit() and self.dist2.isdigit():
#             self.close()
#         else:
#             self.force = 0
#             self.dist1 = 0
#             self.dist2 = 0
#             QMessageBox.information(None, '注意！', '请输入数字！')
#
#
# class WindowYueshu3(QWidget):
#     dist = 0
#
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_Yueshu3()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.return_main)
#
#     def return_main(self):
#         self.dist = self.ui.lineEdit.text()
#         if self.dist.isdigit():
#             self.close()
#         else:
#             self.dist = 0
#             QMessageBox.information(None, '注意！', '请输入数字！')
#
#
# class WindowYueshu2(QWidget):
#     dist = 0
#
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_Yueshu2()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.return_main)
#
#     def return_main(self):
#         self.dist = self.ui.lineEdit.text()
#         if self.dist.isdigit():
#             self.close()
#         else:
#             self.dist = 0
#             QMessageBox.information(None, '注意！', '请输入数字！')
#
#
# class WindowYueshu1(QWidget):
#     dist = 0
#
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_Yueshu1()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.return_main)
#
#     def return_main(self):
#         self.dist = self.ui.lineEdit.text()
#         if self.dist.isdigit():
#             self.close()
#         else:
#             self.dist = 0
#             QMessageBox.information(None, '注意！', '请输入数字！')


class MainWindow(QMainWindow):
    length = 0
    E = 0
    A = 0
    I = 0
    vforce = []
    vdist = []
    hforce = []
    hdist = []
    forceother = []
    odist = []
    forceZai = []
    dist1 = []
    dist2 = []
    Yueshu3 = []
    Yueshu2 = []
    Yueshu1 = []

    def __init__(self):
        # super().__init__()
        # self.ui = Ui_Form()
        # self.ui.setupUi(self)
        loader = QUiLoader()
        loader.registerCustomWidget(pg.PlotWidget)
        self.ui = loader.load("main.ui")
        self.ui.pushButtonConfirm.clicked.connect(self.save_length)
        self.ui.pushButtonForce_1.clicked.connect(self.savevforce)
        self.ui.pushButtonForce_4.clicked.connect(self.savehforce)
        self.ui.pushButtonForce_2.clicked.connect(self.saveforcezai)
        self.ui.pushButtonForce_3.clicked.connect(self.saveforceother)
        self.ui.pushButton_1.clicked.connect(self.saveyueshu1)
        self.ui.pushButton_2.clicked.connect(self.saveyueshu2)
        self.ui.pushButton_11.clicked.connect(self.saveyueshu3)
        self.ui.pushButtonClear.clicked.connect(self.allclear)
        self.ui.pushButtonCalculate.clicked.connect(self.calculatemap)
        # self.childVForce = WindowVForce()
        # self.childHForce = Ui_HForce()
        # self.childForceOther = Ui_ForceOther()
        # self.childForceZai = Ui_ForceZai()
        # self.childYueshu1 = Ui_Yueshu1()
        # self.childYueshu2 = Ui_Yueshu2()
        # self.childYueshu3 = Ui_Yueshu3()
        # self.ui.pushButtonForce_1.clicked.connect(self.openchildVForce())

    # def openchildVForce(self):
    #     self.childVForce = WindowVForce()
    #     self.childVForce.show()
    #
    # def openchildHForce(self):
    #     self.childHForce = WindowHForce()
    #     self.childHForce.show()
    #
    # def openchildForceOther(self):
    #     self.childForceOther = WindowForceOther()
    #     self.childForceOther.show()
    #
    # def openchildForceZai(self):
    #     self.childForceZai = WindowForceZai()
    #     self.childForceZai.show()
    #
    # def openchildYueshu1(self):
    #     self.childYueshu1 = WindowYueshu1()
    #     self.childYueshu1.show()
    #
    # def openchildYueshu2(self):
    #     self.childYueshu2 = WindowYueshu2()
    #     self.childYueshu2.show()
    #
    # def openchildYueshu3(self):
    #     self.childYueshu3 = WindowYueshu3()
    #     self.childYueshu3.show()

    def save_length(self):
        temp1 = self.ui.lineLength.text()
        if not temp1.isdigit():
            QMessageBox.information(None, '注意！', '请输入数字！')
        else:
            self.length = float(temp1)
            print(self.length)

    def savevforce(self):
        temp1 = self.ui.lineLength_2.text()
        temp2 = self.ui.lineLength_3.text()
        if temp1.isdigit() and temp2.isdigit():
            self.vforce.append(float(temp1))
            self.vdist.append(float(temp2))
        else:
            QMessageBox.information(None, '注意！', '请输入数字！')

    def savehforce(self):
        temp1 = self.ui.lineLength_2.text()
        temp2 = self.ui.lineLength_3.text()
        if temp1.isdigit() and temp2.isdigit():
            self.hforce.append(float(temp1))
            self.hdist.append(float(temp2))
        else:
            QMessageBox.information(None, '注意！', '请输入数字！')

    def saveforceother(self):
        temp1 = self.ui.lineLength_2.text()
        temp2 = self.ui.lineLength_3.text()
        if temp1.isdigit() and temp2.isdigit():
            self.forceother.append(float(temp1))
            self.odist.append(float(temp2))
        else:
            QMessageBox.information(None, '注意！', '请输入数字！')

    def saveforcezai(self):
        temp1 = self.ui.lineLength_2.text()
        temp2 = self.ui.lineLength_3.text()
        temp3 = self.ui.lineLength_4.text()
        if temp1.isdigit() and temp2.isdigit() and temp3.isdigit():
            self.forceZai.append(float(temp1))
            self.dist1.append(float(temp2))
            self.dist2.append(float(temp3))
        else:
            QMessageBox.information(None, '注意！', '请输入数字！')

    def saveyueshu1(self):
        temp2 = self.ui.lineLength_3.text()
        if temp2.isdigit():
            self.Yueshu1.append(float(temp2))
        else:
            QMessageBox.information(None, '注意！', '请输入数字！')

    def saveyueshu2(self):
        temp2 = self.ui.lineLength_3.text()
        if temp2.isdigit():
            self.Yueshu2.append(float(temp2))
        else:
            QMessageBox.information(None, '注意！', '请输入数字！')

    def saveyueshu3(self):
        temp2 = self.ui.lineLength_3.text()
        if temp2.isdigit():
            self.Yueshu3.append(float(temp2))
        else:
            QMessageBox.information(None, '注意！', '请输入数字！')

    def allclear(self):
        self.vforce.clear()
        self.vdist.clear()
        self.hforce.clear()
        self.hdist.clear()
        self.forceother.clear()
        self.odist.clear()
        self.forceZai.clear()
        self.dist1.clear()
        self.dist2.clear()
        self.Yueshu2.clear()
        self.Yueshu1.clear()
        self.Yueshu3.clear()

    def calculatemap(self):
        hyueshu = len(self.Yueshu3) + len(self.Yueshu2)
        vyueshu = len(self.Yueshu1) + len(self.Yueshu2) + 2 * len(self.Yueshu3)
        x1 = np.array([0])
        x2 = np.array([self.length])
        f1 = np.array([0])
        m1 = np.array([0])
        if hyueshu == 1:
            hpos = self.hdist + self.Yueshu2 + self.Yueshu3
            hsum = 0.
            for i in range(0, len(self.hforce)):
                hsum = hsum - self.hforce[i]
            hforce = self.hforce + [hsum]
            hx = np.linspace(0, self.length, 1001)
            hy = np.zeros(1001)
            for i in range(0, len(hpos)):
                flag = 0
                for j in range(0, len(hx)):
                    if hx[j] >= hpos[i]:
                        flag = j
                        break
                hy[flag:] = hy[flag:] + hforce[i]
            hx = np.hstack((x1, hx, x2))
            hy = np.hstack((f1, hy, f1))
            self.ui.widget_zhou.plot(hx, hy)

        elif hyueshu == 2:
            # QMessageBox.information(None, '2', '2')
            hpos = self.hdist + self.Yueshu2 + self.Yueshu3
            hsum = 0.
            hmulti = 0.
            for i in range(0, len(self.hforce)):
                hsum = hsum - self.hforce[i]
                hmulti = hmulti + self.hforce[i] * (hpos[-1] - self.hdist[i])
            force2 = (-hmulti) / (hpos[-2] - hpos[-1])
            force1 = hsum - force2
            hforce = self.hforce + [force2] + [force1]
            hx = np.linspace(0, self.length, 1001)
            hy = np.zeros(1001)
            for i in range(0, len(hpos)):
                flag = 0
                for j in range(0, len(hx)):
                    if hx[j] >= hpos[i]:
                        flag = j
                        break
                hy[flag:] = hy[flag:] + hforce[i]
            hx = np.hstack((x1, hx, x2))
            hy = np.hstack((f1, hy, f1))
            self.ui.widget_zhou.plot(hx, hy)


        if vyueshu == 2:
            vpos = self.vdist + self.Yueshu3 + self.Yueshu2 + self.Yueshu1
            vsum = 0
            for i in range(0, len(self.vdist)):
                vsum = vsum - self.vforce[i]
            for i in range(0, len(self.forceZai)):
                vsum = vsum - self.forceZai[i] * (self.dist2[i] - self.dist1[i])
            if len(self.Yueshu3) == 1:
                vforce = self.vforce + [vsum]
            else:
                tempa = 0
                for i in range(0, len(self.vdist)):
                    tempa = tempa + self.vforce[i] * (self.vdist[i] - self.Yueshu1[0])
                for i in range(0, len(self.forceZai)):
                    tempa= tempa + self.forceZai[i] * (self.dist2[i] - self.dist1[i]) * (self.dist2[i] + self.dist1[i] - 2 * self.Yueshu1[0]) / 2
                yforce2 = (-tempa) / (self.Yueshu2[0] - self.Yueshu1[0])
                yforce1 = vsum - yforce2
                vforce = self.vforce + [yforce2] + [yforce1]

            vx = np.linspace(0, self.length, 1001)
            vy = np.zeros(1001)
            for i in range(0, len(vpos)):
                flag = 0
                for j in range(0, len(vx)):
                    if vx[j] >= vpos[i]:
                        flag = j
                        break
                vy[flag:] = vy[flag:] + vforce[i]
            for i in range(0, len(self.forceZai)):
                for j in range(0, len(vx)):
                    if self.dist1[i] <= vx[j] < self.dist2[i]:
                        vy[j:] = vy[j:] + self.forceZai[i] * self.length / 100
            vx_1 = np.hstack((x1, vx, x2))
            vy = np.hstack((f1, vy, f1))
            self.ui.widget_jian.plot(vx_1, vy)

            vm = np.zeros(1001)
            for i in range(0, len(vx)):
                vm[i:] = vm[i:] + vy[i] * self.length / 100
            if len(self.Yueshu3) == 1:
                tempa = 0
                for i in range(0, len(self.vdist)):
                    tempa = tempa + self.vforce[i] * (self.vdist[i] - self.Yueshu3[0])
                for i in range(0, len(self.forceZai)):
                    tempa = tempa + self.forceZai[i] * (self.dist2[i] - self.dist1[i]) * (self.dist2[i] + self.dist1[i] - 2 * self.Yueshu3[0]) / 2
                for i in range(0, len(self.forceother)):
                    tempa = tempa - self.forceother[i]
                yueshu3 = tempa
                flag = 0
                for i in range(0, len(vx)):
                    if vx[i] >= self.Yueshu3[0]:
                        flag = i
                        break
                vm[flag:] = vm[flag:] + yueshu3
            for i in range(0, len(self.forceother)):
                flag = 0
                for j in range(0, len(vx)):
                    if vx[j] >= self.odist[i]:
                        flag = j
                        break
                vm[flag:] = vm[flag:] + self.forceother[i]
            vx_2 = np.hstack((x1, vx, x2))
            vm = np.hstack((m1, vm, m1))
            self.ui.widget_wan.plot(vx_2, vm)

        elif vyueshu > 2:
            QMessageBox.information(None, '3', '3')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # MainWindow = QMainWindow()
    # ui = Ui_Form()
    # ui.setupUi(MainWindow)
    #
    # ui.pushButtonConfirm.clicked.connect(save_length)
    # ui.pushButtonForce_1.clicked()
    #
    # MainWindow.show()
    mainw = MainWindow()
    mainw.ui.show()
    sys.exit(app.exec_())