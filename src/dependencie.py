from src.service_layer.messageBus import MessageBus
from src.service_layer.handler import uow, event_handlers, command_handlers
from circuitbreaker import circuit, CircuitBreaker
import pybreaker
def get_message_bus() -> MessageBus:
    return MessageBus(uow, event_handlers=event_handlers, command_handlers=command_handlers)

def get_circuit_breaker() -> CircuitBreaker:
    breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)
    return breaker
