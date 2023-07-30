from abc import ABC
from abc import abstractmethod

class Service(ABC):
    @abstractmethod
    def needs_service(self):
        pass