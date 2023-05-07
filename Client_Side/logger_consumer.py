from kafka import KafkaConsumer

class Consumer:

    def __init__(self,topic):
        self.log_consumer = KafkaConsumer(topic)

    def show_msg(self):
        for msg in self.log_consumer:
            print(msg)

s = Consumer('info')
s.show_msg()