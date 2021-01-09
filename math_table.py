import random

def float_check(question):
    try:
        float(question)
        return True
    except ValueError:
        return False
#operation:sum, substraction    
def add_table(mode,operation):
    
    print("Calculate the "+operation+":")
    count=0
    point=0
    
    while count<5:
        if mode!="advanced":
            if mode=="easy":
                top=9
            elif mode=="intermediate":
                top=99
            elif mode=="hard":
                top=999
            
            first_num=random.randint(0,top)
            sec_num=random.randint(0,top)
        else:
            first_round=random.randint(0,4)
            sec_round=random.randint(0,4)
            first_num=round(random.uniform(100,1000),first_round)
            sec_num=round(random.uniform(100,1000),sec_round)
            max_round=max(first_round, sec_round)
            
            
        if operation=="sum":
            if mode!="advanced":
                tot=first_num+sec_num
            else:
                tot=round(first_num+sec_num,max_round)
            op="+"
        elif operation=="substraction":
            if mode!="advanced":
                tot=first_num-sec_num
            else:
                tot=round(first_num-sec_num,max_round)
            op="-"
        question=input(str(first_num)+ op + str(sec_num)+"=")
        while True:
            if question.isdigit():
                question=int(question)
                break
            elif float_check(question):
                question=float(question)
                break
            else:
                print("Please input a number")
                question=input(str(first_num)+op+ str(sec_num)+"=")
        
        if question==tot:
            print("Correct!")
            point+=1
        else:
            print("Wrong. Answer is "+ str(tot))
        count+=1
    
    print("End of the game. You got "+str(point)+ " correct answers out of 5")
    
    
    
    
add_table("advanced","sum")

