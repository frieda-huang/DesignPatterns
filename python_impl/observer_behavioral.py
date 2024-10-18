"""
Observer behavioral pattern establishes a one-to-many relationship between objects.
When one object (called the subject) changes its state, all its dependent objects
(called observers) are automatically notified and updated.

Basic Structure
- Subject interface defines the contract for attaching, detaching, and notifying observers.
- Concrete subject implements the subject interface.
- Observer interface defines the contract for the update() method, which the subject calls to notify observers of changes.
- Concrete observers implement the observer interface and define how they should respond to changes in the subject’s state.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class SubscriberInfo:
    name: str
    start_date: str


class Observer(ABC):
    @abstractmethod
    def update(self, monthly_fee: int):
        pass


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class TwitterSubscriptionService(Subject):
    def __init__(self):
        self.monthly_fee = 20
        self.observers: List[Observer] = []

    def register_observer(self, observer: Observer):
        self.observers.append(observer)
        print(f"Registered observer: {observer.subscriber_info.name}")

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)
        print(f"Removed observer: {observer.subscriber_info.name}")

    def notify_observers(self):
        print(f"Notifying all subscribers of the new monthly fee: ${self.monthly_fee}")
        for observer in self.observers:
            observer.update(self.monthly_fee)

    def set_monthly_fee(self, new_fee: int):
        print(f"Updating monthly fee from ${self.monthly_fee} to ${new_fee}")
        self.monthly_fee = new_fee
        self.notify_observers()


class Subscriber(Observer):
    def __init__(
        self, subscriber_info: SubscriberInfo, subject: TwitterSubscriptionService
    ):
        self.subscriber_info = subscriber_info
        self.subject = subject

    def update(self, monthly_fee: int):
        print(
            f"{self.subscriber_info.name} has been notified that the monthly fee is now ${monthly_fee}."
        )

        if monthly_fee > 25:
            print(f"{self.subscriber_info.name} is unsubscribing due to high fees.")
            self.subject.remove_observer(self)


if __name__ == "__main__":
    twitter_service = TwitterSubscriptionService()

    alice = Subscriber(
        SubscriberInfo(name="Alice", start_date="2024-01-01"), twitter_service
    )
    bob = Subscriber(
        SubscriberInfo(name="Bob", start_date="2024-02-01"), twitter_service
    )

    twitter_service.register_observer(alice)
    twitter_service.register_observer(bob)

    twitter_service.set_monthly_fee(22)
    twitter_service.set_monthly_fee(30)
