# 

import pika
import json
params = pika.URLParameters('amqps://tfslghdt:cPW1J-CcD5AjmvnZgSxt-66XEbCvjMh7@beaver.rmq.cloudamqp.com/tfslghdt')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    property = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=property)