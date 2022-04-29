"""
Voce deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a responsabilida de controlar a velocidade.
Ele oferece os seguintes atributos:
1)Atributo de dado de velocidade
2)Método acelerar, que devera incrementar a velocidade de uma unidade
3)Método frear que devera decrementar a velocidade em duas unidades

A direção tera a responsabilidade de controlar a direção. Ela ofrece os seguintes atributos:
1)Valor de direção com valores possiveis: Norte , sul , leste , oeste.
2)Metodo girar_a_direita
3) Método girar_a_esquerda

    N
 O     L
    S

    Exemplo:
    # Testando motor
    >>>motor = Motor()
    >>>motor.velocidade
    0
    >>>motor.acelerar()
    >>>motor.velocidade
    1
    >>>motor.acelerar()
    >>>motor.velocidade
    2
    >>>motor.acelerar()
    >>>motor.velocidade
    3
    >>>motor.Frear()
    >>>motor.velocidade
    1
    >>>motor.acelerar()
    >>>motor.velocidade
    0
    >>># Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>>direcao.girar_a_direita()
    >>>direcao.valor
    'leste"
     >>>direcao.girar_a_direita()
    >>>direcao.valor
    "Sul"
     >>>direcao.girar_a_direita()
    >>>direcao.valor
    "Oeste"
     >>>direcao.girar_a_direita()
    >>>direcao.valor
    'Norte"
     >>>direcao.girar_a_esquerda()
     >>>direcao.valor
    'Oeste'
    >>>direcao.girar_a_esquerda()
     >>>direcao.valor
     'Sul'
     >>>direcao.girar_a_esquerda()
     >>>direcao.valor
     'Leste
     >>>direcao.girar_a_esquerda()
     >>>direcao.valor
     'Norte'
     >>> carro = Carro(direcao, motor)
     >>> carro.calcular_velocidade()
     0
     >>> carro.acelerar()
     >>> carro.calcular_velocidae()
     1
     >>> carro.acelerar()
     >>> carro.calcular_velocidae()
     2
    >>> carro.frear()
     >>> carro.calcular_velocidae()
     0
     >>> carro.calcular_direcao()
     >>> 'Norte'
     >>> carro.calcular_direcao()
     >>> carro.girar_a_direita()
     >>> 'Leste'
     >>> carro.calcular_direca()
     >>> carro.girar_a_esquerda()
     >>> 'Norte'
     >>> carro.calcular_direca()
     >>> carro.girar_a_esquerda()
     >>> 'Oeste'





    """