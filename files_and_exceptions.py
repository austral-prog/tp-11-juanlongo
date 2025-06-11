def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    ventas = {}
    with open(filename, 'r') as f:
        contenido = f.read().strip()
        if not contenido:
            return ventas
        items = contenido.split(';')
        for item in items:
            if not item:
                continue
            if ':' not in item:
                continue
            producto, valor = item.split(':', 1)
            producto = producto.strip()
            valor = float(valor.strip())
            if producto not in ventas:
                ventas[producto] = []
            ventas[producto].append(valor)
    return ventas


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for producto, montos in data.items():
        total = sum(montos)
        promedio = total / len(montos) if montos else 0
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
