"""
Adapter structural pattern allows two incompatible interfaces to work together. 
It acts as a bridge between two objects that couldn’t otherwise communicate 
due to differences in their interfaces.

Basic Structure
- Client
- Target interface is the interface that the client expects
- Adaptee is the existing class that has an incompatible interface
- Adapter implements the target interface and translates the requests from the client to the adaptee
"""


class EuropeanSocket:
    def provide_220v(self):
        return "Providing 220V"


class AmericanSocket:
    def provide_110v(self):
        pass


class SocketAdapter(AmericanSocket):
    def __init__(self, european_socket: EuropeanSocket):
        self.european_socket = european_socket

    def provide_110v(self):
        voltage = self.european_socket.provide_220v()
        print(f"{voltage} - Converting to 110V")
        return "Providing 110V"


def charge_device(socket: AmericanSocket):
    print(socket.provide_110v())


if __name__ == "__main__":
    european_socket = EuropeanSocket()

    adapter = SocketAdapter(european_socket)

    charge_device(adapter)
