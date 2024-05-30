
def filtrar(umbral, filtro = 'mayor'):
    precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000}
    filtros={}
    if str.lower(filtro) == 'mayor':
        filtros = {k:v for k,v in precios.items() if v > umbral}
    elif 'menor' == str.lower(filtro):
        filtros = {k:v for k,v in precios.items() if v < umbral}
    elif 'menor' != str.lower(filtro) and 'mayor' != str.lower(filtro): 
        print('Lo sentimos, no es una operación válida')
    return filtros


a = filtrar(30000, 'otro')
print (a)
