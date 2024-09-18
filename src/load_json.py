import json

def load_json_to_database(json_filename, output_filename):
    """
    Lee datos de un archivo JSON y los guarda en un nuevo archivo JSON.

    :param json_filename: Nombre del archivo JSON de entrada.
    :param output_filename: Nombre del archivo JSON de salida.
    """
    # Leer datos del archivo JSON
    with open(json_filename, 'r') as json_file:
        scores = json.load(json_file)

    # Guardar datos en un nuevo archivo JSON
    with open(output_filename, 'w') as output_file:
        json.dump(scores, output_file, indent=4)

# Ejemplo de uso
if __name__ == "__main__":
    load_json_to_database('scores.json', 'new_scores.json')



def process_json_data(json_filename):
    """
    Lee datos de un archivo JSON y los procesa (en este caso, los imprime).

    :param json_filename: Nombre del archivo JSON de entrada.
    """
    # Leer datos del archivo JSON
    with open(json_filename, 'r') as json_file:
        scores = json.load(json_file)

    # Procesar los datos (en este caso, simplemente imprimirlos)
    for score in scores:
        print(f"Player: {score['player']}, Score: {score['score']}, Time: {score['time']}, Level: {score['level']}")

# Ejemplo de uso
if __name__ == "__main__":
    process_json_data('scores.json')
