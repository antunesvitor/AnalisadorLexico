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

    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789><!=;\t\n "

    relacoes = [('q0', 'abcdefghijklmnopqrstuvwxyz', 'q1'),('q0', '0123456789', 'q4'), ('q0', '><', 'q8'), ('q0', '=', 'q6'), ('q0', '!', 'q11'),
                ('q1', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'q1'), ('q1', '\t\n;', 'q2'),
                ('q4', '0123456789','q4'),('q4', ';\t\n','q5'),
                ('q8', '\t\n ','q9'),('q8', '\t\n ','q9'), ('q8', '=', 'q10'),
                ('q6', '\t\n ','q7'),('q6', '=','q10'),
                ('q10', '\t\n ','q9'),
                ('q11', '=','q10')]

    alfabeto_array = [char for char in alfabeto];

    dfa_lexico = AutomatoFinitoDeterministico(['q0', 'q1','q2', 'q3', 'q4', 'q5', 'q6','q7', 'q8', 'q9','q10', 'q11'],
                                                alfabeto_array, relacoes, 'q0',['q2','q5', 'q7', 'q9'])

    cadeias = [
        "abcDE9;",
        "abc;",
        "aBCCSDFWE;",
        "2312890378;",
        ">= ",
        "<= ",
        "== ",
        "= ",
        "=123123",
        "ASDffdfdf"
        "28937kjsdkf"
    ]
    

    for cadeia in cadeias:
        resultado_cadeia = dfa_lexico.buscar_estado_final_leitura(cadeia)

        if resultado_cadeia == 'q2':
            print('a cadeia {} é um identificador.'.format(cadeia))
        elif resultado_cadeia == 'q5':
            print('a cadeia {} é um número.'.format(cadeia))
        elif resultado_cadeia == 'q9':
            print('a cadeia {} é um operador relacional'.format(cadeia))
        elif resultado_cadeia == 'q7':
            print('a cadeia {} é um operador de atribuição'.format(cadeia))
        else:
            print("Não foi possível identificar o token")


if __name__ == '__main__':
    main()