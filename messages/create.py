import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'symbol': data['symbol'],
        'ja': data['ja'],
        'en': data['en'],
        'zhCN': data['zhCN'],
        'ko': data['ko'],
        'fr': data['fr'],
        'tl': data['tl'],
        'en029': data['en029'],
        'enGB': data['enGB'],
        'description': data['description'],
        'page': data['page'],
        'valid': TRUE,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
