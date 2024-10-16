class Proceso:
    def __init__(self, etiqueta, BT, AT, Q, Pr):
        self.etiqueta = etiqueta
        self.BT = BT  # Burst Time
        self.AT = AT  # Arrival Time
        self.Q = Q    # Queue
        self.Pr = Pr  # Priority
        self.WT = 0   # Wait Time
        self.CT = 0   # Completion Time
        self.RT = 0   # Response Time
        self.TAT = 0  # Turnaround Time

def leer_procesos(archivo):
    procesos = []
    with open(archivo, 'r') as f:
        lines = f.readlines()[2:]  # Saltar las dos primeras líneas
        for line in lines:
            data = line.strip().split(';')
            etiqueta = data[0].strip()
            BT = int(data[1].strip())
            AT = int(data[2].strip())
            Q = int(data[3].strip())
            Pr = int(data[4].strip())
            procesos.append(Proceso(etiqueta, BT, AT, Q, Pr))
    return procesos

def escribir_salida(procesos, nombre_archivo):
    with open(nombre_archivo, "w") as f:
        f.write(f"# archivo: {nombre_archivo}\n")
        f.write("# etiqueta; BT; AT; Q; Pr; WT; CT; RT; TAT\n")
        for proceso in procesos:
            f.write(f"{proceso.etiqueta};{proceso.BT};{proceso.AT};{proceso.Q};{proceso.Pr};{proceso.WT};{proceso.CT};{proceso.RT};{proceso.TAT}\n")
        
        # Cálculo de promedios
        promedio_WT = sum(p.WT for p in procesos) / len(procesos)
        promedio_CT = sum(p.CT for p in procesos) / len(procesos)
        promedio_RT = sum(p.RT for p in procesos) / len(procesos)
        promedio_TAT = sum(p.TAT for p in procesos) / len(procesos)
        
        f.write(f"WT={promedio_WT}; CT={promedio_CT}; RT={promedio_RT}; TAT={promedio_TAT};\n")

def algoritmo_MLQ(procesos):
    tiempo = 0
    for proceso in procesos:
        if tiempo < proceso.AT:
            tiempo = proceso.AT  # Avanzar al tiempo de llegada

        # Calcular tiempos
        proceso.WT = tiempo - proceso.AT
        proceso.CT = tiempo + proceso.BT
        proceso.TAT = proceso.CT - proceso.AT
        proceso.RT = proceso.WT  # Simplificación para este caso

        # Avanzar el tiempo
        tiempo = proceso.CT

# Leer procesos del archivo
procesos_mlq001 = leer_procesos("mlq001.txt")

# Ejecutar el algoritmo MLQ
algoritmo_MLQ(procesos_mlq001)

# Escribir resultados en el archivo de salida
escribir_salida(procesos_mlq001, "salida_mlq001.txt")
