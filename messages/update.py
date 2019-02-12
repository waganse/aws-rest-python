import json
import time
import logging
import os

from messages import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def update(event, context):
    data = json.loads(event['body'])
    if 'text' not in data or 'available' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # update the todo in the database
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeNames={
          '#symbol': 'symbol',
          '#ja': 'ja',
          '#en': 'en',
          '#zhCN': 'zhCN',
          '#ko': 'ko',
          '#fr': 'fr',
          '#tl': 'tl',
          '#en029': 'en029',
          '#enGB': 'enGB',
          '#description': 'description',
          '#page': 'page',
        },
        ExpressionAttributeValues={
          ':symbol': data['symbol'],
          ':ja': data['ja'],
          ':en': data['en'],
          ':zhCN': data['zhCN'],
          ':ko': data['ko'],
          ':fr': data['fr'],
          ':tl': data['tl'],
          ':en029': data['en029'],
          ':enGB': data['enGB'],
          ':description': data['description'],
          ':page': data['page'],
          ':available': data['available'],
          ':updatedAt': timestamp,
        },
        UpdateExpression='SET #symbol = :symbol, '
                         '#ja = :ja, '
                         '#en = :en, '
                         '#zhCN = :zhCN, '
                         '#ko = :ko, '
                         '#fr = :fr, '
                         '#tl = :tl, '
                         '#en029 = :en029, '
                         '#enGB = :enGB, '
                         '#description = :description, '
                         '#page = :page, '
                         'available = :available, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
