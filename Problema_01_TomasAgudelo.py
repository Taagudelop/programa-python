# Fase 5 - Evaluación Final POA
# Problema 1: Clasificación del nivel de compromiso de sesiones de clientes
# Estudiante: Tomás Andrés Agudelo Pardo


def clasificar_compromiso(duracion, clics):
    """Devuelve 'Alto', 'Bajo' o 'Medio' según la duración (segundos) y los clics."""
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


def mostrar_informe(sesiones):
    """Recorre la matriz y muestra el ID del cliente con su clasificación."""
    print("INFORME DE COMPROMISO POR SESIÓN")
    print("-" * 40)
    print(f"{'ID Cliente':<12}{'Duración (s)':<15}{'Clics':<8}{'Compromiso'}")
    print("-" * 40)
    for fila in sesiones:
        id_cliente = fila[0]
        duracion = fila[1]
        clics = fila[2]
        nivel = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<12}{duracion:<15}{clics:<8}{nivel}")


# Matriz de sesiones: [ID del cliente, duración en segundos, número de clics]
sesiones = [
    [101, 240, 12],   # duración y clics altos
    [102, 45, 10],    # duración menor a 60
    [103, 120, 5],    # caso intermedio
    [104, 300, 2],    # muchos segundos pero pocos clics
    [105, 181, 9],    # justo por encima de los límites de "Alto"
    [106, 180, 9],    # duración exactamente 180, no supera el límite
    [107, 60, 3],     # justo en los límites de "Bajo", queda en Medio
    [108, 200, 8],    # clics exactamente 8, no supera el límite
]

mostrar_informe(sesiones)
