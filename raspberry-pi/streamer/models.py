from typing import Dict

USER_BY_ID: Dict[int, "User"] = {}
"""This global dictionary acts as a simple database."""


class User:
    """Simple user model."""
    
    # TODO: make this a database model and persist user.
    
    def __init__(self, id: int, name: str, password: str):
        self.id = id
        self.name = name
        self.password = password
    
    @classmethod
    def create(cls, name: str, password: str):
        """Creates a user with a unique ID."""
        index = 0
        while index in USER_BY_ID:
            index += 1
        
        user = cls(id=index, name=name, password=password)
        USER_BY_ID[index] = user
        return user