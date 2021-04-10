import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
import base64
import PostgreSQL

class RecipeWidget(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super(qtw.QWidget, self).__init__(*args, **kwargs)

        self.background_label = qtw.QLabel()
        self.background_label.setStyleSheet("""QWidget {background-color: rgba(254,174,0,20)}""")
        self.main_title = qtw.QLabel()
        self.main_title.setStyleSheet("""QWidget {font: 55pt 'Avenir'; font-weight: bold}""")
        self.test_info = info_widget()

        self.ingredients_title = qtw.QLabel()
        self.ingredients_title.setText("Ingredients")
        self.ingredients_title.setStyleSheet("""QWidget {font: 25pt 'Avenir'; font-weight: bold}""")
        self.ingredients_body = qtw.QLabel()
        self.ingredients_body.setStyleSheet("""QWidget {font: 16pt 'Avenir'}""")

        self.instructions_title = qtw.QLabel()
        self.instructions_title.setText("Instructions")
        self.instructions_title.setStyleSheet("""QWidget {font: 25pt 'Avenir'; font-weight: bold}""")
        self.instructions_body = qtw.QLabel()
        self.instructions_body.setStyleSheet("""QWidget {font: 16pt 'Avenir'}""")
        self.instructions_body.setWordWrap(True)

        self.picture = qtw.QLabel()
        binary_img = open("/Users/josephsmith/Documents/recipe-manager/recipe_images/mexican-style_stuffed_sweet_potatoes.webp", 'rb').read()
        self.picture_data = binary_img
        
        middle_label1 = qtw.QLabel()

        layout = qtw.QGridLayout()
        layout.addWidget(self.main_title, 0, 1, 1, 3)
        layout.addWidget(self.test_info, 2, 1, 1, 3)
        layout.addWidget(middle_label1, 3, 1, 1, 1)
        layout.addWidget(self.ingredients_title, 4, 1, 1, 1)
        layout.addWidget(self.ingredients_body, 6, 1, 1, 1)
        layout.addWidget(self.instructions_title, 8, 1, 1, 1)
        layout.addWidget(self.instructions_body, 10, 1, 1, 3)
        layout.addWidget(self.picture, 4, 2, 5, 2)

        #rows = [2, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1]
        cols = [1, 6, 6, 6, 6]
        #for n in range(len(rows)):
        #    layout.setRowStretch(n, rows[n])
        for n in range(len(cols)):
            layout.setColumnStretch(n, cols[n])

        layout.setContentsMargins(60,30,80,0)
        self.setLayout(layout)

    def addTitle(self, title_string):
        self.main_title.setText(title_string)

    def addIngredient(self, ingredient_string):

        self.ingredients_body.setText(self.ingredients_body.text() + "- " + ingredient_string + "\n")

    def addInstruction(self, instruction_string):
        self.instructions_body.setText(self.instructions_body.text() + instruction_string + "\n" + "\n")

    def addInfo(self, input_info):
        for n, info in enumerate(input_info):
            self.test_info.info_body[n].setText(self.test_info.info_body[n].text() + info)

    def addPicture(self, picture_data):
        self.picture_data = picture_data

    def drawPicture(self):
        image = qtg.QImage()
        image.loadFromData(self.picture_data)
        pixmap = qtg.QPixmap.fromImage(image.scaled(350,350, qtc.Qt.KeepAspectRatio, qtc.Qt.SmoothTransformation))
        radius = 50
        rounded = qtg.QPixmap(pixmap.size())
        rounded.fill(qtg.QColor("transparent"))
        painter = qtg.QPainter(rounded)
        painter.setRenderHint(qtg.QPainter.Antialiasing)
        painter.setBrush(qtg.QBrush(pixmap))
        painter.setPen(qtg.QPen(qtc.Qt.black, 5))
        path = qtg.QPainterPath()
        rect = qtc.QRectF(pixmap.rect())
        path.addRoundedRect(rect, radius, radius)
        painter.setClipPath(path)
        painter.fillPath(path, painter.brush())
        painter.strokePath(path, painter.pen())
        painter.end()
        self.picture.setPixmap(rounded)
        self.picture.setAlignment(qtc.Qt.AlignCenter)

    def getRecipe(self, id_num):
        psql = PostgreSQL.PostgreSQL()
        psql.openConnection()
        title, feeds, calories, prep, cook, instructions, image = psql.extractRecipe(id_num)
        psql.closeConnection()
        recipe_info = [str(feeds), str(calories), str(prep), str(cook)]

        ingredient_list = ["4 sweet potatoes", "1 brown onion", "2 peppers", "2 red chillis",
                            "1 bunch of spring onions", "400g black beans", "3 limes", 
                            "2 large avocados", "2 garlic cloves", "2 tsp ground cumin", 
                            "2 tsp paprika", "2 tsp chilli flakes", "1 handful of coriander"]

        self.addTitle(title)
        for ingredient in ingredient_list:
            self.addIngredient(ingredient)
        self.addInstruction(instructions)
        self.addInfo(recipe_info)
        self.addPicture(image)
        self.drawPicture()
        return(self)

class info_widget(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super(qtw.QWidget, self).__init__(*args, **kwargs)

        self.feeds_title = qtw.QLabel()
        self.feeds_title.setText("Feeds:")
        self.calories_title = qtw.QLabel()
        self.calories_title.setText("Calories:")
        self.prep_title = qtw.QLabel()
        self.prep_title.setText("Prep time:")
        self.cook_title = qtw.QLabel()
        self.cook_title.setText("Cook time:")

        self.feeds_info = qtw.QLabel()
        self.calories_info = qtw.QLabel()
        self.prep_info = qtw.QLabel()
        self.cook_info = qtw.QLabel()

        self.info_title = [self.feeds_title, self.calories_title, self.prep_title, self.cook_title]
        self.info_body = [self.feeds_info, self.calories_info, self.prep_info, self.cook_info]

        for info in self.info_title:
            info.setStyleSheet("""QWidget {font: 16pt 'Avenir'; font-weight: bold}""")

        for info in self.info_body:
            info.setStyleSheet("""QWidget {font: 16pt 'Avenir'}""")

        layout = qtw.QGridLayout()
        layout.addWidget(self.feeds_title, 0, 0, 1, 1)
        layout.addWidget(self.feeds_info, 0, 1, 1, 1)
        layout.addWidget(self.calories_title, 0, 2, 1, 1)
        layout.addWidget(self.calories_info, 0, 3, 1, 1)
        layout.addWidget(self.prep_title, 0, 4, 1, 1)
        layout.addWidget(self.prep_info, 0, 5, 1, 1)
        layout.addWidget(self.cook_title, 0, 6, 1, 1)
        layout.addWidget(self.cook_info, 0, 7, 1, 1)
        
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        
        cols = [1, 6, 1, 7, 1, 8, 1, 25]
        for n in range(8):
            layout.setColumnStretch(n, cols[n])