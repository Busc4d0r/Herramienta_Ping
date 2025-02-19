import subprocess
import platform
import os
import speedtest

ip_dm='192.168.1.1'
ip_hex='192.168.254.1'
ip_prov1='192.168.101.1'
ip_prov2='172.21.156.2'
ip_dns='8.8.8.8'

def limpiar_pantalla():
    if platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def test_speed():
    try:
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        st.results.share()
        results = st.results.dict()
        
        print(f"    Velocidad de descarga: {results['download'] / 1_000_000:.2f} Mbps")
        print(f"    Velocidad de subida: {results['upload'] / 1_000_000:.2f} Mbps")
        print(f"    Ping: {results['ping']} ms")
    except Exception as e:
        print(f"Ocurrió un error al testear la velocidad de conexión: {e}")

def tracert_dns():
    try:
        comando = ['tracert', ip_dns] if subprocess.os.name == 'nt' else ['traceroute', ip_dns]
        result = subprocess.run(comando, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f'    Error al ejecutar el comando: {result.stderr}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

def ping_dns():
    try:
        if platform.system().lower() == "windows":
            comando = ['ping','-n','4',ip_dns]
        else:
            comando = ['ping','-c','4',ip_dns]

        resultado = subprocess.run(
            comando,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if resultado.returncode == 0:
            print(f'    Hay conexión a internet\n')
            #print(resultado.stdout)
        else:
            print(f'    NO hay conexión a internet\n')
            #print(resultado.stderr)
    except Exception as e:
        print(f'Ocurrió un error: {e}')

def ping_dm():
    try:
        if platform.system().lower() == 'windows':
            comando = ['ping','-n','4',ip_dm]
        else:
            comando = ['ping','-c','4',ip_dm]

        resultado = subprocess.run(
            comando,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if resultado.returncode == 0:
            print('    Hay conexión con el router Dream Machine\n')
            #print(resultado.stdout)
        else:
            print('    NO hay conexión con el router Dream Machine\n')
            #print(resultado.stderr)

    except Exception as e:
        print(f'Ocurrió un error: {e}')

def ping_prov1():
    try:
        if platform.system().lower() == 'windows':
            comando = ['ping','-n','4',ip_prov1]
        else:
            comando = ['ping','-c','4',ip_prov1]

        resultado = subprocess.run(
            comando,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if resultado.returncode == 0:
            print('    Hay conexión con Inter\n')
            #print(resultado.stdout)
        else:
            print('    NO hay conexión con Inter\n')
            #print(resultado.stderr)

    except Exception as e:
        print(f'Ocurrió un error: {e}')

def ping_prov2():
    try:
        if platform.system().lower() == 'windows':
            comando = ['ping','-n','4',ip_prov2]
        else:
            comando = ['ping','-c','4',ip_prov2]

        resultado = subprocess.run(
            comando,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if resultado.returncode == 0:
            print('    Hay conexión con Fibex\n')
            #print(resultado.stdout)
        else:
            print('    NO hay conexión con Fibex\n')
            #print(resultado.stderr)

    except Exception as e:
        print(f'Ocurrió un error: {e}')

def diag_auto():
    print('verificando conexión con el router...')
    ping_dm()
    print('verificando conexión con Inter...')
    ping_prov1()
    print('verificando conexión con Fibex...')
    ping_prov2()
    print('verificando conexión con el DNS...')
    ping_dns()

def opc_av():
    while True:
        print('1: Verificar conexión con el router Dream Machine')
        print('2: Verificar conexión con Inter')
        print('3: Verificar conexión con Fibex')
        print('4: Verificar conexión con el DNS')
        print('5: Trazar ruta hacia el DNS')
        option=int(input('Ingrese el número de la acción correspondiente: '))
        limpiar_pantalla()

        if option == 1:
            print('Verificando conexión con el router Dream Machine...\n')
            ping_dm()
            input('Presione Enter para volver al menú ')
            limpiar_pantalla()

        elif option == 2:
            print('Verificando conexión con Inter...\n')
            ping_prov1()
            input('Presione Enter para volver al menú ')
            limpiar_pantalla()

        elif option == 3:
            print('Verificando conexión con Fibex...\n')
            ping_prov2()
            input('Presione Enter para volver al menú ')
            limpiar_pantalla()

        elif option == 4:
            print('Verificando conexión con el DNS...\n')
            ping_dns()
            input('Presione Enter para volver al menú ')
            limpiar_pantalla()

        elif option == 5:
            print('Trazando ruta hacia el DNS...\n')
            tracert_dns()
            input('Presione Enter para volver al menú ')
            limpiar_pantalla()

        elif option == 0:
            break

        else:
            print('La opción no es válida')

def menu():
    while True:
        print('1: Diagnóstico automático')
        print('2: Prueba de velocidad')
        print('3: Opciones avanzadas')
        print('0: Salir\n')
        opcion = int(input('Ingrese el número de la acción correspondiente: '))
        limpiar_pantalla()

        if opcion == 1:
            print('Ejecutando diagnóstico automático...\n')
            diag_auto()
            input('Presione Enter para volver al menú ')
            limpiar_pantalla()

        elif opcion == 2:
            print(f'Ejecutando prueba de velocidad...\n')
            test_speed()
            input('Presione Enter para volver al menú ')
            limpiar_pantalla()

        elif opcion == 3:
            opc_av()
            limpiar_pantalla()

        elif opcion == 0:
            break

        else:
            print('La opción no es válida')

menu()