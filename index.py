import json
import datetime
import cbpro
import os

def handler(event, context):

    c = cbpro.PublicClient()
    [(date, open_price, max_price, min_price, close_price, capitalization)] = c.get_product_historic_rates(product_id='BTC-EUR', start="2022-01-10T12:00:00",end="2022-01-10T12:10:00",granularity=3600)

    data = {
        'BTC_EUR' : close_price,
        'TABLE_NAME' : os.environ['TABLE_NAME']
    }

    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
