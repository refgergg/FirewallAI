import openai
import json
from colorama import init, Fore, Back, Style
from dotenv import load_dotenv, dotenv_values
import os
import time

load_dotenv() 
client = openai.OpenAI(api_key=os.getenv("OPENAI_KEY"))

# get fancy colors
init(autoreset=True)


def process_log_line(line):
    response = client.responses.create(
        model="gpt-4o",
        
        input=[
            {
                "role": "developer",
                "content": ("Classify the log line with one of the following: 'No Attack', "
                "'SQL Injection', 'Path Traversal', 'Code Injection'")
            },
            {
                "role": "user",
                "content": f"Log Line: {line}"
            }
        ]
    )

    print(f"{Fore.RED}Warning, AI has detected a {response} attack!")

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