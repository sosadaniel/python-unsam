import csv

def parse_csv(objeto_iterable, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    if select != None and has_headers == False:
        raise RuntimeError('Para seleccionar, necesito encabezados.')
    
    rows = csv.reader(objeto_iterable)
    if has_headers:
        headers = next(rows)
        if select:
            indices = [headers.index(nombre_columna) for nombre_columna in select]
            headers = select                
        else:
            indices = []
        registros = []

        for i,row in enumerate(rows):
            try:
                if not row:    # Saltea filas sin datos
                    continue
                if indices: 
                    row = [row[index] for index in indices]
                if types:
                    row = [func(val) for func, val in zip(types, row) ]
                registro = dict(zip(headers, row))
                registros.append(registro)
            except Exception as e:
                if not silence_errors:
                    print(f'No se pudo procesar la fila {i}: {row}')
                    print(f'Motivo: {e}')
    else:
        registros = [tuple(row) for row in rows]

    return registros