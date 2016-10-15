
# -*- coding: utf-8 -*-
###IMPORT
#starting spacy
from __future__ import unicode_literals
def NewFunction():
    return u'£'
from PyDictionary import PyDictionary

from spacy.en import English
#from __future__ import unicode_literals   
nlp = English()
import sys
import pandas as pd
#import resource
#import sys

#XOR
XOR_RULES=0
XOR_RULE_R1=0
XOR_RULE_R2=0
XOR_RULE_R7_DOC=0
XOR_RULE_R1_DOC=0

#-------
#ATIVIDADE
ACTIVITY_RULES=0
ACTIVITY_RULE_R1=0
ACTIVITY_RULE_R2=0
ACTIVITY_RULE_R3=0
ACTIVITY_RULE_R4=0
ACTIVITY_RULE_R6_DOC=0
ACTIVITY_RULE_R11_DOC=0
#-------
#AND
AND_RULES=0
AND_RULE_R1=0
AND_RULE_R2=0

#-------
#EVENT
EVENT_RULES=0
EVENT_RULE_R1=0
EVENT_RULE_R6_DOC=0
EVENT_RULE_R11_DOC=0



#opening sentences file
f = open('sentences.txt', 'r')
sentences = f.readlines()



#------------------------------------------------------- PEGAR O TIPO DE SENTENÇA--------------------------------------------------------------
def get_type_senteces(doc_atual):
	for idx, val in enumerate (doc_atual):          
		if (isSIGNAL_WORDS_XOR(idx,val,doc_atual) ==True):
			#print ("XOOOOOOOR")
			return TIPO_SENTENCA_XOR
	for idx, val in enumerate (doc_atual):          
		if (isSIGNAL_WORDS_AND(idx,val,doc_atual) ==True):
			#print ("ANDDDDDD")
		    return TIPO_SENTENCA_AND
	return TIPO_SENTENCA_OTHERS    
     
#-------------------------------------------------------SIGNAL WORDS--------------------------------------------------------------
def Get_String ():

	String_result1=dictionary.synonym(str("if"))	
	String_result2=dictionary.synonym(str("only"))	

	String_result1.append(String_result2)
def Get_dep_String_XOR (indice,doc_atual):
	
	String_result=None
	for indice, val in enumerate (doc_atual): 
		String_result = ''.join(w.text_with_ws for w in doc_atual[indice].subtree)
		#print ("String_result-->" + str(String_result))
		isSynonyms,Conteudo= isSynonyms_XOR(String_result)
		if (isSynonyms==True):
			#print ("ENTROOOOOOOOOOOOOU get dep")
			return True
	return False
	
def isSynonyms_XOR(String):
	#dictionary=PyDictionary()
	#print ("STTRING--->"+ str(String))
	String_result=None
	#synonym_word= (dictionary.getSynonyms("only"),list)
	isSynonyms=False
	Conteudo=None
	#print ("Entrou aqui 20")
	
	if (isSynonyms==False):
		#If
		#print ("Entrou aqui 21")
		String_result=dictionary.synonym(str("if"))	
		
		if (str(String).lower() in String_result):
			#print ("if")
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo
	if (isSynonyms==False):
		#print ("Entrou aqui 22")
		#only
		String_result=dictionary.synonym(str("only"))
		if (str(String).lower() in String_result):
			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo
	if (isSynonyms==False):
		#print ("Entrou aqui 23")
		String_result=dictionary.synonym(str("whether"))
		if (str(String).lower() in String_result):			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo
	if (isSynonyms==False):
		#print ("Entrou aqui 24")
		String_result=dictionary.synonym(str("or"))
		if (str(String).lower() in String_result):
			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo
	if (isSynonyms==False):
		#print ("Entrou aqui 25")
		String_result=dictionary.synonym(str("otherwise"))
		if (str(String).lower() in String_result):
			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo
	if (isSynonyms==False):
		#print ("Entrou aqui 26")
		String_result=dictionary.synonym(str("till"))
		if (str(String).lower() in String_result):
			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo
	if (isSynonyms==False):
		#print ("Entrou aqui 27")
		String_result=dictionary.synonym(str("until"))
		if (str(String).lower() in String_result):
			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo
	if (isSynonyms==False):
		#print ("Entrou aqui 28")
		String_result=dictionary.synonym(str("unless"))
		if (str(String).lower() in String_result):
			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo
	
	if (isSynonyms==False):
		#print ("Entrou aqui 29")
		String_result=dictionary.synonym(str("when"))
		if (str(String).lower() in String_result):			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo		

	
	return isSynonyms,Conteudo	
	
def isSIGNAL_WORDS_XOR(idx,val,doc_atual):
	
	if doc_atual[idx].dep_ in 'mark' and ("if" == str(val).lower()  or "whether" == str(val).lower() or  "otherwise"  == str(val).lower() or "either"  == str(val).lower() or  "only"  == str(val).lower() or "till"  == str(val).lower() or "until"  == str(val).lower() or "when"  == str(val).lower()):
		#print("passo por aqui 4")
		return True    
	
	elif "if" == str(val).lower() :
		#print("passo por aqui 2")
		z=doc_atual[idx+1]
		if "not" == str(z).lower(): 
			#print("passo por aqui 3")
			
			return True
	elif "in"  == str(val).lower():
		#print("passo por aqui 5")
		z=doc_atual[idx+1]
		y=doc_atual[idx+2]
		if ("case"  == str(z).lower() or ("case"  == str(z).lower() and "of"  == str(y).lower())):
			#print("passo por aqui 6")			
			return True
	
	'''isSynonyms,Conteudo= isSynonyms_XOR(val)
	if (isSynonyms==True):
		return True		
	else:
		#print("passo por aqui 7")
		return False'''
	return False
def Get_dep_String_AND (indice,doc_atual):
	String_result=None
	for indice, val in enumerate (doc_atual): 
		String_result = ''.join(w.text_with_ws for w in doc_atual[indice].subtree)
		#print ("String_result-->" + str(String_result))
		isSynonyms,Conteudo= isSynonyms_AND(String_result)
		if (isSynonyms==True):
			print ("ENTROOOOOOOOOOOOOU get dep")
			return True

	return False
def isSynonyms_AND(String):
	String_result=None
	#synonym_word= (dictionary.getSynonyms("only"),list)
	isSynonyms=False
	Conteudo=None
	if (isSynonyms==False):
		#If
		#print ("Entrou aqui 20")
		String_result=dictionary.synonym(str("while"))
		if (str(String).lower() in String_result):			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo	
	if (isSynonyms==False):
		#only
		#print ("Entrou aqui 21")
		String_result=dictionary.synonym(str("meanwhile"))
		if (str(String).lower() in String_result):			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo	
	if (isSynonyms==False):
		#print ("Entrou aqui 22")
		String_result=dictionary.synonym(str("concurrently"))
		if (str(String).lower() in String_result):			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo		
	if (isSynonyms==False):
		#print ("Entrou aqui 23")
		String_result=dictionary.synonym(str("meantime"))
		if (str(String).lower() in String_result):			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo	

	if (isSynonyms==False):
		#print ("Entrou aqui 24")
		String_result=dictionary.synonym(str("simultaneously"))
		if (str(String).lower() in String_result):			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo	
	if (isSynonyms==False):
		#print ("Entrou aqui 25")
		String_result=dictionary.synonym(str("whereas"))
		if (str(String).lower() in String_result):			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo	
	if (isSynonyms==False):
		#print ("Entrou aqui 26")
		String_result=dictionary.synonym(str("until"))
		if (str(String).lower() in String_result):			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo	
	if (isSynonyms==False):
		#print ("Entrou aqui 27")
		String_result=dictionary.synonym(str("unless"))
		if (str(String).lower() in String_result):			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo	
	
	if (isSynonyms==False):
		#print ("Entrou aqui 28")
		String_result=dictionary.synonym(str("when"))
		if (str(String).lower() in String_result):			
			Conteudo=str(String).lower()
			isSynonyms=True
			return isSynonyms,Conteudo				

	return isSynonyms,Conteudo	

def isSIGNAL_WORDS_AND(idx,val,doc_atual):
	#print (val)
	#print("passo por aqui 8")
	if "while"  == str(val).lower()  or "meanwhile" == str(val).lower() or "concurrently" == str(val).lower() or "meantime" == str(val).lower() or "simultaneously" == str(val).lower() or "whereas"  == str(val).lower():
		print("passo por aqui 9")
		return True
	elif "in"  == str(val).lower():
		#print("passo por aqui 10")
		z=doc_atual[idx+1]
		y=doc_atual[idx+2]
		q=doc_atual[idx+3]
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
		z=doc_atual[idx+1]
		y=doc_atual[idx+2]
		q=doc_atual[idx+3]
		if ("the"  == str(z).lower() and "same" == str(y).lower() and "time" == str(q).lower()):
		    #print("passo por aqui 15")
		    return True           
	
		
	'''isSynonyms,Conteudo= isSynonyms_AND(val)
	if (isSynonyms==True):
		#print ("passo aqui VERDADEIRO")
		return True
	else:
		#print("passo por aqui 16")
		return False'''
	return False


