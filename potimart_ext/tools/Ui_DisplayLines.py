# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_DisplayLines.ui'
#
# Created: Mon Oct 11 09:34:06 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DisplayLines(object):
    def setupUi(self, DisplayLines):
        DisplayLines.setObjectName("DisplayLines")
        DisplayLines.resize(589, 353)
        self.buttons = QtGui.QDialogButtonBox(DisplayLines)
        self.buttons.setGeometry(QtCore.QRect(410, 270, 171, 32))
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttons.setObjectName("buttons")
        self.groupBoxSelection = QtGui.QGroupBox(DisplayLines)
        self.groupBoxSelection.setGeometry(QtCore.QRect(10, 70, 571, 181))
        self.groupBoxSelection.setObjectName("groupBoxSelection")
        self.LinesComboBox = QtGui.QComboBox(self.groupBoxSelection)
        self.LinesComboBox.setEnabled(True)
        self.LinesComboBox.setGeometry(QtCore.QRect(20, 50, 531, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LinesComboBox.sizePolicy().hasHeightForWidth())
        self.LinesComboBox.setSizePolicy(sizePolicy)
        self.LinesComboBox.setEditable(False)
        self.LinesComboBox.setMaxVisibleItems(10)
        self.LinesComboBox.setMaxCount(100)
        self.LinesComboBox.setObjectName("LinesComboBox")
        self.label_3 = QtGui.QLabel(self.groupBoxSelection)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 511, 31))
        self.label_3.setMinimumSize(QtCore.QSize(411, 31))
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtGui.QWidget(self.groupBoxSelection)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 80, 271, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fwRadioButton = QtGui.QRadioButton(self.layoutWidget)
        self.fwRadioButton.setObjectName("fwRadioButton")
        self.horizontalLayout.addWidget(self.fwRadioButton)
        self.bwRadioButton = QtGui.QRadioButton(self.layoutWidget)
        self.bwRadioButton.setObjectName("bwRadioButton")
        self.horizontalLayout.addWidget(self.bwRadioButton)
        self.bothRadioButton = QtGui.QRadioButton(self.layoutWidget)
        self.bothRadioButton.setChecked(True)
        self.bothRadioButton.setObjectName("bothRadioButton")
        self.horizontalLayout.addWidget(self.bothRadioButton)
        self.label = QtGui.QLabel(self.groupBoxSelection)
        self.label.setGeometry(QtCore.QRect(20, 91, 111, 16))
        self.label.setObjectName("label")
        self.MissionsComboBox = QtGui.QComboBox(self.groupBoxSelection)
        self.MissionsComboBox.setEnabled(False)
        self.MissionsComboBox.setGeometry(QtCore.QRect(20, 142, 531, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MissionsComboBox.sizePolicy().hasHeightForWidth())
        self.MissionsComboBox.setSizePolicy(sizePolicy)
        self.MissionsComboBox.setEditable(False)
        self.MissionsComboBox.setMaxVisibleItems(10)
        self.MissionsComboBox.setMaxCount(100)
        self.MissionsComboBox.setObjectName("MissionsComboBox")
        self.displayMissonCheckBox = QtGui.QCheckBox(self.groupBoxSelection)
        self.displayMissonCheckBox.setGeometry(QtCore.QRect(20, 120, 521, 18))
        self.displayMissonCheckBox.setObjectName("displayMissonCheckBox")
        self.groupBoxAfficherTout = QtGui.QGroupBox(DisplayLines)
        self.groupBoxAfficherTout.setGeometry(QtCore.QRect(10, 10, 571, 51))
        self.groupBoxAfficherTout.setObjectName("groupBoxAfficherTout")
        self.displayAllCheckBox = QtGui.QCheckBox(self.groupBoxAfficherTout)
        self.displayAllCheckBox.setEnabled(True)
        self.displayAllCheckBox.setGeometry(QtCore.QRect(20, 20, 499, 20))
        self.displayAllCheckBox.setMinimumSize(QtCore.QSize(0, 0))
        self.displayAllCheckBox.setMaximumSize(QtCore.QSize(499, 16777215))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.displayAllCheckBox.setFont(font)
        self.displayAllCheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.displayAllCheckBox.setObjectName("displayAllCheckBox")

        self.retranslateUi(DisplayLines)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL("accepted()"), DisplayLines.accept)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL("rejected()"), DisplayLines.reject)
        QtCore.QObject.connect(self.displayAllCheckBox, QtCore.SIGNAL("toggled(bool)"), self.groupBoxSelection.setDisabled)
        QtCore.QObject.connect(self.displayMissonCheckBox, QtCore.SIGNAL("toggled(bool)"), self.bwRadioButton.setDisabled)
        QtCore.QObject.connect(self.displayMissonCheckBox, QtCore.SIGNAL("toggled(bool)"), self.fwRadioButton.setDisabled)
        QtCore.QObject.connect(self.displayMissonCheckBox, QtCore.SIGNAL("toggled(bool)"), self.bothRadioButton.setDisabled)
        QtCore.QObject.connect(self.displayMissonCheckBox, QtCore.SIGNAL("toggled(bool)"), self.MissionsComboBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(DisplayLines)

    def retranslateUi(self, DisplayLines):
        DisplayLines.setWindowTitle(QtGui.QApplication.translate("DisplayLines", "Potimart - Afficher les lignes", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxSelection.setTitle(QtGui.QApplication.translate("DisplayLines", "Sélection", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DisplayLines", "Sélectionner une ligne du réseau de transport :", None, QtGui.QApplication.UnicodeUTF8))
        self.fwRadioButton.setText(QtGui.QApplication.translate("DisplayLines", "Aller", None, QtGui.QApplication.UnicodeUTF8))
        self.bwRadioButton.setText(QtGui.QApplication.translate("DisplayLines", "Retour", None, QtGui.QApplication.UnicodeUTF8))
        self.bothRadioButton.setText(QtGui.QApplication.translate("DisplayLines", "Les deux", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DisplayLines", "Sens de la ligne : ", None, QtGui.QApplication.UnicodeUTF8))
        self.displayMissonCheckBox.setText(QtGui.QApplication.translate("DisplayLines", "Afficher une mission de la ligne :", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxAfficherTout.setTitle(QtGui.QApplication.translate("DisplayLines", "Afficher tout", None, QtGui.QApplication.UnicodeUTF8))
        self.displayAllCheckBox.setText(QtGui.QApplication.translate("DisplayLines", "  Toutes les lignes et tous les arrêts, dans les deux sens", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DisplayLines = QtGui.QDialog()
    ui = Ui_DisplayLines()
    ui.setupUi(DisplayLines)
    DisplayLines.show()
    sys.exit(app.exec_())

