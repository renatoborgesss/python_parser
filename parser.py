
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
	if doc[idx].dep_ in 'mark' and ("if" == str(val).lower()  or "whether" == str(val).lower() or  "otherwise"  == str(val).lower() or "either"  == str(val).lower() or  "only"  == str(val).lower() or "till"  == str(val).lower() or "until"  == str(val).lower() or "when"  == str(val).lower()):
		print("passo por aqui 4")
		return True    
	
	elif "if" == str(val).lower() :
		print("passo por aqui 2")
		z=doc[idx+1]
		if "not" == str(z).lower(): 
			#print("passo por aqui 3")
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
def isAgent (doc):
	Main_Verb = Definition_Main_Verb_Activity_or_Event (doc)
	for indice, conteudo in enumerate (doc):
		if (doc[indice].dep_ in ('agent') and str(doc[indice].head) == str (Main_Verb)):
			return True
	return False
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f

def isPresent_Perfect (doc):
	Main_Verb = Definition_Main_Verb_Activity_or_Event (doc)
	for indice, conteudo in enumerate (doc):
		if "has"  == str(conteudo).lower() or "have" == str(conteudo).lower() or "Hasn't" == str(conteudo).lower() or "Haven't" == str(conteudo).lower():
				if (doc[indice].dep_ in ('aux') and doc[indice].head == Main_Verb):
					print ("present_perfect")
					return True
	return False
def isConjuction (doc):
	for indice, conteudo in enumerate (doc):
		if doc[indice].dep_ in ('conj', 'cc', 'in'):
			print ("conjuncao")
			return True

	return False

<<<<<<< HEAD
=======
=======
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
def Go_Rules_Activity_Event(doc):
	#print ("sentenca3---"+ str (sent))
	Main_Verb = Definition_Main_Verb_Activity_or_Event (doc)
	Result_Verb_Tense = Definition_Verb_tense_Main_Verb(Main_Verb,doc) 
	if (Result_Verb_Tense == TIPO_SENTENCA_Activity):
		if (Execute_Rules_Activity (doc)==True):
			print ("")
		
		#Terminei aqui
	elif (Result_Verb_Tense == TIPO_SENTENCA_Event):
		if (Execute_Rules_Event (doc)==True):		
			print("")
		#Fazendo Aqui


        
def Definition_Main_Verb_Activity_or_Event (doc):
	for word in doc:
		#print ("teste= "+ word.pos_)
		print(word.text_with_ws + " <- "  + word.head.text_with_ws + " ("  + word.dep_ + ")" )
			#Aqui eu comparo se a palavra é ela mesma e se ela é "root" ou seja, o verbo principal da sentenca
		if (word.text_with_ws in (word.head.text_with_ws) and  word.dep_ in ('ROOT')):
			Main_Verb1=word
			return Main_Verb1

def Definition_Verb_tense_Main_Verb (Main_Verb,doc):
	# aqui eu vejo qual tempo verbal é o verbo principal 
	#VB Verb, base form
	# VBD Verb, past tense
	#VBG Verb, gerund or present participle
	#VBN Verb, past participle
	#VBP Verb, non-3rd person singular present
	# VBZ Verb, 3rd person singular present
	to_be = False
	for idx, val in enumerate (doc):
		#print("valor->"+str(val))
		if "is"  == str(val).lower() or "are" == str(val).lower() or "will be" == str(val).lower():
<<<<<<< HEAD
			print ("doc[idx].head->"+str(doc[idx].head))
			print ("Main_Verb->"+ str (Main_Verb))
=======
<<<<<<< HEAD
			print ("doc[idx].head->"+str(doc[idx].head))
			print ("Main_Verb->"+ str (Main_Verb))
=======
			#print ("doc[idx].head->"+str(doc[idx].head))
			#print ("Main_Verb->"+ str (Main_Verb))
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
			if (doc[idx].dep_ in ('auxpass') and doc[idx].head == Main_Verb):
				to_be=True
				break
	present_perfect= False			
	for idx, val in enumerate (doc):
		#print("valor->"+str(val))
		if "has"  == str(val).lower() or "have" == str(val).lower():
			#print ("doc[idx].head->"+str(doc[idx].head))
			#print ("Main_Verb->"+ str (Main_Verb))
			if (doc[idx].dep_ in ('aux') and doc[idx].head == Main_Verb and (doc[idx].tag_ =="VBP" or doc[idx].tag_ == "VBN" or doc[idx].tag_== "VBZ")):
				present_perfect=True
				break
	print ("Main_Verb->"+ str (Main_Verb))	
	print ("tag->"+str(Main_Verb.tag_))	
<<<<<<< HEAD
	if ((Main_Verb.tag_ == "VBP" or Main_Verb.tag_ == "VBZ" or Main_Verb.tag_ == "VB" or Main_Verb.tag_ == "VBG") or to_be==True):
		print ("Atividade")
		return TIPO_SENTENCA_Activity
	elif (Main_Verb.tag_ == "VBD" or Main_Verb.tag_ == "VBN" or present_perfect==True):
		print ("Evento")
=======
<<<<<<< HEAD
	if ((Main_Verb.tag_ == "VBP" or Main_Verb.tag_ == "VBZ" or Main_Verb.tag_ == "VB" or Main_Verb.tag_ == "VBG") or to_be==True):
		print ("Atividade")
		return TIPO_SENTENCA_Activity
	elif (Main_Verb.tag_ == "VBD" or Main_Verb.tag_ == "VBN" or present_perfect==True):
		print ("Evento")
=======
	if ((Main_Verb.tag_ == "VBP" or Main_Verb.tag_ == "VBZ" or Main_Verb.tag_ == "VB" or Main_Verb.tag_ == "VBG") or to_be==True or present_perfect==False):
		
		return TIPO_SENTENCA_Activity
	elif (Main_Verb.tag_ == "VBD" or Main_Verb.tag_ == "VBN" or to_be==False or present_perfect==True):
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
		return TIPO_SENTENCA_Event
#---------------------------------PEGAR SUJEITO, VERBO E OBJETO --- INDICE E CONTEUDO ---------

def Get_Content_Indice_Subject (doc):
	sujeito=None
	indice_sujeito=None
	for indice, conteudo in enumerate (doc):
		#indice do sujeito
		if doc[indice].dep_ in ('nsubj' , 'csubj','nsubjpass','xsubj','agent','csubjpass'):
			#print ("entrou aqui 2")
			sujeito = ''.join(w.text_with_ws for w in doc[indice].subtree)
			indice_sujeito=indice
			#suj_small=conteudo
<<<<<<< HEAD
			#print ('sujeito: ' + sujeito)
=======
			print ('sujeito: ' + sujeito)
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
			break

	return sujeito,indice_sujeito