#-------------------------------------------------------IR REGRAS DE ATIVIDADE E EVENTOS--------------------------------------------------------------

# define se é atividade ou evento
def isAgent (doc_atual):
	Main_Verb = Definition_Main_Verb_Activity_or_Event (doc_atual)
	for indice, conteudo in enumerate (doc_atual):
		if (doc_atual[indice].dep_ in ('agent') and str(doc_atual[indice].head) == str (Main_Verb)):
			return True
	return False

def isPresent_Perfect (doc_atual):
	Main_Verb = Definition_Main_Verb_Activity_or_Event (doc_atual)
	for indice, conteudo in enumerate (doc_atual):
		if "has"  == str(conteudo).lower() or "have" == str(conteudo).lower() or "Has not" == str(conteudo).lower() or "Have not" == str(conteudo).lower():
				if (doc_atual[indice].dep_ in ('aux') and doc_atual[indice].head == Main_Verb):
					print ("present_perfect")
					return True
	return False
def isConjuction (doc_atual):
	for indice, conteudo in enumerate (doc_atual):
		if doc_atual[indice].dep_ in ('conj', 'cc', 'in'):
			print ("conjuncao")
			return True

	return False

def Get_String_do_DOC (doc_atual):
	for indice,cont in enumerate (doc_atual):
		String_do_texto= ''.join(w.text_with_ws for w in doc_atual)
	return String_do_texto

def Go_Rules_Activity_Event(doc_atual):
	#print ("sentenca3---"+ str (sent))
	Main_Verb = Definition_Main_Verb_Activity_or_Event (doc_atual)
	Result_Verb_Tense = Definition_Verb_tense_Main_Verb(Main_Verb,doc_atual) 
	if (Result_Verb_Tense == TIPO_SENTENCA_Activity):
		if (Execute_Rules_Activity (doc_atual)==True):
			print ("")
		
		#Terminei aqui
	elif (Result_Verb_Tense == TIPO_SENTENCA_Event):
		if (Execute_Rules_Event (doc_atual)==True):		
			print("")
		#Terminei aqui


        
def Definition_Main_Verb_Activity_or_Event (doc_atual):
	for word in doc_atual:
		#print ("teste= "+ word.pos_)
		print(word.text_with_ws + " <- "  + word.head.text_with_ws + " ("  + word.dep_ + ")" )
			#Aqui eu comparo se a palavra é ela mesma e se ela é "root" ou seja, o verbo principal da sentenca
		if (word.text_with_ws in (word.head.text_with_ws) and  word.dep_ in ('ROOT')):
			Main_Verb1=word
			return Main_Verb1
def isToBE (doc_atual,Main_Verb):

	to_be = False
	for idx, val in enumerate (doc_atual):
		#print("valor->"+str(val))
		if "is"  == str(val).lower() or "are" == str(val).lower() or "will be" == str(val).lower():
			print ("doc_atual[idx].head->"+str(doc_atual[idx].head))
			print ("Main_Verb->"+ str (Main_Verb))
			if (doc_atual[idx].dep_ in ('auxpass') and doc_atual[idx].head == Main_Verb):
				to_be=True
				print ("Entrou aqui to be")
				return to_be,idx
	return to_be			

def Definition_Verb_tense_Main_Verb (Main_Verb,doc_atual):
	# aqui eu vejo qual tempo verbal é o verbo principal 
	#VB Verb, base form
	# VBD Verb, past tense
	#VBG Verb, gerund or present participle
	#VBN Verb, past participle
	#VBP Verb, non-3rd person singular present
	# VBZ Verb, 3rd person singular present
	to_be = False
	for idx, val in enumerate (doc_atual):
		#print("valor->"+str(val))
		if "is"  == str(val).lower() or "are" == str(val).lower() or "will be" == str(val).lower():
			print ("doc_atual[idx].head->"+str(doc_atual[idx].head))
			print ("Main_Verb->"+ str (Main_Verb))
			if (doc_atual[idx].dep_ in ('auxpass') and doc_atual[idx].head == Main_Verb):
				to_be=True
				print ("Entrou aqui to be")
				break
	present_perfect= False			
	for idx, val in enumerate (doc_atual):
		#print("valor->"+str(val))
		if "has"  == str(val).lower() or "have" == str(val).lower():
			#print ("doc_atual[idx].head->"+str(doc_atual[idx].head))
			#print ("Main_Verb->"+ str (Main_Verb))
			if (doc_atual[idx].dep_ in ('aux') and doc_atual[idx].head == Main_Verb and (doc_atual[idx].tag_ =="VBP" or doc_atual[idx].tag_ == "VBN" or doc_atual[idx].tag_== "VBZ")):
				present_perfect=True
				break
	print ("Main_Verb->"+ str (Main_Verb))	
	print ("tag->"+str(Main_Verb.tag_))	
	if ((Main_Verb.tag_ == "VBP" or Main_Verb.tag_ == "VBZ" or Main_Verb.tag_ == "VB" or Main_Verb.tag_ == "VBG") or to_be==True):
		print ("Atividade")
		return TIPO_SENTENCA_Activity
	elif (Main_Verb.tag_ == "VBD" or Main_Verb.tag_ == "VBN" or present_perfect==True):
		print ("Evento")
		return TIPO_SENTENCA_Event
#---------------------------------PEGAR SUJEITO, VERBO E OBJETO --- INDICE E CONTEUDO ---------

def Get_Content_Indice_Subject (doc_atual):
	sujeito=None
	indice_sujeito=None
	for indice, conteudo in enumerate (doc_atual):
		#indice do sujeito
		if doc_atual[indice].dep_ in ('nsubj' , 'csubj','nsubjpass','xsubj','agent','csubjpass'):
			#print ("entrou aqui 2")
			sujeito = ''.join(w.text_with_ws for w in doc_atual[indice].subtree)
			indice_sujeito=indice
			#suj_small=conteudo
			#print ('sujeito: ' + sujeito)
			break

	return sujeito,indice_sujeito

def Get_Content_Indice_Verbo (doc_atual):
	Verbo=None	
	indice_verbo=None
	for indice, conteudo in enumerate (doc_atual):
			#print (''+dependency_labels_to_root(word)[0])
			#print word.text_with_ws 
			#print  dependency_labels_to_root(word)
			#print word.text_with_ws + ' '+word.tag_			
			#indice do verbo
			if (str(doc_atual[indice])) in (str(doc_atual[indice].head)) and  doc_atual[indice].dep_ in ('ROOT'):
				#print ("entrou aqui 1")a
				print("Verbo----->" + str(doc_atual[indice]))
				indice_verbo=indice
				Verbo=conteudo
				break
	return Verbo,indice_verbo
def Get_Content_Indice_Object (doc_atual):
	indice_objeto=None
	objeto=None
	for indice, conteudo in enumerate (doc_atual):
		if doc_atual[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod','pobj','oprd'):
			#print ("entrou aqui 3")
			obj=conteudo
			objeto=''.join(w.text_with_ws for w in doc_atual[indice].subtree)
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + objeto)
			indice_objeto=indice
			break
	return 	objeto,	indice_objeto


#-------------------------------------------------------REGRAS ATIVIDADES--------------------------------------------------------------
	#--------REGRA 1 ------------------- SVO
def Get_indice_Sub_Obj_rule_1 (doc_atual):
	#print ("sentenca---"+ str (sent))
	indice_verbo=None
	indice_sujeito=None
	indice_objeto=None
	ERROR=1000
	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc_atual)			
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc_atual)			
	objeto,indice_objeto = Get_Content_Indice_Object (doc_atual)			
	# verificar se há conjunção na frase, se houver entao nao é esta regra e sim a regra 4
	other_rule=False
	if (isConjuction (doc_atual) == True):
		other_rule=True
	for indice, conteudo in enumerate (doc_atual):    
		if "will"  == str(conteudo).lower():
			other_rule=True
			#print("indice_will--->"+ str(indice_will))			
			break	
	print ("indices- SVO->"+ str (indice_sujeito) + str (indice_verbo) + str(indice_objeto))
	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or other_rule==True):
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,ERROR]
	else:
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,-1]

	return result_indice	

	#--------REGRA 2 ------------------- WILL
