import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as QtGui

class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Recipe Manager")
        self.showMaximized()

app = qtw.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()