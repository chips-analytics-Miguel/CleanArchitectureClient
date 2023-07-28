from src.interfaces.abstract_unit_of_work import AbstractUnitOfWork
from src.adapters.mongoadapter import MongoDBAdapter
from src.config import settings

class MongoUnitOfWork(AbstractUnitOfWork):
    def __init__(self) -> None:
        self.repository = MongoDBAdapter(mongo_uri=settings.MONGO_URI)
        self.new_events = []
       

    def commit(self):
        self.repository.commit()

    def rollback(self):
        self.repository.rollback()

    def collect_new_events(self):
        # Renvoie la liste des nouveaux événements collectés et les réinitialise
        new_events = self.new_events
        self.new_events = []
        return new_events
    def add_new_event(self, event):
        # Ajoute un nouvel événement à la liste des événements collectés
        self.new_events.append(event)
    