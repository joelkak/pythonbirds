class Pessoa:
    olhos= 2

    def __init__(self, *filhos, nome=None, idade=43):
        self.idade = idade
        self.nome= nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
    @staticmethod
    def metodo_statico( ):
        return 43

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos { cls.olhos} '

if __name__ == '__main__':
    renzo = Pessoa(nome= 'Renzo')
    luciano = Pessoa(nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome ='Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos) , id(renzo.olhos))
    print(Pessoa.metodo_statico(), luciano.metodo_statico())
    print(Pessoa.nome_e_atributos_de_classes(), luciano.nome_e_atributos_de_classes())

