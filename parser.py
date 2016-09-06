
# -*- coding: utf-8 -*-
###IMPORT
#starting spacy
from __future__ import unicode_literals
def NewFunction():
    return u'£'

from spacy.en import English
#from __future__ import unicode_literals   
nlp = English()
import sys

#import resource
#import sys


#opening sentences file
f = open('sentences.txt', 'r')
sentences = f.readlines()



#------------------------------------------------------- PEGAR O TIPO DE SENTENÇA--------------------------------------------------------------
def get_type_senteces(doc):
	for idx, val in enumerate (doc):          
		if isSIGNAL_WORDS_XOR(idx,val,doc):
			return TIPO_SENTENCA_XOR
	for idx, val in enumerate (doc):          
		if isSIGNAL_WORDS_AND(idx,val,doc):
		    return TIPO_SENTENCA_AND
	return TIPO_SENTENCA_OTHERS    
     
#-------------------------------------------------------SIGNAL WORDS--------------------------------------------------------------
def isSIGNAL_WORDS_XOR(idx,val,doc):
    #print (val)
    #print("passo por aqui 1")
    if "if" == str(val).lower():
     #  print("passo por aqui 2")
        
        z=doc[idx+1]       
        if "not" == str(z).lower(): 
            #print("passo por aqui 3")
            return True
    elif "if" == str(val).lower()  or "otherwise"  == str(val).lower() or "either"  == str(val).lower() or  "only"  == str(val).lower() or "till"  == str(val).lower() or "until"  == str(val).lower() or "when"  == str(val).lower():
        #print("passo por aqui 4")
        return True
    
    elif "in"  == str(val).lower():
        #print("passo por aqui 5")
        z=doc[idx+1]
        y=doc[idx+2]
        if "case"  == str(z).lower() or ("case"  == str(z).lower() and "of"  == str(y).lower()):
            #print("passo por aqui 6")
            return True
    else:
        #print("passo por aqui 7")
        return False




def isSIGNAL_WORDS_AND(idx,val,doc):
	print (val)
	#print("passo por aqui 8")
	if "while"  == str(val).lower()  or "meanwhile" == str(val).lower() or "concurrently" == str(val).lower() or "meantime" == str(val).lower() or "simultaneously" == str(val).lower() or "whereas"  == str(val).lower():
		#print("passo por aqui 9")
		return True
	elif "In"  == str(val).lower():
		#print("passo por aqui 10")
		z=doc[idx+1]
		y=doc[idx+2]
		q=doc[idx+3]
		if ("parallel"  == str(z).lower() or ("parallel"  == str(z).lower() and "with"  == str(y).lower() and "this" == str(q).lower())):
			#print("passo por aqui 11")
			return True 
		elif ("the"  == str(z).lower() and "meantime" == str(y).lower()):
			#print("passo por aqui 12")
			return True
		elif ("addition"  == str(z).lower() and "to"  == str(y).lower()):
			#print("passo por aqui 13")
			return True
	
	elif "at"  == str(val).lower():
		#print("passo por aqui 14")
		z=doc[idx+1]
		y=doc[idx+2]
		q=doc[idx+3]
		if ("the"  == str(z).lower() and "same" == str(y).lower() and "time" == str(q).lower()):
		    #print("passo por aqui 15")
		    return True           
	else:
		#print("passo por aqui 16")
		return False


#-------------------------------------------------------IR REGRAS DE ATIVIDADE E EVENTOS--------------------------------------------------------------

# define se é atividade ou evento
def Go_Rules_Activity_Event(doc):
	#print ("sentenca3---"+ str (sent))
	Main_Verb = Definition_Main_Verb_Activity_or_Event (doc)
	Result_Verb_Tense = Definition_Verb_tense_Main_Verb(Main_Verb) 
	if (Result_Verb_Tense == TIPO_SENTENCA_Activity):
		if (Execute_Rules_Activity (doc)==True):
			print ("Is Activity")
		
		#FAZENDO AQUI
	else:
		Go_Rules_Event (doc)
		print("Is Event")
	#Não Fiz aqui


        
def Definition_Main_Verb_Activity_or_Event (doc):
	for word in doc:
		#print ("teste= "+ word.pos_)
		print(word.text_with_ws + " <- "  + word.head.text_with_ws + " ("  + word.dep_ + ")" )
			#Aqui eu comparo se a palavra é ela mesma e se ela é "root" ou seja, o verbo principal da sentenca
		if (word.text_with_ws in (word.head.text_with_ws) and  word.dep_ in ('ROOT')):
			Main_Verb1=word
			return Main_Verb1

