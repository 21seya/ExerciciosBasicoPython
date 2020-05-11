def replace(frase,velha,nova):
    palavra = ''
    i = 0
    while i <len(frase) + 1 -len(velha):
        if frase[i:i+len(velha)] != velha:
          palavra += frase[i]
        else:
            i += len(velha)
            palavra += nova 
            continue
        i += i

    palavra += frase[i]

    return palavra

print(replace('mississippi','ss','zzz'))
    