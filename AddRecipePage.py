import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg

class AddRecipeWidget(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super(AddRecipeWidget, self).__init__(*args, **kwargs)

        self.background_label = qtw.QLabel()
        self.background_label.setStyleSheet("""QWidget {background-color: rgba(254,174,0,30)}""")

        self.title_label = qtw.QLabel()
        self.title_label.setText("Add Recipe")
        self.title_label.setStyleSheet("""QWidget {font: 55pt 'Avenir'; font-weight: bold; margin: 20px}""")
        self.title_label.setAlignment(qtc.Qt.AlignLeft)

        self.mainLayout = qtw.QGridLayout()
        self.categoryLayout = qtw.QVBoxLayout()
        self.categoryLayout.setSpacing(40)
        self.mainLayout.addWidget(self.background_label, 0, 0, 3, 2)
        self.mainLayout.addWidget(self.title_label, 0, 0, 1, 1)
        self.mainLayout.setRowStretch(1, 3)
        self.mainLayout.setContentsMargins(0,0,0,0)

        self.setLayout(self.mainLayout)