from src.domain.events import Event
from confluent_kafka import Producer
from src.adapters.kafka.producer import delivery_report

#producer = Producer({'bootstrap.servers': 'localhost:9092'})
class EventHandler(Event):
    """Event Handler for events emitted"""

    def PatientCreated(self,event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        #producer.produce(self.event_type, str(self.event_data).encode('utf-8'), callback=delivery_report)
        #producer.flush() 

    def PatientDeleted(self,event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        #producer.produce(self.event_type, str(self.event_data).encode('utf-8'), callback=delivery_report)
        #producer.flush() 
    

    def PatientContactAdded(self,event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        #producer.produce(self.event_type, str(self.event_data).encode('utf-8'), callback=delivery_report)
        #producer.flush()
    
    def PatientContactRemoved(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        #producer.produce(self.event_type, str(self.event_data).encode('utf-8'), callback=delivery_report)
        #producer.flush()

    def PatientNameChanged(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        #producer.produce(self.event_type, str(self.event_data).encode('utf-8'), callback=delivery_report)
        #producer.flush()
    
    def PatientActivated(self,event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        #producer.produce(self.event_type, str(self.event_data).encode('utf-8'), callback=delivery_report)
        #producer.flush()

    def PatientDeactivated(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        #producer.produce(self.event_type, str(self.event_data).encode('utf-8'), callback=delivery_report)
        #producer.flush()

    def PatientGenderChanged(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        #producer.produce(self.event_type, str(self.event_data).encode('utf-8'), callback=delivery_report)
        #producer.flush()
    
    def PatientBirthdayChanged(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data
        #producer.produce(self.event_type, str(self.event_data).encode('utf-8'), callback=delivery_report)
        #producer.flush()
