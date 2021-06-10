from AutomatoDeterministicoModule import AutomatoFinitoDeterministico

def main():

    # Q = {a, b, c},
    # ∑ = {0, 1},
    # q0 = {a},
    # F = {c}
    relacoes = [('a', 0, 'a'),('a', 1, 'b'),
                ('b', 0, 'c'), ('b', 1, 'a'),
                ('c', 0, 'a'), ('c', 1, 'c')]
    primeiro_dfa = AutomatoFinitoDeterministico(['a', 'b', 'c'], [0, 1], relacoes, 'a',['c'])

    print(primeiro_dfa);


if __name__ == '__main__':
    main()