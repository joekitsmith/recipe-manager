import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg

import Sidebar
import RecipePage
import FeaturedPage
import BrowsePage
import ListPage
import TimetablePage
import NutritionPage
import AddRecipePage

class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Recipe Manager")
        
        total_widget = qtw.QWidget()
        sidebar = Sidebar.SidebarWidget()
        sidebarContent = sidebar.sidebarContent
        
        self.test_recipe = RecipePage.RecipeWidget()
        self.test_recipe.exampleRecipe()
        
        self.scroll = qtw.QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.test_recipe)
        self.scroll.setFrameShape(qtw.QFrame.NoFrame)

        sidebarContent.featured_button.clicked.connect(self.openFeaturedPage)
        sidebarContent.browse_button.clicked.connect(self.openBrowsePage)
        sidebarContent.list_button.clicked.connect(self.openListPage)
        sidebarContent.timetable_button.clicked.connect(self.openTimetablePage)
        sidebarContent.nutrition_button.clicked.connect(self.openNutritionPage)
        sidebarContent.add_button.clicked.connect(self.openAddPage)

        grid_layout = qtw.QGridLayout()
        grid_layout.addWidget(sidebar, 0, 0)
        grid_layout.addWidget(self.scroll, 0, 1)
        grid_layout.setColumnStretch(1, 15)
        grid_layout.setColumnStretch(0, 1)
        grid_layout.setSpacing(0)
        grid_layout.setContentsMargins(0,0,0,0)
        total_widget.setLayout(grid_layout)

        self.setCentralWidget(total_widget)

        self.showMaximized()

    def openFeaturedPage(self):
        self.FeaturedPage = FeaturedPage.FeaturedWidget()
        self.test_recipe = RecipePage.RecipeWidget()
        self.test_recipe.exampleRecipe()
        self.FeaturedPage.addFeaturedCategory("Vegan")
        self.FeaturedPage.addFeaturedCategory("Vegetarian")
        self.FeaturedPage.addFeaturedRecipe(self.test_recipe, "Vegan")
        self.FeaturedPage.addFeaturedRecipe(self.test_recipe, "Vegan")
        self.FeaturedPage.addFeaturedRecipe(self.test_recipe, "Vegan")
        self.FeaturedPage.addFeaturedRecipe(self.test_recipe, "Vegan")
        self.FeaturedPage.addFeaturedRecipe(self.test_recipe, "Vegan")
        self.FeaturedPage.addFeaturedRecipe(self.test_recipe, "Vegan")
        self.FeaturedPage.addFeaturedRecipe(self.test_recipe, "Vegetarian")
        self.FeaturedPage.addFeaturedRecipe(self.test_recipe, "Vegetarian")
        self.FeaturedPage.addFeaturedRecipe(self.test_recipe, "Vegetarian")
        self.FeaturedPage.addFeaturedRecipe(self.test_recipe, "Vegetarian")
        self.FeaturedPage.addFeaturedRecipe(self.test_recipe, "Vegetarian")
        self.FeaturedPage.addFeaturedRecipe(self.test_recipe, "Vegetarian")
        self.scroll.setWidget(self.FeaturedPage)

    def openBrowsePage(self):
        self.BrowsePage = BrowsePage.BrowseWidget()
        self.scroll.setWidget(self.BrowsePage)

    def openListPage(self):
        self.ListPage = ListPage.ListWidget()
        self.scroll.setWidget(self.ListPage)

    def openTimetablePage(self):
        self.TimetablePage = TimetablePage.TimetableWidget()
        self.scroll.setWidget(self.TimetablePage)

    def openNutritionPage(self):
        self.NutritionPage = NutritionPage.NutritionWidget()
        self.scroll.setWidget(self.NutritionPage)

    def openAddPage(self):
        self.AddPage = AddRecipePage.AddRecipeWidget()
        self.scroll.setWidget(self.AddPage)
        

if __name__ == '__main__':  
    app = qtw.QApplication(sys.argv)
    app.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())