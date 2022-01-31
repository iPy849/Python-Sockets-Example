# Reporte de los scripts

## General:
Se agregaron cambios en el servidor en los envios/recibos de mensajes del socket y se implementa la funcionalidad de mensajes directos. 

En cuanto al cliente, se restringe el uso de "@" en el nombre ya que este caracter se encuentra reservado para la funcionalidad de mensajes directos.

Se agrega un paquete "resources" para generar info comun entre el cliente y el servidor, de manera que ambos pueda acceder a este.

## Servidor:
*   **Al recibir un mensaje lo decodifica**, permitiendo trabajar el mensaje entrante com un string y usar todas la funciones que la clase str nos facilita
*   Se agrega la funcionalidad de **Mensaje directo**

    La funcionalidad "Mensaje directo" permite a un usuario enviar un mensaje a una persona deseada, de manera nadie puede ver ese mensaje (exculyendo a emisor y receptor del mensaje). 
    
    Para acceder a esta funcionalidad, se debe usar la syntaxis:
    ````
    @<username>:<message>
    ````
    Al accionar esta funcionalidad, se le provee un mensaje solamente a **\<username>** con el contenido **\<message>**

    En caso de seleccionar a un usuario no existente, se cancela la funcionalidad y se muestra un error en pantalla.
* Se modificaron las funciones de envios de mensajes para codificar la respuesta a lo hora del envio al socket.

## Cliente:
*   El nombre de usuario excluye el caracter "@" ya que este caracter acciona la funcionalidad de "Mensaje directo"

## Paquete resources:
*   El objetivo de este paquete es contener info de utilidad para cliente y servidor, de manera que mantengan una coherencia en los signals y flags que se decida usar.
*   En esta version del codigo se usa para que los dos extremos del socket entiendan la signal "@" y la procesen como convenga en cada programa a los extremos del socket.