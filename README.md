# WebServicesPython

Esta aplicación se realizó con la finalidad de crear una Web Service en Python y consumir los datos por Frontend.

## **Instalación**

### **Paso 1**

**Forma 1:** Dar clic en **Code**, luego **Download Zip** y descomprimir el archivo en tu ordenador.

**Forma 2:** Abrir una terminal en tu ordenador y ejecutar el siguiente comando:

    git clone https://github.com/CarlosAlmeida2000/WebServicesPython.git

### **Paso 2**

Descargar e instalar [**Python**](https://github.com/CarlosAlmeida2000/WebServicesPython.git)

### **Paso 3**

Instalar Django ejecutando el siguente comando en la consola de tu ordenador, para más información [**click aquí.**](https://docs.djangoproject.com/en/3.2/)

    pip install django==3.0.8

### **Paso 3**

Instalar la API para utilizar peticiones **REST** en Django Python, ejecutar el siguiente comando en la consola de tu ordenador y para más información [**click aquí.**](https://www.django-rest-framework.org/)

    pip install djangorestframework

### **Paso 4**

Instalar el controlador de la conexión de PostgreSQL ejecutando el siguiente comando en la consola de tu ordenador.

    pip install psycopg2 ==2.8.6

### **Paso 5**

-   **Primero:** Configurar la conexión de la base de datos en el archivo **setting.py** de la carpeta **../WebServicesPython**

-   **Segundo:** Ejecutar el siguiente comando en consola:

          python manage.py migrate

### **Paso 6**

Instalar la libreria **requests**, ejecutando el siguente comando en consola:

    pip install requests

### **Paso 7**

Consumir las aplicaciones

-   **Primero:** Ejecutar la aplicación de WebService, abriendo la terminal en la carpeta **../WebServicesPython** y ejecutar el siguiente comando en consola:

          python manage.py runserver

-   **Segundo:** Ejecutar la aplicación de consumo, abriendo la terminal en la carpeta **../AppWebConsumo** y ejecutar el siguiente comando en consola:

          python manage.py runserver 7000

-   **Tercero:** Escribir la siguiente URL en el navegador:

          http://127.0.0.1:7000/
