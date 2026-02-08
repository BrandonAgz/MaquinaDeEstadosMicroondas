"""
MICROONDAS - MÁQUINA DE ESTADOS FINITOS (Versión Simplificada)
Autor: Estudiante
Descripción: Implementación de un microondas usando estados finitos con menú numérico
"""

class Microondas:
    def __init__(self):
        self.estado_actual = "APAGADO"
        self.tiempo_restante = 0
        self.potencia = 100
        self.tiempo_configurado = 0
        self.puerta_abierta = False
        self.comida_presente = False
        
        self.opciones_estado = {
            "APAGADO": [
                "Encender microondas",
                "Abrir puerta"
            ],
            "CONFIGURANDO": [
                "Configurar tiempo (1-300 segundos)",
                "Configurar potencia (10-100%)",
                "Comenzar calentamiento",
                "Apagar microondas",
                "Abrir puerta"
            ],
            "CALENTANDO": [
                "Pausar calentamiento",
                "Cancelar y apagar",
                "Abrir puerta (detiene automáticamente)"
            ],
            "PAUSADO": [
                "Reanudar calentamiento",
                "Cancelar y apagar",
                "Abrir puerta"
            ],
            "PUERTA_ABIERTA": [
                "Cerrar puerta",
                "Colocar comida",
                "Retirar comida",
                "Apagar microondas"
            ]
        }
    
    def mostrar_menu(self):
        """Muestra el menú de opciones para el estado actual"""
        print(f"\n{'='*50}")
        print(f"ESTADO ACTUAL: {self.estado_actual}")
        print(f"{'='*50}")
        
        if self.estado_actual == "CALENTANDO":
            print(f"Tiempo restante: {self.tiempo_restante} segundos")
            print(f"Potencia: {self.potencia}%")
            
            if self.tiempo_configurado > 0:
                progreso = ((self.tiempo_configurado - self.tiempo_restante) / self.tiempo_configurado) * 100
                barra = "█" * int(progreso / 5) + "░" * (20 - int(progreso / 5))
                print(f"Progreso: [{barra}] {progreso:.1f}%")
        
        elif self.estado_actual == "PAUSADO":
            print(f"Tiempo restante: {self.tiempo_restante} segundos")
            print(f"Potencia: {self.potencia}%")
        
        elif self.estado_actual == "CONFIGURANDO":
            print(f"Tiempo configurado: {self.tiempo_restante}s")
            print(f"Potencia configurada: {self.potencia}%")
            print(f"Comida presente: {'Sí' if self.comida_presente else 'No'}")
        
        elif self.estado_actual == "PUERTA_ABIERTA":
            print(f"Puerta: ABIERTA")
            print(f"Comida presente: {'Sí' if self.comida_presente else 'No'}")
        
        print(f"{'-'*30}")
        print("OPCIONES DISPONIBLES:")
        
        opciones = self.opciones_estado[self.estado_actual]
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        
        print(f"{'='*50}")
    
    def procesar_opcion(self, opcion):
        """Procesa la opción seleccionada según el estado actual"""
        
        if self.estado_actual == "APAGADO":
            if opcion == 1:  # Encendido
                if not self.comida_presente:
                    print("\nADVERTENCIA: No hay comida en el microondas.")
                    respuesta = input("¿Desea continuar? (s/n): ").lower()
                    if respuesta != 's':
                        return
                self.estado_actual = "CONFIGURANDO"
                print("\nMicroondas encendido. Puede configurar tiempo y potencia.")
            
            elif opcion == 2:  # Abrir puerta
                self.puerta_abierta = True
                self.estado_actual = "PUERTA_ABIERTA"
                print("\nPuerta abierta.")
        
        # Estado: CONFIGURANDO
        elif self.estado_actual == "CONFIGURANDO":
            if opcion == 1:  # Configurar tiempo
                try:
                    tiempo = int(input("\nIngrese tiempo en segundos (1-300): "))
                    if 1 <= tiempo <= 300:
                        self.tiempo_restante = tiempo
                        self.tiempo_configurado = tiempo
                        print(f"Tiempo configurado: {tiempo} segundos")
                    else:
                        print("Error: Tiempo debe estar entre 1 y 300 segundos")
                except:
                    print("Error: Ingrese un número válido")
            
            elif opcion == 2:  # Configurar potencia
                try:
                    potencia = int(input("\nIngrese potencia (10-100%): "))
                    if 10 <= potencia <= 100:
                        self.potencia = potencia
                        print(f"Potencia configurada: {potencia}%")
                    else:
                        print("Error: Potencia debe estar entre 10% y 100%")
                except:
                    print("Error: Ingrese un número válido")
            
            elif opcion == 3:  # Comenzar calentamiento
                if self.tiempo_restante <= 0:
                    print("Error: Configure el tiempo primero")
                elif not self.comida_presente:
                    print("ADVERTENCIA: No hay comida detectada")
                    respuesta = input("¿Desea continuar? (s/n): ").lower()
                    if respuesta == 's':
                        self.estado_actual = "CALENTANDO"
                        print("\nComenzando calentamiento...")
                else:
                    self.estado_actual = "CALENTANDO"
                    print("\nComenzando calentamiento...")
            
            elif opcion == 4:  # Apagar
                self.estado_actual = "APAGADO"
                self.tiempo_restante = 0
                print("\nMicroondas apagado.")
            
            elif opcion == 5:  # Abrir puerta
                self.puerta_abierta = True
                self.estado_actual = "PUERTA_ABIERTA"
                print("\nPuerta abierta.")
        
        # Estado: CALENTANDO
        elif self.estado_actual == "CALENTANDO":
            if opcion == 1:  # Pausar
                self.estado_actual = "PAUSADO"
                print("\nCalentamiento en pausa.")
            
            elif opcion == 2:  # Cancelar
                self.estado_actual = "APAGADO"
                self.tiempo_restante = 0
                print("\nCalentamiento cancelado. Microondas apagado.")
            
            elif opcion == 3:  # Abrir puerta
                self.puerta_abierta = True
                self.estado_actual = "PUERTA_ABIERTA"
                print("\nPuerta abierta. Calentamiento detenido.")
        
        # Estado: PAUSADO
        elif self.estado_actual == "PAUSADO":
            if opcion == 1:  # Reanudar
                self.estado_actual = "CALENTANDO"
                print("\nReanudando calentamiento...")
            
            elif opcion == 2:  # Cancelar
                self.estado_actual = "APAGADO"
                self.tiempo_restante = 0
                print("\nCalentamiento cancelado. Microondas apagado.")
            
            elif opcion == 3:  # Abrir puerta
                self.puerta_abierta = True
                self.estado_actual = "PUERTA_ABIERTA"
                print("\nPuerta abierta.")
        
        # Estado: PUERTA_ABIERTA
        elif self.estado_actual == "PUERTA_ABIERTA":
            if opcion == 1:  # Cerrar puerta
                self.puerta_abierta = False
                if self.tiempo_restante > 0:
                    self.estado_actual = "CONFIGURANDO"
                else:
                    self.estado_actual = "APAGADO"
                print("\nPuerta cerrada.")
            
            elif opcion == 2:  # Colocar comida
                self.comida_presente = True
                print("\nComida colocada en el microondas.")
            
            elif opcion == 3:  # Retirar comida
                self.comida_presente = False
                print("\nComida retirada del microondas.")
            
            elif opcion == 4:  # Apagar
                self.estado_actual = "APAGADO"
                self.puerta_abierta = False
                print("\nMicroondas apagado.")
    
    def ejecutar_ciclo_calentamiento(self):
        """Ejecuta un ciclo de calentamiento si está en ese estado"""
        if self.estado_actual == "CALENTANDO" and self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            print(f"\rCalentando... {self.tiempo_restante}s restantes", end="")
            
            if self.tiempo_restante == 0:
                print("\n\n¡DING! ¡Comida lista!")
                self.estado_actual = "APAGADO"
                return False
            
            return True
        return False
    
    def ejecutar(self):
        """Función principal para ejecutar el microondas"""
        import time
        
        print("="*60)
        print("MICROONDAS - SIMULADOR CON MÁQUINA DE ESTADOS")
        print("="*60)
        print("Instrucciones: En cada estado, ingrese el número de la opción")
        print("="*60)
        
        while True:
            # Menú del estado actual
            self.mostrar_menu()
            
            # Si está calentando, ejecutar ciclo automático
            if self.estado_actual == "CALENTANDO":
                print("\n(Presione Enter para mostrar opciones o Ctrl+C para salir)")
                try:
                    # Esperar entrada o timeout
                    import select
                    import sys
                    
                    i, o, e = select.select([sys.stdin], [], [], 1)
                    
                    if i:  # Hay entrada del usuario
                        entrada = sys.stdin.readline().strip()
                        if entrada.lower() == 'salir':
                            break
                        continue
                    
                    # Ejecutar ciclo de calentamiento
                    if not self.ejecutar_ciclo_calentamiento():
                        continue
                    
                except KeyboardInterrupt:
                    print("\n\nPrograma terminado por el usuario")
                    break
                except:
                    pass
            
            # Obtener opción del usuario
            try:
                entrada = input("\nSeleccione una opción (número): ").strip()
                
                if entrada.lower() in ['salir', 'exit', 'quit']:
                    print("\nPrograma terminado")
                    break
                
                opcion = int(entrada)
                opciones_disponibles = len(self.opciones_estado[self.estado_actual])
                
                if 1 <= opcion <= opciones_disponibles:
                    self.procesar_opcion(opcion)
                else:
                    print(f"Error: Opción debe estar entre 1 y {opciones_disponibles}")
            
            except ValueError:
                print("Error: Ingrese un número válido")
            except KeyboardInterrupt:
                print("\n\nPrograma terminado por el usuario")
                break
            except Exception as e:
                print(f"Error inesperado: {e}")


# Ejecutar el programa
if __name__ == "__main__":
    microondas = Microondas()
    microondas.ejecutar()