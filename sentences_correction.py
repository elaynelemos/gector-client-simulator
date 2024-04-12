import time
import requests
from datetime import datetime
import concurrent.futures
import sys
import logging
import pandas as pd

API_URL = f'{sys.argv[1]}'
REQUEST_ROUTE = '/correct'
ENDPOINT = API_URL + REQUEST_ROUTE
MAX_THREADS = 512
HEADERS = {'Content-Type': 'application/json'}
DF_COLUMNS = ['sent', 'received', 'received_time', 'latency', 'status_code']

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
    global DF_COLUMNS

    try:
        r = requests.post(ENDPOINT, headers=HEADERS, data='{"sentence": '+ f'"{sentence}"' + '}')
    except:
        return dict(zip(DF_COLUMNS, [sentence, '', int(datetime.now().timestamp()), 60, 504]))
    return dict(zip(DF_COLUMNS, [sentence, r.text, int(datetime.now().timestamp()), r.elapsed.total_seconds(), r.status_code]))

if __name__ == '__main__':
    log.info('======= Starting GECToR load simulation! =======')
    init_time = datetime.now()

    for i in range(10):
        results = []
        n_sentences = 2**i

        input_path = f'./data/conll/iter_{sys.argv[2]}/official-2014.{n_sentences}-sentences.combined.src'
        with open(input_path, 'r', encoding='utf-8') as f:
            sentence_list = f.read().splitlines()

        log.info(f'Running for: {len(sentence_list)} sentences\n')
        with concurrent.futures.ThreadPoolExecutor(MAX_THREADS) as executor:
            results = executor.map(send_api_request, sentence_list)

        df = pd.DataFrame(results, columns=DF_COLUMNS)
        df['sent'] = df['sent'].str.replace('\n', '\\n', regex=True)
        df['received'] = df['received'].str.replace('\n', '\\n', regex=True)

        df.to_csv(f'client-simulation-iter_{sys.argv[2]}-{n_sentences}.csv', index=False, sep="#")

        time.sleep(5)

    end_time = datetime.now()

    log.info('======= Ending GECToR load simulation! =======')
    log.info(f'Simulation duration: {end_time - init_time}')
