"""
State behavioral pattern allows an object to change its behavior
when its internal state changes. It is used to encapsulate the
varying behavior of an object based on its state.

Basic Structure
- Context maintains a reference to a state object representing its current state
- State interface
- Concrete state classes
"""

from abc import ABC, abstractmethod


class ElevatorState(ABC):
    @abstractmethod
    def request_floor(self, elevator, floor):
        pass

    @abstractmethod
    def open_doors(self, elevator):
        pass

    @abstractmethod
    def close_doors(self, elevator):
        pass

    @abstractmethod
    def move(self, elevator):
        pass


class Elevator:
    def __init__(self) -> None:
        self.current_floor = 0
        self.requested_floor = None
        self.state = IdleState()

    def set_state(self, state):
        self.state = state

    def request_floor(self, floor):
        self.state.request_floor(self, floor)

    def open_doors(self):
        self.state.open_doors(self)

    def close_doors(self):
        self.state.close_doors(self)

    def move(self):
        self.state.move(self)


class IdleState(ElevatorState):
    def request_floor(self, elevator: Elevator, floor):
        print(f"Requesting floor {floor} from idle state.")
        if floor > elevator.current_floor:
            elevator.set_state(MovingUpState())
        elif floor < elevator.current_floor:
            elevator.set_state(MovingDownState())
        elevator.requested_floor = floor
        elevator.move()

    def open_doors(self, elevator: Elevator):
        print(f"Doors are opening.")
        elevator.set_state(DoorsOpenState())

    def close_doors(self, elevator: Elevator):
        print("Cannot close doors, they are already closed.")

    def move(self, elevator: Elevator):
        print("Elevator is idle, waiting for floor request.")


class DoorsOpenState(ElevatorState):
    def request_floor(self, elevator: Elevator, floor):
        print("Cannot request a floor while doors are open.")

    def open_doors(self, elevator: Elevator):
        print(f"Doors are already open.")

    def close_doors(self, elevator: Elevator):
        print(f"Doors are now closed.")
        elevator.set_state(IdleState())

    def move(self, elevator: Elevator):
        print(f"Elevator cannot move while the doors are open.")


class MovingUpState(ElevatorState):
    def request_floor(self, elevator: Elevator, floor):
        print(f"Already moving up, cannot change destination to floor {floor}.")

    def open_doors(self, elevator: Elevator):
        print(f"Cannot open doors while moving.")

    def close_doors(self, elevator: Elevator):
        print(f"Doors are already closed.")

    def move(self, elevator: Elevator):
        print(f"Moving up to floor {elevator.requested_floor}.")
        elevator.current_floor = elevator.requested_floor
        elevator.set_state(IdleState())
        elevator.open_doors()


class MovingDownState(ElevatorState):
    def request_floor(self, elevator: Elevator, floor):
        print(f"Already moving down, cannot change destination to floor {floor}.")

    def open_doors(self, elevator: Elevator):
        print(f"Cannot open doors while moving.")

    def close_doors(self, elevator: Elevator):
        print(f"Doors are already closed.")

    def move(self, elevator: Elevator):
        print(f"Moving down to floor {elevator.requested_floor}.")
        elevator.current_floor = elevator.requested_floor
        elevator.set_state(IdleState())
        elevator.open_doors()


if __name__ == "__main__":
    elevator = Elevator()
    elevator.request_floor(3)
    elevator.close_doors()
    elevator.request_floor(1)
    elevator.close_doors()
