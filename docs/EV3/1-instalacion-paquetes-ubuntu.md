# Instalación de paquetes en Ubuntu

Para instalar los paquetes en ubuntu deberemos a activar el ambiente virtual, e instalar los siguentes componentes

- Instalar libbluetooth

    ```sh
    sudo apt-get install libbluetooth-dev
    ```

- Luego, instalar las siguientes librerias de python

    ```sh
    pip install ev3-dc    
    pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez
    ```

Con esto ya tendremos todo lo necesarios para controlar nuestro LEGO **NXT** desde un PC usando Python. Si se presenta algún error con la instalación hacer la instalación usando el archivo [`requirements.txt`](./requirements.txt). Con el archivo descargado escribiremos en el terminal:

```bat
pip install -r requirements.txt
```