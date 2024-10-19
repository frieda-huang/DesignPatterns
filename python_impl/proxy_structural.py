"""
Proxy structural pattern provides a surrogate or placeholder for another object to control access to it.

Basic Structure
- Subject Interface
- Real Subject
- Proxy
"""

import time
from abc import ABC, abstractmethod


class ApiService(ABC):
    @abstractmethod
    def request(self, user_id):
        pass


class RealApiService(ApiService):
    def request(self, user_id):
        print(f"Processing request for user {user_id}")


class RateLimiterProxy(ApiService):
    def __init__(self, real_service: RealApiService):
        self.real_service = real_service
        self.user_requests = {}
        self.request_limit = 5
        self.time_window = 60

    def request(self, user_id):
        current_time = time.time()

        if user_id not in self.user_requests:
            self.user_requests[user_id] = []

        self.user_requests[user_id] = [
            t
            for t in self.user_requests[user_id]
            if current_time - t <= self.time_window
        ]

        if len(self.user_requests[user_id]) < self.request_limit:
            self.user_requests[user_id].append(current_time)
            self.real_service.request(user_id)
        else:
            print(f"Rate limit exceeded for user {user_id}. Please try again later.")


if __name__ == "__main__":
    real_service = RealApiService()

    proxy_service = RateLimiterProxy(real_service)

    user_id = "user_123"

    for i in range(7):
        print(f"Request {i+1} from {user_id}")
        proxy_service.request(user_id)
        time.sleep(10)
