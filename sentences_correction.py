#!/usr/bin/python3
import time
import requests
from datetime import datetime
import concurrent.futures
import sys
import logging
from uuid import uuid4

API_URL = f'{sys.argv[1]}'
REQUEST_ROUTE = '/correct'
ENDPOINT = API_URL + REQUEST_ROUTE
MAX_THREADS = 1024
HEADERS = {'Content-Type': 'application/json'}

logging.basicConfig(
    filename=f'client-simulation-iter_{sys.argv[2]}-{datetime.timestamp(datetime.now())}.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w',
    level = logging.INFO
)

log = logging.getLogger()

def send_api_request(sentence, id):
    global ENDPOINT
    global HEADERS

    log.info(f'[SENT][{id}] {sentence}')
    r = requests.post(ENDPOINT, headers=HEADERS, data='{"sentence": '+ f'"{sentence}"' + '}')
    log.info(f'[RECEIVED][{id}] {r.text}')

if __name__ == '__main__':
    log.info('============== Starting GECToR load simulation! ==============')

    for i in range(11):
        n_sentences = 2**i
        uuids = [ str(uuid4()).replace("-", "") for _ in range(n_sentences) ]

        input_path = f'./data/conll/iter_{sys.argv[2]}/official-2014.{n_sentences}-sentences.combined.src'
        with open(input_path, 'r', encoding='utf-8') as f:
            sentence_list = f.read().splitlines()

        log.info('\n========================= New load ==========================')
        log.info(f'Running for: {len(sentence_list)} sentences\n')

        with concurrent.futures.ThreadPoolExecutor(MAX_THREADS) as executor:
            executor.map(send_api_request, sentence_list, uuids)

        time.sleep(5)

    log.info('=============== Ending GECToR load simulation! ===============')
