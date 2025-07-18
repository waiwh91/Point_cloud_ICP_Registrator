# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.8.0.dev2411221125
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from pyqtgraph.opengl import GLViewWidget
import pyqtgraph as pg
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog

import point_cloud_viewer
import Icp_registrator
import pre_change_attributions


import open3d as o3d
import numpy as np
import copy
import datetime
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1625, 863)
        MainWindow.setStyleSheet("background-color: rgb(155, 155, 155);")

        # self.Navigator = QtWidgets.QTabWidget(MainWindow)
        # self.Navigator.setGeometry(QtCore.QRect(0, 0, 100, 100))
        #
        # self.tab1 = QtWidgets.QWidget()
        # self.tab1.setObjectName("tab1")
        # self.tab2 = QtWidgets.QWidget()
        # self.tab2.setObjectName("tab2")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Pcd_template = GLViewWidget(parent=self.centralwidget)
        self.Pcd_template.setBackgroundColor(QtGui.QColor(135, 135, 135))
        self.Pcd_template.setObjectName("Pcd_template")
        self.Pcd_template.setGeometry(QtCore.QRect(20, 10, 701, 381))
        self.Pcd_template.setObjectName("Pcd_template")
        self.Ict_target = GLViewWidget(parent=self.centralwidget)
        self.Ict_target.setBackgroundColor(QtGui.QColor(135, 135, 135))
        self.Ict_target.setGeometry(QtCore.QRect(20, 410, 701, 381))
        self.Ict_target.setObjectName("Ict_target")
        self.ict_result = GLViewWidget(parent=self.centralwidget)
        self.ict_result.setBackgroundColor(QtGui.QColor(135, 135, 135))
        self.ict_result.setGeometry(QtCore.QRect(740, 10, 731, 641))
        self.ict_result.setObjectName("ict_result")
        self.input_template = QtWidgets.QPushButton(parent=self.centralwidget)
        self.input_template.setGeometry(QtCore.QRect(1500, 30, 111, 61))
        self.input_template.setObjectName("input_template")
        self.input_target = QtWidgets.QPushButton(parent=self.centralwidget)
        self.input_target.setGeometry(QtCore.QRect(1500, 120, 111, 61))
        self.input_target.setObjectName("input_target")

        self.ict_settings = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ict_settings.setGeometry(QtCore.QRect(1500, 210, 111, 61))
        self.ict_settings.setObjectName("ict_settings")

        self.start_ict = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_ict.setGeometry(QtCore.QRect(1500, 340, 111, 61))
        self.start_ict.setObjectName("start_ict")
        self.save_matrix = QtWidgets.QPushButton(parent=self.centralwidget)
        self.save_matrix.setGeometry(QtCore.QRect(1500, 440, 111, 61))
        self.save_matrix.setObjectName("save_matrix")
        self.matrix = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.matrix.setGeometry(QtCore.QRect(740, 660, 731, 131))
        self.matrix.setObjectName("matrix")
        self.load_matrix = QtWidgets.QPushButton(parent=self.centralwidget)
        self.load_matrix.setGeometry(QtCore.QRect(1500, 540, 111, 61))
        self.load_matrix.setObjectName("load_matrix")
        self.transform_with_matrix = QtWidgets.QPushButton(parent=self.centralwidget)
        self.transform_with_matrix.setGeometry(QtCore.QRect(1500, 640, 111, 61))
        self.transform_with_matrix.setObjectName("transform_with_matrix")
        self.compare = QtWidgets.QPushButton(parent=self.centralwidget)
        self.compare.setGeometry(QtCore.QRect(1500, 740, 111, 61))
        self.compare.setObjectName("compare")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1625, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_bind()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Radar_ICT_Tool"))
        self.input_template.setText(_translate("MainWindow", "导入模版"))
        self.input_target.setText(_translate("MainWindow", "导入目标"))
        self.start_ict.setText(_translate("MainWindow", "开始配准"))
        self.save_matrix.setText(_translate("MainWindow", "保存变换矩阵"))
        self.load_matrix.setText(_translate("MainWindow", "导入变换矩阵"))
        self.transform_with_matrix.setText(_translate("MainWindow", "预设变换"))
        self.compare.setText(_translate("MainWindow", "重叠对比"))
        self.ict_settings.setText(_translate("MainWindow", "粗配准设定"))

    def button_bind(self):
        self.input_template.clicked.connect(self.import_template)
        self.input_target.clicked.connect(self.import_target)
        self.start_ict.clicked.connect(self.start_registration)
        self.compare.clicked.connect(self.result_compare)
        self.save_matrix.clicked.connect(self.save_transformation_matrix)
        self.load_matrix.clicked.connect(self.open_saved_transformation_matrix)
        self.transform_with_matrix.clicked.connect(self.transform_with_loaded_matrix)
        self.ict_settings.clicked.connect(self.open_pre_change)

    def import_target(self):
        print('import_target')

        select_form = QFileDialog()

        pcd_target_filepath, _ = select_form.getOpenFileName(None, '选择配准目标', '.', 'pcd(*.pcd)')
        self.global_transformation_matrix = np.asarray([[0.0, 0.0, 1.0, 0.0],
                                                  [-1.0, 0.0, 0.0, 0.0],
                                                  [0.0, -1.0, 0.0, 0.0],
                                                   [0.0, 0.0, 0.0, 1.0]])

        self.target_name = os.path.basename(pcd_target_filepath)
        self.original_pcd_target = o3d.io.read_point_cloud(pcd_target_filepath)
        self.pcd_target = o3d.io.read_point_cloud(pcd_target_filepath).transform(self.global_transformation_matrix)

        print(pcd_target_filepath)

        self.show_target_pcd(self.pcd_target)

    def import_template(self):
        print('import_template')

        select_form = QFileDialog()

        pcd_template_filepath, _ = select_form.getOpenFileName(None, '选择配准模版', '.', 'pcd(*.pcd)' )

        self.pcd_template = o3d.io.read_point_cloud(pcd_template_filepath)

        print(pcd_template_filepath)

        self.show_template_pcd(self.pcd_template)



        # if select_form.exec() :
        #     fileNames = select_form.selectedFiles()

    def show_template_pcd(self, pcd):
        template_viewer = point_cloud_viewer.PointCloudViewer(parent=self.Pcd_template, pcd=pcd, type="Template")
        self.Pcd_template.clear()
        self.Pcd_template.addItem(template_viewer.pcd_plot_item)


    def show_target_pcd(self, pcd):
        target_viewer = point_cloud_viewer.PointCloudViewer(parent=self.Ict_target, pcd=pcd, type="Target")
        self.Ict_target.clear()
        self.Ict_target.addItem(target_viewer.pcd_plot_item)


    def start_registration(self):
        icp_registrator = Icp_registrator.ICP_Registrator(self.pcd_template, self.pcd_target)
        self.icp_result, self.icp_matrix = icp_registrator.icp_registration()
        o3d.io.write_point_cloud(f"Data/Output/Output{self.target_name}.pcd", self.icp_result)
        self.matrix.setPlainText(str(self.icp_matrix))
        result_viewer = point_cloud_viewer.PointCloudViewer(parent=self.ict_result, pcd=self.icp_result, type="Result")
        self.ict_result.clear()
        self.ict_result.addItem(result_viewer.pcd_plot_item)

    def result_compare(self):

   ###########################################################################################COMPARE WITH GIVEN RESULT
        # compare_pcd = o3d.io.read_point_cloud('/home/martin/Point-Cloud-Registration/Data/001/output.pcd')

        # self.draw_registration_result(self.icp_result, self.pcd_target)
        rot90 = np.asarray([[0, -1, 0, 0],
                           [1, 0, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])
        self.draw_registration_result(self.pcd_template, self.icp_result)

    def draw_registration_result(self, source, target):
        print(source)
        print('123123')
        print(target)
        source_temp = copy.deepcopy(source)
        target_temp = copy.deepcopy(target)
        source_temp.paint_uniform_color([1, 0.706, 0])
        target_temp.paint_uniform_color([0, 0.651, 0.929])

        o3d.visualization.draw_geometries([source_temp, target_temp],
                                      zoom=0.4459,
                                      front=[0.9288, -0.2951, -0.2242],
                                      lookat=[1.6784, 2.0612, 1.4451],
                                      up=[-0.3402, -0.9189, -0.1996])
    def save_transformation_matrix(self):
        time = datetime.datetime.now()
        print(time)
        npmatrix = np.asarray(self.icp_matrix)
        np.save(f"{time}.npy", npmatrix)


    def open_saved_transformation_matrix(self):
        select_form = QFileDialog()
        matrix_filepath, _ = select_form.getOpenFileName(None, '选择变换矩阵', '.', 'npy(*.npy)' )
        # loaded_file = open(f"{pcd_template_filepath}", 'r')
        self.loaded_matrix = np.load(f"{matrix_filepath}")
        self.matrix.setPlainText(str(self.loaded_matrix))

    def transform_with_loaded_matrix(self):
        matrix = self.loaded_matrix
        print(matrix.shape)
        self.pcd_target = self.pcd_target.transform(self.global_transformation_matrix)
        self.icp_result = self.pcd_target.transform(matrix)

        result_viewer = point_cloud_viewer.PointCloudViewer(parent=self.ict_result, pcd=self.icp_result, type="Result")
        self.ict_result.clear()
        self.ict_result.addItem(result_viewer.pcd_plot_item)

    def open_pre_change(self):

        # # app = QtWidgets.QApplication(sys.argv)

        self.pre_change_window = GLViewWidget()

        self.ui = pre_change.Ui_pre_change(self.original_pcd_target, self.pcd_template)

        self.ui.setupUi(self.pre_change_window)

        self.pre_change_window.show()
        # # sys.exit(app.exec())




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = pg.QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
