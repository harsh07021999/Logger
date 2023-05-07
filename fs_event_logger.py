from Event_Handler import logger_event_watcher

class Log_directory:
    def __init__(self,path):
        self.filepath = path

log_directory = Log_directory('./logs')

log_watcher = logger_event_watcher.Watcher()
log_watcher.run(log_directory.filepath)