def Definition_Verb_tense_Main_Verb (Main_Verb):
	# aqui eu vejo qual tempo verbal é o verbo principal 

	#VB Verb, base form
	# VBD Verb, past tense
	#VBG Verb, gerund or present participle
	#VBN Verb, past participle
	#VBP Verb, non-3rd person singular present
	# VBZ Verb, 3rd person singular present
	    
	print ("MAIN VERG-> "+str (Main_Verb.text_with_ws))
	print ("TAG- MAIN VERB->"+ str(Main_Verb.tag_))
	if (Main_Verb.tag_ == "VBP" or Main_Verb.tag_ == "VBZ" or Main_Verb.tag_ == "VB"):
		
		return TIPO_SENTENCA_Activity
	elif (Main_Verb.tag_ == "VBD" or Main_Verb.tag_ == "VBN" ):
		return TIPO_SENTENCA_Event

#-------------------------------------------------------REGRAS ATIVIDADES--------------------------------------------------------------
	#--------REGRA 1 ------------------- SVO
def Get_indice_Sub_Obj_rule_1 (doc):
	#print ("sentenca---"+ str (sent))
	indice_verbo=None
	indice_sujeito=None
	indice_objeto=None
	ERROR=1000
	for indice, conteudo in enumerate (doc):
			#print (''+dependency_labels_to_root(word)[0])
			#print word.text_with_ws 
			#print  dependency_labels_to_root(word)
			#print word.text_with_ws + ' '+word.tag_
			
			#indice do verbo
			if (str(doc[indice])) in (str(doc[indice].head)) and  doc[indice].dep_ in ('ROOT'):
				print ("entrou aqui 1")
				print("Verbo----->" + str(doc[indice]))
				indice_verbo=indice
	for indice, conteudo in enumerate (doc):
			#indice do sujeito
			if doc[indice].dep_ in ('nsubj' , 'csubj'):
				print ("entrou aqui 2")
				sujeito = ''.join(w.text_with_ws for w in doc[indice].subtree)
				indice_sujeito=indice
				print ('sujeito: ' + sujeito)


			#if word.tag_ in ('VBZ'):
			#    print ('verb:' + word.text_with_ws)
			#   print(''.join(w.text_with_ws for w in word.subtree))

			#indice do objeto
	for indice, conteudo in enumerate (doc):
		if doc[indice].dep_ in ('dobj', 'iobj'):
			print ("entrou aqui 3")
			obj=''.join(w.text_with_ws for w in doc[indice].subtree)
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + obj)
			indice_objeto=indice
			for w in doc[indice].subtree:
				if w.dep_ in ('dobj', 'iobj'):
					print ("entrou aqui 4")
					print ("verbo: " + doc[indice].head.text_with_ws)
					print ("-->" + w.text_with_ws)
		
			
	# verificar se há conjunção na frase, se houver entao nao é esta regra e sim a regra 4
	Rule4=False;
	for indice, conteudo in enumerate (doc):
		if doc[indice].dep_ in ('conj', 'cc', 'in'):
			#Get_rule_4 (doc)
			Rule4= True

	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or Rule4==True):
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,ERROR]
	else:
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,-1]

	return result_indice	





	result_indice = [indice_verbo,indice_sujeito,indice_objeto]
	return result_indice


	#--------REGRA 2 ------------------- WILL
