def conta_palavras(texto):
    contador = {}
    for palavra in texto.split(''):
        corrente = contador.get(palavra,0)

        contador[palavra] = corrente+1
    return contador    
    