def Get_Content_Indice_Verbo (doc):
	Verbo=None	
	indice_verbo=None
	for indice, conteudo in enumerate (doc):
			#print (''+dependency_labels_to_root(word)[0])
			#print word.text_with_ws 
			#print  dependency_labels_to_root(word)
			#print word.text_with_ws + ' '+word.tag_			
			#indice do verbo
			if (str(doc[indice])) in (str(doc[indice].head)) and  doc[indice].dep_ in ('ROOT'):
<<<<<<< HEAD
				#print ("entrou aqui 1")a
=======
<<<<<<< HEAD
				#print ("entrou aqui 1")a
=======
				#print ("entrou aqui 1")
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
				print("Verbo----->" + str(doc[indice]))
				indice_verbo=indice
				Verbo=conteudo
				break
	return Verbo,indice_verbo
def Get_Content_Indice_Object (doc):
	indice_objeto=None
	objeto=None
<<<<<<< HEAD
	for indice, conteudo in enumerate (doc):
		if doc[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod','pobj','oprd'):
			#print ("entrou aqui 3")
			obj=conteudo
			objeto=''.join(w.text_with_ws for w in doc[indice].subtree)
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + objeto)
			indice_objeto=indice
=======
	for indice, conteudo in enumerate (doc):
<<<<<<< HEAD
		if doc[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod','pobj','oprd'):
			#print ("entrou aqui 3")
			obj=conteudo
			objeto=''.join(w.text_with_ws for w in doc[indice].subtree)
=======
			#indice do sujeito
			if doc[indice].dep_ in ('nsubj' , 'csubj','nsubjpass','xsubj','agent','csubjpass'):
				#print ("entrou aqui 2")
				sujeito = ''.join(w.text_with_ws for w in doc[indice].subtree)
				indice_sujeito=indice
				print ('sujeito: ' + sujeito)


			#if word.tag_ in ('VBZ'):
			#    print ('verb:' + word.text_with_ws)
			#   print(''.join(w.text_with_ws for w in word.subtree))

			#indice do objeto
	for indice, conteudo in enumerate (doc):
		if doc[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod','pobj','oprd'):
			#print ("entrou aqui 3")
			obj=''.join(w.text_with_ws for w in doc[indice].subtree)
>>>>>>> origin/master
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + objeto)
			indice_objeto=indice
<<<<<<< HEAD
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
			break
	return 	objeto,	indice_objeto


#-------------------------------------------------------REGRAS ATIVIDADES--------------------------------------------------------------
	#--------REGRA 1 ------------------- SVO
def Get_indice_Sub_Obj_rule_1 (doc):
	#print ("sentenca---"+ str (sent))
	indice_verbo=None
	indice_sujeito=None
	indice_objeto=None
	ERROR=1000
	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)			
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)			
	objeto,indice_objeto = Get_Content_Indice_Object (doc)			
<<<<<<< HEAD
	# verificar se há conjunção na frase, se houver entao nao é esta regra e sim a regra 4
	other_rule=False
	if (isConjuction (doc) == True):
		other_rule=True
=======
	# verificar se há conjunção na frase, se houver entao nao é esta regra e sim a regra 4
	other_rule=False
	if (isConjuction (doc) == True):
		other_rule=True
=======
			#for w in doc[indice].subtree:
				#if w.dep_ in ('dobj', 'iobj'):
					#print ("entrou aqui 4")
					#print ("verbo: " + doc[indice].head.text_with_ws)
					#print ("-->" + w.text_with_ws)
		
			
	# verificar se há conjunção na frase, se houver entao nao é esta regra e sim a regra 4
	other_rule=False
	for indice, conteudo in enumerate (doc):
		if doc[indice].dep_ in ('conj', 'cc', 'in'):
			#Get_rule_4 (doc)
			print("conjunção")
			other_rule=True
			break
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f

	print ("indices- SVO->"+ str (indice_sujeito) + str (indice_verbo) + str(indice_objeto))
	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or other_rule==True):
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,ERROR]
	else:
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,-1]

	return result_indice	

	#--------REGRA 2 ------------------- WILL
def Get_indice_Sub_Obj_rule_2 (doc):
	
	indice_verbo=None
	indice_sujeito=None
	indice_objeto=None
	indice_will=None
	ERROR = 1000

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f

	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)			
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)			
	objeto,indice_objeto = Get_Content_Indice_Object (doc)
<<<<<<< HEAD
=======
=======
	for indice, conteudo in enumerate (doc):
			#print (''+dependency_labels_to_root(word)[0])
			#print word.text_with_ws 
			#print  dependency_labels_to_root(word)
			#print word.text_with_ws + ' '+word.tag_
			
			#indice do verbo
			if (str(doc[indice])) in (str(doc[indice].head)) and  doc[indice].dep_ in ('ROOT'):
				#print ("entrou aqui 1")
				print("Verbo----->" + str(doc[indice]))
				indice_verbo=indice
	for indice, conteudo in enumerate (doc):
				#indice do sujeito
				if doc[indice].dep_ in ('nsubj' , 'csubj','nsubjpass','xsubj','agent','csubjpass'):
					#print ("entrou aqui 2")
					sujeito = ''.join(w.text_with_ws for w in doc[indice].subtree)
					indice_sujeito=indice
					#print ("indice sujeito " + str(indice_sujeito))
					print ('sujeito: ' + sujeito)
				
	
	for indice, conteudo in enumerate (doc):
		#print (str (doc[indice].dep_))
		#Advérbio é uma palavra invariável que modifica o sentido do verbo, do adjetivo e do próprio advérbio.
		#ADVCL Adverbial clause modifier 
		#ADVMOD Adverbial modifier
		if (doc[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod','pobj','oprd')):
			#print ("entrou aqui 3")
			obj=''.join(w.text_with_ws for w in doc[indice].subtree)
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + obj)
			indice_objeto=indice
			for w in doc[indice].subtree:
				if w.dep_ in ('dobj', 'iobj'):
					#print ("entrou aqui 4")
					#print ("verbo: " + doc[indice].head.text_with_ws)
					#print ("-->" + w.text_with_ws)
					break
			#print("indice_objeto-->" +str (indice_objeto))
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f

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
	indice_sujeito=None
	indice_verbo=None
	indice_article=None
	indice_objeto=None	
	ERROR = 1000

<<<<<<< HEAD
	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)			
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)			
	objeto,indice_objeto = Get_Content_Indice_Object (doc)			
=======
<<<<<<< HEAD
	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)			
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)			
	objeto,indice_objeto = Get_Content_Indice_Object (doc)			
