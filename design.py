# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Sat Feb  7 18:05:45 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(374, 526)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(3, 5, 3, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.batteryComboBox = QtGui.QComboBox(self.centralwidget)
        self.batteryComboBox.setObjectName(_fromUtf8("batteryComboBox"))
        self.batteryComboBox.addItem(_fromUtf8(""))
        self.batteryComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.batteryComboBox)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.installed = QtGui.QLabel(self.centralwidget)
        self.installed.setFrameShape(QtGui.QFrame.Box)
        self.installed.setFrameShadow(QtGui.QFrame.Plain)
        self.installed.setAlignment(QtCore.Qt.AlignCenter)
        self.installed.setObjectName(_fromUtf8("installed"))
        self.horizontalLayout.addWidget(self.installed)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_25 = QtGui.QLabel(self.centralwidget)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_2.addWidget(self.label_25)
        self.ac_connected = QtGui.QLabel(self.centralwidget)
        self.ac_connected.setFrameShape(QtGui.QFrame.Box)
        self.ac_connected.setAlignment(QtCore.Qt.AlignCenter)
        self.ac_connected.setObjectName(_fromUtf8("ac_connected"))
        self.horizontalLayout_2.addWidget(self.ac_connected)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_13)
        self.state = QtGui.QLabel(self.centralwidget)
        self.state.setFrameShape(QtGui.QFrame.Box)
        self.state.setAlignment(QtCore.Qt.AlignCenter)
        self.state.setObjectName(_fromUtf8("state"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.state)
        self.cycle_count = QtGui.QLabel(self.centralwidget)
        self.cycle_count.setFrameShape(QtGui.QFrame.Box)
        self.cycle_count.setAlignment(QtCore.Qt.AlignCenter)
        self.cycle_count.setObjectName(_fromUtf8("cycle_count"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cycle_count)
        self.current_now = QtGui.QLabel(self.centralwidget)
        self.current_now.setFrameShape(QtGui.QFrame.Box)
        self.current_now.setAlignment(QtCore.Qt.AlignCenter)
        self.current_now.setObjectName(_fromUtf8("current_now"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.current_now)
        self.current_avg = QtGui.QLabel(self.centralwidget)
        self.current_avg.setFrameShape(QtGui.QFrame.Box)
        self.current_avg.setAlignment(QtCore.Qt.AlignCenter)
        self.current_avg.setObjectName(_fromUtf8("current_avg"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.current_avg)
        self.power_now = QtGui.QLabel(self.centralwidget)
        self.power_now.setFrameShape(QtGui.QFrame.Box)
        self.power_now.setAlignment(QtCore.Qt.AlignCenter)
        self.power_now.setObjectName(_fromUtf8("power_now"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.power_now)
        self.power_avg = QtGui.QLabel(self.centralwidget)
        self.power_avg.setFrameShape(QtGui.QFrame.Box)
        self.power_avg.setAlignment(QtCore.Qt.AlignCenter)
        self.power_avg.setObjectName(_fromUtf8("power_avg"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.power_avg)
        self.last_full_capacity = QtGui.QLabel(self.centralwidget)
        self.last_full_capacity.setFrameShape(QtGui.QFrame.Box)
        self.last_full_capacity.setAlignment(QtCore.Qt.AlignCenter)
        self.last_full_capacity.setObjectName(_fromUtf8("last_full_capacity"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.last_full_capacity)
        self.remaining_percent = QtGui.QLabel(self.centralwidget)
        self.remaining_percent.setFrameShape(QtGui.QFrame.Box)
        self.remaining_percent.setAlignment(QtCore.Qt.AlignCenter)
        self.remaining_percent.setObjectName(_fromUtf8("remaining_percent"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.remaining_percent)
        self.remaining_running_time = QtGui.QLabel(self.centralwidget)
        self.remaining_running_time.setFrameShape(QtGui.QFrame.Box)
        self.remaining_running_time.setAlignment(QtCore.Qt.AlignCenter)
        self.remaining_running_time.setObjectName(_fromUtf8("remaining_running_time"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.remaining_running_time)
        self.remaining_charge_time = QtGui.QLabel(self.centralwidget)
        self.remaining_charge_time.setFrameShape(QtGui.QFrame.Box)
        self.remaining_charge_time.setAlignment(QtCore.Qt.AlignCenter)
        self.remaining_charge_time.setObjectName(_fromUtf8("remaining_charge_time"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.remaining_charge_time)
        self.remaining_capacity = QtGui.QLabel(self.centralwidget)
        self.remaining_capacity.setFrameShape(QtGui.QFrame.Box)
        self.remaining_capacity.setAlignment(QtCore.Qt.AlignCenter)
        self.remaining_capacity.setObjectName(_fromUtf8("remaining_capacity"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.remaining_capacity)
        self.horizontalLayout_4.addLayout(self.formLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_24 = QtGui.QLabel(self.centralwidget)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_24)
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_14)
        self.label_22 = QtGui.QLabel(self.centralwidget)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_22)
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_20)
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_17)
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_16)
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_18)
        self.label_23 = QtGui.QLabel(self.centralwidget)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_23)
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_21)
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_19)
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_15)
        self.design_capacity = QtGui.QLabel(self.centralwidget)
        self.design_capacity.setFrameShape(QtGui.QFrame.Box)
        self.design_capacity.setAlignment(QtCore.Qt.AlignCenter)
        self.design_capacity.setObjectName(_fromUtf8("design_capacity"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.FieldRole, self.design_capacity)
        self.manufacturing_date = QtGui.QLabel(self.centralwidget)
        self.manufacturing_date.setFrameShape(QtGui.QFrame.Box)
        self.manufacturing_date.setAlignment(QtCore.Qt.AlignCenter)
        self.manufacturing_date.setObjectName(_fromUtf8("manufacturing_date"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.manufacturing_date)
        self.chemistry = QtGui.QLabel(self.centralwidget)
        self.chemistry.setFrameShape(QtGui.QFrame.Box)
        self.chemistry.setAlignment(QtCore.Qt.AlignCenter)
        self.chemistry.setObjectName(_fromUtf8("chemistry"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.chemistry)
        self.manufacturer = QtGui.QLabel(self.centralwidget)
        self.manufacturer.setFrameShape(QtGui.QFrame.Box)
        self.manufacturer.setAlignment(QtCore.Qt.AlignCenter)
        self.manufacturer.setObjectName(_fromUtf8("manufacturer"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.manufacturer)
        self.design_voltage = QtGui.QLabel(self.centralwidget)
        self.design_voltage.setFrameShape(QtGui.QFrame.Box)
        self.design_voltage.setAlignment(QtCore.Qt.AlignCenter)
        self.design_voltage.setObjectName(_fromUtf8("design_voltage"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.design_voltage)
        self.model = QtGui.QLabel(self.centralwidget)
        self.model.setFrameShape(QtGui.QFrame.Box)
        self.model.setAlignment(QtCore.Qt.AlignCenter)
        self.model.setObjectName(_fromUtf8("model"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.model)
        self.first_use_date = QtGui.QLabel(self.centralwidget)
        self.first_use_date.setFrameShape(QtGui.QFrame.Box)
        self.first_use_date.setAlignment(QtCore.Qt.AlignCenter)
        self.first_use_date.setObjectName(_fromUtf8("first_use_date"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.first_use_date)
        self.serial = QtGui.QLabel(self.centralwidget)
        self.serial.setFrameShape(QtGui.QFrame.Box)
        self.serial.setAlignment(QtCore.Qt.AlignCenter)
        self.serial.setObjectName(_fromUtf8("serial"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.serial)
        self.barcoding = QtGui.QLabel(self.centralwidget)
        self.barcoding.setFrameShape(QtGui.QFrame.Box)
        self.barcoding.setAlignment(QtCore.Qt.AlignCenter)
        self.barcoding.setObjectName(_fromUtf8("barcoding"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.barcoding)
        self.voltage = QtGui.QLabel(self.centralwidget)
        self.voltage.setFrameShape(QtGui.QFrame.Box)
        self.voltage.setAlignment(QtCore.Qt.AlignCenter)
        self.voltage.setObjectName(_fromUtf8("voltage"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.voltage)
        self.temperature = QtGui.QLabel(self.centralwidget)
        self.temperature.setFrameShape(QtGui.QFrame.Box)
        self.temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature.setObjectName(_fromUtf8("temperature"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.temperature)
        self.horizontalLayout_4.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_49 = QtGui.QLabel(self.groupBox)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.horizontalLayout_6.addWidget(self.label_49)
        self.start_charge_slider = QtGui.QSlider(self.groupBox)
        self.start_charge_slider.setSliderPosition(1)
        self.start_charge_slider.setOrientation(QtCore.Qt.Horizontal)
        self.start_charge_slider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.start_charge_slider.setTickInterval(25)
        self.start_charge_slider.setObjectName(_fromUtf8("start_charge_slider"))
        self.horizontalLayout_6.addWidget(self.start_charge_slider)
        self.start_charge_spinbox = QtGui.QSpinBox(self.groupBox)
        self.start_charge_spinbox.setMinimum(1)
        self.start_charge_spinbox.setObjectName(_fromUtf8("start_charge_spinbox"))
        self.horizontalLayout_6.addWidget(self.start_charge_spinbox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_50 = QtGui.QLabel(self.groupBox)
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.horizontalLayout_5.addWidget(self.label_50)
        self.stop_charge_slider = QtGui.QSlider(self.groupBox)
        self.stop_charge_slider.setMinimum(1)
        self.stop_charge_slider.setMaximum(100)
        self.stop_charge_slider.setOrientation(QtCore.Qt.Horizontal)
        self.stop_charge_slider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.stop_charge_slider.setTickInterval(25)
        self.stop_charge_slider.setObjectName(_fromUtf8("stop_charge_slider"))
        self.horizontalLayout_5.addWidget(self.stop_charge_slider)
        self.stop_charge_spinbox = QtGui.QSpinBox(self.groupBox)
        self.stop_charge_spinbox.setMinimum(1)
        self.stop_charge_spinbox.setMaximum(100)
        self.stop_charge_spinbox.setObjectName(_fromUtf8("stop_charge_spinbox"))
        self.horizontalLayout_5.addWidget(self.stop_charge_spinbox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.btn_reload = QtGui.QPushButton(self.centralwidget)
        self.btn_reload.setObjectName(_fromUtf8("btn_reload"))
        self.horizontalLayout_7.addWidget(self.btn_reload)
        self.btn_write = QtGui.QPushButton(self.centralwidget)
        self.btn_write.setObjectName(_fromUtf8("btn_write"))
        self.horizontalLayout_7.addWidget(self.btn_write)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.start_charge_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.start_charge_spinbox.setValue)
        QtCore.QObject.connect(self.stop_charge_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.stop_charge_spinbox.setValue)
        QtCore.QObject.connect(self.start_charge_spinbox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.start_charge_slider.setValue)
        QtCore.QObject.connect(self.stop_charge_spinbox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.stop_charge_slider.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Battery:", None))
        self.batteryComboBox.setItemText(0, _translate("MainWindow", "BAT0", None))
        self.batteryComboBox.setItemText(1, _translate("MainWindow", "BAT1", None))
        self.label_2.setText(_translate("MainWindow", "Battery Installed:", None))
        self.installed.setText(_translate("MainWindow", "N/A", None))
        self.label_25.setText(_translate("MainWindow", "AC Connected:", None))
        self.ac_connected.setText(_translate("MainWindow", "N/A", None))
        self.label_3.setText(_translate("MainWindow", "State:", None))
        self.label_4.setText(_translate("MainWindow", "Cycle Count:", None))
        self.label_5.setText(_translate("MainWindow", "Current Now:", None))
        self.label_6.setText(_translate("MainWindow", "Current Avg.:", None))
        self.label_7.setText(_translate("MainWindow", "Power Now:", None))
        self.label_8.setText(_translate("MainWindow", "Power Avg.:", None))
        self.label_9.setText(_translate("MainWindow", "Last Full Capacity:", None))
        self.label_10.setText(_translate("MainWindow", "Remaining Percent:", None))
        self.label_11.setText(_translate("MainWindow", "Rem. Running Time:", None))
        self.label_12.setText(_translate("MainWindow", "Rem. Charge Time:", None))
        self.label_13.setText(_translate("MainWindow", "Remaining Capacity:", None))
        self.state.setText(_translate("MainWindow", "N/A", None))
        self.cycle_count.setText(_translate("MainWindow", "N/A", None))
        self.current_now.setText(_translate("MainWindow", "N/A", None))
        self.current_avg.setText(_translate("MainWindow", "N/A", None))
        self.power_now.setText(_translate("MainWindow", "N/A", None))
        self.power_avg.setText(_translate("MainWindow", "N/A", None))
        self.last_full_capacity.setText(_translate("MainWindow", "N/A", None))
        self.remaining_percent.setText(_translate("MainWindow", "N/A", None))
        self.remaining_running_time.setText(_translate("MainWindow", "N/A", None))
        self.remaining_charge_time.setText(_translate("MainWindow", "N/A", None))
        self.remaining_capacity.setText(_translate("MainWindow", "N/A", None))
        self.label_24.setText(_translate("MainWindow", "Temperature:", None))
        self.label_14.setText(_translate("MainWindow", "Design Capacity:", None))
        self.label_22.setText(_translate("MainWindow", "Manufacturing Date:", None))
        self.label_20.setText(_translate("MainWindow", "Chemistry:", None))
        self.label_17.setText(_translate("MainWindow", "Manufacturer:", None))
        self.label_16.setText(_translate("MainWindow", "Design Voltage:", None))
        self.label_18.setText(_translate("MainWindow", "Model:", None))
        self.label_23.setText(_translate("MainWindow", "First Use Date:", None))
        self.label_21.setText(_translate("MainWindow", "Serial:", None))
        self.label_19.setText(_translate("MainWindow", "Barcoding:", None))
        self.label_15.setText(_translate("MainWindow", "Voltage:", None))
        self.design_capacity.setText(_translate("MainWindow", "N/A", None))
        self.manufacturing_date.setText(_translate("MainWindow", "N/A", None))
        self.chemistry.setText(_translate("MainWindow", "N/A", None))
        self.manufacturer.setText(_translate("MainWindow", "N/A", None))
        self.design_voltage.setText(_translate("MainWindow", "N/A", None))
        self.model.setText(_translate("MainWindow", "N/A", None))
        self.first_use_date.setText(_translate("MainWindow", "N/A", None))
        self.serial.setText(_translate("MainWindow", "N/A", None))
        self.barcoding.setText(_translate("MainWindow", "N/A", None))
        self.voltage.setText(_translate("MainWindow", "N/A", None))
        self.temperature.setText(_translate("MainWindow", "N/A", None))
        self.groupBox.setTitle(_translate("MainWindow", "Charging Thresholds", None))
        self.label_49.setText(_translate("MainWindow", "Start Charge Thresh:", None))
        self.label_50.setText(_translate("MainWindow", "Stop Charge Thresh:", None))
        self.btn_reload.setText(_translate("MainWindow", "Reload Settings", None))
        self.btn_write.setText(_translate("MainWindow", "Write Settings", None))

