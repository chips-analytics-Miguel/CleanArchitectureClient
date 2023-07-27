from typing import List, Dict
from allocation.domain.model import Product
from allocation.adapters.repository import AbstractRepository
from allocation.adapters.notifications import AbstractNotifications


class AbstractUnitOfWork:
    products: AbstractRepository[Product]

    def __enter__(self) -> "AbstractUnitOfWork":
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        pass

    def rollback(self):
        pass

    def collect_new_events(self):
        pass


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session) -> None:
        self.session = session
        self.products = SqlAlchemyProductRepository(session)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def collect_new_events(self):
        return []


class MongoUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session) -> None:
        self.session = session
        self.products = MongoProductRepository(session)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def collect_new_events(self):
        return []


class RedisUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session, notifications: AbstractNotifications) -> None:
        self.session = session
        self.notifications = notifications
        self.products = RedisProductRepository(session)

    def commit(self):
        self.session.commit()
        self.notifications.publish()

    def rollback(self):
        self.session.rollback()

    def collect_new_events(self):
        return self.notifications.pop_events()
