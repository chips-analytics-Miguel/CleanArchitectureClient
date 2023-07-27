from abc import ABC, abstractmethod
from typing import List, Dict


class AbstractUnitOfWork(ABC):
   
    def __enter__(self) -> "AbstractUnitOfWork":
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

    @abstractmethod
    def collect_new_events(self):
        pass