def Get_indice_Sub_Obj_rule_2 (doc):
	
	indice_verbo=None
	indice_sujeito=None
	indice_objeto=None
	indice_will=None
	ERROR = 1000

	for indice, conteudo in enumerate (doc):
			#print (''+dependency_labels_to_root(word)[0])
			#print word.text_with_ws 
			#print  dependency_labels_to_root(word)
			#print word.text_with_ws + ' '+word.tag_
			
			#indice do verbo
			if (str(doc[indice])) in (str(doc[indice].head)) and  doc[indice].dep_ in ('ROOT'):
				print ("entrou aqui 1")
				print("Verbo----->" + str(doc[indice]))
				indice_verbo=indice
	for indice, conteudo in enumerate (doc):
				#indice do sujeito
				if doc[indice].dep_ in ('nsubj' , 'csubj'):
					print ("entrou aqui 2")
					sujeito = ''.join(w.text_with_ws for w in doc[indice].subtree)
					indice_sujeito=indice
					print ("indice sujeito " + str(indice_sujeito))
					print ('sujeito: ' + sujeito)
				
	
	for indice, conteudo in enumerate (doc):
		#print (str (doc[indice].dep_))
		#Advérbio é uma palavra invariável que modifica o sentido do verbo, do adjetivo e do próprio advérbio.
		#ADVCL Adverbial clause modifier 
		#ADVMOD Adverbial modifier
		if (doc[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod')):
			print ("entrou aqui 3")
			obj=''.join(w.text_with_ws for w in doc[indice].subtree)
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + obj)
			indice_objeto=indice
			for w in doc[indice].subtree:
				if w.dep_ in ('dobj', 'iobj'):
					print ("entrou aqui 4")
					print ("verbo: " + doc[indice].head.text_with_ws)
					#print ("-->" + w.text_with_ws)
					break
			print("indice_objeto-->" +str (indice_objeto))

	for indice, conteudo in enumerate (doc):    
		if "will"  == str(conteudo).lower():
			indice_will=indice
			#print("indice_will--->"+ str(indice_will))			
			break

	
	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or indice_will==None):
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,indice_will,ERROR]
	else:
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,indice_will,-1]

	return result_indice	




	#--------REGRA 3 -------------------VERB + ART + OBJ		
