from AutomatoDeterministicoModule import AutomatoFinitoDeterministico

def main():


    #O analisador lexico tem como objetivo descobrir se uma palavra é um
    #identificador, numero, pontuacao, operador relacional ou operador de atribuição
    #De modo que:
    #IDENTIFICADOR: (a-z)(a-z|A-Z|0-9)*
    #NUMERO: (0-9)+
    #PONTUACAO: ;
    #OPERADOR RELACIONAL: > | >= | < | <= | == | !=
    #ATRIBUIÇÃO: = 

    #DFA para saber se uma cadeia de zeros e um's começa com 1 e termina em zero

    alfabeto = "01"
    relacoes = [('q0', '1', 'q1'),
                ('q1', '0', 'q2'),
                ('q2', '1', 'q3')]

    alfabeto_array = [char for char in alfabeto];

    dfa_lexico = AutomatoFinitoDeterministico(['q0', 'q1', 'q2','q3'], alfabeto_array, relacoes, 'q0',['q3'])

    cadeias = [
        "00001",
        "011110",
        "10000",
        "111111",
        "111110",
        "10101010",
        "1010101",
        "101"
    ]

    for cadeia in cadeias:

        if dfa_lexico.validar_cadeia(cadeia):
            print("AFD aceita {}".format(cadeia));
        else:
            print("AFD não aceita {}".format(cadeia));


if __name__ == '__main__':
    main()