from estadisticas import *

def mostrar_iterable_tab(iterable):
    for elemento in iterable:
        print("\t", elemento)

def test_lectura_registros(registros):
    print("TESTEANDO LA FUNCIÓN LECTURA_REGISTROS")
    print(f"Se han leído {len(registros)} registros.")
    print("Los tres primeros son: ")
    mostrar_iterable_tab(registros[:3])
    print()
    print("Los tres últomos son: ")
    mostrar_iterable_tab(registros[-3:])

def main_tests():
    registros = lectura_registros("data/registros.csv")
    test_lectura_registros(registros)

if __name__ == "__main__":
    main_tests()