def Get_indice_Sub_Obj_rule_2 (doc_atual):
	
	indice_verbo=None
	indice_sujeito=None
	indice_objeto=None
	indice_will=None
	ERROR = 1000


	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc_atual)			
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc_atual)			
	objeto,indice_objeto = Get_Content_Indice_Object (doc_atual)

	for indice, conteudo in enumerate (doc_atual):    
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
def Get_indice_Sub_Obj_rule_3(doc_atual):
	indice_sujeito=None
	indice_verbo=None
	indice_article=None
	indice_objeto=None	
	ERROR = 1000

	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc_atual)			
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc_atual)			
	objeto,indice_objeto = Get_Content_Indice_Object (doc_atual)			
	for indice, conteudo in enumerate (doc_atual):    
		if (doc_atual[indice].dep_ in ('DT', 'det') and ("a"  == str(conteudo).lower() or "an"  == str(conteudo).lower())):
			indice_article=indice
			#print("indice_artigo--->"+ str(indice_article))
			#print ("artigo-->" + str(conteudo))
			break
	#print ("V->"+str(indice_verbo))		
	#print ("a->"+str(indice_article))	
	#print ("O->"+str(indice_objeto))	
	if (indice_verbo==None or indice_article==None or indice_objeto==None):
		result_indice = [indice_verbo,indice_article,indice_objeto,ERROR]
	else:
		result_indice = [indice_verbo,indice_article,indice_objeto,-1]
	return result_indice



def Get_rule_4(doc_atual,String_Current):
	
	ERROR=1000
	#Se o lado esquerdo ou direito for verdadeiro é tarefa senao não é tarefa
	Left= False
	Right = False
	for idx, val in enumerate (doc_atual):
		if (("and" == str(val).lower() or "or" == str(val).lower()) and idx > 2):
			
			if (("and" == str(val).lower())):
				vetor_all= String_Current.split('and')
			else:
				vetor_all= String_Current.split('or')

			String_vetor_left=vetor_all[0]
			String_vetor_right= vetor_all[1]
			# colocando cada frase em um doc_atual para verificar se a frase do lado direito ou esquerdo é realmente uma tarefa
			doc_Left = nlp(String_vetor_left)
			doc_Right = nlp(String_vetor_right)

			if (Execute_Rules_Activity (doc_Left)==True):
				Left=True
			if (Execute_Rules_Activity (doc_Right)==True):
				Right=True
			break

	if (Left == True and Right ==True):
	 	print("OK")
	 	return True
	else:
		print ("FALSE")
		return False
def Get_rule_6 (doc_atual):
	indice_verbo=None
	indice_sujeito=None
	indice_objeto=None
	ERROR=1000
	indice_verbo_tobe=None
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc_atual)	
	for indice, conteudo in enumerate (doc_atual):
			#indice do sujeito
			print ("tag_sujeito->"+str(doc_atual[indice].tag_))
			if doc_atual[indice].dep_ in ('nsubj' , 'csubj','nsubjpass','xsubj','agent','csubjpass') and doc_atual[indice].tag_ in ('NN') :
				#print ("entrou aqui 2")
				sujeito = ''.join(w.text_with_ws for w in doc_atual[indice].subtree)
				indice_sujeito=indice
				print ('sujeito: ' + sujeito)
				break
	
	Main_Verb= Definition_Main_Verb_Activity_or_Event (doc_atual)
	to_be,indice_verbo_tobe=isToBE (doc_atual,Main_Verb)
	
	for indice, conteudo in enumerate (doc_atual):
		print ("doc-obj->"+str(doc_atual[indice].dep_))
		print ("doc_tag->"+str(doc_atual[indice].tag_))
		if doc_atual[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod','pobj','oprd') and doc_atual[indice].tag_ in ('NN','NNS', 'NNP', 'NNPS') :
			#print ("entrou aqui 3")
			obj=''.join(w.text_with_ws for w in doc_atual[indice].subtree)
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + obj)
			indice_objeto=indice	
			print ("objeto->" +str(obj))
			break	
			
	# verificar se há conjunção na frase, se houver entao nao é esta regra e sim a regra 4
	other_rule=False
	if (isConjuction (doc_atual) == True):
		other_rule=True


	print ("indices- SVO_6->"+ str (indice_sujeito) + str (indice_verbo) + str(indice_objeto) + str (indice_verbo_tobe))
	if (indice_verbo==None or indice_sujeito==None or other_rule==True or indice_verbo_tobe==None):
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,ERROR,indice_verbo_tobe]
	else:
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,-1,indice_verbo_tobe]

	return result_indice	