def Get_indice_Sub_Obj_rule_3(doc):
	
	indice_verbo=None
	indice_article=None
	indice_objeto=None	
	ERROR = 1000

	for indice, conteudo in enumerate (doc):
			#print (''+dependency_labels_to_root(word)[0])
			#print word.text_with_ws 
			#print  dependency_labels_to_root(word)
			#print word.text_with_ws + ' '+word.tag_
			
			#indice do verbo
		if (str(doc[indice])) in (str(doc[indice].head)) and  doc[indice].dep_ in ('ROOT'):
			print ("entrou aqui 1.3")
			print("Verbo----->" + str(doc[indice]))
			indice_verbo=indice
	for indice, conteudo in enumerate (doc):
		#print (str (doc[indice].dep_))
		#Advérbio é uma palavra invariável que modifica o sentido do verbo, do adjetivo e do próprio advérbio.
		#ADVCL Adverbial clause modifier 
		#ADVMOD Adverbial modifier
		if (doc[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod')):
			print ("entrou aqui 3.3")
			obj=''.join(w.text_with_ws for w in doc[indice].subtree)
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + obj)
			indice_objeto=indice
			for w in doc[indice].subtree:
				if w.dep_ in ('dobj', 'iobj'):
					print ("entrou aqui 3.3")
					print ("verbo: " + doc[indice].head.text_with_ws)
					#print ("-->" + w.text_with_ws)
					break
			
	for indice, conteudo in enumerate (doc):    
		if (doc[indice].dep_ in ('DT', 'det') or "a"  == str(conteudo).lower() or "an"  == str(conteudo).lower()):
			indice_article=indice
			print("indice_artigo--->"+ str(indice_article))
			print ("artigo-->" + str(conteudo))
			break

	print ("V->"+str(indice_verbo))		
	print ("a->"+str(indice_article))	
	print ("O->"+str(indice_objeto))	
	if (indice_verbo==None or indice_article==None or indice_objeto==None):
		result_indice = [indice_verbo,indice_article,indice_objeto,ERROR]
	else:
		result_indice = [indice_verbo,indice_article,indice_objeto,-1]
	return result_indice

def Get_rule_4(doc):
	
	ERROR=1000
	#Se o lado esquerdo ou direito for verdadeiro é tarefa senao não é tarefa
	Left= False
	Right = False
	for idx, val in enumerate (doc):
		if (("and" == str(val).lower() or "or" == str(val).lower()) and idx > 2):
			
			vetor_all= sent.split('and')
			String_vetor_left=vetor_all[0]
			String_vetor_right= vetor_all[1]
			# colocando cada frase em um doc para verificar se a frase do lado direito ou esquerdo é realmente uma tarefa
			doc_Left = nlp(String_vetor_left)
			doc_Right = nlp(String_vetor_right)


			#------------------------------------VERIFICA REGRA 1

			#------------------------------------LEFT ------------------
			vetor_result_indice_rule1= Get_indice_Sub_Obj_rule_1(doc_Left)
			Result_rule_1= Check_vetor_rule_1 (vetor_result_indice_rule1)
			if (Result_rule_1 == True):					
					Activity=True
					Left=True
					print ("LEFTTTTTTTTTT")
					
			#------------------------------------RIGHT --------------------		
			vetor_result_indice_rule1= Get_indice_Sub_Obj_rule_1(doc_Right)
			Result_rule_1= Check_vetor_rule_1 (vetor_result_indice_rule1)
			if (Result_rule_1 == True):				
					Activity=True
					Right=True
					print ("Rightttttttttt")
					
			#------------------------------------VERIFICA REGRA 2
			#------------------------------------LEFT ------------------		
			if (Left==False):				
				vetor_result_indice_rule2= Get_indice_Sub_Obj_rule_2(doc_Left)
				Result_rule_2= Check_vetor_rule_2(vetor_result_indice_rule2)
				if (Result_rule_2 == True):						
					Activity=True
					Left=True
					print ("LEFTTTTTTTTTT")
					
			#------------------------------------RIGHT ------------------		
			if (Right==False):
				vetor_result_indice_rule2= Get_indice_Sub_Obj_rule_2(doc_Right)
				Result_rule_2= Check_vetor_rule_2(vetor_result_indice_rule2)
				if (Result_rule_2 == True):						
					Activity=True
					Right=True
					print ("Rightttttttttt")						
						
			#------------------------------------VERIFICA REGRA 3 
			#------------------------------------LEFT ------------------	
			if (Left==False):
				vetor_result_indice_rule3= Get_indice_Sub_Obj_rule_3(doc_Left)
				Result_rule_3= Check_vetor_rule_3 (vetor_result_indice_rule3)
				if (Result_rule_3 == True):						
					Activity=True
					Left=True
					print ("LEFTTTTTTTTTT")
						
			#------------------------------------Right ------------------	
			if (Right==False):
				vetor_result_indice_rule3= Get_indice_Sub_Obj_rule_3(doc_Right)
				Result_rule_3= Check_vetor_rule_3 (vetor_result_indice_rule3)
				if (Result_rule_3 == True):						
					Activity=True
					Right=True
					print ("Rightttttttttt")
			break

	if (Left == True and Right ==True):
	 	print("OK")
	 	return True
	else:
		print ("FALSE")
		return False
def Check_vetor_rule_1 (vetor):
	ERROR=1000

	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_1(doc)
	if (vetor[3] == ERROR):
		print ("entrou aqui 1.flag")
		print ("R1- ERROR")
		
		return False
		
	else:
		#Deu CERTO
		indice_verbo2 = vetor[0]
		indice_sujeito2=vetor[1]
		indice_objeto2= vetor[2]
		
		if (indice_sujeito2<indice_verbo2 and indice_verbo2<indice_objeto2):
			#regra 1
			print("Regra do SVO")
			print("Sentença: "+ sent)
			print("-------------------------")
			print("Indica-se uma Tarefa ")
			print("-------------------------")
			return True
		else:
			print ("R1- ERROR")
			return False

def Check_vetor_rule_2 (vetor):
	ERROR=1000
	if (vetor[4] == ERROR):
		print ("entrou aqui 2.flag")
		print ("R2- ERROR")
		return False

	else:

		indice_verbo2 = vetor[0]
		indice_sujeito2 =vetor[1]
		indice_objeto2=vetor[2]
		indice_will = vetor[3]
		
		if (indice_sujeito2<indice_will and indice_will < indice_verbo2 and indice_verbo2 < indice_objeto2):
			print("Regra do WILL")
			print ("Sentença: "+ sent)
			print("-------------------------")
			print ("Indica-se uma Tarefa ") 
			print("-------------------------")
			return True
		else:
			print ("R2- ERROR")
			return False

def Check_vetor_rule_3 (vetor):
	ERROR=1000
	if (vetor[3] == ERROR):
				print ("entrou aqui 3.flag")
				print ("R3- ERROR")
				return False
		
	else:	

		indice_verbo3 = vetor[0]
		indice_article3=vetor[1]
		indice_objeto3= vetor[2]

		if (indice_verbo3<indice_article3 and indice_article3<indice_objeto3):
			print("Regra do VAO")
			print("Sentença: "+ sent)
			print("-------------------------")
			print("Indica-se uma Tarefa ")
			print("-------------------------")
			return True
		else:
			print ("R3- ERROR")
			return False

def Execute_Rules_Activity(doc):		
	
	flag=1
	ERROR=1000
	flag2=1
	flag3=1
	Activity=False
	#--------REGRA 1 ------------------- SVO
	if (flag==1):
		vetor_result_indice_rule1= Get_indice_Sub_Obj_rule_1(doc)		
		Result_rule_1 = Check_vetor_rule_1 (vetor_result_indice_rule1) 
		if (Result_rule_1 == True):
				#ACTIVITY_RULE_1= ACTIVITY_RULE_1+1
				Activity=True
				flag=2
				return Activity			
	#--------REGRA 2 ------------------- S + WILL + VERB+OBJ	
	if (flag==1):
		
		vetor_result_indice_rule2 = Get_indice_Sub_Obj_rule_2(doc)	
		Result_rule_2= Check_vetor_rule_2 (vetor_result_indice_rule2)
		if (Result_rule_2 == True):
				#ACTIVITY_RULE_1= ACTIVITY_RULE_1+1
				Activity=True
				flag=2
				return Activity	
	#--------REGRA 3 ------------------- <Verb>+<article>+<Obj>
	
	if (flag==1):
		vetor_result_indice_rule3= Get_indice_Sub_Obj_rule_3(doc)
		Result_rule_3= Check_vetor_rule_3 (vetor_result_indice_rule3)
		if (Result_rule_3 == True):
				#ACTIVITY_RULE_1= ACTIVITY_RULE_1+1
				Activity=True
				flag=2
				return Activity

	#--------REGRA 4 ------------------- < Sujeito> + <verb> + <obj> [and,or] + <verb> + <obj>
	if (flag==1):
		
		result_rule_4= Get_rule_4(doc)
		
		if (result_rule_4 ==True):
			print("Regra do Sujeito> + <verb> + <obj> [and,or] + <verb> + <obj>")
			print("Sentença: "+ sent)
			print("-------------------------")
			
			print("-------------------------")
			flag=2
			Activity=True
			return Activity
	
	if (Activity==False):		
		print("Sentença: "+ sent+"---> Não definida pelo protótipo")
		
#-------------------------------------------------------TESTES AQUIIIII--------------------------------------------------------------

def Testes_Aqui  (doc):
	for word in doc:
		#print ("teste= "+ word.pos_)
		print(word.text_with_ws + " <- "  + word.head.text_with_ws + " ("  + word.dep_ + ")" )
			#Aqui eu comparo se a palavra é ela mesma e se ela é "root" ou seja, o verbo principal da sentenca
		if (word.text_with_ws in (word.head.text_with_ws) and  word.dep_ in ('ROOT')):
			Main_Verb1=word

	print ("MAIN VERG-> "+str (Main_Verb1.text_with_ws))
	print ("TAG- MAIN VERB->"+ str(Main_Verb1.tag_))
	
#-------------------------------------------------------MAIN--------------------------------------------------------------

i=0

for sent in sentences:
	
	print ("--")
	print ("Sentenca " + str(i) + " inicial: "+ sent)
	#-------------------NOTEBOOK-----------------------------------
	
	sent = sent.replace(".","").replace("\n","")
	sent = (u'The first activity is to check and repair the hardware.')
	doc = nlp(sent)
	#------------------PC UFRGS -----------------------------------
	#doc = nlp(str(sent.replace(".","").replace("\n","")))
	#--------------------------------------------------------------
	i=i+1
	


	Testes_Aqui (doc)
	'''
	for w in doc:
		print (w.text_with_ws+"- "+str (w.dep_))
		if w.dep_ in 'ROOT':
			print (w.text_with_ws+"-tag->"+ str(w.tag_))
		#print ("tag->"+w.text_with_ws+"- "+str (w.tag_))
	'''

	TIPO_SENTENCA_XOR = 1
	TIPO_SENTENCA_AND = 2    
	TIPO_SENTENCA_OTHERS = 3
	TIPO_SENTENCA_Activity = 4
	TIPO_SENTENCA_Event = 5

	Activity = False
	Event = False
	Xor= False
	And=False
	
	type_of_sentence = get_type_senteces(doc)


	print("tipo da sentenca abaixo")
	print(type_of_sentence)    

	if type_of_sentence == TIPO_SENTENCA_XOR:
	    Go_Rule_XOR(doc)
	elif type_of_sentence == TIPO_SENTENCA_AND:
	    Go_Rule_AND(doc)
	else:
	    Go_Rules_Activity_Event(doc)




	

