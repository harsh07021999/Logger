import os
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
#from kafka import KafkaProducer
from Kafka_Producer import producer

class Watcher:
    def __init__(self):
        self.observer = Observer()
  
    def run(self,Log_directory):
        event_handler = Handler()
        self.observer.schedule(event_handler, Log_directory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
        self.observer.join()

class Handler(FileSystemEventHandler):
  
    @staticmethod
    def on_any_event(event):
        log_producer  = producer.Producer()
        if event.is_directory:
            return None
  
        elif event.event_type == 'created':
            print("Received created event - % s." % event.src_path)
            msg = "Received created event - % s." % event.src_path
            print(event.src_path.replace(os.path.dirname(os.path.abspath('.')),'').split('\\'))
            topic = event.src_path.replace(os.path.dirname(os.path.abspath('.')),'').split('\\')[2]
            log_producer.send(topic,msg.encode('utf-8'))

        elif event.event_type == 'modified':
            print("Received modified event - % s." % event.src_path)
            msg = "Received modified event - % s." % event.src_path
            topic = event.src_path.replace(os.path.dirname(os.path.abspath('.')),'').split('/')[3]
            log_producer.send_msg(topic,msg)
