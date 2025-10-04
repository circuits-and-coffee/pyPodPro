from PySide6.QtCore import Qt, QAbstractListModel

class MenuModel(QAbstractListModel):
    # Instead of tuples of "todos", we're going to have a tuple of (menu_item, action)
    def __init__(self, *args, menuItems=None, **kwargs):
        super().__init__()
        self.menuItems = menuItems or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            menu_item, action = self.menuItems[index.row()]
            # Return the menu text only.
            return menu_item

    def rowCount(self, index):
        return len(self.menuItems)