=======
	for indice, conteudo in enumerate (doc):
			#print (''+dependency_labels_to_root(word)[0])
			#print word.text_with_ws 
			#print  dependency_labels_to_root(word)
			#print word.text_with_ws + ' '+word.tag_
			
			#indice do verbo
		if (str(doc[indice])) in (str(doc[indice].head)) and  doc[indice].dep_ in ('ROOT'):
			#print ("entrou aqui 1.3")
			print("Verbo----->" + str(doc[indice]))
			indice_verbo=indice
	for indice, conteudo in enumerate (doc):
		#print (str (doc[indice].dep_))
		#Advérbio é uma palavra invariável que modifica o sentido do verbo, do adjetivo e do próprio advérbio.
		#ADVCL Adverbial clause modifier 
		#ADVMOD Adverbial modifier
		if (doc[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod','pobj')):
			#print ("entrou aqui 3.3")
			obj=''.join(w.text_with_ws for w in doc[indice].subtree)
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + obj)
			indice_objeto=indice
			for w in doc[indice].subtree:
				if w.dep_ in ('dobj', 'iobj'):
					#print ("entrou aqui 3.3")
					print ("verbo: " + doc[indice].head.text_with_ws)
					#print ("-->" + w.text_with_ws)
					break
			
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
	for indice, conteudo in enumerate (doc):    
		if (doc[indice].dep_ in ('DT', 'det') and ("a"  == str(conteudo).lower() or "an"  == str(conteudo).lower())):
			indice_article=indice
			#print("indice_artigo--->"+ str(indice_article))
			#print ("artigo-->" + str(conteudo))
			break
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======

>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
	#print ("V->"+str(indice_verbo))		
	#print ("a->"+str(indice_article))	
	#print ("O->"+str(indice_objeto))	
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
			
			if (("and" == str(val).lower())):
				vetor_all= sent.split('and')
			else:
				vetor_all= sent.split('or')

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
def Get_rule_6 (doc):
	indice_verbo=None
	indice_sujeito=None
	indice_objeto=None
	ERROR=1000
<<<<<<< HEAD
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)	
=======
<<<<<<< HEAD
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)	
=======
	for indice, conteudo in enumerate (doc):
			#print (''+dependency_labels_to_root(word)[0])
			#print word.text_with_ws 
			#print  dependency_labels_to_root(word)
			#print word.text_with_ws + ' '+word.tag_
			
			#indice do verbo
			if (str(doc[indice])) in (str(doc[indice].head)) and  doc[indice].dep_ in ('ROOT'):
				#print ("entrou aqui 1")
				print("Verbo----->" + str(doc[indice]))
				indice_verbo=indice
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
	for indice, conteudo in enumerate (doc):
			#indice do sujeito
			if doc[indice].dep_ in ('nsubj' , 'csubj','nsubjpass','xsubj','agent','csubjpass') and doc[indice].tag_ in ('NN') :
				#print ("entrou aqui 2")
				sujeito = ''.join(w.text_with_ws for w in doc[indice].subtree)
				indice_sujeito=indice
				print ('sujeito: ' + sujeito)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======


			#if word.tag_ in ('VBZ'):
			#    print ('verb:' + word.text_with_ws)
			#   print(''.join(w.text_with_ws for w in word.subtree))

			#indice do objeto
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
	for indice, conteudo in enumerate (doc):
		if doc[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod','pobj','oprd') and doc[indice].tag_ in ('NN') :
			#print ("entrou aqui 3")
			obj=''.join(w.text_with_ws for w in doc[indice].subtree)
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + obj)
<<<<<<< HEAD
			indice_objeto=indice		
=======
<<<<<<< HEAD
			indice_objeto=indice		
			
	# verificar se há conjunção na frase, se houver entao nao é esta regra e sim a regra 4
	other_rule=False
	if (isConjuction (doc) == True):
		other_rule=True

	#print ("indices- SVO->"+ str (indice_sujeito) + str (indice_verbo) + str(indice_objeto))
	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or other_rule==True):
=======
			indice_objeto=indice
			#for w in doc[indice].subtree:
				#if w.dep_ in ('dobj', 'iobj'):
					#print ("entrou aqui 4")
					#print ("verbo: " + doc[indice].head.text_with_ws)
					#print ("-->" + w.text_with_ws)
		
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
			
	# verificar se há conjunção na frase, se houver entao nao é esta regra e sim a regra 4
	other_rule=False
	if (isConjuction (doc) == True):
		other_rule=True

	#print ("indices- SVO->"+ str (indice_sujeito) + str (indice_verbo) + str(indice_objeto))
<<<<<<< HEAD
	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or other_rule==True):
=======
	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or Rule4==True):
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,ERROR]
	else:
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,-1]

	return result_indice	
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======





	#result_indice = [indice_verbo,indice_sujeito,indice_objeto]
	#return result_indice
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
#------------- regra 11 .Doc ---------------------
def Get_rule_11 (doc):
	ERROR=1000
	#Se o lado esquerdo ou direito for verdadeiro é tarefa senao não é tarefa
	Left= False
	Right = False
	indice_verbo_left = None
	indice_verbo_right= None
	indice_objeto_right= None

	for idx, val in enumerate (doc):
		if (("and" == str(val).lower() or "or" == str(val).lower()) and idx > 2):
			
			if (("and" == str(val).lower())):
				vetor_all= sent.split('and')
			else:
				vetor_all= sent.split('or')

			String_vetor_left=vetor_all[0]
			String_vetor_right= vetor_all[1]
			# colocando cada frase em um doc para verificar se a frase do lado direito ou esquerdo é realmente uma tarefa
			doc_Left = nlp(String_vetor_left)
			doc_Right = nlp(String_vetor_right)
			#print ("string right->" + String_vetor_right)
			#verbo esquerdo
			#Testes_Aqui (doc_Right)
			#Testes_Aqui (doc_Left)
			for indice, conteudo in enumerate (doc_Left):
				print ("entrou aqui 11.1")
				
				if (doc_Left[indice].tag_=='VBP' or doc_Left[indice].tag_ == 'VBZ'  or doc_Left[indice].tag_ == 'VB' ):
					print ("entrou aqui 11.2")
					indice_verbo_left= indice
					break
			#verbo direito
			for indice, conteudo in enumerate (doc_Right): 
				if (doc_Right[indice].dep_ in ('ROOT') or doc_Right[indice].tag_=='VBP' or doc_Right[indice].tag_ == 'VBZ'  or doc_Right[indice].tag_ == 'VB' ):
					print ("entrou aqui 11.3")
					indice_verbo_right = indice
					break
				
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
<<<<<<< HEAD

#---------------------CHECKS VETOR ATIVIDADES----------------------------------------------
=======
<<<<<<< HEAD

