"""Algorithm selection screen for the Searching module."""

import tkinter as tk

import theme


class SearchingMenu(tk.Frame):
    def __init__(self, parent, select_callback, back_callback):
        super().__init__(parent, bg=theme.BACKGROUND)
        self.select_callback = select_callback
        self.back_callback = back_callback
        self._build_ui()

    def _build_ui(self):
        tk.Button(
            self, text="← Back to Main Menu", command=self.back_callback,
            font=theme.FONT_SUBTITLE, fg=theme.CYAN, bg=theme.BACKGROUND,
            activebackground=theme.BACKGROUND, activeforeground=theme.FOREGROUND,
            relief="flat", bd=0, cursor="hand2",
        ).pack(anchor="w", padx=32, pady=(24, 0))

        content = tk.Frame(self, bg=theme.BACKGROUND)
        content.place(relx=0.5, rely=0.47, anchor="center")

        tk.Label(
            content, text="Searching", font=theme.FONT_TITLE,
            fg=theme.GREEN, bg=theme.BACKGROUND,
        ).pack(pady=(0, 8))

        tk.Label(
            content, text="Choose an algorithm to explore.",
            font=theme.FONT_SUBTITLE, fg=theme.MUTED, bg=theme.BACKGROUND,
        ).pack(pady=(0, 34))

        cards = tk.Frame(content, bg=theme.BACKGROUND)
        cards.pack()

        self._algorithm_card(
            cards, column=0, name="LINEAR SEARCH",
            description="Check each element one by one.",
            number="01", accent=theme.CYAN, status="AVAILABLE",
            callback=lambda: self.select_callback("LINEAR"),
        )
        self._algorithm_card(
            cards, column=1, name="BINARY SEARCH",
            description="Repeatedly halve a sorted search range.",
            number="02", accent=theme.PURPLE, status="COMING SOON",
            callback=lambda: self.select_callback("BINARY"),
        )

        tk.Label(
            self, text="TRACE | DATA STRUCTURES & ALGORITHMS",
            font=theme.FONT_FOOTER, fg=theme.MUTED, bg=theme.BACKGROUND,
        ).pack(side="bottom", pady=20)

    def _algorithm_card(self, parent, column, name, description, number,
                        accent, status, callback):
        card = tk.Frame(
            parent, bg=theme.SURFACE, width=270, height=220,
            highlightthickness=1, highlightbackground=theme.MUTED,
        )
        card.grid(row=0, column=column, padx=14)
        card.pack_propagate(False)

        number_label = tk.Label(
            card, text=number, font=theme.FONT_BUTTON_NUMBER,
            fg=accent, bg=theme.SURFACE,
        )
        number_label.pack(pady=(24, 12))

        title = tk.Label(
            card, text=name, font=theme.FONT_BUTTON_TITLE,
            fg=theme.FOREGROUND, bg=theme.SURFACE,
        )
        title.pack(pady=(0, 10))

        detail = tk.Label(
            card, text=description, font=theme.FONT_BUTTON_DESCRIPTION,
            fg=theme.MUTED, bg=theme.SURFACE, wraplength=220,
            justify="center",
        )
        detail.pack(pady=(0, 18))

        status_label = tk.Label(
            card, text=status, font=theme.FONT_BUTTON_NUMBER,
            fg=accent, bg=theme.SURFACE,
        )
        status_label.pack()

        for widget in (card, number_label, title, detail, status_label):
            widget.bind("<Enter>", lambda _event, c=card, a=accent:
                        c.configure(bg=theme.SURFACE_HOVER))
            widget.bind("<Leave>", lambda _event, c=card:
                        c.configure(bg=theme.SURFACE))
            widget.bind("<Button-1>", lambda _event, action=callback: action())
            widget.configure(cursor="hand2")
