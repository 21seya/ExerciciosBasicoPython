try:
    a = open('arquivo.txt','r')
except:
    print('Deu erro!')
    a = open('arquivo.txt','w')
    a.write('ERRO!!!!!!!!')  
finally:     
    a.close() 
    