#---------------------CHECKS VETOR ATIVIDADES----------------------------------------------
=======
def Get_rule_7 (doc):
	indice_verbo=None
	indice_sujeito=None
	indice_objeto=None
	ERROR=1000
	to_be = False
	indice_to_be=None
	indice_and_or=None
	Main_Verb = Definition_Main_Verb_Activity_or_Event (doc)
	for idx, val in enumerate (doc):
		print("valor->"+str(val))
		if "is"  == str(val).lower() or "are" or "will be" == str(val).lower():
			print ("doc[idx].head->"+str(doc[idx].head))
			print ("Main_Verb->"+ str (Main_Verb))
			if (doc[idx].dep_ in ('auxpass') and doc[idx].head == Main_Verb):
				indice_to_be=idx
				break	

	for indice, conteudo in enumerate (doc):
			#print (''+dependency_labels_to_root(word)[0])
			#print word.text_with_ws 
			#print  dependency_labels_to_root(word)
			#print word.text_with_ws + ' '+word.tag_
			
			#indice do verbo
			if (str(doc[indice])) in (str(doc[indice].head)) and  doc[indice].dep_ in ('ROOT'):
				#print ("entrou aqui 1")
				print("Verbo----->" + str(doc[indice]))
				indice_verbo=indice
				break
				print ("depois do break")
	for indice, conteudo in enumerate (doc):
			#indice do sujeito
			if doc[indice].dep_ in ('nsubj' , 'csubj','nsubjpass','xsubj','agent','csubjpass') and doc[indice].tag_ in ('NN') :
				#print ("entrou aqui 2")
				sujeito = ''.join(w.text_with_ws for w in doc[indice].subtree)
				indice_sujeito=indice
				print ('sujeito: ' + sujeito)
				break

	for indice, conteudo in enumerate (doc):
		if doc[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod','pobj','oprd') and doc[indice].tag_ in ('NN') :
			#print ("entrou aqui 3")
			obj=''.join(w.text_with_ws for w in doc[indice].subtree)
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + obj)
			indice_objeto=indice

	for indice, conteudo in enumerate (doc):
		#print ("indice->"+ str (indice))
		#print ("conteudo->" + str (conteudo))
		#print ("doc[indice].dep_ -->" + str (doc[indice].dep_))
		if (("and" == str(conteudo).lower() or "or" == str(conteudo).lower()) and idx > 2 and doc[indice].dep_ in ('conj', 'cc', 'in')) :
			print ("indice_and_or")
			indice_and_or=indice

	#print ("VSOAT->"+ str(indice_verbo)+str(indice_sujeito)+str(indice_objeto)+str(indice_and_or)+str(indice_to_be))
	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or indice_and_or==True or indice_to_be==True):
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,indice_and_or,indice_to_be,ERROR]
	else:
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,indice_and_or,indice_to_be,-1]

	return result_indice	
#---------------------CHECKS VETOR ----------------------------------------------
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
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
			print("Sentença: "+ str(sent.encode('utf-8')))
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
			print ("Sentença: "+ str(sent.encode('utf-8')))
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
			print("Sentença: "+ str(sent.encode('utf-8')))
			print("-------------------------")
			print("Indica-se uma Tarefa ")
			print("-------------------------")
			return True
		else:
			print ("R3- ERROR")
			return False

def Check_vetor_rule_6(vetor):
	ERROR=1000

<<<<<<< HEAD
	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_6(doc)
=======
<<<<<<< HEAD
	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_6(doc)
=======
	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_1(doc)
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
	if (vetor[3] == ERROR):
		print ("entrou aqui 1.flag")
		print ("R1- ERROR")
		
		return False
		
	else:
		#Deu CERTO
		indice_verbo2 = vetor[0]
		indice_sujeito2=vetor[1]
		indice_objeto2= vetor[2]
		
		if (indice_sujeito2<indice_objeto2 and indice_objeto2<indice_verbo2):
			#regra 1
			print("Regra 6")
			print("Sentença: "+ str(sent.encode('utf-8')))
			print("-------------------------")
			print("Indica-se uma Tarefa ")
			print("-------------------------")
			return True
		else:
			print ("R1- ERROR")
			return False

def Check_vetor_rule_11 (vetor):
	ERROR=1000

	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_1(doc)
	if (vetor[3] == ERROR):
<<<<<<< HEAD
		print ("entrou aqui 11.flag")
		print ("R11- ERROR")		
=======
<<<<<<< HEAD
		print ("entrou aqui 11.flag")
		print ("R11- ERROR")		
=======
		print ("entrou aqui 1.flag")
		print ("R1- ERROR")
		
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
		return False
		
	else:
		#Deu CERTO
		indice_verbo_left = vetor[0]
		indice_verbo_right=vetor[1]
		indice_objeto_right= vetor[2]
		#[indice_verbo_left,indice_verbo_right,indice_objeto_right,ERROR]
		if (indice_verbo_right< indice_objeto_right):
			#regra 1
			print("Regra 11")
<<<<<<< HEAD
			print("Sentença: "+ str(sent.encode('utf-8')))
=======
			print("Sentença: "+ sent)
			print("-------------------------")
			print("Indica-se uma Tarefa ")
			print("-------------------------")
			return True
		else:
<<<<<<< HEAD
			print ("R11- ERROR")
			return False

=======
			print ("R1- ERROR")
			return False


def Check_vetor_rule_7(vetor):
	ERROR=1000

	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_1(doc)
	#print ("vetor-->" + str (vetor [5]))
	if (vetor[5] == ERROR):
		print ("entrou aqui 1.flag")
		print ("R1- ERROR")
		
		return False
		
	else:
	
		#result_indice = [indice_verbo,indice_sujeito,indice_objeto,indice_and_or,indice_to_be,ERROR]
		indice_verbo = vetor[0]
		indice_sujeito=vetor[1]
		indice_objeto= vetor[2]
		indice_and_or=vetor[3]
		indice_to_be=vetor[4]
		
		if (indice_sujeito< indice_objeto and indice_objeto<indice_and_or and indice_and_or < indice_to_be and indice_to_be < indice_verbo ):
			#regra 1
			print("Regra 7")
			print("Sentença: "+ sent)
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
			print("-------------------------")
			print("Indica-se uma Tarefa ")
			print("-------------------------")
			return True
		else:
			print ("R11- ERROR")
			return False

<<<<<<< HEAD
=======

>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
def Execute_Rules_Activity(doc):		
	
	flag=1
	ERROR=1000
	flag2=1
	flag3=1
	Activity=False
	#--------REGRA 1 ------------------- SVO
<<<<<<< HEAD
	if (Activity==False):
=======
<<<<<<< HEAD
	if (Activity==False):
=======
	if (flag==1):
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
		print ("entrou aqi R1")
		vetor_result_indice_rule1= Get_indice_Sub_Obj_rule_1(doc)		
		Result_rule_1 = Check_vetor_rule_1 (vetor_result_indice_rule1) 
		if (Result_rule_1 == True):
				#ACTIVITY_RULE_1= ACTIVITY_RULE_1+1
				Activity=True
				
				return Activity			
	#--------REGRA 2 ------------------- S + WILL + VERB+OBJ	
<<<<<<< HEAD
	if (Activity==False):
=======
<<<<<<< HEAD
	if (Activity==False):
=======
	if (flag==1):
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
		print ("entrou aqi R2")
		vetor_result_indice_rule2 = Get_indice_Sub_Obj_rule_2(doc)	
		Result_rule_2= Check_vetor_rule_2 (vetor_result_indice_rule2)
		if (Result_rule_2 == True):
				#ACTIVITY_RULE_1= ACTIVITY_RULE_1+1
				Activity=True
				
				return Activity	
	#--------REGRA 3 ------------------- <Verb>+<article>+<Obj>
	