#------------- regra 11 .Doc ---------------------
def Get_rule_11 (doc_atual,String_Current):
	ERROR=1000
	#Se o lado esquerdo ou direito for verdadeiro é tarefa senao não é tarefa
	Left= False
	Right = False
	indice_verbo_left = None
	indice_verbo_right= None
	indice_objeto_right= None

	for idx, val in enumerate (doc_atual):
		if (("and" == str(val).lower() or "or" == str(val).lower()) and idx > 2):
			
			if (("and" == str(val).lower())):
				vetor_all= String_Current.split('and')
			else:
				vetor_all= String_Current.split('or')

			String_vetor_left=vetor_all[0]
			String_vetor_right= vetor_all[1]
			# colocando cada frase em um doc para verificar se a frase do lado direito ou esquerdo é realmente uma tarefa
			doc_Left = nlp(String_vetor_left)
			doc_Right = nlp(String_vetor_right)
			#print ("string right->" + String_vetor_right)
			#verbo esquerdo
			Testes_Aqui (doc_Right)
			print ("--------")
			Testes_Aqui (doc_Left)
			for indice, conteudo in enumerate (doc_Left):
				print ("entrou aqui 11.1")
				
				if (doc_Left[indice].tag_=='VBP' or doc_Left[indice].tag_ == 'VBZ'  or doc_Left[indice].tag_ == 'VB' ):
					print ("entrou aqui 11.2")
					indice_verbo_left= indice
					
			#verbo direito
			for indice, conteudo in enumerate (doc_Right): 
				if (doc_Right[indice].dep_ in ('ROOT') or doc_Right[indice].tag_=='VBP' or doc_Right[indice].tag_ == 'VBZ'  or doc_Right[indice].tag_ == 'VB' ):
					print ("entrou aqui 11.3")
					indice_verbo_right = indice
					
				
			#OBJETO
			for indice, conteudo in enumerate (doc_Right): 
				#print ("dep11->"+ str (doc_Right[indice].dep_))
				if doc_Right[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod','pobj','oprd') or doc_Right[indice].tag_=='NN':
			
					obj=''.join(w.text_with_ws for w in doc_Right[indice].subtree)
					#print (word.subtree[0].text_with_ws)
					#print('objeto11: ' + obj)
					indice_objeto_right=indice	
			break
	
	print ("indices verbo e obj->" + str (indice_verbo_left)+str (indice_verbo_right)+str (indice_objeto_right) )
	if (indice_verbo_left==None or indice_verbo_right==None or indice_objeto_right==None):
		result_indice = [indice_verbo_left,indice_verbo_right,indice_objeto_right,ERROR]
	else:
		result_indice = [indice_verbo_left,indice_verbo_right,indice_objeto_right,-1]
	return result_indice		

#---------------------CHECKS VETOR ATIVIDADES----------------------------------------------
def Check_vetor_rule_1 (doc_atual,vetor,String_Current):
	ERROR=1000

	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_1(doc)
	if (vetor[3] == ERROR):
		print ("entrou aqui 1.flag")
		print ("R1- ERROR")
		
		return False
		
	else:
		#Deu CERTO
		sujeito,indice_sujeito = Get_Content_Indice_Subject (doc_atual)			
		Verbo, indice_verbo = Get_Content_Indice_Verbo (doc_atual)			
		objeto,indice_objeto = Get_Content_Indice_Object (doc_atual)
		indice_verbo2 = vetor[0]
		indice_sujeito2=vetor[1]
		indice_objeto2= vetor[2]
		
		if (indice_sujeito2<indice_verbo2 and indice_verbo2<indice_objeto2):
			#regra 1
			print("Regra do SVO")
			print("Sentença: "+ str(String_Current.encode('utf-8')))
			print("-------------------------")
			print("Indica-se uma Tarefa ")
			print ("Lane:"+ str (sujeito))
			print ("Ação: "+ str(Verbo) + " "+ str (objeto)) 
			print("-------------------------")
			return True
		else:
			print ("R1- ERROR")
			return False

def Check_vetor_rule_2 (doc_atual,vetor,String_Current):
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
		sujeito,indice_sujeito = Get_Content_Indice_Subject (doc_atual)			
		Verbo, indice_verbo = Get_Content_Indice_Verbo (doc_atual)			
		objeto,indice_objeto = Get_Content_Indice_Object (doc_atual)
		if (indice_sujeito2<indice_will and indice_will < indice_verbo2 and indice_verbo2 < indice_objeto2):
			print("Regra do WILL")
			print ("Sentença: "+ str(String_Current.encode('utf-8')))
			print("-------------------------")
			print ("Indica-se uma Tarefa ")
			print ("Lane:"+ str (sujeito))
			print ("Ação: "+ str(Verbo) + " "+ str (objeto)) 
			print("-------------------------")
			return True
		else:
			print ("R2- ERROR")
			return False

def Check_vetor_rule_3 (doc_atual,vetor,String_Current):
	ERROR=1000
	if (vetor[3] == ERROR):
				print ("entrou aqui 3.flag")
				print ("R3- ERROR")
				return False
		
	else:	

		indice_verbo3 = vetor[0]
		indice_article3=vetor[1]
		indice_objeto3= vetor[2]
		sujeito,indice_sujeito = Get_Content_Indice_Subject (doc_atual)			
		Verbo, indice_verbo = Get_Content_Indice_Verbo (doc_atual)			
		objeto,indice_objeto = Get_Content_Indice_Object (doc_atual)	
		if (indice_verbo3<indice_article3 and indice_article3<indice_objeto3):
			print("Regra do VAO")
			print("Sentença: "+ str(String_Current.encode('utf-8')))
			print("-------------------------")
			print ("Indica-se uma Tarefa ")
			print ("Lane:"+ str (sujeito))
			print ("Ação: "+ str(Verbo) + " "+ str (objeto)) 
			print("-------------------------")
			return True
		else:
			print ("R3- ERROR")
			return False

def Check_vetor_rule_6(doc_atual,vetor,String_Current):
	ERROR=1000

	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_6(doc)
	if (vetor[3] == ERROR):
		print ("R6- ERROR")		
		return False
		
	else:
		#Deu CERTO
		indice_verbo2 = vetor[0]
		indice_sujeito2=vetor[1]
		indice_objeto2= vetor[2]
		indice_tobe= vetor [4]
		
		if (indice_sujeito2<indice_tobe and indice_tobe<indice_verbo2):
			#regra 1
			print("Regra 6")
			print("Sentença: "+ str(String_Current.encode('utf-8')))
			print("-------------------------")
			print("Indica-se uma Tarefa ")
			print("-------------------------")
			return True
		else:
			print ("R1- ERROR")
			return False

def Check_vetor_rule_11 (doc_atual,vetor,String_Current):
	ERROR=1000

	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_1(doc)
	if (vetor[3] == ERROR):
		print ("entrou aqui 11.flag")
		print ("R11- ERROR")		
		return False
		VerboLeft=None
		VerboRight=None
	else:
		for idx, val in enumerate (doc_atual):
			if (("and" == str(val).lower() or "or" == str(val).lower()) and idx > 2):
				print ("val->"+str(val))
				if (("and" == str(val).lower())):
					vetor_all= String_Current.split('and')
				else:
					vetor_all= String_Current.split('or')

				String_vetor_left=vetor_all[0]
				print("strin1->"+str(String_vetor_left))
				String_vetor_right= vetor_all[1]
				print("string2->"+str(String_vetor_right))
				# colocando cada frase em um doc para verificar se a frase do lado direito ou esquerdo é realmente uma tarefa
				doc_Left = nlp(String_vetor_left)
				doc_Right = nlp(String_vetor_right)

				#verbo esquerdo
				for indice, conteudo in enumerate (doc_Left):
					print ("entrou aqui 11.1")			
					print("Conteudo->" +str (conteudo))
					print ("tag->"+ str (doc_Left[indice].tag_))
					if ((doc_Left[indice].tag_=='VBP' or doc_Left[indice].tag_ == 'VBZ'  or doc_Left[indice].tag_ == 'VB')):
						if (("is" != str(conteudo).lower()  or  "are" != str(conteudo).lower())):
							print ("entrou aqui 11.2")
							indice_verbo_left= indice
							VerboLeft=conteudo
							print ("verbo---->"+ str (VerboLeft))
							
				#verbo direito
				for indice, conteudo in enumerate (doc_Right): 
					if (doc_Right[indice].dep_ in ('ROOT') or doc_Right[indice].tag_=='VBP' or doc_Right[indice].tag_ == 'VBZ'  or doc_Right[indice].tag_ == 'VB' ):
						print ("entrou aqui 11.3")
						indice_verbo_right = indice
						VerboRight=conteudo
						
						
				#OBJETO
				for indice, conteudo in enumerate (doc_Right): 
					#print ("dep11->"+ str (doc_Right[indice].dep_))
					if doc_Right[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod','pobj','oprd') or doc_Right[indice].tag_=='NN':
				
						obj=''.join(w.text_with_ws for w in doc_Right[indice].subtree)
						#print (word.subtree[0].text_with_ws)
						#print('objeto11: ' + obj)
						indice_objeto_right=indice
						break

				sujeito,indice_sujeito = Get_Content_Indice_Subject (doc_atual)
				break	
		#Deu CERTO
		indice_verbo_left = vetor[0]
		indice_verbo_right=vetor[1]
		indice_objeto_right= vetor[2]
		#[indice_verbo_left,indice_verbo_right,indice_objeto_right,ERROR]
		if (indice_verbo_right< indice_objeto_right):
			#regra 1
			print("Regra 11")
			print("Sentença: "+ str(String_Current.encode('utf-8')))
			print("-------------------------")
			print("Indica-se uma Tarefa ")
			print("Lane:"+ str (sujeito))
			print ("Ações: " + str (VerboLeft) + " "+ str (obj) + " "+"e" + " "+str (VerboRight) + " "+ str (obj))
			print("-------------------------")
			return True
		else:
			print ("R11- ERROR")
			return False

def Execute_Rules_Activity(doc_atual):		
	
	flag=1
	ERROR=1000
	flag2=1
	flag3=1
	Activity=False
	String_Current= Get_String_do_DOC(doc_atual)
	global ACTIVITY_RULES
	print ("ActA-all2->"+str(ACTIVITY_RULES))
	#--------REGRA 1 ------------------- SVO
	if (Activity==False):
		print ("entrou aqi R1")
		vetor_result_indice_rule1= Get_indice_Sub_Obj_rule_1(doc_atual)		
		Result_rule_1 = Check_vetor_rule_1 (doc_atual,vetor_result_indice_rule1,String_Current) 
		if (Result_rule_1 == True):
				#ACTIVITY_RULE_1= ACTIVITY_RULE_1+1
				
				global ACTIVITY_RULE_R1
				print ("ActA-all4->"+str(ACTIVITY_RULES))
				ACTIVITY_RULES=ACTIVITY_RULES+1
				ACTIVITY_RULE_R1=ACTIVITY_RULE_R1+1
				Activity=True
				
				return Activity			
	#--------REGRA 2 ------------------- S + WILL + VERB+OBJ	
	if (Activity==False):
		print ("entrou aqi R2")
		vetor_result_indice_rule2 = Get_indice_Sub_Obj_rule_2(doc_atual)	
		Result_rule_2= Check_vetor_rule_2 (doc_atual,vetor_result_indice_rule2,String_Current)
		if (Result_rule_2 == True):
				#ACTIVITY_RULE_1= ACTIVITY_RULE_1+1
				
				global ACTIVITY_RULE_R2
				#print ("ActA-all5->"+str(ACTIVITY_RULES))
				Activity=True
				ACTIVITY_RULES=ACTIVITY_RULES+1
				ACTIVITY_RULE_R2=ACTIVITY_RULE_R2+1
				return Activity	
	#--------REGRA 3 ------------------- <Verb>+<article>+<Obj>
	
	if (Activity==False):
		print ("entrou aqi R3")
		vetor_result_indice_rule3= Get_indice_Sub_Obj_rule_3(doc_atual)
		Result_rule_3= Check_vetor_rule_3 (doc_atual,vetor_result_indice_rule3,String_Current)
		if (Result_rule_3 == True):
				print ("ActA-all_antes->"+str(ACTIVITY_RULES))
				global ACTIVITY_RULE_R3
				Activity=True
				ACTIVITY_RULES=ACTIVITY_RULES+1
				ACTIVITY_RULE_R3=ACTIVITY_RULE_R3+1
				print ("ActA-all_Depois->"+str(ACTIVITY_RULES))
				return Activity

	#--------REGRA 4 ------------------- < Sujeito> + <verb> + <obj> [and,or] + <verb> + <obj>
	if (Activity==False):
		print ("entrou aqui R4")
		result_rule_4= Get_rule_4(doc_atual,String_Current)
		
		if (result_rule_4 ==True):
			print("Regra do Sujeito> + <verb> + <obj> [and,or] + <verb> + <obj>")
			print("Sentença: "+ str(String_Current.encode('utf-8')))			
			
			global ACTIVITY_RULE_R4
			ACTIVITY_RULES=ACTIVITY_RULES+1
			ACTIVITY_RULE_R4=ACTIVITY_RULE_R4+1
			Activity=True
			return Activity
	
	#-----------REGRA 6 do .DOC -----------------------------------------------
	if (Activity==False):
		print ("entrou aqi R6")
		print ("String ATUAL 6->" + String_Current )
		vetor_result_indice_rule6 =Get_rule_6 (doc_atual)
		result_rule_6 = Check_vetor_rule_6 (doc_atual,vetor_result_indice_rule6,String_Current)
		if (result_rule_6==True):
				Activity=True
				
				global ACTIVITY_RULE_R6_DOC
				ACTIVITY_RULES=ACTIVITY_RULES+1
				ACTIVITY_RULE_R6_DOC=ACTIVITY_RULE_R6_DOC+1
				return Activity
# ------------ Regra 11 do .Doc -------------------------
	if (Activity==False):
		print ("entrou aqi 11")
		vetor_result_indice_rule11 =Get_rule_11 (doc_atual,String_Current)
		result_rule_11 = Check_vetor_rule_11 (doc_atual,vetor_result_indice_rule11,String_Current)
		if (result_rule_11==True):
				print ("11	<Subject (ocult)>+<Verb> + [and,or]+ <verb> + <obj>")
				Activity=True	
				
				global ACTIVITY_RULE_R11_DOC			
				ACTIVITY_RULES=ACTIVITY_RULES+1
				ACTIVITY_RULE_R11_DOC=ACTIVITY_RULE_R11_DOC+1
				return Activity

#NÃO ENTROU EM NENHUMA REGRA
	print ("ActA-all3->"+str(ACTIVITY_RULES))
	if (Activity==False):		
		print("Sentença: "+str(String_Current.encode('utf-8'))+"---> Não definida pelo protótipo")

#-------------------------------------------------------REGRAS EVENTOS--------------------------------------------------------------
#--------REGRA 1 ------------------- SVO---- tutorial
def Get_indice_Sub_Obj_rule_1_Event (doc_atual):
	#print ("sentenca---"+ str (sent))
	#indice_verbo=None
	#indice_sujeito=None
	#indice_objeto=None
	ERROR=1000
	Verbo=None
	sujeito=None
	suj_small=None
	objeto=None
	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc_atual)
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc_atual)	
	objeto,indice_objeto = Get_Content_Indice_Object (doc_atual)
	
	other_rule=False	
	#if (isConjuction (doc_atual) == True):
	#	other_rule=True
	if (isAgent (doc_atual)==True):
		other_rule=True
	if (isPresent_Perfect (doc_atual)==True):
		other_rule=True
		

	print ("indices- SVO->"+ str (indice_sujeito) + str (indice_verbo) + str(indice_objeto))
	
	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or other_rule==True):
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,ERROR]
	else:
		
		
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,-1]


	return result_indice
