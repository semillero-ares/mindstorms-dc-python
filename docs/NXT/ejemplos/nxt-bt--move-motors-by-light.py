import bluetooth as bluez
import nxt.backend.bluetooth
import nxt.locator
import nxt.sensor
import nxt.sensor.generic

from time import sleep

brick = nxt.backend.bluetooth.BluetoothSock(
    bluetooth=bluez, host='00:16:53:1A:A8:B3')
with brick.connect() as b:
    # Conectar el motor al puerto B
    motorDerecha = b.get_motor(nxt.motor.Port.B)
    # Conectar el motor al puerto C
    motorIzquierda = b.get_motor(nxt.motor.Port.C)
    # Conectar el sensor de Luz al puerto 2
    sensorLuz = b.get_sensor(nxt.sensor.Port.S2, nxt.sensor.generic.Light)
    print("Presiona Ctrl-C para interrumpir el programa")
    while True:
        # Tomar la medida del sensor de Luz
        medida = sensorLuz.get_sample()
        print(medida)
        # Calcular una accion dependiendo del valor de la Luz
        accion = int((500-medida)/5)
        # Enviar acciones a cada motor
        motorDerecha.run(accion, regulated=True)
        motorIzquierda.run(accion, regulated=True)
        # Esperar 0.2 segundos
        sleep(0.2)