<<<<<<< HEAD
	if (Activity==False):
=======
<<<<<<< HEAD
	if (Activity==False):
=======
	if (flag==1):
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
		print ("entrou aqi R3")
		vetor_result_indice_rule3= Get_indice_Sub_Obj_rule_3(doc)
		Result_rule_3= Check_vetor_rule_3 (vetor_result_indice_rule3)
		if (Result_rule_3 == True):
				#ACTIVITY_RULE_1= ACTIVITY_RULE_1+1
				Activity=True
				
				return Activity

	#--------REGRA 4 ------------------- < Sujeito> + <verb> + <obj> [and,or] + <verb> + <obj>
<<<<<<< HEAD
	if (Activity==False):
=======
<<<<<<< HEAD
	if (Activity==False):
=======
	if (flag==1):
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
		print ("entrou aqui R4")
		result_rule_4= Get_rule_4(doc)
		
		if (result_rule_4 ==True):
			print("Regra do Sujeito> + <verb> + <obj> [and,or] + <verb> + <obj>")
<<<<<<< HEAD
			print("Sentença: "+ str(sent.encode('utf-8')))
=======
			print("Sentença: "+ sent)
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
			
			Activity=True
			return Activity
	
	#-----------REGRA 6 do .DOC -----------------------------------------------
<<<<<<< HEAD
	if (Activity==False):
=======
<<<<<<< HEAD
	if (Activity==False):
=======
	if (flag==1):
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
		print ("entrou aqi R6")
		vetor_result_indice_rule6 =Get_rule_6 (doc)
		result_rule_6 = Check_vetor_rule_6 (vetor_result_indice_rule6)
		if (result_rule_6==True):
				Activity=True
<<<<<<< HEAD
				
				return Activity
# ------------ Regra 11 do .Doc -------------------------
	if (Activity==False):
=======
<<<<<<< HEAD
				
				return Activity
# ------------ Regra 11 do .Doc -------------------------
	if (Activity==False):
=======
				flag=2
				return Activity
# ------------ Regra 11 do .Doc -------------------------
	if (flag==1):
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
		print ("entrou aqi 11")
		vetor_result_indice_rule11 =Get_rule_11 (doc)
		result_rule_11 = Check_vetor_rule_11 (vetor_result_indice_rule11)
		if (result_rule_11==True):
				print ("11	<Subject (ocult)>+<Verb> + [and,or]+ <verb> + <obj>")
<<<<<<< HEAD
				Activity=True				
				return Activity

=======
<<<<<<< HEAD
				Activity=True				
				return Activity

=======
				Activity=True
				flag=2
				return Activity
# ------------- REGRA 7 do .Doc --------------
	if (flag==1):
		print ("entrou aqi R7")
		vetor_result_indice_rule7 =Get_rule_7 (doc)
		result_rule_7= Check_vetor_rule_7 (vetor_result_indice_rule7)
		if (result_rule_7==True):
				print ("print regra 7")
				Activity=True
				flag=2
				return Activity
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
#NÃO ENTROU EM NENHUMA REGRA
	if (Activity==False):		
		print("Sentença: "+str(sent.encode('utf-8'))+"---> Não definida pelo protótipo")

#-------------------------------------------------------REGRAS EVENTOS--------------------------------------------------------------
#--------REGRA 1 ------------------- SVO---- tutorial
def Get_indice_Sub_Obj_rule_1_Event (doc):
	#print ("sentenca---"+ str (sent))
<<<<<<< HEAD
	#indice_verbo=None
	#indice_sujeito=None
	#indice_objeto=None
=======
<<<<<<< HEAD
	#indice_verbo=None
	#indice_sujeito=None
	#indice_objeto=None
=======
	indice_verbo=None
	indice_sujeito=None
	indice_objeto=None
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
	ERROR=1000
	Verbo=None
	sujeito=None
	suj_small=None
	objeto=None
<<<<<<< HEAD
	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)	
	objeto,indice_objeto = Get_Content_Indice_Object (doc)
	
	other_rule=False	
	#if (isConjuction (doc) == True):
	#	other_rule=True
	if (isAgent (doc)==True):
		other_rule=True
	if (isPresent_Perfect (doc)==True):
		other_rule=True
		
=======
<<<<<<< HEAD
	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)	
	objeto,indice_objeto = Get_Content_Indice_Object (doc)
	
	other_rule=False	
	if (isConjuction (doc) == True):
		other_rule=True
	if (isAgent (doc)==True):
		other_rule=True
	if (isPresent_Perfect (doc)==True):
		other_rule=True
		
=======
	for indice, conteudo in enumerate (doc):
			#print (''+dependency_labels_to_root(word)[0])
			#print word.text_with_ws 
			#print  dependency_labels_to_root(word)
			#print word.text_with_ws + ' '+word.tag_
			
			#indice do verbo
			if (str(doc[indice])) in (str(doc[indice].head)) and  doc[indice].dep_ in ('ROOT'):
				#print ("entrou aqui 1")a
				print("Verbo----->" + str(doc[indice]))
				indice_verbo=indice
				Verbo=conteudo
				break
	for indice, conteudo in enumerate (doc):
			#indice do sujeito
			if doc[indice].dep_ in ('nsubj' , 'csubj','nsubjpass','xsubj','agent','csubjpass'):
				#print ("entrou aqui 2")
				sujeito = ''.join(w.text_with_ws for w in doc[indice].subtree)
				indice_sujeito=indice
				suj_small=conteudo
				print ('sujeito: ' + sujeito)

				break


			#if word.tag_ in ('VBZ'):
			#    print ('verb:' + word.text_with_ws)
			#   print(''.join(w.text_with_ws for w in word.subtree))

			#indice do objeto
	for indice, conteudo in enumerate (doc):
		if doc[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod','pobj','oprd'):
			#print ("entrou aqui 3")
			obj=conteudo
			objeto=''.join(w.text_with_ws for w in doc[indice].subtree)
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + objeto)
			indice_objeto=indice
			break
			#for w in doc[indice].subtree:
				#if w.dep_ in ('dobj', 'iobj'):
					#print ("entrou aqui 4")
					#print ("verbo: " + doc[indice].head.text_with_ws)
					#print ("-->" + w.text_with_ws)
		
			
	other_rule=False
	
	Main_Verb = Definition_Main_Verb_Activity_or_Event (doc)
	for indice, conteudo in enumerate (doc):
		# verificar se há conjunção na frase, se houver entao nao é esta regra e sim outra regra
		if doc[indice].dep_ in ('conj', 'cc', 'in'):
			#Get_rule_4 (doc)
			print("conjunção")
			other_rule=True
			break
		# verificar se ha agent e se ele é dependente do Verbo da frase.
		if (isAgent (doc)==True):
			#print ("dep->"+ str(doc[indice].dep_))
			print ("agent")
			other_rule=True
			break
		if "has"  == str(val).lower() or "have" == str(val).lower():
			if (doc[idx].dep_ in ('aux') and doc[idx].head == Main_Verb):
				print ("present_perfect")
				other_rule=True
				break
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f

	print ("indices- SVO->"+ str (indice_sujeito) + str (indice_verbo) + str(indice_objeto))
	
	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or other_rule==True):
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,ERROR]
	else:
