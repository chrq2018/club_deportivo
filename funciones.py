def menu():
    print()
    opc = 0
    while opc < 1 or opc > 5:
        print()
        print('1) Alta')
        print('2) Baja')
        print('3) Modificar')
        print('4) Listar')
        print('5) Salir')
        opc = int(input('Elija una opción: '))
    return opc
        