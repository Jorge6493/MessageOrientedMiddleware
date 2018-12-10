# Sistemas Operativos 2 - Proyecto 2

Repositorio para entregable del proyecto 2

### Estudiantes
- Franz Pichardo R. 2015-6315
- Jorge Ramos 2013-7102

### Instrucciones
*Para correr el servidor:*
- server.py

*Para correr el cliente ejemplo:*
- client.py

### Requerimientos
- [Python 3](https://www.python.org/downloads/release/python-371/)
- [Pika lib](https://pika.readthedocs.io/en/latest/index.html)
- [Erlang/OTP](http://www.erlang.org/downloads)
- [RabbitMQ](https://www.rabbitmq.com/download.html)

### Explicaciones
*Explicación del cliente para usuario:*
- El cliente debe tener una funcion de Send, que cree la conexión en el canal del servidor por medio de la libreria Pika de RabbitMQ.
- Luego se declara el canal con queue_declare(queue='nombre del queue')
- Se declara un while True para poder recibir input indefinidamente, y desde este mismo se hace un basic_publish en el canal, enviando la informacion del input. Se cierra la conexión al final.
- Para recibir mensajes se hace la misma conexión y se declara en el canal que se hara el exchange de información. Se debe utilizar el exchange_type fanout para que la información se comparta en todos los clientes.
- Se declara el canal/queue exlusive=true para borrar el queue luego de cerrar la conexión.
- Hay que hacer un basic_consume para consumir el mensaje que envia el queue.
- Basado en el consume se ejecuta callback cuando llegue un mensaje.