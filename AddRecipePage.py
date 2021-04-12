import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
import PostgreSQL

class AddRecipeWidget(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        super(AddRecipeWidget, self).__init__(*args, **kwargs)
        
        self.createWidgets()
        self.configureLayout()
        
    def createWidgets(self):
        
        self.background_label = qtw.QLabel()
        self.background_label.setStyleSheet("""QWidget {background-color: rgba(254,174,0,20)}""")

        self.main_title = qtw.QLineEdit()
        self.main_title.setPlaceholderText("Recipe title")
        self.main_title.setMinimumHeight(70)
        self.main_title.setStyleSheet("""QWidget {font: 30pt 'Avenir'; 
                                      font-weight: bold;
                                      padding: 10px 10px 10px 10px;}""")
        
        self.info_widget = InfoWidget()

        self.ingredients_title = qtw.QLabel()
        self.ingredients_title.setText("Ingredients")
        self.ingredients_title.setStyleSheet("""QWidget {font: 25pt 'Avenir'; 
                                        font-weight: bold}""")

        self.ingredients_widget = IngredientWidget()

        self.instructions_title = qtw.QLabel()
        self.instructions_title.setText("Instructions")
        self.instructions_title.setStyleSheet("""QWidget {font: 25pt 'Avenir'; 
                                         font-weight: bold}""")

        self.instructions_edit = qtw.QTextEdit()
        self.instructions_edit.setPlaceholderText("Instructions")
        self.instructions_edit.setMinimumHeight(300)
        self.instructions_edit.setStyleSheet("""QWidget {font: 16pt 'Avenir'; 
                                             padding 5px 5px 5px 5px}""")

        self.picture = qtw.QLabel()
        image = "icons/photo_black.tiff"
        icon = qtg.QIcon()
        icon.addFile(image)
        pixmap = icon.pixmap(qtc.QSize(100,70))
        self.picture.setPixmap(pixmap)
        self.picture.setAlignment(qtc.Qt.AlignCenter)

        self.save_widget = SaveWidget()
        save_button = self.save_widget.save_button
        save_button.clicked.connect(self.click_save)

    def configureLayout(self):
        
        top_layout = qtw.QGridLayout()
        top_layout.addWidget(self.main_title, 0, 0, 1, 1)
        top_layout.addWidget(self.info_widget, 1, 0, 1, 1)

        bottom_layout = qtw.QGridLayout()
        bottom_layout.addWidget(self.ingredients_title, 0, 0, 1, 1)
        bottom_layout.addWidget(self.ingredients_widget, 1, 0, 1, 1)
        bottom_layout.addWidget(self.picture, 1, 1, 1, 1)
        bottom_layout.addWidget(self.instructions_title, 2, 0, 1, 1)
        bottom_layout.addWidget(self.instructions_edit, 3, 0, 1, 2)
        bottom_layout.setColumnStretch(1,2)

        right_layout = qtw.QGridLayout()
        right_layout.setContentsMargins(0,0,0,0)
        right_layout.addWidget(self.save_widget, 0, 0, 1, 1)

        layout = qtw.QGridLayout()
        layout.addLayout(top_layout, 0, 0, 1, 1)
        layout.addLayout(bottom_layout, 1, 0, 1, 1)
        layout.addLayout(right_layout, 0, 1, 1, 1)

        top_layout.setContentsMargins(60,30,20,0)
        top_layout.setVerticalSpacing(30)

        bottom_layout.setContentsMargins(60,30,20,40)
        bottom_layout.setVerticalSpacing(30)

        layout.setContentsMargins(0,0,0,0)

        self.setLayout(layout)

    def error_check(self):
        # Check if correct information has been added to text edits

        def check_num(string):
            char_true = False
            if check_len(string):
                for char in string:
                    if char.isdigit():
                        char_true = True
                    else:
                        char_true = False
                        break
            return(char_true)

        def check_len(string):
            if len(string) > 0:
                return(True)
            else:
                return(False)

        true_list = []

        true_list.append(check_len(self.main_title.text()))

        true_list.append(check_num(self.info_widget.feeds_info.text()))
        true_list.append(check_num(self.info_widget.calories_info.text()))
        true_list.append(check_num(self.info_widget.prep_info.text()))
        true_list.append(check_num(self.info_widget.cook_info.text()))

        ingred_true = []
        for n, ingredient_edit in enumerate(self.ingredients_widget.ingredient_edit_list):
            ingredient = ingredient_edit.text()
            amount = self.ingredients_widget.amount_edit_list[n].text()
            prep = self.ingredients_widget.prep_edit_list[n].text()
            if check_len(ingredient) or check_len(amount) or check_len(prep) == False:
                ingred_true.append(False)
            else:
                ingred_true.append(True)
        if False in ingred_true:
            true_list.append(False)
        else:
            true_list.append(True)

        true_list.append(check_len(self.instructions_edit.toPlainText()))

        print(true_list)
        if true_list == [True] * 7:
            return(True)
        else:
            return(False)

    def click_save(self):
        # TODO Upload recipe information to database
        
        print("hello")
        if self.error_check() == True:
            print("worked")

            title = self.main_title.text()

            feeds_info = self.info_widget.feeds_info.text()
            calories_info = self.info_widget.calories_info.text()
            prep_info = self.info_widget.prep_info.text()
            cook_info = self.info_widget.cook_info.text()

            ingredient_list = []
            amount_list = []
            prep_list = []
            for n, ingredient_edit in enumerate(self.ingredients_widget.ingredient_edit_list):
                ingredient_list.append(ingredient_edit.text())
                amount = self.ingredients_widget.amount_edit_list[n]
                amount_list.append(amount.text())
                prep = self.ingredients_widget.prep_edit_list[n]
                prep_list.append(prep.text())
                

            instructions = self.instructions_edit.toPlainText()

            print("Passed")
        
        else:
            print("Failed")


class SaveWidget(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        super(SaveWidget, self).__init__(*args, **kwargs)

        self.createWidgets()
        self.configureLayout()

    def createWidgets(self):
        
        self.background_label = qtw.QLabel()
        self.background_label.setStyleSheet("""QWidget {background-color: rgba(254,174,0,50)}""")
        self.background_label.setMinimumWidth(100)

        self.save_picture = qtw.QLabel()
        self.save_picture.setContentsMargins(0,20,0,0)
        self.save_text = qtw.QLabel()
        
        self.discard_picture = qtw.QLabel()
        self.discard_text = qtw.QLabel()

        pic_list = [self.save_picture, self.discard_picture]
        image_list = ["icons/save_green.tiff",
                       "icons/delete_red.tiff"]
        text_list = [self.save_text, self.discard_text]
        text_string_list = ["Save", "Delete"]

        for i, image in enumerate(image_list):
            icon = qtg.QIcon()
            icon.addFile(image)
            pixmap = icon.pixmap(qtc.QSize(60,40))
            pic_list[i].setPixmap(pixmap)
            pic_list[i].setAlignment(qtc.Qt.AlignCenter)
            text_list[i].setText(text_string_list[i])
            text_list[i].setAlignment(qtc.Qt.AlignCenter | qtc.Qt.AlignTop)
            text_list[i].setStyleSheet("""QWidget {font: 12pt 'Avenir'; font-weight: bold}""")
            text_list[i].setContentsMargins(0,0,0,20)

        self.save_button = qtw.QPushButton()
        self.discard_button = qtw.QPushButton()
        self.button_list = [self.save_button, self.discard_button]
        for button in self.button_list:
            button.setStyleSheet("""QWidget {background-color: rgba(254,255,255,0); margin: 15px}""")
            button.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))

    def configureLayout(self):
        
        layout = qtw.QGridLayout()
        layout.addWidget(self.background_label, 0, 0, 5, 1)
        layout.addWidget(self.save_picture, 1, 0, 1, 1)
        layout.addWidget(self.save_button, 1, 0, 1, 1)
        layout.addWidget(self.save_text, 2, 0, 1, 1)
        layout.addWidget(self.discard_picture, 3, 0, 1, 1)
        layout.addWidget(self.discard_button, 3, 0, 1, 1)
        layout.addWidget(self.discard_text, 4, 0, 1, 1)

        layout.setAlignment(qtc.Qt.AlignCenter | qtc.Qt.AlignTop)

        layout.setContentsMargins(0,0,20,0)
        layout.setSpacing(10)

        self.setLayout(layout)


