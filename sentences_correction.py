#!/usr/bin/python3.8
import time
import requests
import datetime
import concurrent.futures
import sys

HOST = 'https://local-scenario'
API_PATH = '/correct'
ENDPOINT = HOST + API_PATH
MAX_THREADS = 1024

def send_api_request(sentence):
    r = requests.get(ENDPOINT, data={'sentence': sentence})
    print ('Received: ', datetime.datetime.now(), r.content)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    print ('Starting:', start_time)

    for i in range(11):
        n_sentences = 2**i
        input_path = f'./data/conll/iter_{sys.argv[1]}/official-2014.{n_sentences}-sentences.combined.src'

        with open(input_path, 'r', encoding='utf-8') as f:
            sentence_list = f.read().splitlines()

        print('\n######### NEW_BATCH #########')
        print('Running for:', len(sentence_list),'(sentences)\n')
        with concurrent.futures.ThreadPoolExecutor(MAX_THREADS) as executor:
            futures = [ executor.submit(send_api_request(s)) for s in sentence_list ]
        
        time.sleep(5)

    print('\nEnd time:', datetime.datetime.now())
