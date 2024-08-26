# Instalación de los paquetes

Para instalar los paquetes vamos a activar el ambiente virtual, y una vez activado vamos a escribir en un terminal.

```bat
pip install nxt-python    
pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez
```

Con esto ya tendremos todo lo necesarios para controlar nuestro LEGO **NXT** desde un PC usando Python. Si se presenta algún error con la instalación hacer la instalación usando el archivo [`requirements.txt`](./requirements.txt). Con el archivo descargado escribiremos en el terminal:

```bat
pip install -r requirements.txt
```