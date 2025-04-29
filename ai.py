import openai
import json
from colorama import init, Fore
from dotenv import load_dotenv, dotenv_values
import os
import time
import random

load_dotenv() 
client = openai.OpenAI(api_key=os.getenv("OPENAI_KEY"))

# get fancy colors
init(autoreset=True)


def process_log_line(line):
    if not line:
        return




    # simulate ai response
    if random.randint(0, 1) == 0:
        response = "SQL Injection"
    else:
        response = "No Attack"
    response = client.responses.create(
        model="gpt-4o-mini",
        
        input=[
            {
                "role": "developer",
                "content": ("Classify the log line with one of the following: 'No Attack', "
                "'SQL Injection', 'Path Traversal', 'Code Injection', 'File Inclusion', 'LDAP Injection'."
                "Only respond with the classification, nothing else.")
            },
            {
                "role": "user",
                "content": f"Log Line: {line}"
            }
        ]
    )

    response = response.output_text

    if response == "No Attack":
        print(f"{Fore.GREEN}AI has determined that there is no attack.")
    else:
        print(f"{Fore.RED}Warning, AI has detected a {response} attack! Log trace: {line}")

def log_analysis(log_file):
    with open(log_file, "r") as f:
        f.seek(0, os.SEEK_END)
        print(f"{Fore.YELLOW}Monitoring log file for new entries...\n")
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            process_log_line(line)


if __name__ == '__main__':
    log_file = "requests.log"
    log_analysis(log_file)