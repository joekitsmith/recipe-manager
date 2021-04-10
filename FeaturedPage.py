import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg

class FeaturedWidget(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super(FeaturedWidget, self).__init__(*args, **kwargs)

        self.background_label = qtw.QLabel()
        self.background_label.setStyleSheet("""QWidget {background-color: rgba(254,174,0,30)}""")

        self.title_label = qtw.QLabel()
        self.title_label.setText("Featured recipes")
        self.title_label.setStyleSheet("""QWidget {font: 55pt 'Avenir'; font-weight: bold; margin: 20px}""")
        self.title_label.setAlignment(qtc.Qt.AlignLeft)

        self.mainLayout = qtw.QGridLayout()
        self.categoryLayout = qtw.QVBoxLayout()
        self.categoryLayout.setSpacing(0)
        self.categoryLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.addWidget(self.background_label, 0, 0, 3, 2)
        self.mainLayout.addWidget(self.title_label, 0, 0, 1, 1)
        self.mainLayout.addLayout(self.categoryLayout, 1, 0, 1, 1)
        self.mainLayout.setRowStretch(2, 3)
        self.mainLayout.setContentsMargins(0,0,0,0)

        self.category_dict = {}

        self.setLayout(self.mainLayout)

    def addFeaturedRecipe(self, recipe, category):
        featured_recipe = FeaturedRecipe()
        featured_recipe.picture_data = recipe.picture_data
        featured_recipe.title_text = recipe.main_title.text()
        featured_recipe.layoutFeaturedRecipe()
        category = self.category_dict[category]
        category.listLayout.addWidget(featured_recipe)

    def addFeaturedCategory(self, category):
        featured_category = FeaturedCategory(category)
        self.category_dict[category] = featured_category
        self.categoryLayout.addWidget(featured_category.categoryTitle, 1)
        self.categoryLayout.addWidget(featured_category.scroll, 6)
        spacer = qtw.QLabel()
        spacer.setFixedSize(1200,50)
        self.categoryLayout.addWidget(spacer)
        
        

class FeaturedCategory(qtw.QWidget):
    def __init__(self, category_string, *args, **kwargs):
        super(FeaturedCategory, self).__init__(*args, **kwargs)

        widget = qtw.QWidget()
        self.scroll = qtw.QScrollArea()
        self.scroll.setFrameShape(qtw.QFrame.NoFrame)
        self.scroll.setWidgetResizable(True)
        self.scroll.verticalScrollBar().setEnabled(False)
        self.scroll.horizontalScrollBar().setEnabled(True)
        self.scroll.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        widget.setSizePolicy(qtw.QSizePolicy.MinimumExpanding, qtw.QSizePolicy.MinimumExpanding)

        self.categoryTitle = qtw.QLabel()
        self.categoryTitle.setText(category_string)
        self.categoryTitle.setStyleSheet("""QWidget {background-color: rgba(235,235,235,255);font: 25pt 'Avenir'; font-weight: bold; margin: 0px 0px 0px 30px; padding: 5px 5px 5px 5px}""")
        self.categoryTitle.setSizePolicy(qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Maximum)

        self.listLayout = qtw.QHBoxLayout()
        widget.setLayout(self.listLayout)

        self.listLayout.setSpacing(80)
        self.listLayout.setContentsMargins(30,15,0,0)
        self.scroll.setWidget(widget)
        self.scroll.setMinimumHeight(340)


class FeaturedRecipe(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super(FeaturedRecipe, self).__init__(*args, **kwargs)

        self.title = qtw.QLabel()
        self.picture = qtw.QLabel()
        self.title_text = None
        self.picture_data = None

    def layoutFeaturedRecipe(self):
        
        self.title.setText(self.title_text)
        self.title.setStyleSheet("""QWidget {font: 20pt 'Avenir'; font-weight: 300; padding: 0px 0px 10px 0px;}""")
        self.title.setMaximumWidth(250)

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
        self.title.setAlignment(qtc.Qt.AlignTop | qtc.Qt.AlignHCenter)
        self.title.setWordWrap(True)
        self.picture.setAlignment(qtc.Qt.AlignVCenter | qtc.Qt.AlignHCenter)
        self.setLayout(self.layout)