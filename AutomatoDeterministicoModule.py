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
            raise ValueError("O caractere {} não pertence ao alfabeto".format(caractere));

    def __init__(self, estados, alfabeto, relacoes, estadoInicial, estadosFinais):
        self.estados = estados;
        self.alfabeto = alfabeto;

        #validar se os estados estão na lista de estados e se o simbolo lido
        #e validar se o símbolo lido também está no alfabeto
        for (qi, simbolos, qf) in relacoes:

            self.__verificar_estado(qi);
            self.__verificar_estado(qf);

            for simbolo in simbolos:
                self.__verificar_caractere(simbolo)

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
            estadoNovo = [qf for (qi, x, qf) in lista_relacoes_atuais if caractere in x]

            if estadoNovo == None or estadoNovo == []:
                return None

            estadoAtual = estadoNovo[0]

        return estadoAtual;

    def analisar_cadeia(self, cadeia):
        """Retorna uma lista ordenada de estados finais encontrados"""

        estadoAtual = self.estadoInicial;
        listaDeTokensEncontrados = []
        i = 0
        while i < len(cadeia):
            
            #pega as funções de transição que o estadoAtual possui
            lista_relacoes_atuais = [relacao for relacao in self.relacoes if relacao[0] == estadoAtual]
            
            caractere = cadeia[i]

            #busca o novo estado após ler o caractere
            estadoNovo = [qf for (qi, x, qf) in lista_relacoes_atuais if caractere in x]

            # print('esta em {} leu {} e vai para {}'.format(estadoAtual, caractere, estadoNovo))

            if estadoNovo == [] or estadoNovo == None:

                # estadoNovo é invalido, isto é, precisa retornar a origem pois não é possível formar um token valido
                # mesmo assim None deve ser gravado mostrando que não é possível formar token em parte da cadeia
                # isso é suficiente para erguer um erro e interromper uma compilação
                estadoAtual = self.estadoInicial;
                listaDeTokensEncontrados.append(None)

            elif estadoAtual in self.estadosFinais and self.estadoInicial in estadoNovo: 

                #verifica se encontrou um token e precisa retornar o simbolo
                listaDeTokensEncontrados.append(estadoAtual)
                estadoAtual = self.estadoInicial

                # como isso significa o fim de um token e inicio de outro, 
                # precisamos retornar uma posição para ele ler esse caratere novamente mas partindo do estado inicial
                i -= 1 

            else:
                estadoAtual = estadoNovo[0]

            i += 1

        if estadoAtual in self.estadosFinais:
            listaDeTokensEncontrados.append(estadoAtual);

        return listaDeTokensEncontrados


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
