import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(nombre_columna) for nombre_columna in select]
                headers = select
            else:
                indices = []
            registros = []

            for row in rows:
                if not row:    # Saltea filas sin datos
                    continue
                if indices: 
                    row = [row[index] for index in indices]
                if types:
                    row = [func(val) for func, val in zip(types, row) ]
                registro = dict(zip(headers, row))
                registros.append(registro)
        else:
            registros = [tuple(row) for row in rows]

    return registros