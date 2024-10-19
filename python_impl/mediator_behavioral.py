"""
Mediator behavioral pattern facilitates communication between objects
by defining a mediator object. The mediator controls the interactions
and communication between these objects.

Basic Structure
- Mediator interface
- Concrete mediator
- Colleague class
"""

from abc import ABC, abstractmethod
from typing import List


class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message, user):
        pass


class ChatRoomMediator(ChatMediator):
    def __init__(self):
        self.users: List["User"] = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, user: "User"):
        for u in self.users:
            if u != user:
                u.receive_message(message)


class User:
    def __init__(self, name, mediator: ChatRoomMediator):
        self.name = name
        self.mediator = mediator

    def send_message(self, message):
        print(f"{self.name} sends message: {message}")
        self.mediator.send_message(message, self)

    def receive_message(self, message):
        print(f"{self.name} receives message: {message}")


if __name__ == "__main__":
    chat_mediator = ChatRoomMediator()

    user1 = User("Alice", chat_mediator)
    user2 = User("Bob", chat_mediator)
    user3 = User("Charlie", chat_mediator)

    chat_mediator.add_user(user1)
    chat_mediator.add_user(user2)
    chat_mediator.add_user(user3)

    user1.send_message("Hello everyone!")
    user2.send_message("Hi Alice!")
    user3.send_message("Hello Bob and Alice!")