#----------------------REGRA 6 EVENT .DOC------------
def Get_indice_Sub_Obj_rule_6_Event(doc_atual):
	#indice_verbo=None
	#indice_sujeito=None
	#indice_objeto=None
	ERROR=1000
	Verbo=None
	sujeito=None
	
	objeto=None
	
	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc_atual)

	print ("suj->"+ str (sujeito))
	print ("indice->" + str (indice_sujeito))

	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc_atual)
	print ("ver->"+ str (Verbo))
	print ("indice->" + str (indice_verbo))
	objeto,indice_objeto = Get_Content_Indice_Object (doc_atual)
	print ("objeto->"+ str (objeto))
	print ("indice->" + str (indice_objeto))
	


	other_rule=False
	#if (isConjuction (doc_atual) == True):
	#	other_rule=True
	if (isPresent_Perfect (doc_atual)==True):
		other_rule=True	

	print ("indices- SVO->"+ str (indice_sujeito) + str (indice_verbo) + str(indice_objeto))
	
	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or other_rule==True):
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,ERROR]
	else:
		
		
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,-1]


	return result_indice


#----------------------REGRA 11 EVENT .doc------------
def Get_indice_Sub_Obj_rule_11_Event(doc_atual):
	indice_verbo=None
	indice_sujeito=None
	indice_objeto=None
	ERROR=1000
	Verbo=None
	sujeito=None
	
	objeto=None
	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc_atual)			
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc_atual)			
	objeto,indice_objeto = Get_Content_Indice_Object (doc_atual)
	other_rule=False
	#if (isConjuction (doc_atual) == True):
	#	other_rule=True

	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or other_rule==True):
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,ERROR]
	else:			
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,-1]


	return result_indice

	
		
#-----------------------------CHECK  VETOR EVENTOS-----------
def Check_vetor_rule_1_Event (doc_atual,vetor,String_Current):
	ERROR=1000

	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_1(doc_atual)
	if (vetor[3] == ERROR):
		print ("entrou aqui 1.flag")
		print ("R1- ERROR")
		
		return False

	else:
			
		indice_verbo2 = vetor[0]
		indice_sujeito2=vetor[1]
		indice_objeto2= vetor[2]
		
		if (indice_sujeito2<indice_verbo2 and indice_verbo2<indice_objeto2):
			#regra 1
			sujeito,indice_sujeito = Get_Content_Indice_Subject (doc_atual)			
			Verbo, indice_verbo = Get_Content_Indice_Verbo (doc_atual)			
			objeto,indice_objeto = Get_Content_Indice_Object (doc_atual)
			
			print ("---------------")		
			print("Sentença: "+ str(String_Current.encode('utf-8')))
			print ("Indicação de Lane: " + str (sujeito))
			print ("Indicação de Label:" + str (objeto) + " " +str (Verbo))	

			print("Regra do SVO 1")			
			print("-------------------------")
			print("Indica-se um Evento")
			print("-------------------------")
			return True
		else:
			print ("R1- ERROR")
			return False



def Check_vetor_rule_6_Event(doc_atual,vetor,String_Current):
	ERROR=1000

	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_1(doc_atual)
	if (vetor[3] == ERROR):
		print ("R6- ERROR")
		return False
		
	else:
			
		indice_verbo2 = vetor[0]
		indice_sujeito2=vetor[1]
		indice_objeto2= vetor[2]
		
		if (indice_sujeito2<indice_verbo2 and indice_verbo2<indice_objeto2):
			#regra 6
			sujeito,indice_sujeito = Get_Content_Indice_Subject (doc_atual)			
			Verbo, indice_verbo = Get_Content_Indice_Verbo (doc_atual)			
			objeto,indice_objeto = Get_Content_Indice_Object (doc_atual)
			print ("---------------")
			print("Sentença: "+ str(String_Current.encode('utf-8')))	
			print ("Indicação de Lane: " + str (objeto))
			print ("Indicação de Label:" + str (sujeito) + "" +str (Verbo))
			print("Regra do SVO 6")			
			print("-------------------------")
			print("Indica-se um Evento")
			print("-------------------------")
			return True
		else:
			print ("R6- ERROR")
			return False
def Check_vetor_rule_11_Event(doc_atual,vetor,String_Current):
	ERROR=1000

	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_1(doc_atual)
	if (vetor[3] == ERROR):
		print ("R11- ERROR")
		return False
		
	else:
			
		indice_verbo2 = vetor[0]
		indice_sujeito2=vetor[1]
		indice_objeto2= vetor[2]
		
		if (indice_sujeito2<indice_verbo2 and indice_verbo2<indice_objeto2):
			#regra 6
			sujeito,indice_sujeito = Get_Content_Indice_Subject (doc_atual)			
			Verbo, indice_verbo = Get_Content_Indice_Verbo (doc_atual)			
			objeto,indice_objeto = Get_Content_Indice_Object (doc_atual)
			print("Sentença: "+ str(String_Current.encode('utf-8')))
			if (isAgent (doc_atual)==True):
				print ("---------------")
				print ("Indicação de Lane: " + str (objeto))
				print ("Indicação de Label:" + str (sujeito) + " " +str (Verbo))
			else:
				print ("---------------")
				print ("Indicação de Lane: " + str (sujeito))
				print ("Indicação de Label:" + str (objeto) + " " +str (Verbo))
				
			print("Regra do SVO 11")
			print("-------------------------")
			print("Indica-se um Evento")
			print("-------------------------")	
			return True		
		else:
			print ("R11- ERROR")
			return False


