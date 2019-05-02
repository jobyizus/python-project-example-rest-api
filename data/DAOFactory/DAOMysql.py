#antes descargar el library de mysql for python
 #pip install mysql-connector-python --user


#Lo primero que hacemos es importar el módulo que nos permite conectarnos con MySQL
import mysql.connector

#llamamos a la función connect pasando la ubicación de nuestro servidor que es 'localhost', 
#el usuario que por defecto al instalar MySQL se creó el usuario 'root' y la clave de ese usuario 
conexion1=mysql.connector.connect(host="192.168.99.100", port="32779",
                                  user="root", 
                                  passwd="jesus", 
                                  database="southwind")
#Luego a partir del objeto 'conexion1' que es de la clase 'MySQLConnection' llamamos al método 'cursor':
cursor1=conexion1.cursor()
#A partir del objeto 'cursor1' llamamos al método execute y le pasamos como parámetro un comando SQL, en este caso 'show tables':
cursor1.execute("show tables")
#Imprimimos con un for todas las tablas y cerramos la conexión:
for tabla in cursor1:
    print(tabla)
conexion1.close() 

#Ahora implementaremos un programa que inserte un par de filas en la tabla 'articulos'.
    insert_products(valor1,valor2,valor3)
