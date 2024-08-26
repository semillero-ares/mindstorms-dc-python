# Conexión usando Bluetooth

Para usar la conexión por bluetooth, debemos realizar las siguientes tareas: 

1. Emparejar el LEGO con el computador.

    Para esto, encenderemos el LEGO, buscaremos en el menú de herramientas  la opción `Bluetooth` > `Connections` > `Search`. Esto iniciará la búsqueda del PC, después de un rato aparecerá en pantalla el nombre de tu computador (siempre y cuando, el PC tenga bluetooth, el bluetooth este en modo visible y encendido). Seleccionamos del PC, le damos conectar, y dejamos la contraseña 1234. En el PC deberá aparecer la solicitud, aceptamos la solicitud e ingresamos la contraseña 1234. 

2. Obtener la dirección MAC del Bluetooth del lego.

    Para esto, encenderemos el LEGO, buscaremos en el menú de herramientas  la opción `Brick Info`. Aparecerá en pantalla información sobre el LEGO, de donde necesitaremos la última información con nombre de `ID`. En el LEGO que estoy usando el `ID` es `001653508A86` este número lo necesitaremos para conectarnos con el LEGO desde Python. 

    Necesitaremos rescribirlos, agregando "`:`" cada dos caracteres, de la siguiente forma:

    `00:16:53:50:8A:86`

3. Verificar que el PC ve el LEGO.

    Para esto usaremos el código de Python que pueden descargar [aquí](../ejemplos/pybluez-inquiry-example.py)

    ```python
    # Simple inquiry example
    import bluetooth

    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        print("  {} - {}".format(addr, name))
    ```

    En mi caso la respuesta después de correr el código (con el ambiente virtual activado) es:

    ```txt
    Found 1 devices.
      00:16:53:50:8A:86 - EV3
    ``` 

4. Probemos un codigo para mover un motor conectador en el Puerto A:

    El código de prueba lo podemos descargar de [aquí](./ejemplos/ev3-bt--move-motor-a.py), que es igual al mostrado a continuación, **Debemos cambiar la dirección MAC** del LEGO por la correcta.

    ```python 
    import ev3_dc as ev3

    with ev3.EV3(protocol=ev3.BLUETOOTH, host='00:16:53:50:8A:86') as brick:
        # Conectar el motor en el Puerto A
        my_motor = ev3.Motor(ev3.PORT_A, ev3_obj=brick)
        print("Presiona Ctrl-C para interrumpir el programa")
        while True:
            # Hará una rotación completa en una dirección
            my_motor.start_move_to(360, speed=25)
            while my_motor.busy:
                pass
            # Hará una rotación completa en la otra dirección
            my_motor.start_move_to(0, speed=25)
            while my_motor.busy:
                pass
    ```

Para más información de las funciones que se pueden usar consultar la [**documentación**](https://ev3-dc.readthedocs.io/en/latest/api_documentation.html).