import requests
import argparse
import pandas as pd

def request_to_prometheus(url, query, start, end, step):
    params = {
        'query': query,
        'start': start,
        'end': end,
        'step': step
    }

    r = requests.get(f'{url}/api/v1/query_range', params=params).json()
    return r['data']['result'][0]['values']


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--url',
        help='Prometheus server URL.',
        required=True)
    parser.add_argument(
        '--query',
        help='Prometheus query.',
        required=True)
    parser.add_argument(
        '--start',
        help='Path to the model file.',
        required=True)
    parser.add_argument(
        '--end',
        help='End time timestamp.',
        required=True)
    parser.add_argument(
        '--step',
        help='Query step.',
        required=True)
    parser.add_argument(
        '--metric_title',
        help='Name metric to table.',
        required=True)


    args = parser.parse_args()
    data = request_to_prometheus(
        url=args.url,
        query=args.query,
        start=args.start,
        end=args.end,
        step=args.step
    )
    print(data)

    df = pd.DataFrame(data, columns=['timestamp', args.metric_title])
    df.to_csv(f'{args.metric_title}-{args.start}-{args.end}.csv', index=False)
