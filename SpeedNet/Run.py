from threading  import Thread
from os import popen,system
from time import sleep
from tqdm import tqdm
from progress.bar import Bar
from random import randint
mode = ''
def netowork():
    global mode
    result = popen('speedtest-cli')
    string = result.read()
    ip = string[string.find('from'):string.find(')')]
    host = string[string.find('Hosted'):string.find('ms')]
    Download = string[string.find('Download'):string.find('Mbit/s')+len('Mbit/s')]
    Upload = string[string.find('Upload'):]
    mode = 'ok'
    sleep(10)
    print(ip)
    print(host)
    print(Download)
    print(Upload)
    input('Enter To Close Window')
    

t = Thread(target=netowork)
t.start()
while True:
    bar = Bar('Run Test Networks', max = 100)
    for i in range(100):
        bar.next()
        s = f'0.{randint(1, 2)}'
        sleep(float(s))
    system('cls')
    bar.finish()
    if mode == 'ok':
        print('Done Test!')
        break



        
