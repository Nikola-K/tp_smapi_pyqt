#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2015 Nikola Kovacevic
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from PyQt4 import QtGui
import sys

import design


class TPSmapiGUI(QtGui.QMainWindow, design.Ui_MainWindow):
    # noinspection PyUnresolvedReferences
    def __init__(self, parent=None):
        super(TPSmapiGUI, self).__init__(parent)
        self.setupUi(self)
        self.current_battery = "BAT0"
        self.values = {
            "installed": self.installed,
            "state": self.state,
            "../ac_connected": self.ac_connected,
            "cycle_count": self.cycle_count,
            "current_now": self.current_now,  # instantaneous current
            "current_avg": self.current_avg,  # last minute average
            "power_now": self.power_now,  # instantaneous power
            "power_avg": self.power_avg,  # last minute average
            "last_full_capacity": self.last_full_capacity,
            "remaining_percent": self.remaining_percent,
            "remaining_running_time": self.remaining_running_time,
            "remaining_charging_time": self.remaining_charge_time,
            "remaining_capacity": self.remaining_capacity,
            "design_capacity": self.design_capacity,
            "voltage": self.voltage,
            "design_voltage": self.design_voltage,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "barcoding": self.barcoding,
            "chemistry": self.chemistry,
            "serial": self.serial,
            "manufacture_date": self.manufacturing_date,
            "first_use_date": self.first_use_date,
            "temperature": self.temperature  # in milli-Celsius
        }

        self.get_battery_values()
        self.get_charge_values()
        self.batteryComboBox.currentIndexChanged.connect(self.__change_battery)
        self.btn_reload.clicked.connect(self._reload_values)
        self.btn_write.clicked.connect(self._write_values)

    def _reload_values(self):
        self.get_battery_values()
        self.get_charge_values()

    def __change_battery(self):
        self.current_battery = str(self.batteryComboBox.currentText())
        self.get_battery_values()
        self.get_charge_values()


    def _get_value(self, value_key, default_return="N/a"):
        base = "/sys/devices/platform/smapi/{}/".format(self.current_battery)
        try:
            with open(base + value_key) as input_file:
                return input_file.read().rstrip()
        except:
            return default_return

    def _set_value(self, value_key, key_value):
        base = "/sys/devices/platform/smapi/{}/".format(self.current_battery)
        try:
            with open(base + value_key, "w") as output_file:
                output_file.write(key_value)
                return True
        except IOError:
            return False

    # noinspection PyTypeChecker
    def _failed_write_msg(self):
        QtGui.QMessageBox.critical(self, "Error",
                                   "Failed to write new charging setting values,"
                                   "use reload button to see current values.\n"
                                   "Do you have write permissions for '/sys/devices/platform/'?\n"
                                   "You can try running the tool as root if you aren't already.",
                                   QtGui.QMessageBox.Ok)

    def _write_values(self):
        start_threshold = int(self._get_value("start_charge_thresh", 0))
        stop_threshold = int(self._get_value("stop_charge_thresh", 0))
        inhibit_charge_min = int(self._get_value("inhibit_charge_minutes", 0))
        new_start = int(self.start_charge_slider.value())
        new_stop = int(self.stop_charge_slider.value())
        new_inhibit = int(self.inhibit_charge_slider.value())

        if new_start != start_threshold:
            if not self._set_value("start_charge_thresh", str(new_start)):
                self._failed_write_msg()
                return

        if new_stop != stop_threshold:
            if not self._set_value("stop_charge_thresh", str(new_stop)):
                self._failed_write_msg()
                return
        if new_inhibit != inhibit_charge_min:
            if not self._set_value("inhibit_charge_minutes", str(new_inhibit)):
                self._failed_write_msg()
                return

    # noinspection PyTypeChecker
    def get_charge_values(self):
        start_threshold = int(self._get_value("start_charge_thresh", 0))
        stop_threshold = int(self._get_value("stop_charge_thresh", 0))
        inhibit_charge_min = int(self._get_value("inhibit_charge_minutes", 0))
        self.start_charge_slider.setValue(start_threshold)
        self.stop_charge_slider.setValue(stop_threshold)
        self.inhibit_charge_slider.setValue(inhibit_charge_min)

    def get_battery_values(self):
        for value_key, value_label in self.values.items():
            value = self._get_value(value_key)
            if value == "0":
                value = "False"
            elif value == "1":
                value = "True"
            value_label.setText(value)


def main():
    app = QtGui.QApplication(sys.argv)
    form = TPSmapiGUI()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()