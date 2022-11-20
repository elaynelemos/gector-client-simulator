#!/usr/bin/python3
import time
import requests
from datetime import datetime
import concurrent.futures
import sys
import logging

API_URL = f'{sys.argv[1]}'
REQUEST_ROUTE = '/correct'
ENDPOINT = API_URL + REQUEST_ROUTE
MAX_THREADS = 1024
HEADERS = {'Content-Type': 'application/json'}


def send_api_request(sentence):
    print(f'Sent ({datetime.now()}): {sentence}')
    r = requests.post(ENDPOINT, headers=HEADERS, data='{"sentence": '+ f'"{sentence}"' + '}')
    print(f'Received ({datetime.now()}): {r.text}')

if __name__ == '__main__':
    print ('Starting:', datetime.now())

    for i in range(11):
        n_sentences = 2**i
        input_path = f'./data/conll/iter_{sys.argv[2]}/official-2014.{n_sentences}-sentences.combined.src'

        with open(input_path, 'r', encoding='utf-8') as f:
            sentence_list = f.read().splitlines()

        print('\n######### NEW_BATCH #########')
        print(f'Running for: {len(sentence_list)} sentences ({datetime.now()})\n')
        with concurrent.futures.ThreadPoolExecutor(MAX_THREADS) as executor:
            executor.map(send_api_request, sentence_list)

        time.sleep(5)

    print('\nEnd time:', datetime.now())
