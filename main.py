
# main.py

import tkinter as tk

import theme
from ui.main_menu import MainMenu


class TraceDSA:
    def __init__(self, root):
        self.root = root
        self.root.title("Trace | Data Structures & Algorithms")

        self.root.geometry(
            f"{theme.WINDOW_WIDTH}x{theme.WINDOW_HEIGHT}"
        )

        self.root.minsize(
            theme.MIN_WIDTH,
            theme.MIN_HEIGHT
        )

        self.root.configure(
            bg=theme.BACKGROUND
        )

        self.current_screen = None
        self.show_main_menu()


    def clear_screen(self):
        if self.current_screen is not None:
            self.current_screen.destroy()
            self.current_screen = None


    def show_main_menu(self):
        self.clear_screen()

        self.current_screen = MainMenu(
            self.root,
            self.show_module
        )


    def show_module(self, module_name):
        self.clear_screen()

        screen = tk.Frame(
            self.root,
            bg=theme.BACKGROUND
        )

        screen.pack(fill="both", expand=True)

        title = tk.Label(
            screen,
            text=module_name,
            font=theme.FONT_TITLE,
            fg=theme.GREEN,
            bg=theme.BACKGROUND
        )

        title.pack(pady=40)

        description = tk.Label(
            screen,
            text="This module is currently under development.",
            font=theme.FONT_SUBTITLE,
            fg=theme.MUTED,
            bg=theme.BACKGROUND
        )

        description.pack(pady=10)

        back_button = tk.Button(
            screen,
            text="← Back to Main Menu",
            font=theme.FONT_BUTTON_TITLE,
            fg=theme.BACKGROUND,
            bg=theme.GREEN,
            relief="flat",
            cursor="hand2",
            command=self.show_main_menu
        )

        back_button.pack(pady=30)

        footer = tk.Label(
            screen,
            text="TRACE | DATA STRUCTURES & ALGORITHMS",
            font=theme.FONT_FOOTER,
            fg=theme.MUTED,
            bg=theme.BACKGROUND
        )

        footer.pack(side="bottom", pady=20)

        self.current_screen = screen


if __name__ == "__main__":
    root = tk.Tk()
    app = TraceDSA(root)
    root.mainloop()
