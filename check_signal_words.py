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
