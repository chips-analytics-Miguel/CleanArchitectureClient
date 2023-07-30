from typing import Callable, Dict, List, Type,Union
from src.domain import commands
from src.domain import  events
from src.service_layer.unit_of_work import MongoUnitOfWork

Message = Union[commands.Command ,events.Event]


class MessageBus:
    def __init__(
        self,
        uow: MongoUnitOfWork,
        event_handlers: Dict[Type[events.Event], List[Callable]],
        command_handlers: Dict[Type[commands.Command], Callable],
    ):
        self.uow = uow
        self.event_handlers = event_handlers
        self.command_handlers = command_handlers

    def handle(self, message: Message):
        self.queue = [message]
        
        while self.queue:
            message = self.queue.pop(0)
            if isinstance(message, events.Event):
               self.handle_event(message)
               
               
            elif isinstance(message, commands.Command):
                result=self.handle_command(message)
                print("handle", result)
                return result
            else:
                raise Exception(f"{message} was not an Event or Command")

    def handle_event(self, event: events.Event):
        for handler in self.event_handlers[type(event)]:
            try:
                handler(event)
                self.queue.extend(self.uow.collect_new_events())
            except Exception:
                # Gérer les exceptions et les erreurs ici
                continue

    def handle_command(self, command: commands.Command):
        try:
            handler = self.command_handlers[type(command)]
            result =handler(command) 
            print("handle command", result)
            self.queue.extend(self.uow.collect_new_events())
            return result
        except Exception:
            # Gérer les exceptions et les erreurs ici
            raise
   