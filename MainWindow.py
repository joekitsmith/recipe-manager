import sys
import os
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
        
        self.createWidgets()
        self.configureLayout()

        self.sidebarContent.featured_button.clicked.connect(self.openFeaturedPage)
        self.sidebarContent.browse_button.clicked.connect(self.openBrowsePage)
        self.sidebarContent.list_button.clicked.connect(self.openListPage)
        self.sidebarContent.timetable_button.clicked.connect(self.openTimetablePage)
        self.sidebarContent.nutrition_button.clicked.connect(self.openNutritionPage)
        self.sidebarContent.add_button.clicked.connect(self.openAddPage)
        
        self.setCentralWidget(self.total_widget)

        self.showMaximized()
        
    def createWidgets(self):
        
        self.total_widget = qtw.QWidget()
        self.sidebar = Sidebar.SidebarWidget()
        self.sidebarContent = sidebar.sidebarContent
        
        self.test_recipe = RecipePage.RecipeWidget()
        self.test_recipe.getRecipe(1)
        
        self.scroll = qtw.QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.test_recipe)
        self.scroll.setFrameShape(qtw.QFrame.NoFrame)
        
    def configureLayout(self):

        grid_layout = qtw.QGridLayout()
        grid_layout.addWidget(self.sidebar, 0, 0)
        grid_layout.addWidget(self.scroll, 0, 1)
        grid_layout.setColumnStretch(1, 15)
        grid_layout.setColumnStretch(0, 1)
        grid_layout.setSpacing(0)
        grid_layout.setContentsMargins(0,0,0,0)
        self.total_widget.setLayout(grid_layout) 
        
    def openFeaturedPage(self):
        
        self.FeaturedPage = FeaturedPage.FeaturedWidget()

        self.FeaturedPage.addFeaturedCategory("Vegetarian")
        self.FeaturedPage.addFeaturedCategory("Carb heavy")
        self.FeaturedPage.addFeaturedCategory("Saltier than the sea")

        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(1), "Vegetarian")
        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(2), "Vegetarian")
        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(3), "Vegetarian")
        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(4), "Vegetarian")
        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(5), "Vegetarian")
        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(9), "Vegetarian")
        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(6), "Saltier than the sea")
        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(7), "Saltier than the sea")
        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(10), "Saltier than the sea")
        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(10), "Carb heavy")
        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(8), "Carb heavy")
        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(7), "Carb heavy")
        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(1), "Carb heavy")
        self.FeaturedPage.addFeaturedRecipe(RecipePage.RecipeWidget().getRecipe(5), "Carb heavy")
        
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