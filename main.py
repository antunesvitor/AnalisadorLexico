from AutomatoDeterministicoModule import AutomatoFinitoDeterministico

def main():


    #O analisador lexico tem como objetivo descobrir se uma palavra é um
    #identificador, numero, pontuacao, operador relacional ou operador de atribuição
    #De modo que:
    #IDENTIFICADOR: (a-z)(a-z|A-Z|0-9)*
    #NUMERO: (0-9)+
    #PONTUACAO: ;
    #SEPERACAO: espaço em branco, \t ou \n
    #OPERADOR RELACIONAL: > | >= | < | <= | == | !=
    #ATRIBUIÇÃO: = 

    #DFA para saber se uma cadeia de zeros e um's começa com 1 e termina em zero

    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789><!=;\t\n "

    relacoes = [('q0', 'abcdefghijklmnopqrstuvwxyz', 'q1'),('q0', '0123456789', 'q2'), ('q0', '=', 'q3'), ('q0', '><', 'q5'), ('q0', '!', 'q6'), ('q0', ' \t\n', 'q7'), ('q0', ';', 'q8'),
                ('q1', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'q1'), ('q1', '><!=;\t\n ', 'q0'),
                ('q2', '0123456789','q2'), ('q2', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ;\t\n><!= ','q0'),
                ('q3', '=','q4'), ('q3', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789><!;\t\n ','q0'),
                ('q4', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789><!=;\t\n ', 'q0'),
                ('q5', '=','q4'), ('q5', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789><!;\t\n ','q0'),
                ('q6', '=','q4'),
                ('q7', ' \t\n', 'q7'), ('q7', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789><!=;', 'q0'),
                ('q8', ';', 'q8'), ('q8', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789><!=\t\n ', 'q0')]

    alfabeto_array = [char for char in alfabeto];

    dfa_lexico = AutomatoFinitoDeterministico(['q0', 'q1','q2', 'q3', 'q4', 'q5', 'q6','q7', 'q8'],
                                                alfabeto_array, relacoes, 'q0',['q1', 'q2', 'q3', 'q4', 'q5', 'q7', 'q8'])


    #dando nomes aos bois, digo, atribuindo nomes aos estados terminais de nosso AFD (que são os tokens retornados)
    nomesTokens = {
        'q1': 'IDENTIFICADOR', 
        'q2': 'NÚMERO',
        'q3': 'ATRIBUIÇÃO',
        'q4': 'RELAÇÃO',
        'q5': 'RELAÇÃO',
        'q7': 'SEPARADOR',
        'q8': 'PONTUADOR',
        None: 'INVÁLIDO'
    }

    cadeias = [ "abc=5;\n3284238 <= 78912312\t "] 
    

    for cadeia in cadeias:
        lista_de_tokens = dfa_lexico.analisar_cadeia(cadeia)

        strg = ''

        for token in lista_de_tokens:

            if token != 'q7':
                strg += '{} '.format(nomesTokens[token])

        print(cadeia)
        print(strg)
            

if __name__ == '__main__':
    main()