def Execute_Rules_Event (doc_atual):
	flag=1
	ERROR=1000
	Event=False
	global EVENT_RULES
	#-----------------------------R1 tutorial
	String_Current=Get_String_do_DOC(doc_atual)
	if (Event==False):
		print ("entrou aqi R1")
		vetor_result_indice_rule1_Event= Get_indice_Sub_Obj_rule_1_Event(doc_atual)		
		Result_rule_1_Event = Check_vetor_rule_1_Event (doc_atual,vetor_result_indice_rule1_Event,String_Current) 
		if (Result_rule_1_Event == True):
				global EVENT_RULE_R1
				EVENT_RULES = EVENT_RULES+1
				EVENT_RULE_R1 = EVENT_RULE_R1+1

				Event=True				
				return Event
	#-----------------R6 S+V+AGENT+O			
	if (Event==False):
		# SVO + Agent
		print ("entrou aqi R6")
		vetor_result_indice_rule6_Event= Get_indice_Sub_Obj_rule_6_Event(doc_atual)		
		Result_rule_6_Event = Check_vetor_rule_6_Event (doc_atual,vetor_result_indice_rule6_Event,String_Current) 
		if (Result_rule_6_Event == True):
				#EVENT_RULE= EVENT_RULE+1
				global EVENT_RULE_R6_DOC
				EVENT_RULES = EVENT_RULES+1
				EVENT_RULE_R6_DOC = EVENT_RULE_R6_DOC+1
				Event=True				
				return Event

	#--------------------R11 . DOC -----------
	if (Event==False):
		print ("entrou aqi R11")
		vetor_result_indice_rule11_Event= Get_indice_Sub_Obj_rule_11_Event(doc_atual)		
		Result_rule_11_Event = Check_vetor_rule_11_Event (doc_atual,vetor_result_indice_rule11_Event,String_Current) 
		if (Result_rule_11_Event == True):
				#EVENT_RULE= EVENT_RULE+1
				global EVENT_RULE_R11_DOC
				EVENT_RULES = EVENT_RULES+1
				EVENT_RULE_R11_DOC = EVENT_RULE_R11_DOC+1
				Event=True				
				return Event

	 # ----------------------NÃO ENTROU EM NENHUMA REGRA
	if (Event==False):
		print("Sentença: "+ str(String_Current.encode('utf-8'))+"---> Não definida pelo protótipo")

#-------------------------------------------------------REGRAS XOR--------------------------------------------------------------
def Get_Word_alternative (doc_atual):
	isAlternative_Word=False
	Word=False
	Right=False
	for indice, val in enumerate (doc_atual):
		if (("," == str(val).lower() and doc_atual[indice].dep_ in ('punct'))):
			
			vetor_all= sent.split(',')
			String_vetor_left=vetor_all[0]
			String_vetor_right= vetor_all[1]
			# colocando cada frase em um doc para verificar se a frase do lado direito ou esquerdo é realmente uma tarefa
			doc_Left = nlp(String_vetor_left)
			doc_Right = nlp(String_vetor_right)
			lista = ["but","than", "else","unless", "without", "either","other", "if", "otherwise"]			
			for indice1, val1 in enumerate (doc_Left):
				for indice2, val2 in enumerate (lista):
					if (str(val1).lower() == "if"):						
						z=doc_Left[indice1+1]
						if "not" == str(z).lower():							
							Word=True	
					if (val2 == str(val1).lower()):
						Word=True	
			if (Word==False):
				return False
			else:		
				if (Execute_Rules_Activity (doc_Right)==True or Execute_Rules_Event (doc_Right)==True  ):
					Right=True
				
				if (Right==True):
					print ("-------------------------")
					print ("Sentença:"+ str(sent.encode('utf-8')))
					print ("Indica-se um XOR (alternative)")
					print ("Tarefa/Evento:"+str(String_vetor_right))
					print ("-------------------------")
					return True


	return False	    

def Get_Word_indice_content_Divide (doc_atual):
	lista = ["whether","if","either", "only", "till", "until", "when"]	
	Indice_Word=None
	Conteudo=None
	Divide=False
	
	for indice1, val1 in enumerate (doc_atual):
				if "if" == str(val1).lower():
					print("passo por aqui 2")
					z=doc_atual[indice1+1]
					if "not" == str(z).lower(): 
						#print("passo por aqui 3")						
						Indice_Word=indice1
						Divide=True
						Conteudo="if not"
						break
				if "in"  == str(val1).lower():
					#print("passo por aqui 5")
					z=doc_atual[indice1+1]
					y=doc_atual[indice1+2]
					if ("case"  == str(z).lower() and "of"  == str(y).lower()):						
						Indice_Word=indice1
						Divide=True
						Conteudo="In case of"
						break
					if "case"  == str(z).lower():
						#print("passoIndice_Word=indice1
						Indice_Word=indice1
						Divide=True
						Conteudo="in case"
						break
				#verifica na lista
				for indice2, val2 in enumerate (lista):					
					if (val2 == str(val1).lower()):
						Indice_Word=indice1
						Divide=True
						Conteudo=val1
						break
				#verifica se tem sinonimos 
				'''for indice2, val2 in enumerate (doc_atual):		
					isSynonyms,Conteudo2= isSynonyms_XOR(val1)
					if (Get_dep_String_XOR(indice1,doc_atual)==True or isSynonyms==True):
						Indice_Word=indice1
						Divide=True
						Conteudo=Conteudo2
						break	'''

	print ("indice,Conteudo,Divide-->"+str(Indice_Word)+str(Conteudo)+str(Divide))
	return Indice_Word,Conteudo,Divide


# ----------------------REGRA 1 TUTORIAL ----

def Get_Condict_Sub_Obj_rule_1_XOR(doc_atual):
	Left=False
	Right=False
	
	Indice_Word,Conteudo,Divide = Get_Word_indice_content_Divide(doc_atual)
	if (Indice_Word<2):
		for indice, val in enumerate (doc_atual):
			if (("," == str(val).lower() and doc_atual[indice].dep_ in ('punct')) and Divide ==True):
				
				vetor_all= sent.split(',')
				String_vetor_left=vetor_all[0]
				String_vetor_right= vetor_all[1]
				# colocando cada frase em um doc para verificar se a frase do lado direito ou esquerdo é realmente uma tarefa
				doc_Left = nlp(String_vetor_left)
				doc_Right = nlp(String_vetor_right)

				if (Execute_Rules_Activity (doc_Left)==True or Execute_Rules_Event (doc_Left)==True):
					Left=True
				if (Execute_Rules_Activity (doc_Right)==True or Execute_Rules_Event (doc_Right)==True):
					Right=True

				break

				
		if (Left == True and Right==True):
			print("-------------------------")
			print ("Sentença:"+ str(sent.encode('utf-8')))
			print("Regra - 1 XOR")
			print("Indica-se um XOR")
			print ("Condição:" + str (String_vetor_left))
			print ("Tarefa/Evento:"+str(String_vetor_right))
			print("-------------------------")			
			return True
		else:
			return False
	else:
		return False
def Get_Condict_Sub_Obj_rule_2_XOR (doc_atual):
	Left=False
	Right=False

	
	Indice_Word,Conteudo,Divide = Get_Word_indice_content_Divide(doc_atual)
	if (Indice_Word>2 and Divide ==True):
			vetor_all= sent.split(str(Conteudo))
			String_vetor_left=vetor_all[0]
			String_vetor_right= vetor_all[1]
			# colocando cada frase em um doc para verificar se a frase do lado direito ou esquerdo é realmente uma tarefa
			doc_Left = nlp(String_vetor_left)
			doc_Right = nlp(String_vetor_right)

			if (Execute_Rules_Activity (doc_Left)==True or Execute_Rules_Event (doc_Left)==True):
				Left=True
			if (Execute_Rules_Activity (doc_Right)==True or Execute_Rules_Event (doc_Right)==True):
				Right=True
		
			if (Left == True and Right==True):
				print("-------------------------")
				print ("Sentença:" +str(sent.encode('utf-8')))
				print("Regra - 2 XOR")
				print("Indica-se um XOR")
				print ("Tarefa/Evento::" + str (String_vetor_left))
				print ("Condição:"+str(String_vetor_right))
				print("-------------------------")	
				return True
			else:
				return False
	else:
		return False	


