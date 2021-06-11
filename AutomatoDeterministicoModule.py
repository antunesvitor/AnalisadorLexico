class AutomatoFinitoDeterministico:

    estados = [];
    estadoInicial = '';
    estadosFinais = [];
    relacoes = [];
    #relacoes = [("q1",'x', "q2"), ("q1", 'y', "q3"), ....]
    alfabeto = [];


    def __verificar_estado(self, estado):
        if not estado in self.estados:
            raise ValueError("O estado {} não pertence ao conjunto de estados".format(estado));

    def __verificar_caractere(self, caractere):
        if not caractere in self.alfabeto:
            raise ValueError("O estado {} não pertence ao conjunto de estados".format(caractere));

    def __init__(self, estados, alfabeto, relacoes, estadoInicial, estadosFinais):
        self.estados = estados;
        self.alfabeto = alfabeto;

        #validar se os estados estão na lista de estados e se o simbolo lido
        #e validar se o símbolo lido também está no alfabeto
        for (qi, i, qf) in relacoes:

            self.__verificar_estado(qi);
            self.__verificar_estado(qf);

            if (not i in estados):
                self.__verificar_caractere(i)

        self.relacoes = relacoes;

        self.__verificar_estado(estadoInicial);

        for estadoFinal in estadosFinais:
            self.__verificar_estado(estadoFinal);

        self.estadoInicial = estadoInicial;
        self.estadosFinais = estadosFinais;


    def  buscar_estado_final_leitura(self, cadeia):
        """Retorna o estado final do AFD após ler a cadeia"""
        estadoAtual = self.estadoInicial;
        
        for caractere in cadeia:

            #pega as funções de transição que o estadoAtual possui
            lista_relacoes_atuais = [relacao for relacao in self.relacoes if relacao[0] == estadoAtual]

            #busca o novo estado após ler o caractere
            estadoAtual = [qf for (qi, x, qf) in lista_relacoes_atuais if x == caractere]
            estadoAtual = estadoAtual[0]

        return estadoAtual;

    def validar_cadeia(self, cadeia):
        """Retorna true caso o ultimo estado do AFD após ler a cadeia é um estado final (aceita) ou false caso contrário (rejeita)"""
        estado_final_leitura = self.buscar_estado_final_leitura(cadeia);

        return estado_final_leitura in self.estadosFinais;


    def __str__(self):
        _str = "({}, {},".format(self.estados, self.alfabeto);

        for (qi, i, qf) in self.relacoes:
            _str += "{} <- {} = {} |".format(qi, i, qf);

        _str += ",{}, {})".format(self.estadoInicial, self.estadosFinais);

        return _str;
