"""
Strategy pattern is a behavioral design pattern that allows you to define a family of algorithms,
excapsulate each one, and make them interchangeable.

Basic Structure
- Context uses a Strategy to execute a particular algorithm.
- Strategy interface defines the contract that the concrete strategies must follow.
- Concrete strategies represent different algorithms or approaches to the same task.
"""

from abc import ABC, abstractmethod


class ColPaliSearchStrategy(ABC):
    @abstractmethod
    def search(self, query: str):
        pass


class SearchEngine:
    def __init__(self, cpss: ColPaliSearchStrategy):
        self._strategy = cpss

    @property
    def strategy(self) -> ColPaliSearchStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, cpss: ColPaliSearchStrategy):
        self._strategy = cpss

    def search(self, query: str):
        return self._strategy.search(query)


class ANNHNSWHamming(ColPaliSearchStrategy):
    def search(self, query: str):
        print(f"Search '{query}' using {__class__.__name__}")


class ExactMaxSim(ColPaliSearchStrategy):
    def search(self, query: str):
        print(f"Search '{query}' using {__class__.__name__}")


if __name__ == "__main__":
    query = "What is the meaning of life?"

    ann = SearchEngine(ANNHNSWHamming())
    ann.search(query)

    exact = SearchEngine(ExactMaxSim())
    exact.search(query)
