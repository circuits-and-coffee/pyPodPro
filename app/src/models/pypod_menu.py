import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class TkPodMenuApp:
    """Nested iPod-style menu implemented with Tkinter.
    - Expects a nested dict structure (labels -> dict or callable or None).
    - Fixed header with title (left) and clock (right).
    - Listbox-driven navigation with a back stack.
    """

    def __init__(self, root: tk.Tk, structure: dict, *, window_title: str = 'pyPodPro'):
        self.root = root
        self.structure = structure
        self.stack = []  # list[(title, node_dict)] for back navigation
        self.ctx = {
            "states": {
                "current_page": str,
                "previous_page": None,
                "preferences": {
                    "theme": "light",
                    "brightness": 100,
                    "language": "en",
                    "volume": 50,
                    "shuffle": False,
                    "repeat": False 
                }
            },
            "playback": {
                "is_playing": False,
                "current_track": None,
                "track_position": 0
            },
            "actions": {
                "QUIT": self.root.destroy,
                "OPEN_JELLYFIN_CONNECT": None
            }
        }
        

        # Window
        self.root.title(window_title)
        self.root.geometry('320x240')
        self.root.resizable(False, False)

        # --- Header ---------------------------------------------------------
        self.header = tk.Frame(self.root, bg='white')
        self.header.pack(fill=tk.X)

        self.title_var = tk.StringVar(value='pyPodPro')
        self.title_lbl = tk.Label(self.header, textvariable=self.title_var, fg='black',bg='white', font=('Helvetica', 12))
        self.title_lbl.pack(side=tk.LEFT, padx=8, pady=4)

        self.clock_var = tk.StringVar()
        self.clock_lbl = tk.Label(self.header, textvariable=self.clock_var, fg='black',bg='white', font=('Helvetica', 12))
        self.clock_lbl.pack(side=tk.RIGHT, padx=8)
        self._tick_clock()

        ttk.Separator(self.root, orient=tk.HORIZONTAL).pack(fill=tk.X)

        # --- Content --------------------------------------------------------
        content = tk.Frame(self.root, bg='white')
        content.pack(fill=tk.BOTH, expand=True)

        list_frame = tk.Frame(content, bg='white')
        list_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=6)

        self.scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(
            list_frame,
            yscrollcommand=self.scrollbar.set,
            activestyle='none',
            highlightthickness=0,
            selectmode=tk.SINGLE,fg='black',bg='white',
            font=('Helvetica', 12),
            borderwidth=0
        )
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.focus_set()

        # Bind interactions
        # self.listbox.bind('<Double-Button-1>', self._activate_selected)
        self.listbox.bind('<Return>', self._activate_selected)
        self.listbox.bind('<Escape>', lambda e: self.go_back())
        self.listbox.bind('<Up>', self.on_arrow_up)
        self.listbox.bind('<Down>', self.on_arrow_down)

        # Start at root
        self.show_node('Main', self.structure)

    # --------------------------- Clock -------------------------------------
    def _tick_clock(self):
        self.clock_var.set(datetime.datetime.now().strftime('%I:%M %p').lstrip('0'))
        self.root.after(1000, self._tick_clock)

    # ----------------------- Navigation helpers ----------------------------
    def show_node(self, title: str, node: dict):
        self.title_var.set(title)
        self._current_title = title
        self._current_node = node

        # Populate list
        self.listbox.delete(0, tk.END)
        for label in node.keys():
            self.listbox.insert(tk.END, label)
        if node:
            self.listbox.selection_set(0)
            # ensure keyboard focus + visible active row
            self.listbox.activate(0)
            self.listbox.see(0)
            self.listbox.focus_set()

    def go_back(self):
        if not self.stack:
            return
        title, node = self.stack.pop()
        self.show_node(title, node)

    def on_arrow_up(self, event):
        curselection = self.listbox.curselection()
        if curselection[0] > 0:
            self.listbox.selection_clear(curselection[0])
            self.listbox.selection_set(curselection[0] - 1)
            self.listbox.activate(curselection[0] - 1)
  
    def on_arrow_down(self, event):
        curselection = self.listbox.curselection()
        if curselection[0] < self.listbox.size() - 1:
            self.listbox.selection_clear(curselection[0])
            self.listbox.selection_set(curselection[0] + 1)
            self.listbox.activate(curselection[0] + 1)

    def _activate_selected(self, event=None):
        sel = self.listbox.curselection()
        if not sel:
            return
        index = sel[0]
        label = self.listbox.get(index)
        value = self._current_node.get(label)
    

        # Case 1: submenu (dict)
        if isinstance(value, dict):
            self.stack.append((self._current_title, self._current_node))
            self.show_node(label, value)
            return

        # Case 2: Context-aware callable
        if isinstance(value, str):
            try:
                self.ctx['actions'][value]()
            except Exception as e:
                # Throws that TkPodMenuApp has no attribute 'Quit', need to debug
                messagebox.showerror('Error', str(e))
            return