# Instalación de paquetes en Windows

Para instalar los paquetes vamos a activar el ambiente virtual, y una vez activado vamos a escribir en un terminal.

```bat
pip install ev3-dc      
pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez
```

En caso de que se presente un error con la instalación de PyBluez, podremos usar el _wheel_, este archivo de instalación debe estar en concordancia con la versión de Python, el sistema Operativo y el procesador.

```bat
pip install PyBluez-0.30-cp311-cp311-win_amd64.whl
```

- [Python 3.11 | Window | AMD64 ~ PyBluez-0.30-cp311-cp311-win_amd64.whl](../dist/PyBluez-0.30-cp311-cp311-win_amd64.whl)

Con esto ya tendremos todo lo necesarios para controlar nuestro LEGO **EV3** desde un PC usando Python. Si se presenta algún error con la instalación hacer la instalación usando el archivo [`requirements.txt`](./requirements.txt). Con el archivo descargado escribiremos en el terminal:

```bat
pip install -r requirements.txt
```