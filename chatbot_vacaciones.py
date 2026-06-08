
#chatbot vacacioes
#base de datos simulada


#diccionario de almacenaiento de empeados
#clave = id de empleaods
#valor = diccionario interno por cada empleado con nomobre y dias
empleados = {
    1: {"nombre": "Juan Pérez", "dias": 15},
    2: {"nombre": "Ana Gómez", "dias": 10},
    3: {"nombre": "Pedro Ruiz", "dias": 5},
    4: {"nombre": "María López", "dias": 20},
    5: {"nombre": "Carlos Fernández", "dias": 8}
}

#lista para guardar solicitudes
solicitudes = []

print( "=" * 40)
print("Sistema de gestion de vacaciones")
print( "=" * 40)

#Esperando id de empleado
try:
    id_empleado = int(input("Ingrese su id de empleado: "))
# si el usuario ingresa otra letras
except ValueError:
    print("Error debe ingresar un número")
    exit

#verifica si el id existe

if id_empleado not in empleados:
    print("Error! Empleado no encontrado")
    exit

#guarda los datos del empleado
empleado = empleados[id_empleado]

#muestra ifor acion del empleaado
print(f"\nBienvenido: {empleado['nombre']}")
print(f"Dias disponibles: {empleado['dias']}")

#esperando dias
#se solicita cantidad de dias
try:
    dias_solicitados = int(input("Ingresa la cantidad de dias que desea solicitar: "))

except ValueError:
    print("Error Ingresa solo números")
    exit

#validando dias
#verifica si tiene diassuficientes
if dias_solicitados <= empleado['dias']:
#solicitud aprobada
    empleado['dias'] -= dias_solicitados

#se guarda la solictud en el registro
    solicitudes.append({
    "id_empleado": id_empleado,
    "dias_solicitados": dias_solicitados,
    "estado": "Aprobada"
})

#se informa resultados al usuario
    print("\nSolicitud aporbada")
    print(f"Dias restantes: {empleado['dias']}")

#solicitud rechazada
else:
#guarda la solicitud rechazada
    solicitudes.append({
        "id_empleado": id_empleado,
        "dias_solicitados": dias_solicitados,
        "estado": "Rechazada"
    })

#informa resultados al usuario
    print("\nSolicitud rechazada")
    print(f"Saldo disponilbe {empleado['dias']} dias")

#finaliza el proceso
print("Proceso finalizado")