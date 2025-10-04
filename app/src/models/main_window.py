from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QListView, QStackedWidget
from PySide6.QtCore import QFile, QIODevice, Qt, QAbstractItemModel
from PySide6 import QtUiTools
from pathlib import Path
from models.menu_struct import MENU_STRUCTURE

from models.menu import MenuModel

# The goal of doing it this way is to have MainWindow handle all the UI loading
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.navigate_to = None  # Placeholder for navigation function
        base = Path(__file__).parent.parent / "ui"

        # Load the shell (QMainWindow) and show it
        shell = self.load_ui(base / "main_window.ui")
        self.resize(640, 480)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setCentralWidget(shell.centralWidget())

        # Grab the stack inside the shell
        self.stack = self.findChild(QStackedWidget, "stackedWidget")
        if self.stack is None:
            raise RuntimeError("stackedWidget not found in main_window.ui")
        # Load the Main Menu page (a QWidget) and insert it
        menu_page = self.load_ui(base / "menu_element.ui")
        self.menu_page = menu_page
        
        self.menu_model = MenuModel(menuItems=MENU_STRUCTURE)

        self.mainMenuList = self.menu_page.findChild(QListView, "mainMenuListView")
        if self.mainMenuList is None:
            raise RuntimeError("mainMenuListView not found in menu_element.ui")
        self.stack.addWidget(menu_page)
        self.stack.setCurrentWidget(menu_page)
        self.populate_menu(menu_page, self.action_triggered, menu_struct=None)
        self.mainMenuList.setModel(self.menu_model)
        self.mainMenuList.selectionModel().selectionChanged.connect(
            lambda selected, deselected: 
                self.menu_item_changed(
                    self.menu_model.menuItems[selected.indexes()[0].row()][1]
                ) if selected.indexes() else None)
        self.mainMenuList.clicked.connect(lambda index: self.action_triggered(self.menu_model.menuItems[index.row()][1]))

        
        
    # Populate the menu, depending on which level of MENU_STRUCTURE we're at.
    def populate_menu(self, menu_page, action_triggered, menu_struct): # Takes the menu_page widget and the action_triggered function
        # I don't think I need menu_page anymore, since that's now self.menu_page?
        print(f"Populating menu with structure: {menu_struct or MENU_STRUCTURE}")
        current = menu_struct or MENU_STRUCTURE
        self.menu_model.beginResetModel()
        self.menu_model.menuItems = current
        self.menu_model.endResetModel()
        
        # Ensure something is selected so enter works
        # if self.menu_model.rowCount(None) > 0:
        #     self.mainMenuList.setCurrentIndex(self.menu_model.index(0, 0))
        #     self.mainMenuList.setFocus()

        self.mainMenuList.setModel(self.menu_model)
        
        
    def load_ui(self, path, parent=None):
        ui_file = QFile(str(path))
        if not ui_file.open(QIODevice.ReadOnly):
            raise RuntimeError(f"Unable to open UI: {path}")
        w = QtUiTools.QUiLoader().load(ui_file, parent)
        ui_file.close()
        if not w:
            raise RuntimeError(f"Failed to load UI: {path}")
        return w
    
    def menu_item_changed(self, menu_item):
        # print(f"Menu item changed: {menu_item}")
        # Here you could update a status bar or other UI element with details about the selected item
        return menu_item
    
    # I want to eventually change this to just call functions directly
    # based on the action string in the menu tuple
    # e.g. ("Local Music", show_local_music)
    def action_triggered(self, action_name):
        print(f"Action triggered: {action_name}")
        
        # If the action is a list, it's a submenu, so we need to handle that differently
        if isinstance(action_name, list):
            
            self.stack.setCurrentWidget(self.menu_page)
            
            # Populate the main menu
            mainMenuList = self.menu_page.findChild(QListView, "mainMenuListView")
            if mainMenuList is None:
                raise RuntimeError("mainMenuListView not found in menu_element.ui")
            self.populate_menu(self.menu_page, self.action_triggered, menu_struct=action_name)
        
        # if action_name == "show_local_music":
        #     show_local_music()
        # elif action_name == "show_online_music":
        #     show_online_music()
        # elif action_name == "show_photos":
        #     show_photos()
        # elif action_name == "show_videos":
        #     show_videos()
        # elif action_name == "show_settings":
        #     show_settings()
        elif action_name == "quit_app":
            exit()
        else:
            print(f"Unknown action: {action_name}")
