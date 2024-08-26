# Creación del ambiente virtual

Para la configuración del ambiente virtual usaremos el paquete `virtualenv` y seguiremos los pasos a continuación, **Los pasos se presentan para usuarios de WINDOWS**.

1. Verificar que tenemos Python y PIP instalados.

    - Para verificar Python en un terminal escribiremos:

        ```bat
        python --version
        ```
    
    - Para verificar PIP en un terminal escribiremos:

        ```bat
        pip --version
        ```
    
    Si no tenemos errores tendremos instalados Python y PIP, si hay algún error buscar en linea soluciones. 

2. Instalar `virtualenv`:

    Para la instalación en un terminal escribiremos:

    ```bat
    python -m pip install virtualenv
    ```

3. Crear el ambiente virtual 

    Crearemos un ambiente virtual con el nombre que quieran, en mi caso, usare `LEGO` para mi ambiente. En un terminal escribiremos:

    ```bat
    python -m virtualenv -p python3.11 LEGO
    ```

    En la creación de este ambiente estoy declarando la versión de python que voy a usar, esto es necesario para usar el bluetooth, ya que a día de hoy (2024-08-26) el paquete `pybluez` no soporta python 3.12.

4. Activar el ambiente virtual

    Cada vez que vayamos a utilizar nuestro programa de python para controlar el LEGO, deberemos activar el ambiente virtual. Para esto, estando en la misma carpeta de donde creamos el ambiente virtual, en el terminal escribiremos:

    ```bat
    .\LEGO\Scripts\activate
    ```

    Así aparecera la palabra LEGO al inicio del la línea en el Terminal y tendremos activado el ambiente virtual. 