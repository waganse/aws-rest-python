import json
import logging
import os
import time
import uuid
import decimal
import pandas as pd
import boto3

from decimal import *

dynamodb = boto3.resource('dynamodb')


def upload(event, context):
    request = event['body']
    base64String = request['base64String']

    buffer = base64.decodestring(base64String)

    initial_df = pd.read_csv(buffer)

    print(initial_df)

    # timestamp = int(time.time() * 1000)

    # table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # item = {
    #     'id': str(uuid.uuid1()),
    #     'symbol': data['symbol'],
    #     'ja': data['ja'],
    #     'en': data['en'],
    #     'zhCN': data['zhCN'],
    #     'ko': data['ko'],
    #     'fr': data['fr'],
    #     'tl': data['tl'],
    #     'en029': data['en029'],
    #     'enGB': data['enGB'],
    #     'description': data['description'],
    #     'page': data['page'],
    #     'available': data['available'],
    #     'createdAt': timestamp,
    #     'updatedAt': timestamp,
    # }

    # # write the todo to the database
    # table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": "{}"
    }

    return response
