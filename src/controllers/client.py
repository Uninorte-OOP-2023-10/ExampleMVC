from __future__ import annotations
from tkinter import StringVar
from tkinter.messagebox import showinfo
from typing import Optional

from models.client import Client

class ClientController:

    @staticmethod
    def add_client(text_variable: StringVar) -> None:
        Client()

        showinfo(
            title = 'Added Successful',
            message = 'Successfully added the client'
        )

        text_variable.set(f'Number of Clients = {Client.number_of_clients()}')

    @staticmethod
    def get_client_by_id(id: str) -> None:
        try:
            client = Client.search_by_id(int(id))
            if client is None:
                message = 'Error 404: Client not found'
            else:
                message = (
                    f'Client ID: {client.id}\n'
                    f'Client Name: {client.name}'
                )
        except ValueError:
            showinfo(
                title = 'Error',
                message = 'ID must be numeric'
            )
        else:
            showinfo(
                title = 'Information',
                message = message
            )
        
