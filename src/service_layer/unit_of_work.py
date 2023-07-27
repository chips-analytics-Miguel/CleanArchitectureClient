from src.interfaces.abstract_unit_of_work import AbstractUnitOfWork
from src.adapters.mongoadapter import MongoDBAdapter
from src.config import settings

class MongoUnitOfWork(AbstractUnitOfWork):
    def __init__(self) -> None:
        self.repository = MongoDBAdapter(mongo_uri=settings.MONGO_URI)

    def commit(self):
        self.repository.commit()

    def rollback(self):
        self.repository.rollback()

    def collect_new_events(self):
        return []
    