"""
Composite structural pattern is used to compose objects into tree-like structures to represent part-whole hierarchies.

Basic Structure
- Component interface
- Leaf
- Composite
- Client
"""

from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent: str = ""):
        pass


class File(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name

    def display(self, indent: str = ""):
        print(f"{indent}- File: {self.name}")


class Directory(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def display(self, indent: str = ""):
        print(f"{indent}+ Directory: {self.name}")
        for child in self.children:
            child.display(indent + "  ")


if __name__ == "__main__":
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")

    dir1 = Directory("Documents")
    dir2 = Directory("Pictures")
    dir3 = Directory("Videos")

    dir1.add(file1)
    dir1.add(file2)
    dir2.add(file3)
    dir3.add(dir1)

    dir3.display()