<<<<<<< HEAD
		
=======
<<<<<<< HEAD
		
=======
		print ("---------------")
		
		print ("Indicação de Lane: " + str (sujeito))
		print ("Indicação de Label:" + str (objeto) + " " +str (Verbo))
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
		
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,-1]


	return result_indice
#----------------------REGRA 6 EVENT .DOC------------
def Get_indice_Sub_Obj_rule_6_Event(doc):
<<<<<<< HEAD
	#indice_verbo=None
	#indice_sujeito=None
	#indice_objeto=None
=======
<<<<<<< HEAD
	#indice_verbo=None
	#indice_sujeito=None
	#indice_objeto=None
=======
	indice_verbo=None
	indice_sujeito=None
	indice_objeto=None
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
	ERROR=1000
	Verbo=None
	sujeito=None
	
	objeto=None
<<<<<<< HEAD
	
	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)
=======
<<<<<<< HEAD
	
	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)

	print ("suj->"+ str (sujeito))
	print ("indice->" + str (indice_sujeito))

	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)
	print ("ver->"+ str (Verbo))
	print ("indice->" + str (indice_verbo))
	objeto,indice_objeto = Get_Content_Indice_Object (doc)
	print ("objeto->"+ str (objeto))
	print ("indice->" + str (indice_objeto))
	


	other_rule=False
	if (isConjuction (doc) == True):
		other_rule=True
	if (isPresent_Perfect (doc)==True):
		other_rule=True	
=======
	for indice, conteudo in enumerate (doc):
			#print (''+dependency_labels_to_root(word)[0])
			#print word.text_with_ws 
			#print  dependency_labels_to_root(word)
			#print word.text_with_ws + ' '+word.tag_
			
			#indice do verbo
			if (str(doc[indice])) in (str(doc[indice].head)) and  doc[indice].dep_ in ('ROOT'):
				#print ("entrou aqui 1")a
				print("Verbo----->" + str(doc[indice]))
				indice_verbo=indice
				Verbo=conteudo
				break
	for indice, conteudo in enumerate (doc):
			#indice do sujeito
			if doc[indice].dep_ in ('nsubj' , 'csubj','nsubjpass','xsubj','agent','csubjpass'):
				#print ("entrou aqui 2")
				sujeito = ''.join(w.text_with_ws for w in doc[indice].subtree)
				indice_sujeito=indice
				
				print ('sujeito: ' + sujeito)
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f

	print ("suj->"+ str (sujeito))
	print ("indice->" + str (indice_sujeito))

	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)
	print ("ver->"+ str (Verbo))
	print ("indice->" + str (indice_verbo))
	objeto,indice_objeto = Get_Content_Indice_Object (doc)
	print ("objeto->"+ str (objeto))
	print ("indice->" + str (indice_objeto))
	


	other_rule=False
<<<<<<< HEAD
	#if (isConjuction (doc) == True):
	#	other_rule=True
	if (isPresent_Perfect (doc)==True):
		other_rule=True	
=======
	Main_Verb = Definition_Main_Verb_Activity_or_Event (doc)
	for indice, conteudo in enumerate (doc):
		# verificar se há conjunção na frase, se houver entao nao é esta regra e sim outra regra
		if doc[indice].dep_ in ('conj', 'cc', 'in'):
			#Get_rule_4 (doc)
			print("conjunção")
			other_rule=True
			break
		if "has"  == str(conteudo).lower() or "have" == str(conteudo).lower():
			if (doc[indice].dep_ in ('aux') and doc[indice].head == Main_Verb):
				print ("present_perfect")
				other_rule=True
				break
		
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f

	print ("indices- SVO->"+ str (indice_sujeito) + str (indice_verbo) + str(indice_objeto))
	
	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or other_rule==True):
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,ERROR]
	else:
<<<<<<< HEAD
		
=======
<<<<<<< HEAD
		
=======
		print ("---------------")
		
		print ("Indicação de Lane: " + str (objeto))
		print ("Indicação de Label:" + str (sujeito) + "" +str (Verbo))
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
		
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,-1]


	return result_indice


#----------------------REGRA 11 EVENT .DOC------------
def Get_indice_Sub_Obj_rule_11_Event(doc):
	indice_verbo=None
	indice_sujeito=None
	indice_objeto=None
	ERROR=1000
	Verbo=None
	sujeito=None
	
	objeto=None
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
	sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)			
	Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)			
	objeto,indice_objeto = Get_Content_Indice_Object (doc)
	other_rule=False
<<<<<<< HEAD
	#if (isConjuction (doc) == True):
	#	other_rule=True
=======
	if (isConjuction (doc) == True):
		other_rule=True

	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or other_rule==True):
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,ERROR]
	else:			
=======
	for indice, conteudo in enumerate (doc):
			#print (''+dependency_labels_to_root(word)[0])
			#print word.text_with_ws 
			#print  dependency_labels_to_root(word)
			#print word.text_with_ws + ' '+word.tag_
			
			#indice do verbo
			if (str(doc[indice])) in (str(doc[indice].head)) and  doc[indice].dep_ in ('ROOT'):
				#print ("entrou aqui 1")a
				print("Verbo----->" + str(doc[indice]))
				indice_verbo=indice
				Verbo=conteudo
				break
	for indice, conteudo in enumerate (doc):
			#indice do sujeito
			if doc[indice].dep_ in ('nsubj' , 'csubj','nsubjpass','xsubj','agent','csubjpass'):
				#print ("entrou aqui 2")
				sujeito = ''.join(w.text_with_ws for w in doc[indice].subtree)
				indice_sujeito=indice
				
				print ('sujeito: ' + sujeito)

				break


			#if word.tag_ in ('VBZ'):
			#    print ('verb:' + word.text_with_ws)
			#   print(''.join(w.text_with_ws for w in word.subtree))

			#indice do objeto
	for indice, conteudo in enumerate (doc):
		if doc[indice].dep_ in ('dobj', 'iobj','advcl', 'advcmod','pobj','oprd'):
			#print ("entrou aqui 3")
			obj=conteudo
			objeto=''.join(w.text_with_ws for w in doc[indice].subtree)
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + objeto)
			indice_objeto=indice
			break
			#for w in doc[indice].subtree:
				#if w.dep_ in ('dobj', 'iobj'):
					#print ("entrou aqui 4")
					#print ("verbo: " + doc[indice].head.text_with_ws)
					#print ("-->" + w.text_with_ws)

>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f

	if (indice_verbo==None or indice_sujeito==None or indice_objeto==None or other_rule==True):
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,ERROR]
<<<<<<< HEAD
	else:			
