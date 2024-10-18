"""
Command behavioral pattern turns a request or an action into 
a stand-alone object that contains all the necessary information to execute the action. 

Basic Structure
- Command interface declares a method, e.g., execute().
- Concrete command holds a reference to the receiver and implements the action by calling methods on the receiver.
- Receiver is an object that performs the actual work.
- Invoker is the object that triggers the execution of the command.
- Client creates command objects, sets the receivers, and assigns commands to the invoker.
"""

import os
from typing import List
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class FileSystem:
    def create_file(self, filename: str, content=""):
        with open(filename, "w") as f:
            f.write(content)
        print(f"File {filename} created with content: {content}")

    def file_exists(self, filename: str):
        return os.path.exists(filename)

    def delete_file(self, filename: str):
        if self.file_exists(filename):
            os.remove(filename)
            print(f"File {filename} deleted")
        else:
            print(f"File {filename} does not exist")

    def rename_file(self, old_name: str, new_name: str):
        if self.file_exists(old_name):
            os.rename(old_name, new_name)
            print(f"File renamed from {old_name} to {new_name}")
        else:
            print(f"File {old_name} does not exist")

    def read_file(self, filename: str):
        if self.file_exists(filename):
            with open(filename, "r") as f:
                return f.read()
        return None


class CreateFileCommand(Command):
    def __init__(self, fs: FileSystem, filename: str, content=""):
        self.fs = fs
        self.filename = filename
        self.content = content

    def execute(self):
        self.fs.create_file(self.filename, self.content)

    def undo(self):
        self.fs.delete_file(self.filename)


class DeleteFileCommand(Command):
    def __init__(self, fs: FileSystem, filename: str):
        self.fs = fs
        self.filename = filename
        self.content = None

    def execute(self):
        if self.fs.file_exists(self.filename):
            self.content = self.fs.read_file(self.filename)
            self.fs.delete_file(self.filename)
        else:
            print(f"File {self.filename} does not exist, cannot delete")

    def undo(self):
        if self.content:
            self.fs.create_file(self.filename, self.content)
        else:
            print(f"Undo delete operation not possible")


class RenameFileCommand(Command):
    def __init__(self, fs: FileSystem, old_name, new_name):
        self.fs = fs
        self.old_name = old_name
        self.new_name = new_name

    def execute(self):
        self.fs.rename_file(self.old_name, self.new_name)

    def undo(self):
        self.fs.rename_file(self.new_name, self.old_name)


class FileManager:
    def __init__(self):
        self.undo_stack: List[Command] = []
        self.redo_stack: List[Command] = []

    def execute_command(self, command: Command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            self.redo_stack.append(command)
        else:
            print("No commands to undo")

    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.undo_stack.append(command)
        else:
            print("No commands to redo")


if __name__ == "__main__":
    # Receiver
    fs = FileSystem()

    # Invoker
    manager = FileManager()

    # Create a file
    create_cmd = CreateFileCommand(fs, "example.txt", "Hello world!")
    manager.execute_command(create_cmd)

    # Rename a file
    rename_cmd = RenameFileCommand(fs, "example.txt", "renamed.txt")
    manager.execute_command(rename_cmd)

    manager.undo()
    manager.redo()

    # Delete a file
    delete_cmd = DeleteFileCommand(fs, "renamed.txt")
    manager.execute_command(delete_cmd)

    manager.undo()
