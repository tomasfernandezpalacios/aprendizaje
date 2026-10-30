from collections import namedtuple
import csv
from datetime import datetime

Contador = namedtuple("Contador", ["fecha", "tipo", "cantidad"])

def lectura_registros(ruta: str) -> list[Contador]:
    """
        Lee el archivo csv propuesto y devuelve la información en una lista de tuplas de tipo Contador

        :param ruta: Ruta del fichero
        :return: Lista de tuplas de tipo Contador
    """

    registros = []

    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f)

        next(lector)  #hay encabezado en el archivo csv

        for fecha, tipo, cantidad in lector:                                    
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            tipo = tipo.strip()
            cantidad = int(cantidad)
            registros.append(Contador(fecha, tipo, cantidad))
    
    return registros