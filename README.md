# Maquina De Estados Microondas
1. INFORMACIÓN GENERAL\n
   •	Proyecto: Maquina De Estados Microondas
   •	Paradigma: Programación por Estados
   •	Lenguaje: Python 3
2. OBJETIVO DEL PROYECTO
Desarrollar un simulador de microondas que implemente una máquina de estados finitos para modelar su comportamiento, demostrando transiciones entre estados y manejo de eventos.
3. ESTADOS DEFINIDOS
3.1 Estado: APAGADO
   •	Descripción: Estado inicial del microondas, completamente inactivo
   •	Variables asociadas:
      o	tiempo_restante: 0
      o	potencia: 100%
      o	puerta_abierta: False
   •	Opciones disponibles:
      1.	Encender microondas → CONFIGURANDO
      2.	Abrir puerta → PUERTA_ABIERTA
3.2 Estado: CONFIGURANDO
   •	Descripción: Microondas encendido, configurando parámetros
   •	Variables asociadas:
      o	tiempo_restante: Configurable (1-300s)
      o	potencia: Configurable (10-100%)
   •	Opciones disponibles:
      1.	Configurar tiempo
      2.	Configurar potencia
      3.	Comenzar calentamiento → CALENTANDO
      4.	Apagar microondas → APAGADO
      5.	Abrir puerta → PUERTA_ABIERTA
3.3 Estado: CALENTANDO
   •	Descripción: Microondas en funcionamiento, calentando comida
   •	Comportamiento especial: Decrementa tiempo automáticamente
   •	Opciones disponibles:
      1.	Pausar calentamiento → PAUSADO
      2.	Cancelar y apagar → APAGADO
      3.	Abrir puerta → PUERTA_ABIERTA
3.4 Estado: PAUSADO
   •	Descripción: Calentamiento en pausa, tiempo congelado
   •	Opciones disponibles:
      1.	Reanudar calentamiento → CALENTANDO
      2.	Cancelar y apagar → APAGADO
      3.	Abrir puerta → PUERTA_ABIERTA
3.5 Estado: PUERTA_ABIERTA
   •	Descripción: Puerta abierta por seguridad
   •	Restricción: No se puede calentar
   •	Opciones disponibles:
      1.	Cerrar puerta → ESTADO ANTERIOR
      2.	Colocar comida
      3.	Retirar comida
      4.	Apagar microondas → APAGADO
4. REGLAS DE TRANSICIÓN
4.1 Transiciones desde APAGADO
   •	Opción 1 → CONFIGURANDO (con verificación de comida)
   •	Opción 2 → PUERTA_ABIERTA (abre puerta)
4.2 Transiciones desde CONFIGURANDO
   •	Opción 3 → CALENTANDO (si tiempo > 0)
   •	Opción 4 → APAGADO (reset variables)
   •	Opción 5 → PUERTA_ABIERTA (detiene configuración)
4.3 Transiciones desde CALENTANDO
   •	Opción 1 → PAUSADO (pausa tiempo)
   •	Opción 2 → APAGADO (cancelar)
   •	Opción 3 → PUERTA_ABIERTA (detiene por seguridad)
4.4 Transiciones desde PAUSADO
   •	Opción 1 → CALENTANDO (continúa tiempo)
   •	Opción 2 → APAGADO (cancelar)
   •	Opción 3 → PUERTA_ABIERTA
4.5 Transiciones desde PUERTA_ABIERTA
   •	Opción 1 → ESTADO ANTERIOR (cierra puerta)
   •	Opción 4 → APAGADO (apaga microondas)
5. VALIDACIONES IMPLEMENTADAS
5.1 Validaciones de Entrada
   •	Tiempo: 1-300 segundos
   •	Potencia: 10-100%
   •	Opciones numéricas dentro del rango válido
5.2 Validaciones de Estado
   •	No calentar sin tiempo configurado
   •	No calentar sin comida (con advertencia)
   •	No operar con puerta abierta
   •	Reset de tiempo al apagar
6. FUNCIONALIDADES ESPECIALES
6.1 Barra de Progreso
   •	Visualización gráfica del progreso del calentamiento
   •	Actualización en tiempo real
6.2 Temporización Automática
   •	Decremento automático del tiempo en estado CALENTANDO
   •	Manejo concurrente de entrada de usuario
6.3 Persistencia de Configuración
   •	Mantiene tiempo y potencia entre estados
   •	Preserva configuración al pausar
7. ESTRUCTURA DEL CÓDIGO
7.1 Clase Principal: Microondas
   •	Atributos de estado
   •	Diccionario de opciones por estado
   •	Métodos para manejo de estados
7.2 Métodos Clave
   1.	mostrar_menu(): Interfaz de usuario por estado
   2.	procesar_opcion(): Lógica de transiciones
   3.	ejecutar_ciclo_calentamiento(): Temporización automática
   4.	ejecutar(): Bucle principal
7.3 Flujo del Programa
   INICIO → APAGADO → Mostrar Menú → Procesar Opción
         ↓
   Transición de Estado
         ↓
   Ejecutar Comportamiento
         ↓
   Repetir hasta SALIR
CONCLUSIONES
Este proyecto demuestra efectivamente:
   1.	Modelado de estados finitos para sistemas del mundo real
   2.	Separación de responsabilidades por estado
   3.	Manejo de transiciones con validaciones
   4.	Interfaz de usuario intuitiva con menú numérico
El microondas implementado sigue el comportamiento de uno real, con todas las características de seguridad y funcionalidad esperadas, sirviendo como excelente ejemplo de programación por estados.