def Get_Condict_Sub_Obj_rule_1_DOC_XOR(doc_atual):	
	Indice_Word,Conteudo,Divide = Get_Word_indice_content_Divide(doc_atual)
	Right=False
	isVerb=False
	if (Indice_Word>2 and Divide ==True):
		vetor_all= sent.split(str(Conteudo))
		String_vetor_left=vetor_all[0]
		String_vetor_right= vetor_all[1]
		# colocando cada frase em um doc para verificar se a frase do lado direito ou esquerdo é realmente uma tarefa
		doc_Left = nlp(String_vetor_left)
		doc_Right = nlp(String_vetor_right)
		#Testes_Aqui  (doc_Left)
		#Testes_Aqui  (doc_Right)
		#VB Verb, base form
		# VBD Verb, past tense
		#VBG Verb, gerund or present participle
		#VBN Verb, past participle
		#VBP Verb, non-3rd person singular present
		# VBZ Verb, 3rd person singular present
		for x in doc_Left:
			if (x.tag_ in ('VBZ', 'VB','VBD','VBG','VBN','VBP') and x.dep_ in 'ROOT'):
				isVerb=True
				break
		if (Execute_Rules_Activity (doc_Right)==True or Execute_Rules_Event (doc_Right)==True):
			Right=True
		if (isVerb == True and Right ==True):
			print("-------------------------")
			print ("Sentença:" +str(sent.encode('utf-8')))
			print("Regra - 1 XOR-DOC")
			print("Indica-se um XOR")
			print("-------------------------")	
			return True
		else:
			return False
	else:
		return False



def Execute_Rule_XOR(doc_atual):
	Alternative_Signal_Word=False
	ERROR=1000
	XOR=False
	global XOR_RULES
	#regra 1 tutorial
	if (XOR==False):
		print ("entrou aqi R1")
		Result_rule_1_XOR= Get_Condict_Sub_Obj_rule_1_XOR(doc_atual)		 
		if (Result_rule_1_XOR == True):
				global  XOR_RULE_R1
				XOR_RULES=XOR_RULES+1
				XOR_RULE_R1=XOR_RULE_R1+1
				XOR=True				
				return XOR
	#alternative Signal word
	if (XOR == False):
		print ("entrou aqi R7-alternative XOR")
		Result_rule_alternative_XOR= Get_Word_alternative(doc_atual)		 
		if (Result_rule_alternative_XOR == True):
				global  XOR_RULE_R7_DOC
				XOR_RULES=XOR_RULES+1
				XOR_RULE_R7_DOC=XOR_RULE_R7_DOC+1
				Alternative_Signal_Word=True
				XOR=True				
				return Alternative_Signal_Word
	#regra 2 tutorial ------------
	if (XOR==False):
		print ("entrou aqi R2_XOR")
		Result_rule_2_XOR= Get_Condict_Sub_Obj_rule_2_XOR(doc_atual)		 
		if (Result_rule_2_XOR == True):
				global  XOR_RULE_R2
				XOR_RULES=XOR_RULES+1
				XOR_RULE_R2=XOR_RULE_R2+1
				XOR=True				
				return XOR			

	# regra 1 ----doc_atual
	if (XOR==False):
		print ("entrou aqi R1_DOC_XOR")
		Result_rule_1_DOC_XOR= Get_Condict_Sub_Obj_rule_1_DOC_XOR(doc_atual)		 
		if (Result_rule_1_DOC_XOR == True):
				global  XOR_RULE_R1_DOC
				XOR_RULES=XOR_RULES+1
				XOR_RULE_R1_DOC=XOR_RULE_R1_DOC+1
				XOR=True				
				return XOR	
	# ----------------------NÃO ENTROU EM NENHUMA REGRA
	if (XOR==False):
		print("Sentença: "+ str(sent.encode('utf-8'))+"---> Não definida pelo protótipo_XOR")


#-----------------------------------------------------------REGRAS AND ------------------------
def Get_Word_indice_content_Divide_AND (doc_atual):
	lista = ["while","meanwhile","concurrently", "meantime", "simultaneously", "whereas", "until","unless","when"]	
	Indice_Word=None
	Conteudo=None
	Divide=False
	
	for indice1, val1 in enumerate (doc_atual):
				if "in"  == str(val1).lower():
					#print("passo por aqui 10")
					z=doc_atual[indice1+1]
					y=doc_atual[indice1+2]
					q=doc_atual[indice1+3]
					if ("parallel"  == str(z).lower() and "with"  == str(y).lower() and "this" == str(q).lower()):				
						print ("in parallel with this")
						Indice_Word=indice1
						Divide=True
						Conteudo="in parallel with this"
						break
					if ("parallel"  == str(z).lower()):
						Indice_Word=indice1
						Divide=True
						Conteudo="in parallel"
						break
					if ("the"  == str(z).lower() and "meantime" == str(y).lower()):
						Indice_Word=indice1
						Divide=True
						Conteudo="in the meantime"
						break	
					if ("addition"  == str(z).lower() and "to"  == str(y).lower()):
						Indice_Word=indice1
						Divide=True
						Conteudo="in addition to"
						break	
				if "at"  == str(val1).lower():
					#print("passo por aqui 5")
					z=doc_atual[indice1+1]
					y=doc_atual[indice1+2]
					q=doc_atual[indice1+3]
					if ("the"  == str(z).lower() and "same" == str(y).lower() and "time" == str(q).lower()):						
						Indice_Word=indice1
						Divide=True
						Conteudo="at the same time"
						break
					
				#verifica na lista
				for indice2, val2 in enumerate (lista):					
					if (val2 == str(val1).lower()):
						Indice_Word=indice1
						Divide=True
						Conteudo=val1
						break
				#verifica se tem sinonimos 
				'''for indice2, val2 in enumerate (doc_atual):		
					isSynonyms,Conteudo2= isSynonyms_AND(val1)
					if (Get_dep_String_AND(indice1,doc_atual)==True or isSynonyms==True):
						Indice_Word=indice1
						Divide=True
						Conteudo=Conteudo2
						break	'''

	print ("indice,Conteudo,Divide-->"+str(Indice_Word)+str(Conteudo)+str(Divide))
	return Indice_Word,Conteudo,Divide

		#-------------REGRA 1 ---TUTORIAL
def Get_Condict_Sub_Obj_rule_1_AND(doc_atual):
	Left=False
	Right=False

	String_vetor_left=None
	String_vetor_right=None
	Indice_Word,Conteudo,Divide = Get_Word_indice_content_Divide_AND(doc_atual)
	if (Indice_Word>2 and Divide ==True):
			print (Conteudo)
			vetor_all= sent.split(str(Conteudo))
			String_vetor_left=vetor_all[0]
			String_vetor_right= vetor_all[1]
			# colocando cada frase em um doc para verificar se a frase do lado direito ou esquerdo é realmente uma tarefa
			doc_Left = nlp(String_vetor_left)
			doc_Right = nlp(String_vetor_right)

			if (Execute_Rules_Activity (doc_Left)==True or Execute_Rules_Event (doc_Left)==True):
				Left=True
			if (Execute_Rules_Activity (doc_Right)==True or Execute_Rules_Event (doc_Right)==True):
				Right=True
		
			if (Left == True and Right==True):
				print("-------------------------")
				print ("Sentença:" +str(sent.encode('utf-8')))
				print("Regra - 1 AND")
				print("Indica-se um AND")
				print ("Tarefa/Evento:" + str (String_vetor_left))
				print ("Tarefa/Evento:" +str(String_vetor_right))
				print("-------------------------")	
				return True
			else:
				return False
	else:
		return False	


	#-------------------------------------------Regra 2- AND- TUTORIAL---------------------------
def  Get_Condict_Sub_Obj_rule_2_AND(doc_atual):
	
	Right=False
	String_vetor_left=None
	String_vetor_right=None
	vetor_all=None
	Indice_Word,Conteudo,Divide = Get_Word_indice_content_Divide_AND(doc_atual)
	if (Indice_Word<4 and Divide ==True):
			print (Conteudo)
			vetor_all= sent.split(str(Conteudo))
			print("vetor->"+str(vetor_all[0]))
			String_vetor_left=vetor_all[0]
			String_vetor_right= vetor_all[1]
			# colocando cada frase em um doc para verificar se a frase do lado direito ou esquerdo é realmente uma tarefa
			#doc_Left = nlp(String_vetor_left)
			doc_Right = nlp(String_vetor_right)

			if (Execute_Rules_Activity (doc_Right)==True or Execute_Rules_Event (doc_Right)==True):
				Right=True
		
			if (Right==True):
				print("-------------------------")
				print ("Sentença:" +str(sent.encode('utf-8')))
				print("Regra - 2 AND")
				print("Indica-se um AND")
				print ("Tarefa/Evento::"+str(String_vetor_right))
				print("-------------------------")	
				return True
			else:
				return False
	else:
		return False	

	

