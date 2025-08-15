import tkinter as tk
from models.pypod_menu import TkPodMenuApp
from models.menu_struct import MENU_STRUCTURE



def main():
    root = tk.Tk()
    root.attributes('-topmost', True) 
    root.after(200, lambda: root.attributes('-topmost', False))  # then release
    root.focus_force() 
    app = TkPodMenuApp(root, MENU_STRUCTURE)
    root.mainloop()


if __name__ == '__main__':
    main()