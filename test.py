import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QFileDialog 

form_class = uic.loadUiType("window.ui")[0]                
 
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.browseButton.clicked.connect(self.browse_for_location)
    
    def browse_for_location(self, parent):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))   
        self.currentLocationLabel.setText(directory)
        
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()