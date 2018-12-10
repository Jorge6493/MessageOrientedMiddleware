import pika
import sys
import threading

def Send(msg):
    # print("msg")
    # print(msg)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs',
                            exchange_type='fanout')
    message = msg                        
    if msg != '':
        channel.basic_publish(exchange='logs',
                            routing_key='',
                            body=message)
        print("Sent %r" % message)
    connection.close()

def Receive():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs',
                            exchange_type='fanout')

    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='logs',
                    queue=queue_name)

    print('Waiting for messages')

    channel.queue_declare(queue='hello')

    # def callback(ch, method, properties, body):
    #     print(" [x] %r" % body)

    def callbackhello(ch, method, properties, body):
        Send(body)
        # print(" [c] %r" % body)

    # channel.basic_consume(callback,
    #                     queue=queue_name,
    #                     no_ack=True)

    channel.basic_consume(callbackhello,
                        queue='hello',
                        no_ack=True)

    channel.start_consuming()

# send_thread = threading.Thread(target=Send(""))
receive_thread = threading.Thread(target=Receive)

# send_thread.start()
receive_thread.start()

# send_thread.join()
receive_thread.join()