def segundo_maior(lista):
    lista_unica = list(set(lista))
    lista_unica.sort()
    return lista_unica[-2] if len(lista_unica) > 1 else None
print(segundo_maior([987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]))
