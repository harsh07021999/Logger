from kafka import KafkaProducer

class Producer:
    
    def __init__(self):
        self.log_producer = KafkaProducer()
    
    def send_msg(self,topic,msg):
        self.log_producer.send(topic,msg.encode('utf-8'))

