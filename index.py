import json
import datetime
import cbpro
import os

def getProductLastPrice(pubc: cbpro.PublicClient, productID):
    stat24 = pubc.get_product_24hr_stats(productID)
    return stat24['last']

def handler(event, context):

    c = cbpro.PublicClient()
    last_price = getProductLastPrice(c, "BTC-EUR")

    data = {
        'BTC_EUR' : last_price,
        'TABLE_NAME' : os.environ['TABLE_NAME']
    }

    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
