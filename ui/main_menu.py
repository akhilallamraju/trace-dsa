
"""
ui/main_menu.py:

Defines main menu screen for Trace, providing navigation
to the searching, sorting and binary tree visualisation modules.
"""

import tkinter as tk
import theme


class MainMenu:
    def __init__(self, parent, navigate_callback):

        self.parent = parent
        self.navigate_callback = navigate_callback

        self.frame = tk.Frame(
            parent,
            bg=theme.BACKGROUND
        )

        self.frame.pack(fill="both", expand=True)

        self.create_widgets()


    def create_widgets(self):
        # Main content container
        content = tk.Frame(
            self.frame,
            bg=theme.BACKGROUND
        )

        content.place(
            relx=0.5,
            rely=0.46,
            anchor="center"
        )

        title = tk.Label(
            content,
            text="Trace",
            font=theme.FONT_TITLE,
            fg=theme.GREEN,
            bg=theme.BACKGROUND
        )

        title.pack(pady=(0, 8))

        subtitle = tk.Label(
            content,
            text="Data Structures & Algorithms",
            font=theme.FONT_SUBTITLE,
            fg=theme.MUTED,
            bg=theme.BACKGROUND
        )

        subtitle.pack(pady=(0, 45))

        heading = tk.Label(
            content,
            text="SELECT A MODULE",
            font=(theme.FONT_FAMILY, 10, "bold"),
            fg=theme.FOREGROUND,
            bg=theme.BACKGROUND
        )

        heading.pack(pady=(0, 20))

        button_container = tk.Frame(
            content,
            bg=theme.BACKGROUND
        )

        button_container.pack()

        modules = [
            {
                "name": "SEARCHING",
                "accent": theme.CYAN,
                "number": "01"
            },
            {
                "name": "SORTING",
                "accent": theme.GREEN,
                "number": "02"
            },
            {
                "name": "BINARY TREES",
                "accent": theme.PURPLE,
                "number": "03"
            }
        ]

        for index, module in enumerate(modules):
            button = tk.Button(
                button_container,
                text=(
                    f"{module['number']}\n\n"
                    f"{module['name']}"
                ),
                font=theme.FONT_BUTTON_TITLE,
                fg=theme.FOREGROUND,
                bg=theme.SURFACE,
                activeforeground=module["accent"],
                activebackground=theme.SURFACE_HOVER,
                relief="flat",
                bd=0,
                cursor="hand2",
                width=15,
                height=4,
                wraplength=180,
                justify="center",
                command=lambda name=module["name"]:
                    self.navigate_callback(name)
            )

            button.grid(
                row=0,
                column=index,
                padx=theme.CARD_GAP // 2
            )

            # Hover effect
            button.bind(
                "<Enter>",
                lambda event, b=button, c=module["accent"]:
                    b.config(
                        bg=theme.SURFACE_HOVER,
                        fg=c
                    )
            )

            button.bind(
                "<Leave>",
                lambda event, b=button:
                    b.config(
                        bg=theme.SURFACE,
                        fg=theme.FOREGROUND
                    )
            )

        footer = tk.Label(
            self.frame,
            text="TRACE | DATA STRUCTURES & ALGORITHMS",
            font=theme.FONT_FOOTER,
            fg=theme.MUTED,
            bg=theme.BACKGROUND
        )

        footer.pack(side="bottom", pady=20)

    def destroy(self):
        self.frame.destroy()
