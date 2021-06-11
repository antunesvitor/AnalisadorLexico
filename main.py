from AutomatoDeterministicoModule import AutomatoFinitoDeterministico

def main():

    # Q = {q0, q1, q2, q3},
    # ∑ = {0, 1},
    # q0 = {q0},
    # F = {q2}
    relacoes = [('q0', '0', 'q3'),('q0', '1', 'q1'),
                ('q1', '0', 'q2'), ('q1', '1', 'q1'),
                ('q2', '0', 'q2'), ('q2', '1', 'q1'),
                ('q3', '0', 'q3'), ('q3', '1', 'q3')]

    primeiro_dfa = AutomatoFinitoDeterministico(['q0', 'q1', 'q2', 'q3'], ['0', '1'], relacoes, 'q0',['q2'])

    cadeias = [
        "00001",
        "011110",
        "10000",
        "111111",
        "111110",
        "10101010",
        "1010101"
    ]

    for cadeia in cadeias:

        if primeiro_dfa.validar_cadeia(cadeia):
            print("AFD aceita {}".format(cadeia));
        else:
            print("AFD não aceita {}".format(cadeia));


if __name__ == '__main__':
    main()