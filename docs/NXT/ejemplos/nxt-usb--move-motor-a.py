import nxt.locator
import nxt.motor

with nxt.locator.find() as b:
    # Conectar el motor en el Puerto A
    my_motor = b.get_motor(nxt.motor.Port.A)
    print("Presiona Ctrl-C para interrumpir el programa")
    while True:
        # Hará una rotación completa en una dirección
        my_motor.turn(25, 360)
        # Hará una rotación completa en la otra dirección
        my_motor.turn(-25, 360)
