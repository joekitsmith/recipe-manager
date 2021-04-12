import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg

class FeaturedWidget(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super(FeaturedWidget, self).__init__(*args, **kwargs)
        
        self.createWidgets()
        self.configureLayout()
        
    def createWidgets(self):

        self.background_label = qtw.QLabel()
        self.background_label.setStyleSheet("""QWidget {background-color: rgba(254,174,0,30)}""")

        self.title_label = qtw.QLabel()
        self.title_label.setText("Featured recipes")
        self.title_label.setAlignment(qtc.Qt.AlignLeft)
        self.title_label.setStyleSheet("""QWidget {font: 55pt 'Avenir'; 
                                                font-weight: bold; 
                                                margin: 20px}""")
        
        # Contains list of categories
        self.category_dict = {}
        
    def configureLayout(self):
        
        self.category_layout = qtw.QVBoxLayout()
        self.category_layout.setSpacing(0)
        self.category_layout.setContentsMargins(0,0,0,0)

        self.main_layout = qtw.QGridLayout()
        self.main_layout.addWidget(self.background_label, 0, 0, 3, 2)
        self.main_layout.addWidget(self.title_label, 0, 0, 1, 1)
        self.main_layout.addLayout(self.category_layout, 1, 0, 1, 1)
        self.main_layout.setRowStretch(2, 3)
        self.main_layout.setContentsMargins(0,0,0,0)

        self.setLayout(self.main_layout)
    
    def addFeaturedRecipe(self, recipe, category):
        # Adds title and picture to category scroll area 
        
        featured_recipe = FeaturedRecipe()
        featured_recipe.picture_data = recipe.picture_data
        featured_recipe.title_text = recipe.main_title.text()
        featured_recipe.configureLayout()

        category = self.category_dict[category]
        category.list_layout.addWidget(featured_recipe)
    
    def addFeaturedCategory(self, category):
        # Adds category scroll area to Featured page

        featured_category = FeaturedCategory(category)

        self.category_layout.addWidget(featured_category.category_title, 1)
        self.category_layout.addWidget(featured_category.scroll, 6)
        spacer = qtw.QLabel()
        spacer.setFixedSize(1200,50)
        self.category_layout.addWidget(spacer)

        self.category_dict[category] = featured_category
        

class FeaturedCategory(qtw.QWidget):
    
    def __init__(self, category_string, *args, **kwargs):
        super(FeaturedCategory, self).__init__(*args, **kwargs)
        
        self.createWidgets(category_string)
        self.configureLayout()

    def createWidgets(self, category_string):

        self.main_widget = qtw.QWidget()
        self.main_widget.setSizePolicy(qtw.QSizePolicy.MinimumExpanding, qtw.QSizePolicy.MinimumExpanding)

        # Horizontal scroll area
        self.scroll = qtw.QScrollArea()
        self.scroll.setFrameShape(qtw.QFrame.NoFrame)
        self.scroll.setWidgetResizable(True)
        self.scroll.verticalScrollBar().setEnabled(False)
        self.scroll.horizontalScrollBar().setEnabled(True)
        self.scroll.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        
        self.category_title = qtw.QLabel()
        self.category_title.setText(category_string)
        self.category_title.setStyleSheet("""QWidget {background-color: rgba(235,235,235,255);
                                                        font: 25pt 'Avenir'; 
                                                        font-weight: bold; 
                                                        margin: 0px 0px 0px 30px; 
                                                        padding: 5px 5px 5px 5px}""")
        self.category_title.setSizePolicy(qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Maximum)
        
    def configureLayout(self):

        self.list_layout = qtw.QHBoxLayout()
        self.list_layout.setSpacing(80)
        self.list_layout.setContentsMargins(30,15,0,0)

        self.main_widget.setLayout(self.list_layout)
        self.scroll.setWidget(self.main_widget)
        self.scroll.setMinimumHeight(340)
        
   
class FeaturedRecipe(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        
        super(FeaturedRecipe, self).__init__(*args, **kwargs)

        self.title = qtw.QLabel()
        self.picture = qtw.QLabel()
        self.title_text = None
        self.picture_data = None

    def configureLayout(self):
        
        self.title.setText(self.title_text)
        self.title.setStyleSheet("""QWidget {font: 20pt 'Avenir'; 
                                                font-weight: 300; 
                                                padding: 0px 0px 10px 0px;}""")
        self.title.setMaximumWidth(250)
        self.title.setAlignment(qtc.Qt.AlignTop | qtc.Qt.AlignHCenter)
        self.title.setWordWrap(True)

        # Draw recipe image with rounded border
        image = qtg.QImage()
        image.loadFromData(self.picture_data)
        pixmap = qtg.QPixmap.fromImage(image.scaled(200,200))
        radius = 30
        rounded = qtg.QPixmap(pixmap.size())
        rounded.fill(qtg.QColor("transparent"))
        painter = qtg.QPainter(rounded)
        painter.setRenderHint(qtg.QPainter.Antialiasing)
        painter.setBrush(qtg.QBrush(pixmap))
        painter.setPen(qtg.QPen(qtc.Qt.black, 3))
        path = qtg.QPainterPath()
        rect = qtc.QRectF(pixmap.rect())
        path.addRoundedRect(rect, radius, radius)
        painter.setClipPath(path)
        painter.fillPath(path, painter.brush())
        painter.strokePath(path, painter.pen())
        painter.end()
        self.picture.setPixmap(rounded)
        self.picture.setAlignment(qtc.Qt.AlignCenter)

        self.layout = qtw.QVBoxLayout()
        self.layout.addWidget(self.picture)
        self.layout.addWidget(self.title)

        self.setLayout(self.layout)