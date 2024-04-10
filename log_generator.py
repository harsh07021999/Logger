import argparse
import json
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument("--num_logs", type=int, default=100)
parser.add_argument("--log_dir", type=str, default="log")
parser.add_argument("--generate", type=int, default=1)

def generate_logs(num_logs):
    log_list = list()
    for i in range(num_logs):
        log_list.append(generate_log(i))
    
    return log_list

def generate_log(i):
    log = {
        "id": i,
        "timestamp": int(time.time()),
        "message": f"Log {i}",
        "level": "INFO",
    }
    return log

if __name__ == "__main__":

    num_logs = parser.parse_args().num_logs
    log_dir = parser.parse_args().log_dir
    generate = parser.parse_args().generate
    if generate == 1:
        log_list = generate_logs(num_logs)  
        for i, log in enumerate(log_list):
            with open(f"log/{i}.json", "w") as f:
                json.dump(log, f)
    else:
        # read logs from log_dir and print the number of logs present
        num_of_logs = 0
        for i, log in enumerate(os.listdir(log_dir)):
            with open(f"log/{log}", "r") as f:
                log = json.load(f)
                num_of_logs += 1
        print(((num_of_logs/num_logs) * 100),"% recieved logs") 
