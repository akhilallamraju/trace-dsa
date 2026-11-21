# main.py

import tkinter as tk

import theme
from ui.main_menu import MainMenu
from ui.searching_menu import SearchingMenu
from ui.searching_screen import SearchingScreen


class TraceDSA:
    def __init__(self, root):
        self.root = root
        self.root.title("Trace | Data Structures & Algorithms")
        self.root.geometry(f"{theme.WINDOW_WIDTH}x{theme.WINDOW_HEIGHT}")
        self.root.minsize(theme.MIN_WIDTH, theme.MIN_HEIGHT)
        self.root.configure(bg=theme.BACKGROUND)

        self.current_screen = None
        self.show_main_menu()

    def clear_screen(self):
        if self.current_screen is not None:
            self.current_screen.destroy()
            self.current_screen = None

    def show_main_menu(self):
        self.clear_screen()
        self.current_screen = MainMenu(self.root, self.show_module)

    def show_module(self, module_name):
        if module_name == "SEARCHING":
            self.show_searching_menu()
            return

        self.clear_screen()
        screen = tk.Frame(self.root, bg=theme.BACKGROUND)
        screen.pack(fill="both", expand=True)

        tk.Label(
            screen, text=module_name, font=theme.FONT_TITLE,
            fg=theme.GREEN, bg=theme.BACKGROUND,
        ).pack(pady=40)

        tk.Label(
            screen, text="This module is currently under development.",
            font=theme.FONT_SUBTITLE, fg=theme.MUTED, bg=theme.BACKGROUND,
        ).pack(pady=10)

        tk.Button(
            screen, text="← Back to Main Menu",
            font=theme.FONT_BUTTON_TITLE, fg=theme.BACKGROUND,
            bg=theme.GREEN, relief="flat", cursor="hand2",
            command=self.show_main_menu,
        ).pack(pady=30)

        tk.Label(
            screen, text="TRACE | DATA STRUCTURES & ALGORITHMS",
            font=theme.FONT_FOOTER, fg=theme.MUTED, bg=theme.BACKGROUND,
        ).pack(side="bottom", pady=20)

        self.current_screen = screen

    def show_searching_menu(self):
        self.clear_screen()
        self.current_screen = SearchingMenu(
            self.root,
            select_callback=self.show_search_algorithm,
            back_callback=self.show_main_menu,
        )
        self.current_screen.pack(fill="both", expand=True)

    def show_search_algorithm(self, algorithm_name):
        if algorithm_name == "LINEAR":
            self.clear_screen()
            self.current_screen = SearchingScreen(
                self.root, back_callback=self.show_searching_menu,
            )
            self.current_screen.pack(fill="both", expand=True)
            return

        if algorithm_name == "BINARY":
            self._show_binary_search_placeholder()
            return

        self.show_searching_menu()

    def _show_binary_search_placeholder(self):
        self.clear_screen()
        screen = tk.Frame(self.root, bg=theme.BACKGROUND)
        screen.pack(fill="both", expand=True)

        tk.Button(
            screen, text="← Back to Searching",
            font=theme.FONT_SUBTITLE, fg=theme.CYAN,
            bg=theme.BACKGROUND, activebackground=theme.BACKGROUND,
            activeforeground=theme.FOREGROUND, relief="flat", bd=0,
            cursor="hand2", command=self.show_searching_menu,
        ).pack(anchor="w", padx=32, pady=(24, 0))

        tk.Label(
            screen, text="Binary Search", font=theme.FONT_TITLE,
            fg=theme.PURPLE, bg=theme.BACKGROUND,
        ).pack(pady=(100, 12))

        tk.Label(
            screen, text="COMING SOON", font=theme.FONT_BUTTON_TITLE,
            fg=theme.PURPLE, bg=theme.BACKGROUND,
        ).pack(pady=8)

        tk.Label(
            screen,
            text=("Binary Search will be added in a future update. "
                  "It will work on sorted arrays by repeatedly halving "
                  "the search range."),
            font=theme.FONT_SUBTITLE, fg=theme.MUTED,
            bg=theme.BACKGROUND, wraplength=520, justify="center",
        ).pack(pady=12)

        tk.Label(
            screen, text="TRACE | DATA STRUCTURES & ALGORITHMS",
            font=theme.FONT_FOOTER, fg=theme.MUTED, bg=theme.BACKGROUND,
        ).pack(side="bottom", pady=20)

        self.current_screen = screen


if __name__ == "__main__":
    root = tk.Tk()
    app = TraceDSA(root)
    root.mainloop()
