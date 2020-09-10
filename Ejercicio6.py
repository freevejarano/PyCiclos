def palindroma(palabra):
    j = 0
    k= len(palabra)-1
    aux=''
    palabra=palabra.lower()
    while(j < len(palabra)):
        aux+=palabra[k]
        j += 1
        k -=1
    if(palabra==aux):
        print('La palabra ',palabra,' es palindroma')
    else:
        print('La palabra ',palabra,' no es palindroma')

    return palabra==aux