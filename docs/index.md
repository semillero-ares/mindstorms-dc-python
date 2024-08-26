[NXT]: https://s.click.aliexpress.com/e/_Dkm7FYb
[EV3]: https://s.click.aliexpress.com/e/_DmUt8rH
[BT]: https://s.click.aliexpress.com/e/_DdCQLDN
[WIFI]: https://s.click.aliexpress.com/e/_DdCcaFN
[NXTpy]: https://ni.srht.site/nxt-python/latest/
[NXTgit]: https://github.com/schodet/nxt-python
[EV3py]: https://ev3-dc.readthedocs.io/en/latest/
[EV3git]: https://github.com/ChristophGaukel/ev3-python3
[pybluez]: https://github.com/pybluez/pybluez
[pyusb]: https://github.com/pyusb/pyusb

# Control de LEGO Mindstorms desde Python

Aquí presentamos un tutorial para controlar desde Python dos versiones muy populares de LEGO Mindstorms el [NXT][NXT] y el [EV3][EV3]. Para cada uno de esto existen unos paquetes en python que nos permitirán el control por USB, [Bluetooth][BT] o [Wi-Fi][WIFI] (disponible solo en el EV3). 

- Para el [LEGO Mindstorms NXT][NXT] tenemos el paquete [nxt-python][NXTpy]
- Para el [LEGO Mindstorms EV3][EV3] tenemos el paquete [ev3-dc][EV3py]

En ambos casos tambien necesitaremos dos paquetes auxiliares, los cuales son:

- [PyUSB][pyusb] para la conexión por cable USB.
- [PyBluez][pybluez] para la conexión Bluetooth.

Dependiendo de la conexión que queramos hacer, necesitaremos configurar nuestro computador para controlar exitosamente nuestro LEGO. 

## Requerimientos

Para controlar del LEGO con un computador necesitaremos:

- Un LEGO MindStorms [NXT][NXT] o [EV3][EV3]
- Un computador con Wi-Fi y/o Bluetooth dependiendo de la conexión. Si no tenemos un computador con Wi-Fi o bluetooth podemos comprar un [dongle USB][WIFI] con esta capacidad.
- Python instalado en el PC, la versión de Python debe ser 3.x hasta la versión 3.11. Si tenemos una versión superior a la 3.11, deberemos [configurar un ambiente virtual](ambiente-virtual).
- Instalación de los paquetes necesarios.

En la siguiente página empezaremos configurando el ambiente virtual. 