#!/usr/bin/python3.8
import time
import requests
from datetime import datetime
import concurrent.futures
import sys

API_URL = f'{sys.argv[1]}'
REQUEST_ROUTE = '/correct'
ENDPOINT = API_URL + REQUEST_ROUTE
MAX_THREADS = 1024

def send_api_request(sentence):
    r = requests.get(ENDPOINT, data={'sentence': sentence})
    print(f'Received ({datetime.now()}): {r.content}')


if __name__ == '__main__':
    print ('Starting:', datetime.now())

    for i in range(11):
        n_sentences = 2**i
        input_path = f'./data/conll/iter_{sys.argv[2]}/official-2014.{n_sentences}-sentences.combined.src'

        with open(input_path, 'r', encoding='utf-8') as f:
            sentence_list = f.read().splitlines()

        print('\n######### NEW_BATCH #########')
        print('Running for:', len(sentence_list),'(sentences)\n')
        with concurrent.futures.ThreadPoolExecutor(MAX_THREADS) as executor:
            executor.map(send_api_request, sentence_list)

        time.sleep(5)

    print('\nEnd time:', datetime.now())
