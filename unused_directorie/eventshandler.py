from src.domain.events import Event
from confluent_kafka import Producer
from src.adapters.eventpublisher import Eventpublisher

#producer = Producer({'bootstrap.servers': 'localhost:9092'})
class EventHandler(Event):
    """Event Handler for events emitted"""

    def PatientCreated(self,event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        Eventpublisher().publish(self.event_type, self.event_data)
        

    def PatientDeleted(self,event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        Eventpublisher().publish(self.event_type, self.event_data)
        
    

    def PatientContactAdded(self,event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        Eventpublisher().publish(self.event_type, self.event_data)
        
    
    def PatientContactRemoved(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        Eventpublisher().publish(self.event_type, self.event_data)
        

    def PatientNameChanged(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        Eventpublisher().publish(self.event_type, self.event_data)
       
    
    def PatientActivated(self,event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        Eventpublisher().publish(self.event_type, self.event_data)
        

    def PatientDeactivated(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        Eventpublisher().publish(self.event_type, self.event_data)
        

    def PatientGenderChanged(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        Eventpublisher().publish(self.event_type, self.event_data)
        
    
    def PatientBirthdayChanged(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        Eventpublisher().publish(self.event_type, self.event_data)
        
