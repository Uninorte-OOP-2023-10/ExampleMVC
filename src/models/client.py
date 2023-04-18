from __future__ import annotations
from typing import Optional

class Client:

    __ID = 0
    __CLIENTS = []

    def __init__(self) -> None:
        Client.__ID += 1
        self.__id = Client.__ID
        self.__name = f'Default Client {Client.__ID}'
        Client.__CLIENTS.append(self)

    def __repr__(self) -> str:
        return f'{self.__id} | {self.__name}'
    
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def name(self) -> str:
        return self.__name

    @staticmethod
    def search_by_id(id: int) -> Optional["Client"]:
        if id > Client.__ID:
            return None
        
        for client in Client.__CLIENTS:
            if client.id == id:
                return client
            
        return None
    
    @staticmethod
    def number_of_clients() -> None:
        return len(Client.__CLIENTS)
