###IMPORT
#starting spacy
from spacy.en import English
nlp = English()
from __future__ import unicode_literals     
import resource
import sys
#Main


#opening sentences file
f = open('sentences.txt', 'r')
sentences = f.readlines()



for sent in sentences:
	sent = sent.replace(".","").replace("\n","")
	print ("--")
	print ("Sentenca: "+ sent)
	doc = nlp(str(sent))
	cont1=0
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
	    
	#print("tipo: "+ s.get_type_senteces.text_with_ws)

	#if (regra1(doc)):
	    #cont1=cont1+1 
	    #print ("sentenca:"+ sent)


def get_type_senteces(doc):
	for idx, val in enumerate (doc):          
		if isSIGNAL_WORDS_XOR(idx,val,doc):
			return TIPO_SENTENCA_XOR
	for idx, val in enumerate (doc):          
		if isSIGNAL_WORDS_AND(idx,val,doc):
		    return TIPO_SENTENCA_AND
	return TIPO_SENTENCA_OTHERS    
     

def isSIGNAL_WORDS_XOR(idx,val,doc):
    print (val)
    print("passo por aqui 1")
    if "if" in str(val).lower():
        print("passo por aqui 2")
        z=doc[idx+1]       
        if "not" in str(z).lower(): 
            print("passo por aqui 3")

            return True
    elif "if" in str(val).lower()  or "otherwise"  in str(val).lower() or "either"  in str(val).lower() or  "only"  in str(val).lower() or "till"  in str(val).lower() or "until"  in str(val).lower() or "when"  in str(val).lower():
        print("passo por aqui 4")
        return True
    
    elif "in"  in str(val).lower():
        print("passo por aqui 5")
        z=doc[idx+1]
        y=doc[idx+2]
        if "case"  in str(z).lower() or ("case"  in str(z).lower() and "of"  in str(y).lower()):
            print("passo por aqui 6")
            return True
    else:
        print("passo por aqui 7")
        return False




def isSIGNAL_WORDS_AND(idx,val,doc):
    print (val)
    print("passo por aqui 8")
    if "while"  in str(val).lower()  or "meanwhile" in str(val).lower() or "concurrently" in str(val).lower() or "meantime" in str(val).lower() or "simultaneously" in str(val).lower() or "whereas"  in str(val).lower():
        print("passo por aqui 9")
        return True
    elif "In"  in str(val).lower():
        print("passo por aqui 10")
        z=doc[idx+1]
        y=doc[idx+2]
        q=doc[idx+3]
        if ("parallel"  in str(z).lower() or ("parallel"  in str(z).lower() and "with"  in str(y).lower() and "this" in str(q).lower())):
            print("passo por aqui 11")
            return True
        elif ("the"  in str(z).lower() and "meantime" in str(y).lower()):
            print("passo por aqui 12")
            return True
        elif ("addition"  in str(z).lower() and "to"  in str(y).lower()):
            print("passo por aqui 13")
            return True
    elif "at"  in str(val).lower():
        z=doc[idx+1]
        y=doc[idx+2]
        q=doc[idx+3]
        print("passo por aqui 14")
        if ("the"  in str(z).lower() and "same" in str(y).lower() and "time" in str(q).lower()):
            print("passo por aqui 15")
            return True           
    else:
        print("passo por aqui 16")
        return False




## CHAMADAS DAS REGRAS
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


def regra1(doc):
	cont1=0

	for word in doc:
		#print (''+dependency_labels_to_root(word)[0])
		#print word.text_with_ws 
		#print  dependency_labels_to_root(word)
		#print word.text_with_ws + ' '+word.tag_
		if word.dep_ in ('nsubj' , 'csubj'):
			sujeito = ''.join(w.text_with_ws for w in word.subtree)
			print ('sujeito: ' + sujeito)


		#if word.tag_ in ('VBZ'):
		#    print ('verb:' + word.text_with_ws)
		#   print(''.join(w.text_with_ws for w in word.subtree))


		if word.dep_ in ('dobj', 'iobj'):
			obj=''.join(w.text_with_ws for w in word.subtree)
			#print (word.subtree[0].text_with_ws)
			print('objeto: ' + obj)
			for w in word.subtree:
				if w.dep_ in ('dobj', 'iobj'):
					print ("verbo: " + word.head.text_with_ws)
					print ("-->" + w.text_with_ws)

			#achar_verbo_arvore(word.head)








