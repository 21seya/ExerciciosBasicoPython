class NossoContextManager():
    def imprime(self,msg):
        print(msg)

    def __enter__(self):
        print('Entrando no bloco with')
        return self

    def __exit__(self,tipo,valor,traceback):
        print(tipo,valor,traceback)
                