def Execute_Rule_AND(doc_atual):
	Alternative_Signal_Word=False
	ERROR=1000
	AND=False
	global AND_RULES
	#regra 1 and doc e tutorial 
	if (AND==False):
		print ("entrou aqi R1")
		Result_rule_1_AND= Get_Condict_Sub_Obj_rule_1_AND(doc_atual)		 
		if (Result_rule_1_AND == True):
				global AND_RULE_R1
				AND_RULES=AND_RULES+1
				AND_RULE_R1=AND_RULE_R1+1
				AND=True				
				return AND
	if (AND==False):
		print ("entrou aqi R2")
		Result_rule_2_AND= Get_Condict_Sub_Obj_rule_2_AND(doc_atual)		 
		if (Result_rule_2_AND == True):
				global AND_RULE_R2
				AND_RULES=AND_RULES+1
				AND_RULE_R2=AND_RULE_R2+1
				AND=True				
				return AND

#------------------NÃO ENTROU EM NENHUMA REGA------------
	if (AND==False):
		print("Sentença: "+ str(sent.encode('utf-8'))+"---> Não definida pelo protótipo_AND")			

#-------------------------------------------------------TESTES AQUIIIII--------------------------------------------------------------

def Testes_Aqui  (doc_atual):
	for word in doc_atual:
		#print ("teste= "+ word.pos_)
		print("dep->"+word.text_with_ws + " <- "  + word.head.text_with_ws + " ("  + word.dep_ + ")" )
			#Aqui eu comparo se a palavra é ela mesma e se ela é "root" ou seja, o verbo principal da sentenca
		print ("tag->"+word.text_with_ws + " <- " + " ("  + word.tag_ + ")" )
		if (word.text_with_ws in (word.head.text_with_ws) and  word.dep_ in ('ROOT')):
			Main_Verb1=word

				

	'''for x in String_result:
		if (str(String).lower() == String_result):
			print ("only")
			Conteudo=x
			isSynonyms=True'''
	'''print ("String_result->"+str(String_result))
				print ("Conteudo->"+str(Conteudo))
				print ("isSynonyms->"+str(isSynonyms))'''
	
	'''for indice,cont in enumerate (doc_atual):
		String_do_texto= ''.join(w.text_with_ws for w in doc_atual)'''
	
	
	#String="in the meantime"
	#String_result=dictionary.synonym(str("meanwhile"))
	#print ("string result-->"+ str(String_do_texto))
	#String_result=dictionary.synonym(str("if"))	
	#if (str(String).lower() in String_result):
	#		print ("ENTROOOOOOOOOOOOOU")
	
	#print (String_result)
	
	
	#print (Get_dep_String (0,doc))

	#print ("MAIN VERG-> "+str (Main_Verb1.text_with_ws))
	#print ("TAG- MAIN VERB->"+ str(Main_Verb1.tag_))

#------------------------------	-------------------------MAIN--------------------------------------------------------------
#it the first activity is to check and repair the hardware.
i=0
table_elementos=[]
table_regras=[]
for sent in sentences:
	elemento= {}
	regra= {}
	
	print ("--")
	#print ("Sentenca " + str(i) + " inicial: "+ sent)
	#-------------------NOTEBOOK-----------------------------------
	
	#sent = sent.replace(".","").replace("\n","")
	#sent = (u'The SCT physical file was stored by the Back office.')
	#sent= (u'After the agente has confrmed the claim to the clerk')
	#sent = (u'It first checked whether the claimant is insured by the organization.')
	
	#sent = (u'In parallel with this, Department of sell send the document and notify the department of engineering, then the document is processed.')
	#sent = (u'it the first activity is to check and repair the hardware.')
	sent = (u'A cliente calls the help desk and makes a request.')
	
	doc = nlp(sent)
	#------------------PC UFRGS -----------------------------------
	doc = nlp(str(sent.replace(".","").replace("\n","")))
	#--------------------------------------------------------------
	
	i=i+1  
	
	
	
	
	Testes_Aqui (doc)

	TIPO_SENTENCA_XOR = 1
	TIPO_SENTENCA_AND = 2    
	TIPO_SENTENCA_OTHERS = 3
	TIPO_SENTENCA_Activity = 4
	TIPO_SENTENCA_Event = 5

	Activity = False
	Event = False
	Xor= False
	And=False

	
	#type_of_sentence =12345
	type_of_sentence = get_type_senteces(doc)


	print("tipo da sentenca abaixo")
	print(type_of_sentence)   

	if type_of_sentence == TIPO_SENTENCA_XOR:
	    Execute_Rule_XOR(doc)
	elif type_of_sentence == TIPO_SENTENCA_AND:
	    Execute_Rule_AND(doc)
	else:
	    Go_Rules_Activity_Event(doc)
	
print ("ActA-ATIVIDADES->"+str(ACTIVITY_RULES))
print ("ActA-ACTIVITY_RULE_R1->"+str(ACTIVITY_RULE_R1))  
print ("ActA-ACTIVITY_RULE_R2->"+str(ACTIVITY_RULE_R2))
print ("ActA-ACTIVITY_RULE_R3->"+str(ACTIVITY_RULE_R3))   
print ("ActA-ACTIVITY_RULE_R4->"+str(ACTIVITY_RULE_R4))   
print ("ActA-ACTIVITY_RULE_R6_DOC->"+str(ACTIVITY_RULE_R6_DOC))   
print ("ActA-ACTIVITY_RULE_R11_DOC->"+str(ACTIVITY_RULE_R11_DOC))   
print ("ActA-AND_RULE_R1->"+str(AND_RULE_R1))         
print ("ActA-AND_RULE_R2->"+str(AND_RULE_R2))   
print ("ActA-EVENT_RULE_R1->"+str(EVENT_RULE_R1))   
print ("ActA-EVENT_RULE_R6_DOC->"+str(EVENT_RULE_R6_DOC))   
print ("ActA-EVENT_RULE_R11_DOC->"+str(EVENT_RULE_R11_DOC))   
print ("ActA-XOR_RULE_R1->"+str(XOR_RULE_R1))   
print ("ActA-XOR_RULE_R2->"+str(XOR_RULE_R2))   
print ("XOR_RULE_R7_DOC->"+str(XOR_RULE_R7_DOC))   
print ("ActA-XOR_RULE_R7_DOC->"+str(XOR_RULE_R7_DOC))   
print ("ActA-XOR_RULE_R1_DOC->"+str(XOR_RULE_R1_DOC))   
print ("ActA-AND->"+str(AND_RULES))   
print ("ActA-XOR->"+str(XOR_RULES))   
print ("ActA-EVENT->"+str(EVENT_RULES))  
	#rec["tamanho_das_sentencas"]=len(sentences)

	#--------------------------GRAFICO DE TODOS OS ELEMENTOS 
ALL_RULES=XOR_RULES+ACTIVITY_RULES+AND_RULES+EVENT_RULES
elemento["AND"]=AND_RULES
elemento["XOR"]=XOR_RULES
elemento["ATIVIDADES"]=ACTIVITY_RULES
elemento["EVENT"]=EVENT_RULES
table_elementos.append(elemento)  	  
pd.DataFrame(table_elementos).to_csv("elemento.csv")

#--------------------------GRAFICO DAS REGRAS
regra["XOR_RULE_R1"]=XOR_RULE_R1
regra["XOR_RULE_R2"]=XOR_RULE_R2
regra["XOR_RULE_R7_DOC"]=XOR_RULE_R7_DOC
regra["XOR_RULE_R1_DOC"]=XOR_RULE_R1_DOC
regra["ACTIVITY_RULE_R1"]=ACTIVITY_RULE_R1
regra["ACTIVITY_RULE_R2"]=ACTIVITY_RULE_R2
regra["ACTIVITY_RULE_R3"]=ACTIVITY_RULE_R3
regra["ACTIVITY_RULE_R4"]=ACTIVITY_RULE_R4
regra["ACTIVITY_RULE_R6_DOC"]=ACTIVITY_RULE_R6_DOC
regra["ACTIVITY_RULE_R11_DOC"]=ACTIVITY_RULE_R11_DOC
regra["AND_RULE_R1"]=AND_RULE_R1
regra["AND_RULE_R2"]=AND_RULE_R2
regra["EVENT_RULE_R1"]=EVENT_RULE_R1
regra["EVENT_RULE_R6_DOC"]=EVENT_RULE_R6_DOC
regra["EVENT_RULE_R11_DOC"]=EVENT_RULE_R11_DOC
table_regras.append(regra)  	  
pd.DataFrame(table_regras).to_csv("regra.csv")

#String = "'''usa este codigo para gerar no ypython notebook'''
'''import pandas as pd
  %"matplotlib inline 

df= pd.read_csv('output.csv')
df.hist()''

'''
