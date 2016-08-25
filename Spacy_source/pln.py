# -*- coding: utf-8 -*-

# Cadete: Processamento de linguagem natural
#
# Author: Luís Augusto Weber Mercado <lawmercado@inf.ufrgs.br>
#

"""
Módulo de processamento de linguagem natural (PLN).

"""

from singleton import Singleton
from spacy.en import English

class PLN(metaclass=Singleton):

    def __init__(self):
        self.api = English(entity = False, matcher = False) # Não usa-se todos os recursos
        self.analise = None

    def analisar(self, texto):
        """
        A partir de uma frase, dá início a pipeline de análise

        :param texto: Texto a ser analisado
        :type texto: string
        """

        assert isinstance(texto, str), "O argumento da função 'analisar' deve ser um texto!"

        # Faz a análise sintática da frase
        doc = self.api(texto)

        sentencas = self.__normalizarAnaliseSintatica(doc)

        self.mostrarAnaliseSintatica(sentencas)

    def __normalizarAnaliseSintatica(self, doc):
        """
        Normaliza a análise feita pela api para objetos manejáveis pelos outros
        processos da aplicação

        :param doc: Análise provinda da API
        :type doc: object

        :return: Sentencas com suas devidas informações
        :rtype: list
        """

        sentencas = []

        for frase in doc.sents:
            sentenca = Sentenca(str(frase))

            for palavra in frase:
                if not palavra.is_punct:
                    token = Token(palavra.text)
                    token.posTag = palavra.tag_
                    token.lemma = palavra.lemma_
                    token.dependencia = self.obterDependenciasDoToken(frase, palavra)

                    sentenca.tokens.append(token)

            sentencas.append(sentenca)

        return sentencas

    def obterDependenciasDoToken(self, sentenca, token):
        """
        A partir do token, navega pela árvore de sintaxe até a raiz, obtendo as dependencias

        :param token: Token a ser analisado
        :type token: object

        :return: Tupla com a relação mais próxima
        :rtype: tuple ou None
        """

        dependencia = None
        iPai = None
        iFilho = None

        for i, item in enumerate(sentenca):
            if item is token:
                iFilho = i
            elif item is token.head:
                iPai = i
            elif iPai is not None and iFilho is not None:
                break

        # Na spacy, a raiz tem seu pai (head) como ela mesma
        if token.head is not token:
            dependencia = ("{0} - {1}".format(iPai, token.head.text), token.dep_, "{0} - {1}".format(iFilho, token.text))

        return dependencia
     
		
		
		
    def mostrarAnaliseSintatica(self, sentencas):
        for sentenca in sentencas:
            print("Sentença: {0}".format(sentenca.texto))

            for token in sentenca.tokens:
                print("\tToken: ({0}, {1}, {2})".format(token.texto, token.posTag, token.lemma))
                print("\t\tDependência: {0}".format(token.dependencia))
                print("")

            print("")
	
    #imprimindo 
  #  def dependency_labels_to_root(token):
   #     '''Walk up the syntactic tree, collecting the arc labels.'''
    #    dep_labels = []
    #    while token.head is not token:
    #        dep_labels.append(token.dep_)
            #token = token.head
        #return dep_labels
    		
	#def achar_verbo_arvore(doc):
	
     #   print \"verbo:\" + doc.text_with_ws
        #for token in tree:
        #    if word.tag_ in ('VBZ'):
        #        print 'verb:' + word.text_with_ws 
            
    
    #for sent in sentences:
      #  print \"--\"
      #  print \"Sentenca: \"+ sent
       # doc = nlp(unicode(sent))
      #  for word in doc:
            
            #print word.text_with_ws 
            #print  dependency_labels_to_root(word)
            #print word.text_with_ws + ' '+word.tag_
           # if word.dep_ in ('nsubj' , 'csubj'):
          #      sujeito = ''.join(w.text_with_ws for w in word.subtree)
          #      print 'sujeito: ' + sujeito
            
            #if word.tag_ in ('VBZ'):
            #    print 'verb:' + word.text_with_ws
            #    #print(''.join(w.text_with_ws for w in word.subtree))
            
            
          # if word.dep_ in ('dobj', 'iobj'):
          #      obj=''.join(w.text_with_ws for w in word.subtree)
          #      print 'objeto: ' + obj
           #     print \"verbo: \" + word.head.text_with_ws
                #achar_verbo_arvore(word.head)
                
            
          #      \n
class Sentenca:

    def __init__(self, texto):
        self.texto = texto
        self.tokens = []

class Token:

    def __init__(self, texto):
        self.texto = texto
        self.posTag = None
        self.lemma = None
        self.dependencia = None
