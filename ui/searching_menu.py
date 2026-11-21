"""Algorithm selection screen for the Searching module."""

import tkinter as tk

import theme


class SearchingMenu(tk.Frame):
    """Display searching algorithms as interactive cards."""

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

        cards = tk.Frame(content, bg=theme.BACKGROUND)
        cards.pack()

        self._algorithm_card(
            cards,
            column=0,
            name="LINEAR SEARCH",
            description="Check each element one by one.",
            number="01",
            accent=theme.CYAN,
            status="AVAILABLE",
            algorithm="LINEAR",
        )
        self._algorithm_card(
            cards,
            column=1,
            name="BINARY SEARCH",
            description="Repeatedly halve a sorted search range.",
            number="02",
            accent=theme.PURPLE,
            status="COMING SOON",
            algorithm="BINARY",
        )

        tk.Label(
            self,
            text="TRACE | DATA STRUCTURES & ALGORITHMS",
            font=theme.FONT_FOOTER,
            fg=theme.MUTED,
            bg=theme.BACKGROUND,
        ).pack(side="bottom", pady=20)

    def _algorithm_card(
        self, parent, column, name, description, number, accent, status, algorithm
    ):
        card = tk.Frame(
            parent,
            bg=theme.SURFACE,
            width=270,
            height=220,
            highlightthickness=1,
            highlightbackground=theme.MUTED,
        )
        card.grid(row=0, column=column, padx=14)
        card.pack_propagate(False)

        labels = [
            tk.Label(
                card,
                text=number,
                font=theme.FONT_BUTTON_NUMBER,
                fg=accent,
                bg=theme.SURFACE,
            ),
            tk.Label(
                card,
                text=name,
                font=theme.FONT_BUTTON_TITLE,
                fg=theme.FOREGROUND,
                bg=theme.SURFACE,
            ),
            tk.Label(
                card,
                text=description,
                font=theme.FONT_BUTTON_DESCRIPTION,
                fg=theme.MUTED,
                bg=theme.SURFACE,
                wraplength=220,
                justify="center",
            ),
            tk.Label(
                card,
                text=status,
                font=theme.FONT_BUTTON_NUMBER,
                fg=accent,
                bg=theme.SURFACE,
            ),
        ]

        labels[0].pack(pady=(24, 12))
        labels[1].pack(pady=(0, 10))
        labels[2].pack(pady=(0, 18))
        labels[3].pack()

        # Bind the card and its labels together. Leaving one child for
        # another schedules a check; the hover state only resets once the
        # pointer has actually left the card, preventing flicker.
        widgets = [card, *labels]

        def set_hovered(hovered):
            background = theme.SURFACE_HOVER if hovered else theme.SURFACE
            for widget in widgets:
                widget.configure(bg=background)
            card.configure(
                highlightbackground=accent if hovered else theme.MUTED
            )

        def pointer_is_inside():
            x, y = card.winfo_pointerxy()
            left = card.winfo_rootx()
            top = card.winfo_rooty()
            return (
                left <= x < left + card.winfo_width()
                and top <= y < top + card.winfo_height()
            )

        def on_leave(_event):
            card.after_idle(
                lambda: set_hovered(pointer_is_inside())
                if pointer_is_inside()
                else set_hovered(False)
            )

        def on_enter(_event):
            set_hovered(True)

        def on_click(_event):
            self.select_callback(algorithm)

        for widget in widgets:
            widget.configure(cursor="hand2")
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
            widget.bind("<Button-1>", on_click)
