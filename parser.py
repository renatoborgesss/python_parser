###IMPORT
#starting spacy
from spacy.en import English
#from __future__ import unicode_literals   
nlp = English()
  
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
    print (val)
    print("passo por aqui 1")
    if "if" == str(val).lower():
        print("passo por aqui 2")
        
        z=doc[idx+1]       
        if "not" == str(z).lower(): 
            print("passo por aqui 3")

            return True
    elif "if" == str(val).lower()  or "otherwise"  == str(val).lower() or "either"  == str(val).lower() or  "only"  == str(val).lower() or "till"  == str(val).lower() or "until"  == str(val).lower() or "when"  == str(val).lower():
        print("passo por aqui 4")
        return True
    
    elif "in"  == str(val).lower():
        print("passo por aqui 5")
        z=doc[idx+1]
        y=doc[idx+2]
        if "case"  == str(z).lower() or ("case"  == str(z).lower() and "of"  == str(y).lower()):
            print("passo por aqui 6")
            return True
    else:
        print("passo por aqui 7")
        return False




def isSIGNAL_WORDS_AND(idx,val,doc):
	print (val)
	print("passo por aqui 8")
	if "while"  == str(val).lower()  or "meanwhile" == str(val).lower() or "concurrently" == str(val).lower() or "meantime" == str(val).lower() or "simultaneously" == str(val).lower() or "whereas"  == str(val).lower():
		print("passo por aqui 9")
		return True
	elif "In"  == str(val).lower():
		print("passo por aqui 10")
		z=doc[idx+1]
		y=doc[idx+2]
		q=doc[idx+3]
		if ("parallel"  == str(z).lower() or ("parallel"  == str(z).lower() and "with"  == str(y).lower() and "this" == str(q).lower())):
			print("passo por aqui 11")
			return True 
		elif ("the"  == str(z).lower() and "meantime" == str(y).lower()):
			print("passo por aqui 12")
			return True
		elif ("addition"  == str(z).lower() and "to"  == str(y).lower()):
			print("passo por aqui 13")
			return True
	
	elif "at"  == str(val).lower():
		print("passo por aqui 14")
		z=doc[idx+1]
		y=doc[idx+2]
		q=doc[idx+3]
		if ("the"  == str(z).lower() and "same" == str(y).lower() and "time" == str(q).lower()):
		    print("passo por aqui 15")
		    return True           
	else:
		print("passo por aqui 16")
		return False


#-------------------------------------------------------IR REGRAS DE ATIVIDADE E EVENTOS--------------------------------------------------------------

# define se é atividade ou evento
def Go_Rules_Activity_Event(doc):
	Main_Verb = Definition_Main_Verb_Activity_or_Event (doc)
	Result_Verb_Tense = Definition_Verb_tense_Main_Verb(Main_Verb) 
	if (Result_Verb_Tense == TIPO_SENTENCA_Activity):
		Go_Rules_Activity (doc)
	else:
		Go_Rules_Event (doc)
	#PAREI AQUI


        
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
	    
	if (Main_Verb.tag_ == "VBP" or Main_Verb.tag_ == "VBZ" or Main_Verb.tag_ == "VB"):
		return TIPO_SENTENCA_Activity
	elif (Main_Verb.tag_ == "VBD" or Main_Verb.tag_ == "VBN" ):
		return TIPO_SENTENCA_Event

#-------------------------------------------------------REGRAS ATIVIDADES--------------------------------------------------------------

#--------------------RULE 1 -----------------------------
def Get_indice_Sub_Obj_rule_1 (doc):
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
		
			#achar_verbo_arvore(word.head)
	result_indice = [indice_verbo,indice_sujeito,indice_objeto]
	return result_indice

def Get_indice_Sub_Obj_rule_2 (doc):
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

	print(indice_verbo)
	print(indice_sujeito)
	print(indice_objeto)				
	result_indice = [indice_verbo,indice_sujeito,indice_objeto]
	return result_indice				



def Go_Rules_Activity(doc):	
	#--------REGRA 2 ------------------- S + WILL + VERB+OBJ
	vetor_result_indice_rule2 = Get_indice_Sub_Obj_rule_2(doc)	






	#--------REGRA 1 ------------------- SVO
	vetor_result_indice_rule1= Get_indice_Sub_Obj_rule_1 (doc)
	indice_verbo2 = vetor_result_indice_rule1[0]
	indice_sujeito2=vetor_result_indice_rule1[1]
	indice_objeto2= vetor_result_indice_rule1[2]
	
	if (indice_sujeito2<indice_verbo2 and indice_verbo2<indice_objeto2):
		#regra 1
		print ("Sentença: "+ sent)
		print ("Indica-se uma Tarefa ") 
	

#-------------------------------------------------------MAIN--------------------------------------------------------------

for sent in sentences:
	sent = sent.replace(".","").replace("\n","")
	print ("--")
	print ("Sentenca: "+ sent)
	doc = nlp(str(sent))
	
	
	TIPO_SENTENCA_XOR = 1
	TIPO_SENTENCA_AND = 2    
	TIPO_SENTENCA_OTHERS = 3
	TIPO_SENTENCA_Activity = 4
	TIPO_SENTENCA_Event = 5

	
	type_of_sentence = get_type_senteces(doc)


	print("tipo da sentenca abaixo")
	print(type_of_sentence)    

	if type_of_sentence == TIPO_SENTENCA_XOR:
	    Go_Rule_XOR(doc)
	elif type_of_sentence == TIPO_SENTENCA_AND:
	    Go_Rule_AND(doc)
	else:
	    Go_Rules_Activity_Event(doc)
	    
	


