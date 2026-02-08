# Maquina De Estados Microondas<br>
1. INFORMACIÓN GENERAL<br>
   •	Proyecto: Maquina De Estados Microondas<br>
   •	Paradigma: Programación por Estados<br>
   •	Lenguaje: Python 3<br>
2. OBJETIVO DEL PROYECTO<br>
Desarrollar un simulador de microondas que implemente una máquina de estados finitos para modelar su comportamiento, demostrando transiciones entre estados y manejo de eventos.<br>
3. ESTADOS DEFINIDOS<br>
3.1 Estado: APAGADO<br>
   •	Descripción: Estado inicial del microondas, completamente inactivo<br>
   •	Variables asociadas:<br>
      o	tiempo_restante: 0<br>
      o	potencia: 100%<br>
      o	puerta_abierta: False<br>
   •	Opciones disponibles:<br>
      1.	Encender microondas → CONFIGURANDO<br>
      2.	Abrir puerta → PUERTA_ABIERTA<br>
3.2 Estado: CONFIGURANDO<br>
   •	Descripción: Microondas encendido, configurando parámetros<br>
   •	Variables asociadas:<br>
      o	tiempo_restante: Configurable (1-300s)<br>
      o	potencia: Configurable (10-100%)<br>
   •	Opciones disponibles:<br>
      1.	Configurar tiempo<br>
      2.	Configurar potencia<br>
      3.	Comenzar calentamiento → CALENTANDO<br>
      4.	Apagar microondas → APAGADO<br>
      5.	Abrir puerta → PUERTA_ABIERTA<br>
3.3 Estado: CALENTANDO<br>
   •	Descripción: Microondas en funcionamiento, calentando comida<br>
   •	Comportamiento especial: Decrementa tiempo automáticamente<br>
   •	Opciones disponibles:<br>
      1.	Pausar calentamiento → PAUSADO<br>
      2.	Cancelar y apagar → APAGADO<br>
      3.	Abrir puerta → PUERTA_ABIERTA<br>
3.4 Estado: PAUSADO<br>
   •	Descripción: Calentamiento en pausa, tiempo congelado<br>
   •	Opciones disponibles:<br>
      1.	Reanudar calentamiento → CALENTANDO<br>
      2.	Cancelar y apagar → APAGADO<br>
      3.	Abrir puerta → PUERTA_ABIERTA<br>
3.5 Estado: PUERTA_ABIERTA<br>
   •	Descripción: Puerta abierta por seguridad<br>
   •	Restricción: No se puede calentar<br>
   •	Opciones disponibles:<br>
      1.	Cerrar puerta → ESTADO ANTERIOR<br>
      2.	Colocar comida<br>
      3.	Retirar comida<br>
      4.	Apagar microondas → APAGADO<br>
4. REGLAS DE TRANSICIÓN<br>
4.1 Transiciones desde APAGADO<br>
   •	Opción 1 → CONFIGURANDO (con verificación de comida)<br>
   •	Opción 2 → PUERTA_ABIERTA (abre puerta)<br>
4.2 Transiciones desde CONFIGURANDO<br>
   •	Opción 3 → CALENTANDO (si tiempo > 0)<br>
   •	Opción 4 → APAGADO (reset variables)<br>
   •	Opción 5 → PUERTA_ABIERTA (detiene configuración)<br>
4.3 Transiciones desde CALENTANDO<br>
   •	Opción 1 → PAUSADO (pausa tiempo)<br>
   •	Opción 2 → APAGADO (cancelar)<br>
   •	Opción 3 → PUERTA_ABIERTA (detiene por seguridad)<br>
4.4 Transiciones desde PAUSADO<br>
   •	Opción 1 → CALENTANDO (continúa tiempo)<br>
   •	Opción 2 → APAGADO (cancelar)<br>
   •	Opción 3 → PUERTA_ABIERTA<br>
4.5 Transiciones desde PUERTA_ABIERTA<br>
   •	Opción 1 → ESTADO ANTERIOR (cierra puerta)<br>
   •	Opción 4 → APAGADO (apaga microondas)<br>
5. VALIDACIONES IMPLEMENTADAS<br>
5.1 Validaciones de Entrada<br>
   •	Tiempo: 1-300 segundos<br>
   •	Potencia: 10-100%<br>
   •	Opciones numéricas dentro del rango válido<br>
5.2 Validaciones de Estado<br>
   •	No calentar sin tiempo configurado<br>
   •	No calentar sin comida (con advertencia)<br>
   •	No operar con puerta abierta<br>
   •	Reset de tiempo al apagar<br>
6. FUNCIONALIDADES ESPECIALES<br>
6.1 Barra de Progreso<br>
   •	Visualización gráfica del progreso del calentamiento<br>
   •	Actualización en tiempo real<br>
6.2 Temporización Automática<br>
   •	Decremento automático del tiempo en estado CALENTANDO<br>
   •	Manejo concurrente de entrada de usuario<br>
6.3 Persistencia de Configuración<br>
   •	Mantiene tiempo y potencia entre estados<br>
   •	Preserva configuración al pausar<br>
7. ESTRUCTURA DEL CÓDIGO<br>
7.1 Clase Principal: Microondas<br>
   •	Atributos de estado<br>
   •	Diccionario de opciones por estado<br>
   •	Métodos para manejo de estados<br>
7.2 Métodos Clave<br>
   1.	mostrar_menu(): Interfaz de usuario por estado<br>
   2.	procesar_opcion(): Lógica de transiciones<br>
   3.	ejecutar_ciclo_calentamiento(): Temporización automática<br>
   4.	ejecutar(): Bucle principal<br>
7.3 Flujo del Programa<br>
   INICIO → APAGADO → Mostrar Menú → Procesar Opción<br>
         ↓<br>
   Transición de Estado<br>
         ↓<br>
   Ejecutar Comportamiento<br>
         ↓<br>
   Repetir hasta SALIR<br>
CONCLUSIONES<br>
Este proyecto demuestra efectivamente:<br>
   1.	Modelado de estados finitos para sistemas del mundo real<br>
   2.	Separación de responsabilidades por estado<br>
   3.	Manejo de transiciones con validaciones<br>
   4.	Interfaz de usuario intuitiva con menú numérico<br>
El microondas implementado sigue el comportamiento de uno real, con todas las características de seguridad y funcionalidad esperadas, sirviendo como excelente ejemplo de programación por estados.<br>
