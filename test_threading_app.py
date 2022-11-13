from datetime import datetime
from time import sleep

def lambda_handler(event, context):
    sleep(2)

    return {
        'statusCode': 200,
        'body': {
            'msg': 'OK!',
            'datetime': datetime.now().isoformat()
        }
    }
