import tkinter as tk

from tkinter import END
from typing import Any, Optional

from controllers.client import ClientController
from views.utils.components import Button, Label, Text

class ClientView(tk.Tk):

    def __init__(
        self, 
        title: str = 'Default',
        resolution: str = '500x500',
        **kwargs: Any
    ) -> None:
        super().__init__(**kwargs)
        self.title(title)
        self.geometry(resolution)
        self.__initialize_components()
        self.mainloop()

    def __initialize_components(self):
        Label(
            self, 
            text = (
                '----- MVC Example -----\n'
                'This is a MVC Example\n'
            ), 
            font=('consolas', 11)
        )

        Label(
            self, 
            text = (
                '--- Clients Module ---\n'
                '\nAdd Client:'
            ), 
            font=('consolas', 11)
        )

        number_of_clients = tk.StringVar()
        number_of_clients.set('Number of Clients = 0')

        Button(
            self, 
            text = 'Add Client', 
            command = lambda: ClientController.add_client(number_of_clients), 
            font = ('consolas', 10)
        )

        Label(
            self, 
            textvariable = number_of_clients, 
            font = ('consolas', 11)
        )

        Label(
            self, 
            text = '\nSearch by ID:', 
            font = ('consolas', 11)
        )

        text = Text(
            self, 
            height = 1,
            width = 5,
            font = ('consolas', 11)
        )

        Button(
            self, 
            text = 'Search Client', 
            command = lambda: ClientController.get_client_by_id(text.get('1.0', END)), 
            font = ('consolas', 10)
        )