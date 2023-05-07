Log Moniter 

The following project has Three Components:
1. Log
2. Event_Handler
3. Client_Side

Log is the directory where the logs are being saved from server side and it currently has 2 parts:
Error
Info
for their respective types of log messages.

Event_Handler is the main Moniter where I have used to have a watcher from watchdog library in python that would watch for each event 
using observer along with a Handler which overrides the 'on_any_event' function inside 'FileSystemEventHandler' class for watchdog
so that based on the type of the event triggered we can send the event to kafka.
For kafka setup i have used docker compose method to run kafker server you can look for the documentation i followed at :-
https://developer.confluent.io/quickstart/kafka-docker/
Fot the above programe to run you have to setup the topics for every sub directory crreated in the logs file so that the messages can
sent to that particular topic .

Client_Side is the consumer side which would basically have consumers running at their own end with provided class interface a consumer
can keep listening to the particular topic it has been assigned.

The POC of the program is through 'fs_event_logger.py' file and Event_Handler execution takes place from here itself.
Install all the dependencies from requirements.txt.

Some of the documentation that i looked at are:-
https://kafka-python.readthedocs.io/en/master/
https://pythonhosted.org/watchdog/api.html#watchdog.events.FileSystemEventHandler
https://stackoverflow.com/questions/41146144/how-to-fix-assertionerror-value-must-be-bytes-error-in-python2-7-with-apache
https://docs.python.org/3/library/logging.html


The shortcoming of this implementations are :-
1. This a rushed implementation as there was an issue with my github setup on the machine i am working on due to multiple accounts 
hence a lot of time got wasted there.
2. The client side consumers are not implemented to its possible scale and can be improve by proper concurrent consumer implementations
3. The program relies on thread safety of kafka producers only and does not have thread safety implemented at its own level from Event_Handler's
end.
