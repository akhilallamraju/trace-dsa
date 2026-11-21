"""Algorithm selection screen for the Searching module."""

import tkinter as tk

import theme


class SearchingMenu(tk.Frame):
    """Display available searching algorithms using the main-menu button style."""

    def __init__(self, parent, select_callback, back_callback):
        super().__init__(parent, bg=theme.BACKGROUND)
        self.select_callback = select_callback
        self.back_callback = back_callback
        self._build_ui()

    def _build_ui(self):
        tk.Button(
            self,
            text="← Back to Main Menu",
            command=self.back_callback,
            font=theme.FONT_SUBTITLE,
            fg=theme.CYAN,
            bg=theme.BACKGROUND,
            activebackground=theme.BACKGROUND,
            activeforeground=theme.FOREGROUND,
            relief="flat",
            bd=0,
            cursor="hand2",
        ).pack(anchor="w", padx=32, pady=(24, 0))

        content = tk.Frame(self, bg=theme.BACKGROUND)
        content.place(relx=0.5, rely=0.47, anchor="center")

        tk.Label(
            content,
            text="Searching",
            font=theme.FONT_TITLE,
            fg=theme.GREEN,
            bg=theme.BACKGROUND,
        ).pack(pady=(0, 8))

        tk.Label(
            content,
            text="Choose an algorithm to explore.",
            font=theme.FONT_SUBTITLE,
            fg=theme.MUTED,
            bg=theme.BACKGROUND,
        ).pack(pady=(0, 34))

        buttons = tk.Frame(content, bg=theme.BACKGROUND)
        buttons.pack()

        self._algorithm_button(
            buttons,
            column=0,
            number="01",
            name="LINEAR SEARCH",
            description="Check each element one by one.",
            status="AVAILABLE",
            accent=theme.CYAN,
            algorithm="LINEAR",
        )
        self._algorithm_button(
            buttons,
            column=1,
            number="02",
            name="BINARY SEARCH",
            description="Repeatedly halve a sorted search range.",
            status="COMING SOON",
            accent=theme.PURPLE,
            algorithm="BINARY",
        )

        tk.Label(
            self,
            text="TRACE | DATA STRUCTURES & ALGORITHMS",
            font=theme.FONT_FOOTER,
            fg=theme.MUTED,
            bg=theme.BACKGROUND,
        ).pack(side="bottom", pady=20)

    def _algorithm_button(
        self, parent, column, number, name, description, status, accent, algorithm
    ):
        button = tk.Button(
            parent,
            text=f"{number}\n\n{name}\n\n{description}\n\n{status}",
            font=theme.FONT_BUTTON_TITLE,
            fg=theme.FOREGROUND,
            bg=theme.SURFACE,
            activeforeground=accent,
            activebackground=theme.SURFACE_HOVER,
            relief="flat",
            bd=0,
            cursor="hand2",
            width=27,
            height=8,
            wraplength=270,
            justify="center",
            command=lambda: self.select_callback(algorithm),
        )
        button.grid(row=0, column=column, padx=14)

        # Match the main menu: change the button itself on Enter/Leave.
        # A single widget avoids child-label background gaps and flicker.
        button.bind(
            "<Enter>",
            lambda _event, b=button, colour=accent:
                b.config(bg=theme.SURFACE_HOVER, fg=colour),
        )
        button.bind(
            "<Leave>",
            lambda _event, b=button:
                b.config(bg=theme.SURFACE, fg=theme.FOREGROUND),
        )