=======
	else:
		if (isAgent (doc)==True):
			print ("---------------")
			print ("Indicação de Lane: " + str (objeto))
			print ("Indicação de Label:" + str (sujeito) + "" +str (Verbo))
		else:
			print ("---------------")
			print ("Indicação de Lane: " + str (sujeito))
			print ("Indicação de Label:" + str (Verbo) + "" +str (objeto))
			
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
		result_indice = [indice_verbo,indice_sujeito,indice_objeto,-1]


	return result_indice

	
<<<<<<< HEAD
		
#-----------------------------CHECK  VETOR EVENTOS-----------
def Check_vetor_rule_1_Event (vetor):
	ERROR=1000

	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_1(doc)
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
			sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)			
			Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)			
			objeto,indice_objeto = Get_Content_Indice_Object (doc)
			
			print ("---------------")		
			print("Sentença: "+ sent)
			print ("Indicação de Lane: " + str (sujeito))
			print ("Indicação de Label:" + str (objeto) + " " +str (Verbo))	

			print("Regra do SVO 1")			
=======
		
#-----------------------------CHECK  VETOR EVENTOS-----------
def Check_vetor_rule_1_Event (vetor):
	ERROR=1000

	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_1(doc)
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
<<<<<<< HEAD
			sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)			
			Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)			
			objeto,indice_objeto = Get_Content_Indice_Object (doc)
			
			print ("---------------")		
			print("Sentença: "+ str(sent.encode('utf-8')))
			print ("Indicação de Lane: " + str (sujeito))
			print ("Indicação de Label:" + str (objeto) + " " +str (Verbo))	

			print("Regra do SVO 1")			
=======
			print("Regra do SVO 1")
			print("Sentença: "+ sent)
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
			print("-------------------------")
			print("Indica-se um Evento")
			print("-------------------------")
			return True
		else:
			print ("R1- ERROR")
			return False



def Check_vetor_rule_6_Event(vetor):
	ERROR=1000

	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_1(doc)
	if (vetor[3] == ERROR):
		print ("R6- ERROR")
		return False
		
	else:
			
		indice_verbo2 = vetor[0]
		indice_sujeito2=vetor[1]
		indice_objeto2= vetor[2]
		
		if (indice_sujeito2<indice_verbo2 and indice_verbo2<indice_objeto2):
			#regra 6
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
			sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)			
			Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)			
			objeto,indice_objeto = Get_Content_Indice_Object (doc)
			print ("---------------")
<<<<<<< HEAD
			print("Sentença: "+ str(sent.encode('utf-8')))	
			print ("Indicação de Lane: " + str (objeto))
			print ("Indicação de Label:" + str (sujeito) + "" +str (Verbo))
			print("Regra do SVO 6")			
=======
			print("Sentença: "+ sent)	
			print ("Indicação de Lane: " + str (objeto))
			print ("Indicação de Label:" + str (sujeito) + "" +str (Verbo))
			print("Regra do SVO 6")			
=======
			print("Regra do SVO 6")
			print("Sentença: "+ sent)
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
			print("-------------------------")
			print("Indica-se um Evento")
			print("-------------------------")
			return True
		else:
			print ("R6- ERROR")
			return False
def Check_vetor_rule_11_Event(vetor):
	ERROR=1000

	#pega a posicao do ERRO la no vetor resultante que vem do DEF Get_indice_Sub_Obj_rule_1(doc)
	if (vetor[3] == ERROR):
		print ("R11- ERROR")
		return False
		
	else:
			
		indice_verbo2 = vetor[0]
		indice_sujeito2=vetor[1]
		indice_objeto2= vetor[2]
		
		if (indice_sujeito2<indice_verbo2 and indice_verbo2<indice_objeto2):
			#regra 6
<<<<<<< HEAD
			sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)			
			Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)			
			objeto,indice_objeto = Get_Content_Indice_Object (doc)
			print("Sentença: "+ str(sent.encode('utf-8')))
			if (isAgent (doc)==True):
				print ("---------------")
				print ("Indicação de Lane: " + str (objeto))
				print ("Indicação de Label:" + str (sujeito) + " " +str (Verbo))
			else:
				print ("---------------")
				print ("Indicação de Lane: " + str (sujeito))
				print ("Indicação de Label:" + str (objeto) + " " +str (Verbo))
				
=======
<<<<<<< HEAD
			sujeito,indice_sujeito = Get_Content_Indice_Subject (doc)			
			Verbo, indice_verbo = Get_Content_Indice_Verbo (doc)			
			objeto,indice_objeto = Get_Content_Indice_Object (doc)
			print("Sentença: "+ sent)
			if (isAgent (doc)==True):
				print ("---------------")
				print ("Indicação de Lane: " + str (objeto))
				print ("Indicação de Label:" + str (sujeito) + "" +str (Verbo))
			else:
				print ("---------------")
				print ("Indicação de Lane: " + str (sujeito))
				print ("Indicação de Label:" + str (Verbo) + "" +str (objeto))
				print("Regra do SVO 11")
				print("-------------------------")
				print("Indica-se um Evento")
				print("-------------------------")
				return True
		else:
			print ("R11- ERROR")
=======
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
			print("Regra do SVO 11")
			print("-------------------------")
			print("Indica-se um Evento")
			print("-------------------------")	
			return True
		
		else:
<<<<<<< HEAD
			print ("R11- ERROR")
=======
			print ("R6- ERROR")
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
			return False


def Execute_Rules_Event (doc):
	flag=1
	ERROR=1000
	Event=False
	#-----------------------------R1 tutorial
	if (Event==False):
		print ("entrou aqi R1")
		vetor_result_indice_rule1_Event= Get_indice_Sub_Obj_rule_1_Event(doc)		
		Result_rule_1_Event = Check_vetor_rule_1_Event (vetor_result_indice_rule1_Event) 
		if (Result_rule_1_Event == True):
				#EVENT_RULE= EVENT_RULE+1
				Event=True				
				return Event
	#-----------------R6 S+V+AGENT+O			
	if (Event==False):
		# SVO + Agent
		print ("entrou aqi R6")
		vetor_result_indice_rule6_Event= Get_indice_Sub_Obj_rule_6_Event(doc)		
		Result_rule_6_Event = Check_vetor_rule_6_Event (vetor_result_indice_rule6_Event) 
		if (Result_rule_6_Event == True):
				#EVENT_RULE= EVENT_RULE+1
				Event=True				
				return Event

	#--------------------R11 . DOC -----------
	if (Event==False):
		print ("entrou aqi R11")
		vetor_result_indice_rule11_Event= Get_indice_Sub_Obj_rule_11_Event(doc)		
		Result_rule_11_Event = Check_vetor_rule_11_Event (vetor_result_indice_rule11_Event) 
		if (Result_rule_11_Event == True):
				#EVENT_RULE= EVENT_RULE+1
				Event=True				
				return Event

	 # ----------------------NÃO ENTROU EM NENHUMA REGRA
	if (Event==False):
		print("Sentença: "+ str(sent.encode('utf-8'))+"---> Não definida pelo protótipo")

