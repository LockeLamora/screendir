# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName(_fromUtf8("mainDialog"))
        mainDialog.resize(617, 243)
        self.buttonBox = QtGui.QDialogButtonBox(mainDialog)
        self.buttonBox.setGeometry(QtCore.QRect(310, 200, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.ErrorText = QtGui.QLabel(mainDialog)
        self.ErrorText.setGeometry(QtCore.QRect(10, 150, 301, 21))
        self.ErrorText.setObjectName(_fromUtf8("ErrorText"))
        self.historydropdown = QtGui.QComboBox(mainDialog)
        self.historydropdown.setGeometry(QtCore.QRect(10, 50, 551, 31))
        self.historydropdown.setObjectName(_fromUtf8("historydropdown"))
        self.currentLocation = QtGui.QLabel(mainDialog)
        self.currentLocation.setGeometry(QtCore.QRect(10, 100, 551, 41))
        self.currentLocation.setObjectName(_fromUtf8("currentLocation"))
        self.manualPathTextbox = QtGui.QPlainTextEdit(mainDialog)
        self.manualPathTextbox.setGeometry(QtCore.QRect(10, 10, 551, 31))
        self.manualPathTextbox.setObjectName(_fromUtf8("manualPathTextbox"))
        self.browseButton = QtGui.QPushButton(mainDialog)
        self.browseButton.setGeometry(QtCore.QRect(570, 10, 31, 31))
        self.browseButton.setObjectName(_fromUtf8("browseButton"))

        self.retranslateUi(mainDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mainDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mainDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(_translate("mainDialog", "Screenshot Location Selector", None))
        self.ErrorText.setText(_translate("mainDialog", "error text", None))
        self.currentLocation.setText(_translate("mainDialog", "current location", None))
        self.browseButton.setText(_translate("mainDialog", "...", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainDialog = QtGui.QDialog()
    ui = Ui_mainDialog()
    ui.setupUi(mainDialog)
    mainDialog.show()
    sys.exit(app.exec_())

