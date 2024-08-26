import ev3_dc as ev3

with ev3.EV3(protocol=ev3.USB, host='00:16:53:50:8A:86') as brick:
    print(brick)
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
