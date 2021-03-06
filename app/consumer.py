import pika
import json
params = pika.URLParameters('amqps://tfslghdt:cPW1J-CcD5AjmvnZgSxt-66XEbCvjMh7@beaver.rmq.cloudamqp.com/tfslghdt')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(data)
    
channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()

channel.close()