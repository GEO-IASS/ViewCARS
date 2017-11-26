# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1502, 857)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("/*\n"
"    Copyright 2013 Emanuel Claesson\n"
"\n"
"    Licensed under the Apache License, Version 2.0 (the \"License\");\n"
"    you may not use this file except in compliance with the License.\n"
"    You may obtain a copy of the License at\n"
"\n"
"        http://www.apache.org/licenses/LICENSE-2.0\n"
"\n"
"    Unless required by applicable law or agreed to in writing, software\n"
"    distributed under the License is distributed on an \"AS IS\" BASIS,\n"
"    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n"
"    See the License for the specific language governing permissions and\n"
"    limitations under the License.\n"
"*/\n"
"\n"
"/*\n"
"    COLOR_DARK     = #191919\n"
"    COLOR_MEDIUM   = #353535\n"
"    COLOR_MEDLIGHT = #5A5A5A\n"
"    COLOR_LIGHT    = #DDDDDD\n"
"    COLOR_ACCENT   = #3D7848\n"
"*/\n"
"\n"
"* {\n"
"    background: #191919;\n"
"    color: #DDDDDD;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QCheckBox, QRadioButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator, QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked, QCheckBox::indicator::unchecked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover, QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked, QCheckBox::indicator::checked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #5A5A5A;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover, QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"    background: #DDDDDD;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    margin-top: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -7px;\n"
"    left: 7px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #191919;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 15px;\n"
"    margin: 0px 0px 0px 32px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 15px;\n"
"    margin: 32px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #353535;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    border-width: 0px 1px 0px 1px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    border-width: 1px 0px 1px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background:#353535;\n"
"    border: 1px solid #5A5A5A;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"    position: absolute;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    left: 15px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    top: 15px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: top left;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"}\n"
"\n"
"QScrollBar:left-arrow, QScrollBar::right-arrow, QScrollBar::up-arrow, QScrollBar::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QAbstractButton:pressed {\n"
"    background: #5A5A5A;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"    show-decoration-selected: 1;\n"
"    selection-background-color: #3D7848;\n"
"    selection-color: #DDDDDD;\n"
"    alternate-background-color: #353535;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #191919;\n"
"    border: 1px solid #5A5A5A;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QHeaderView::section:selected, QHeaderView::section::checked {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QTableView {\n"
"    gridline-color: #5A5A5A;\n"
"}\n"
"\n"
"QTabBar {\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-radius: 0px;\n"
"    padding: 4px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"    subcontrol-origin: border;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QSlider {\n"
"    border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    margin: 4px 0px 4px 0px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    margin: 0px 4px 0px 4px;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 15px;\n"
"    margin: -4px 0px -4px 0px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 15px;\n"
"    margin: 0px -4px 0px -4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical, QSlider::sub-page:horizontal {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical, QSlider::add-page:horizontal {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: none;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 1px;\n"
"    background-color: #3D7848;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    background: #353535;\n"
"}")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.image_win = ImageView(self.centralWidget)
        self.image_win.setGeometry(QtCore.QRect(30, 70, 561, 461))
        self.image_win.setObjectName("image_win")
        self.RESET = QtWidgets.QPushButton(self.centralWidget)
        self.RESET.setGeometry(QtCore.QRect(1370, 400, 101, 31))
        self.RESET.setStyleSheet("QPushButton {\n"
"    background: #4a1b15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #62221b;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #762720;     \n"
"}")
        self.RESET.setObjectName("RESET")
        self.update_image = QtWidgets.QPushButton(self.centralWidget)
        self.update_image.setGeometry(QtCore.QRect(1370, 440, 101, 41))
        self.update_image.setStyleSheet("QPushButton {\n"
"    background: #323e30;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #3e5f41;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #537f57;     \n"
"}")
        self.update_image.setObjectName("update_image")
        self.update_spectrum = QtWidgets.QPushButton(self.centralWidget)
        self.update_spectrum.setGeometry(QtCore.QRect(1370, 490, 101, 41))
        self.update_spectrum.setStyleSheet("QPushButton {\n"
"    background: #323e30;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #3e5f41;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #537f57;     \n"
"}")
        self.update_spectrum.setObjectName("update_spectrum")
        self.image_selection_box = QtWidgets.QGroupBox(self.centralWidget)
        self.image_selection_box.setGeometry(QtCore.QRect(1370, 70, 101, 141))
        self.image_selection_box.setObjectName("image_selection_box")
        self.track1_image_select = QtWidgets.QRadioButton(self.image_selection_box)
        self.track1_image_select.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.track1_image_select.setChecked(False)
        self.track1_image_select.setObjectName("track1_image_select")
        self.track2_image_select = QtWidgets.QRadioButton(self.image_selection_box)
        self.track2_image_select.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.track2_image_select.setChecked(False)
        self.track2_image_select.setObjectName("track2_image_select")
        self.sipcars_image_select = QtWidgets.QRadioButton(self.image_selection_box)
        self.sipcars_image_select.setGeometry(QtCore.QRect(10, 110, 82, 17))
        self.sipcars_image_select.setChecked(True)
        self.sipcars_image_select.setObjectName("sipcars_image_select")
        self.sum_image_select = QtWidgets.QRadioButton(self.image_selection_box)
        self.sum_image_select.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.sum_image_select.setChecked(False)
        self.sum_image_select.setObjectName("sum_image_select")
        self.spectrum_win = PlotWidget(self.centralWidget)
        self.spectrum_win.setGeometry(QtCore.QRect(640, 70, 721, 461))
        self.spectrum_win.setObjectName("spectrum_win")
        self.file_box = QtWidgets.QGroupBox(self.centralWidget)
        self.file_box.setGeometry(QtCore.QRect(30, 10, 561, 51))
        self.file_box.setObjectName("file_box")
        self.load_file = QtWidgets.QPushButton(self.file_box)
        self.load_file.setGeometry(QtCore.QRect(440, 19, 91, 21))
        self.load_file.setObjectName("load_file")
        self.cars_file_name = QtWidgets.QLineEdit(self.file_box)
        self.cars_file_name.setGeometry(QtCore.QRect(20, 19, 421, 21))
        self.cars_file_name.setReadOnly(True)
        self.cars_file_name.setObjectName("cars_file_name")
        self.error_box = QtWidgets.QGroupBox(self.centralWidget)
        self.error_box.setGeometry(QtCore.QRect(640, 10, 721, 51))
        self.error_box.setObjectName("error_box")
        self.error_text = QtWidgets.QLineEdit(self.error_box)
        self.error_text.setGeometry(QtCore.QRect(10, 20, 701, 21))
        self.error_text.setReadOnly(True)
        self.error_text.setObjectName("error_text")
        self.plot_selection_box = QtWidgets.QGroupBox(self.centralWidget)
        self.plot_selection_box.setGeometry(QtCore.QRect(1370, 220, 101, 141))
        self.plot_selection_box.setObjectName("plot_selection_box")
        self.track1_plot_select = QtWidgets.QCheckBox(self.plot_selection_box)
        self.track1_plot_select.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.track1_plot_select.setObjectName("track1_plot_select")
        self.track2_plot_select = QtWidgets.QCheckBox(self.plot_selection_box)
        self.track2_plot_select.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.track2_plot_select.setObjectName("track2_plot_select")
        self.sum_plot_select = QtWidgets.QCheckBox(self.plot_selection_box)
        self.sum_plot_select.setGeometry(QtCore.QRect(10, 80, 70, 17))
        self.sum_plot_select.setObjectName("sum_plot_select")
        self.sipcars_plot_select = QtWidgets.QCheckBox(self.plot_selection_box)
        self.sipcars_plot_select.setGeometry(QtCore.QRect(10, 110, 70, 17))
        self.sipcars_plot_select.setChecked(True)
        self.sipcars_plot_select.setObjectName("sipcars_plot_select")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 540, 1441, 251))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setStyleSheet("QTabWidget {\n"
"border: 0;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"border: 0;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.normalisation_tab = QtWidgets.QWidget()
        self.normalisation_tab.setObjectName("normalisation_tab")
        self.normalisation_spectrum_win = PlotWidget(self.normalisation_tab)
        self.normalisation_spectrum_win.setGeometry(QtCore.QRect(830, 10, 591, 201))
        self.normalisation_spectrum_win.setObjectName("normalisation_spectrum_win")
        self.pump_file_name = QtWidgets.QLineEdit(self.normalisation_tab)
        self.pump_file_name.setGeometry(QtCore.QRect(10, 10, 441, 21))
        self.pump_file_name.setReadOnly(True)
        self.pump_file_name.setObjectName("pump_file_name")
        self.load_pump_file = QtWidgets.QPushButton(self.normalisation_tab)
        self.load_pump_file.setGeometry(QtCore.QRect(450, 10, 101, 21))
        self.load_pump_file.setObjectName("load_pump_file")
        self.load_stokes_file = QtWidgets.QPushButton(self.normalisation_tab)
        self.load_stokes_file.setGeometry(QtCore.QRect(450, 40, 101, 21))
        self.load_stokes_file.setObjectName("load_stokes_file")
        self.stokes_file_name = QtWidgets.QLineEdit(self.normalisation_tab)
        self.stokes_file_name.setGeometry(QtCore.QRect(10, 40, 441, 21))
        self.stokes_file_name.setReadOnly(True)
        self.stokes_file_name.setObjectName("stokes_file_name")
        self.load_etalon_file = QtWidgets.QPushButton(self.normalisation_tab)
        self.load_etalon_file.setGeometry(QtCore.QRect(450, 70, 101, 21))
        self.load_etalon_file.setObjectName("load_etalon_file")
        self.load_etalonpump_file = QtWidgets.QPushButton(self.normalisation_tab)
        self.load_etalonpump_file.setGeometry(QtCore.QRect(450, 100, 101, 21))
        self.load_etalonpump_file.setObjectName("load_etalonpump_file")
        self.etalonpump_file_name = QtWidgets.QLineEdit(self.normalisation_tab)
        self.etalonpump_file_name.setGeometry(QtCore.QRect(10, 100, 441, 21))
        self.etalonpump_file_name.setReadOnly(True)
        self.etalonpump_file_name.setObjectName("etalonpump_file_name")
        self.etalon_file_name = QtWidgets.QLineEdit(self.normalisation_tab)
        self.etalon_file_name.setGeometry(QtCore.QRect(10, 70, 441, 21))
        self.etalon_file_name.setReadOnly(True)
        self.etalon_file_name.setObjectName("etalon_file_name")
        self.load_etalonstokes_file = QtWidgets.QPushButton(self.normalisation_tab)
        self.load_etalonstokes_file.setGeometry(QtCore.QRect(450, 130, 101, 21))
        self.load_etalonstokes_file.setObjectName("load_etalonstokes_file")
        self.etalonstokes_file_name = QtWidgets.QLineEdit(self.normalisation_tab)
        self.etalonstokes_file_name.setGeometry(QtCore.QRect(10, 130, 441, 21))
        self.etalonstokes_file_name.setReadOnly(True)
        self.etalonstokes_file_name.setObjectName("etalonstokes_file_name")
        self.normalisation_box = QtWidgets.QGroupBox(self.normalisation_tab)
        self.normalisation_box.setGeometry(QtCore.QRect(580, 10, 221, 201))
        self.normalisation_box.setObjectName("normalisation_box")
        self.lineEdit = QtWidgets.QLineEdit(self.normalisation_box)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 91, 20))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setStyleSheet("border: 0")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pca_comp_no = QtWidgets.QLineEdit(self.normalisation_box)
        self.pca_comp_no.setGeometry(QtCore.QRect(120, 30, 81, 20))
        self.pca_comp_no.setObjectName("pca_comp_no")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.normalisation_box)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 100, 101, 20))
        self.lineEdit_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_5.setStyleSheet("border: 0")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.nrb_no_min = QtWidgets.QLineEdit(self.normalisation_box)
        self.nrb_no_min.setGeometry(QtCore.QRect(150, 120, 51, 20))
        self.nrb_no_min.setObjectName("nrb_no_min")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.normalisation_box)
        self.lineEdit_7.setGeometry(QtCore.QRect(40, 120, 101, 20))
        self.lineEdit_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_7.setStyleSheet("border: 0")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.nrb_no_max = QtWidgets.QLineEdit(self.normalisation_box)
        self.nrb_no_max.setGeometry(QtCore.QRect(150, 140, 51, 20))
        self.nrb_no_max.setObjectName("nrb_no_max")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.normalisation_box)
        self.lineEdit_9.setGeometry(QtCore.QRect(40, 140, 101, 20))
        self.lineEdit_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_9.setStyleSheet("border: 0")
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pca_comp_enter = QtWidgets.QPushButton(self.normalisation_box)
        self.pca_comp_enter.setGeometry(QtCore.QRect(20, 60, 181, 23))
        self.pca_comp_enter.setStyleSheet("QPushButton {\n"
"    background: #323e30;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #3e5f41;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #537f57;     \n"
"}")
        self.pca_comp_enter.setObjectName("pca_comp_enter")
        self.nrb_enter = QtWidgets.QPushButton(self.normalisation_box)
        self.nrb_enter.setGeometry(QtCore.QRect(20, 170, 181, 23))
        self.nrb_enter.setStyleSheet("QPushButton {\n"
"    background: #323e30;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #3e5f41;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #537f57;     \n"
"}")
        self.nrb_enter.setObjectName("nrb_enter")
        self.run_normalisation = QtWidgets.QPushButton(self.normalisation_tab)
        self.run_normalisation.setGeometry(QtCore.QRect(10, 170, 541, 41))
        self.run_normalisation.setStyleSheet("QPushButton {\n"
"    background: #323e30;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #3e5f41;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #537f57;     \n"
"}")
        self.run_normalisation.setObjectName("run_normalisation")
        self.tabWidget.addTab(self.normalisation_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 1421, 201))
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 431, 181))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pca_cluster_choose = QtWidgets.QSpinBox(self.groupBox_5)
        self.pca_cluster_choose.setGeometry(QtCore.QRect(280, 130, 42, 22))
        self.pca_cluster_choose.setMaximum(0)
        self.pca_cluster_choose.setObjectName("pca_cluster_choose")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 30, 101, 20))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_2.setStyleSheet("border: 0")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pca_cluster_comp_no = QtWidgets.QLineEdit(self.groupBox_5)
        self.pca_cluster_comp_no.setGeometry(QtCore.QRect(130, 30, 81, 20))
        self.pca_cluster_comp_no.setObjectName("pca_cluster_comp_no")
        self.pca_cluster_whiten = QtWidgets.QCheckBox(self.groupBox_5)
        self.pca_cluster_whiten.setGeometry(QtCore.QRect(280, 30, 91, 20))
        self.pca_cluster_whiten.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pca_cluster_whiten.setObjectName("pca_cluster_whiten")
        self.pca_cluster_run = QtWidgets.QPushButton(self.groupBox_5)
        self.pca_cluster_run.setGeometry(QtCore.QRect(20, 70, 191, 41))
        self.pca_cluster_run.setStyleSheet("QPushButton {\n"
"    background: #323e30;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #3e5f41;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #537f57;     \n"
"}")
        self.pca_cluster_run.setObjectName("pca_cluster_run")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 130, 171, 20))
        self.lineEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_3.setStyleSheet("border: 0")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pca_cluster_clear = QtWidgets.QPushButton(self.groupBox_5)
        self.pca_cluster_clear.setGeometry(QtCore.QRect(220, 70, 191, 41))
        self.pca_cluster_clear.setStyleSheet("QPushButton {\n"
"    background: #4a1b15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #62221b;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #762720;     \n"
"}")
        self.pca_cluster_clear.setObjectName("pca_cluster_clear")
        self.pca_cluster_image_win = ImageView(self.tab_4)
        self.pca_cluster_image_win.setGeometry(QtCore.QRect(470, 10, 341, 181))
        self.pca_cluster_image_win.setObjectName("pca_cluster_image_win")
        self.pca_cluster_spectrum_win = PlotWidget(self.tab_4)
        self.pca_cluster_spectrum_win.setGeometry(QtCore.QRect(820, 10, 561, 181))
        self.pca_cluster_spectrum_win.setObjectName("pca_cluster_spectrum_win")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.show_state = QtWidgets.QGroupBox(self.centralWidget)
        self.show_state.setGeometry(QtCore.QRect(1370, 10, 101, 51))
        self.show_state.setStyleSheet("background: #323e30")
        self.show_state.setTitle("")
        self.show_state.setObjectName("show_state")
        self.show_state_text = QtWidgets.QLineEdit(self.show_state)
        self.show_state_text.setGeometry(QtCore.QRect(40, 20, 31, 20))
        self.show_state_text.setStyleSheet("border: 0;")
        self.show_state_text.setReadOnly(True)
        self.show_state_text.setObjectName("show_state_text")
        self.cars_data_type = QtWidgets.QComboBox(self.centralWidget)
        self.cars_data_type.setGeometry(QtCore.QRect(1370, 370, 101, 22))
        self.cars_data_type.setObjectName("cars_data_type")
        self.cars_data_type.addItem("")
        self.cars_data_type.addItem("")
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1502, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_Session = QtWidgets.QAction(MainWindow)
        self.actionSave_Session.setObjectName("actionSave_Session")
        self.mainToolBar.addSeparator()
        self.menuFile.addAction(self.actionSave_Session)
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.cars_data_type.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RESET.setText(_translate("MainWindow", "RESET"))
        self.update_image.setText(_translate("MainWindow", "Update Image"))
        self.update_spectrum.setText(_translate("MainWindow", "Update Spectrum"))
        self.image_selection_box.setTitle(_translate("MainWindow", "Image Selection"))
        self.track1_image_select.setText(_translate("MainWindow", "Track1"))
        self.track2_image_select.setText(_translate("MainWindow", "Track 2"))
        self.sipcars_image_select.setText(_translate("MainWindow", "SIPCARS"))
        self.sum_image_select.setText(_translate("MainWindow", "Sum"))
        self.file_box.setTitle(_translate("MainWindow", "CARS Data File"))
        self.load_file.setText(_translate("MainWindow", "Load File"))
        self.error_box.setTitle(_translate("MainWindow", "Notification"))
        self.plot_selection_box.setTitle(_translate("MainWindow", "Plot Selection"))
        self.track1_plot_select.setText(_translate("MainWindow", "Track 1"))
        self.track2_plot_select.setText(_translate("MainWindow", "Track 2"))
        self.sum_plot_select.setText(_translate("MainWindow", "Sum"))
        self.sipcars_plot_select.setText(_translate("MainWindow", "SIPCARS"))
        self.load_pump_file.setText(_translate("MainWindow", "Load Pump"))
        self.load_stokes_file.setText(_translate("MainWindow", "Load Stokes"))
        self.load_etalon_file.setText(_translate("MainWindow", "Load Etalon"))
        self.load_etalonpump_file.setText(_translate("MainWindow", "Load Etalon Pump"))
        self.load_etalonstokes_file.setText(_translate("MainWindow", "Load Etalon Stokes"))
        self.normalisation_box.setTitle(_translate("MainWindow", "Normalisation Details"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "PCA Components:"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Enter NRB Region:"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "Min wavenumber:"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "Max wavenumber:"))
        self.pca_comp_enter.setText(_translate("MainWindow", "Enter"))
        self.nrb_enter.setText(_translate("MainWindow", "Enter"))
        self.run_normalisation.setText(_translate("MainWindow", "Run Normalisation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.normalisation_tab), _translate("MainWindow", "Normalisation"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Factorisation Technique Details"))
        self.lineEdit_2.setText(_translate("MainWindow", "No. of Components:"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "PCA Components:"))
        self.pca_cluster_whiten.setText(_translate("MainWindow", "Whiten data?"))
        self.pca_cluster_run.setText(_translate("MainWindow", "Run PCA Decomposition"))
        self.lineEdit_3.setText(_translate("MainWindow", "Select which component to view:"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "PCA Components:"))
        self.pca_cluster_clear.setText(_translate("MainWindow", "CLEAR"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "PCA"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Kernel PCA"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "ICA"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "NNMF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Unsupervised Clustering"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Image Code Correction"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "tbc..."))
        self.show_state_text.setPlaceholderText(_translate("MainWindow", "Idle"))
        self.cars_data_type.setItemText(0, _translate("MainWindow", "Raw Data"))
        self.cars_data_type.setItemText(1, _translate("MainWindow", "Normalised Data"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSave_Session.setText(_translate("MainWindow", "Save Session"))

from pyqtgraph import ImageView, PlotWidget
