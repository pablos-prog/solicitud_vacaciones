Sistema de Gestión de Vacaciones
Descripción

Este proyecto fue desarrollado como Trabajo Integrador para la materia Organización Empresarial de la Tecnicatura Universitaria en Programación.

El sistema simula un chatbot para la gestión de solicitudes de vacaciones dentro de una organización.

Permite:

Validar empleados.
Consultar saldo disponible.
Solicitar días de vacaciones.
Aprobar o rechazar solicitudes.
Registrar solicitudes realizadas.

El objetivo es automatizar un proceso administrativo utilizando BPMN 2.0 y Python.
Funcionalidades

El sistema permite:

Ingresar un ID de empleado.
Verificar la existencia del empleado.
Consultar la cantidad de días de vacaciones disponibles.
Solicitar días de vacaciones.
Validar los datos ingresados por el usuario.
Aprobar solicitudes cuando existe saldo suficiente.
Rechazar solicitudes cuando no existe saldo suficiente.
Registrar las solicitudes realizadas.
Tecnologías Utilizadas

Para el desarrollo de este proyecto se utilizaron las siguientes tecnologías:

Python 3
BPMN 2.0
Bizagi Modeler
GitHub
ChatGPT (como herramienta de apoyo para documentación y validación conceptual)
Estructura del Proyecto
sistema-gestion-vacaciones/
│
├── chatbot_vacaciones.py
├── README.md
├── empleados.csv
├── solicitudes.csv
└── Informe.pdf
Descripción de los archivos
main.py: Programa principal del simulador.
README.md: Documentación del proyecto.
empleados.csv: Base de datos simulada de empleados.
solicitudes.csv: Registro de solicitudes realizadas.
Informe.pdf: Documento final entregado para la materia.
Ejecución del Programa
Requisitos
Python 3 instalado.
Pasos para ejecutar
Descargar o clonar el repositorio.
Abrir una terminal en la carpeta del proyecto.
Ejecutar el siguiente comando:
python chatbot_vacaciones.py
Resultado esperado

El sistema solicitará:

ID del empleado.
Cantidad de días de vacaciones.

Posteriormente aprobará o rechazará la solicitud según las reglas de negocio implementadas.
## Relación con el BPMN

El sistema fue diseñado a partir de un modelo BPMN 2.0 que representa el proceso de solicitud de vacaciones.

Los gateways del BPMN fueron implementados mediante estructuras condicionales (`if/else`) en Python, permitiendo validar:

- Existencia del empleado.
- Validez de los datos ingresados.
- Disponibilidad de días de vacaciones.

De esta forma se mantiene la coherencia entre el proceso de negocio y la implementación técnica.
## Autor

Pablo Soñez

Trabajo Integrador - Organización Empresarial

Tecnicatura Universitaria en Programación
Repositorio

Este proyecto fue desarrollado como Trabajo Integrador para la materia Organización Empresarial de la Tecnicatura Universitaria en Programación.

Autor

Pablo Soñez

Código Fuente

El archivo principal del proyecto es:

chatbot_vacaciones.py
Documentación

La documentación del proyecto incluye:

Modelo BPMN 2.0
Máquina de Estados
Diccionario de Datos
Manual de Usuario
Casos de Prueba
Informe Final