#-------------------------------------------------------REGRAS XOR--------------------------------------------------------------
def Get_Word_alternative (doc):
	isAlternative_Word=False
	Word=False
	Right=False
	for indice, val in enumerate (doc):
		if (("," == str(val).lower() and doc[indice].dep_ in ('punct'))):
			
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
				if (Execute_Rules_Activity (doc_Right)==True or Execute_Rules_Event (doc_Right)==True):
					Right=True
				
				if (Right==True):
					print ("-------------------------")
					print ("Sentença:"+ str(sent.encode('utf-8')))
					print ("Indica-se um XOR (alternative)")
					print ("Tarefa/Evento:"+str(String_vetor_right))
					print ("-------------------------")
					return True


	return False	    

def Get_Word_indice_content_Divide (doc):
	lista = ["whether","if","either", "only", "till", "until", "when"]	
	Indice_Word=None
	Conteudo=None
	Divide=False
	
	for indice1, val1 in enumerate (doc):
				if "if" == str(val1).lower():
					print("passo por aqui 2")
					z=doc[indice1+1]
					if "not" == str(z).lower(): 
						#print("passo por aqui 3")						
						Indice_Word=indice1
						Divide=True
						Conteudo=val1
						break
				if "in"  == str(val1).lower():
					#print("passo por aqui 5")
					z=doc[indice1+1]
					y=doc[indice1+2]
					if ("case"  == str(z).lower() and "of"  == str(y).lower()):						
						Indice_Word=indice1
						Divide=True
						Conteudo=val1
						break
					if "case"  == str(z).lower():
						#print("passoIndice_Word=indice1
						Indice_Word=indice1
						Divide=True
						Conteudo=val1
						break

				for indice2, val2 in enumerate (lista):					
					if (val2 == str(val1).lower()):
						Indice_Word=indice1
						Divide=True
						Conteudo=val1
						break
	return Indice_Word,Conteudo,Divide


# ----------------------REGRA 1 TUTORIAL ----

def Get_Condict_Sub_Obj_rule_1_XOR(doc):
	Left=False
	Right=False
	
	Indice_Word,Conteudo,Divide = Get_Word_indice_content_Divide(doc)
	if (Indice_Word<2):
		for indice, val in enumerate (doc):
			if (("," == str(val).lower() and doc[indice].dep_ in ('punct'))):
				
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
def Get_Condict_Sub_Obj_rule_2_XOR (doc):
	Left=False
	Right=False

	
	Indice_Word,Conteudo,Divide = Get_Word_indice_content_Divide(doc)
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


def Get_Condict_Sub_Obj_rule_1_DOC_XOR(doc):	
	Indice_Word,Conteudo,Divide = Get_Word_indice_content_Divide(doc)
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



def Execute_Rule_XOR(doc):
	Alternative_Signal_Word=False
	ERROR=1000
	XOR=False
	#regra 1 tutorial
	if (XOR==False):
		print ("entrou aqi R1")
		Result_rule_1_XOR= Get_Condict_Sub_Obj_rule_1_XOR(doc)		 
		if (Result_rule_1_XOR == True):
				#EVENT_RULE= EVENT_RULE+1
				XOR=True				
				return XOR
	#alternative Signal word
	if (XOR == False):
		print ("entrou aqi R1-alternative XOR")
		Result_rule_alternative_XOR= Get_Word_alternative(doc)		 
		if (Result_rule_alternative_XOR == True):
				#EVENT_RULE= EVENT_RULE+1
				Alternative_Signal_Word=True
				XOR=True				
				return Alternative_Signal_Word
	#regra 2 tutorial ------------
	if (XOR==False):
		print ("entrou aqi R2_XOR")
		Result_rule_2_XOR= Get_Condict_Sub_Obj_rule_2_XOR(doc)		 
		if (Result_rule_2_XOR == True):
				#EVENT_RULE= EVENT_RULE+1
				XOR=True				
				return XOR			

	# regra 1 ----DOC
	if (XOR==False):
		print ("entrou aqi R1_DOC_XOR")
		Result_rule_1_DOC_XOR= Get_Condict_Sub_Obj_rule_1_DOC_XOR(doc)		 
		if (Result_rule_1_DOC_XOR == True):
				#EVENT_RULE= EVENT_RULE+1
				XOR=True				
				return XOR	
	# ----------------------NÃO ENTROU EM NENHUMA REGRA
	if (XOR==False):
		print("Sentença: "+ str(sent.encode('utf-8'))+"---> Não definida pelo protótipo_XOR")
#-------------------------------------------------------TESTES AQUIIIII--------------------------------------------------------------

def Testes_Aqui  (doc):
	for word in doc:
		#print ("teste= "+ word.pos_)
		print("dep->"+word.text_with_ws + " <- "  + word.head.text_with_ws + " ("  + word.dep_ + ")" )
			#Aqui eu comparo se a palavra é ela mesma e se ela é "root" ou seja, o verbo principal da sentenca
		print ("tag->"+word.text_with_ws + " <- " + " ("  + word.tag_ + ")" )
		if (word.text_with_ws in (word.head.text_with_ws) and  word.dep_ in ('ROOT')):
			Main_Verb1=word

	print ("MAIN VERG-> "+str (Main_Verb1.text_with_ws))
	print ("TAG- MAIN VERB->"+ str(Main_Verb1.tag_))
	
#-------------------------------------------------------MAIN--------------------------------------------------------------

i=0

for sent in sentences:
	
	print ("--")
	#print ("Sentenca " + str(i) + " inicial: "+ sent)
	#-------------------NOTEBOOK-----------------------------------
	
	#sent = sent.replace(".","").replace("\n","")
	#sent = (u'The SCT physical file was stored by the Back office.')
<<<<<<< HEAD
	#sent= (u'After the agente has confrmed the claim to the clerk')
	sent = (u'It first checked whether the claimant is insured by the organization.')
	#sent = (u'If not, it send to Department of the intelligence.')
=======
	#sent= (u'After the agente has confirmed the claim to the clerk')
<<<<<<< HEAD
	#sent = (u'The claims officer then writed a settlement recommendation')
	sent = (u'department of engineering and sell are informed by Manager')
=======
	#sent = (u'The medicine had not taken by She')
	sent = (u'Urgent document has been received by the Manager.')
>>>>>>> origin/master
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
	doc = nlp(sent)
	#------------------PC UFRGS -----------------------------------
	#doc = nlp(str(sent.replace(".","").replace("\n","")))
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

<<<<<<< HEAD

=======
	
>>>>>>> c1a453ce12daa665b208396c4b9fb886187e7c2f
	type_of_sentence = get_type_senteces(doc)


	print("tipo da sentenca abaixo")
	print(type_of_sentence)   

	if type_of_sentence == TIPO_SENTENCA_XOR:
	    Execute_Rule_XOR(doc)
	elif type_of_sentence == TIPO_SENTENCA_AND:
	    Execute_Rule_AND(doc)
	else:
	    Go_Rules_Activity_Event(doc)




	


