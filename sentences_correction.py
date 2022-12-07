#!/usr/bin/python3
import time
import requests
from datetime import datetime
import concurrent.futures
import sys
import logging
from uuid import uuid4
import pandas as pd

API_URL = f'{sys.argv[1]}'
REQUEST_ROUTE = '/correct'
ENDPOINT = API_URL + REQUEST_ROUTE
MAX_THREADS = 1024
HEADERS = {'Content-Type': 'application/json'}
df = pd.DataFrame(columns=['sent', 'received', 'received_time', 'latency', 'status_code'])

logging.basicConfig(
    filename=f'client-simulation-iter_{sys.argv[2]}-{int(datetime.now().timestamp())}.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w',
    level = logging.INFO
)

log = logging.getLogger()

def send_api_request(sentence):
    global ENDPOINT
    global HEADERS
    global df

    r = requests.post(ENDPOINT, headers=HEADERS, data='{"sentence": '+ f'"{sentence}"' + '}')

    df = df.append(dict(zip(df.columns,[sentence, r.text, datetime.now().timestamp(), r.elapsed, r.status_code])))

if __name__ == '__main__':
    log.info('============== Starting GECToR load simulation! ==============')
    init_time = datetime.now()

    for i in range(11):
        df.drop(df.index, inplace=True)
        n_sentences = 2**i

        input_path = f'./data/conll/iter_{sys.argv[2]}/official-2014.{n_sentences}-sentences.combined.src'
        with open(input_path, 'r', encoding='utf-8') as f:
            sentence_list = f.read().splitlines()

        log.info('\n========================= New load ==========================')
        log.info(f'Running for: {len(sentence_list)} sentences\n')

        with concurrent.futures.ThreadPoolExecutor(MAX_THREADS) as executor:
            executor.map(send_api_request, sentence_list)

        df.to_csv(f'client-simulation-iter_{sys.argv[2]}-{n_sentences}.csv')
        time.sleep(5)

    end_time = datetime.now()

    log.info('=============== Ending GECToR load simulation! ===============')
    log.info(f'Simulation duration: {end_time - init_time}')
