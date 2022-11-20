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

logging.basicConfig(
    filename=f'client-simulation-{datetime.timestamp(datetime.now())}.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w',
    level = logging.INFO
)

log = logging.getLogger()

def send_api_request(sentence):
    global ENDPOINT
    global HEADERS

    log.info(f'[SENT] {sentence}')
    r = requests.post(ENDPOINT, headers=HEADERS, data='{"sentence": '+ f'"{sentence}"' + '}')
    log.info(f'[RECEIVED] {r.text}')

if __name__ == '__main__':
    log.info('============== Starting GECToR load simulation! ==============')

    for i in range(11):
        n_sentences = 2**i
        input_path = f'./data/conll/iter_{sys.argv[2]}/official-2014.{n_sentences}-sentences.combined.src'

        with open(input_path, 'r', encoding='utf-8') as f:
            sentence_list = f.read().splitlines()

        log.info('========================= New load ==========================')
        log.info(f'Running for: {len(sentence_list)} sentences\n')
        with concurrent.futures.ThreadPoolExecutor(MAX_THREADS) as executor:
            executor.map(send_api_request, sentence_list)

        time.sleep(5)

    log.info('=============== Ending GECToR load simulation! ===============')