class IngredientWidget(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        super(IngredientWidget, self).__init__(*args, **kwargs)

        self.createWidgets()
        self.configureLayout()

    def createWidgets(self):
        
        self.ingredient_edit_list = []
        self.amount_edit_list = []
        self.prep_edit_list = []

        self.add_button = qtw.QPushButton()
        self.add_button.setFixedSize(30,30)
        self.add_button.setStyleSheet("""QWidget {background-color: rgba(254,255,255,0);}""")
        self.add_button.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.add_button.clicked.connect(self.addIngredient)

        icon = qtg.QIcon()
        icon.addFile("icons/add_black.tiff")
        pixmap = icon.pixmap(qtc.QSize(20,20))
        self.add_label = qtw.QLabel()
        self.add_label.setPixmap(pixmap)

    def configureLayout(self):
        
        self.total_layout = qtw.QGridLayout()
        self.ingredient_layout = qtw.QGridLayout()
        self.add_layout = qtw.QGridLayout()
        self.add_layout.addWidget(self.add_label, 0, 1, 1, 1)
        self.add_layout.addWidget(self.add_button, 0, 1, 1, 1)
        self.total_layout.addLayout(self.ingredient_layout, 0, 0, 1, 1)
        self.total_layout.addLayout(self.add_layout, 1, 0, 1, 1)

        self.addIngredient()

        self.add_layout.setAlignment(qtc.Qt.AlignTop | qtc.Qt.AlignLeft)
        self.total_layout.setContentsMargins(0,0,0,0)
        self.total_layout.setVerticalSpacing(10)
        self.setLayout(self.total_layout)

    def addIngredient(self):
        # Add new ingredient, amonut and prep text edits to page

        ingredient_edit = qtw.QLineEdit()
        ingredient_edit.setPlaceholderText("Ingredient")
        ingredient_edit.setMinimumWidth(200)
        
        amount_edit = qtw.QLineEdit()
        amount_edit.setPlaceholderText("Amount")
        amount_edit.setMinimumWidth(150)
        
        prep_edit = qtw.QLineEdit()
        prep_edit.setPlaceholderText("Preparation")
        prep_edit.setMinimumWidth(200)
        
        edit_list = [ingredient_edit, amount_edit, prep_edit]
        for edit in edit_list:
            edit.setStyleSheet("""QWidget {font: 16pt 'Avenir'; padding: 3px 3px 3px 3px;}""")
            edit.setContentsMargins(0,0,0,0) 
            
        self.ingredient_edit_list.append(ingredient_edit)
        self.amount_edit_list.append(amount_edit)
        self.prep_edit_list.append(prep_edit)

        row = len(self.ingredient_edit_list) - 1
        self.ingredient_layout.addWidget(ingredient_edit, row, 0, 1, 1)
        self.ingredient_layout.addWidget(amount_edit, row, 1, 1, 1)
        self.ingredient_layout.addWidget(prep_edit, row, 2, 1, 1)


class InfoWidget(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        super(InfoWidget, self).__init__(*args, **kwargs)
        
        self.createWidgets()
        self.configureLayout()
        
    def createWidgets(self):

        self.feeds_title = qtw.QLabel()
        self.feeds_title.setText("Feeds:")
        self.calories_title = qtw.QLabel()
        self.calories_title.setText("Calories:")
        self.prep_title = qtw.QLabel()
        self.prep_title.setText("Prep time:")
        self.cook_title = qtw.QLabel()
        self.cook_title.setText("Cook time:")

        self.feeds_info = qtw.QLineEdit()
        self.prep_info = qtw.QLineEdit()
        self.calories_info = qtw.QLineEdit()
        self.cook_info = qtw.QLineEdit()

        self.info_title = [self.feeds_title, self.calories_title, self.prep_title, self.cook_title]
        self.info_body = [self.feeds_info, self.calories_info, self.prep_info, self.cook_info]

        for info in self.info_title:
            info.setStyleSheet("""QWidget {font: 16pt 'Avenir'; font-weight: bold}""")

        for info in self.info_body:
            info.setStyleSheet("""QWidget {font: 16pt 'Avenir'; padding: 2px 2px 2px 2px}""")
            
    def configureLayout(self):

        layout = qtw.QGridLayout()
        layout.addWidget(self.feeds_title, 0, 0, 1, 1)
        layout.addWidget(self.feeds_info, 0, 1, 1, 1)
        layout.addWidget(self.calories_title, 0, 3, 1, 1)
        layout.addWidget(self.calories_info, 0, 4, 1, 1)
        layout.addWidget(self.prep_title, 0, 6, 1, 1)
        layout.addWidget(self.prep_info, 0, 7, 1, 1)
        layout.addWidget(self.cook_title, 0, 9, 1, 1)
        layout.addWidget(self.cook_info, 0, 10, 1, 1)
        
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        
        cols = [1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2]
        for n in range(10):
            layout.setColumnStretch(n, cols[n])