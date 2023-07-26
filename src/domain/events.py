from abc import ABC, abstractmethod
from typing import Dict
from pydantic import BaseModel


class Event(ABC):
    """Event class for events"""
    event_type : str
    event_data : Dict[str,dict] 

    @abstractmethod
    def PatientCreated(event_type, event_data):
        pass

    @abstractmethod
    def PatientDeleted(event_type, event_data):
        pass
   
    @abstractmethod
    def PatientContactAdded(event_type, event_data):
        pass

    @abstractmethod
    def PatientContactRemoved(event_type, event_data):
        pass
    
    @abstractmethod
    def PatientNameChanged(event_type, event_data):
        pass
    @abstractmethod
    def PatientActivated(event_type, event_data):
        pass

    @abstractmethod
    def PatientDeactivated(event_type, event_data):
        pass
    
    @abstractmethod
    def PatientGenderChanged(event_type, event_data):
        pass

    @abstractmethod
    def PatientBirthdayChanged(event_type, event_data):
        pass
