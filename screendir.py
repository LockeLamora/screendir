import sys, historyoperations, os
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QFileDialog 

form_class = uic.loadUiType("window.ui")[0]                
 
class MyWindowClass(QtGui.QMainWindow, form_class):
    location=''

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.populate_history_combobox(self)
        self.browseButton.clicked.connect(self.browse_for_location)
        self.setButton.clicked.connect(self.set_location)
        self.historyComboBox.currentIndexChanged.connect(self.process_history_combobox)
        self.clearHistoryButton.clicked.connect(self.clear_history)
        self.manualLocationText.editingFinished.connect(self.process_manual_path)

    def process_manual_path(self):
        directory = self.manualLocationText.text()
        self.set_current_directory(self, directory)

    def populate_history_combobox(self, parent):
        self.historyComboBox.clear()
        historyitems = historyoperations.get_history_entries()

        self.historyComboBox.addItem('Choose previous location...')
        for historyitem in historyitems:
            if historyitem.rstrip():
                self.historyComboBox.addItem(historyitem)

    def set_error(self, text):
        self.errorTextLabel.setText(text)

    def process_history_combobox(self, parent):
        if self.historyComboBox.currentText() == 'Choose previous location...':
            self.set_error('')
            return
        
        selection = self.historyComboBox.currentText()
        self.set_current_directory(self, selection)

    def browse_for_location(self, parent):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))   
        self.set_current_directory(self, directory)

    def set_current_directory(self, parent, directory):
        if os.path.isdir(directory) == False:
            self.set_error('WARNING: Path does not exist')
        if os.access(directory, os.W_OK) == False:
            self.set_error('WARNING: Chosen directory is read-only')
        else:
            self.set_error('')
        self.location = str(directory)
        self.manualLocationText.setText(directory)

    def set_location(self, parent):
        if self.location == '':
            self.set_error('WARNING: no directory entered')
            return
        historyoperations.add_to_history_file(self.location)
        os.system('defaults write com.apple.screencapture location ' + self.location)
        os.system('killall SystemUIServer')
        self.populate_history_combobox(self)
        
    def clear_history(self, parent):
        historyoperations.clear_history()
        self.populate_history_combobox(self)


app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()