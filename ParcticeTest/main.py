
from ast import Pass
import os
import json
from random import sample,shuffle





def get_test(data,num):
    Oopnion=["A", "B", "C", "D","E","F","G","H","I","J","K","L"]
    opnion=["A", "B", "C", "D","E","F","G","H","I","J","K","L"]
    testQuestion= sample(data,k=num)
    for temp in testQuestion:
        temp2=temp
        
        qes,ansers=temp2.popitem()
        ques_size= len(ansers)-1
        OopnionT=Oopnion[:ques_size]
        opnionT=opnion[:ques_size]
        
        ques=f"{qes}\n"
        shuffle(opnionT)
        for op,order in zip(opnionT,OopnionT) :
            ques+=f"{order}. {ansers[op]}\n"   
        ans=OopnionT[opnionT.index(ansers['Anser'])] 
        yield ques,ans,OopnionT

def start_test(data,ques_amount,isshow):
    #Oopnion=["A", "B", "C", "D"]
    try:
        mytest= get_test(data,ques_amount)
        ques_number=0
        right_answer=0
        Mistake_arr=[]
        for test,ans,Oopnion in mytest:
            ques_number+=1
            temp=test.split('?')
            print ("\nquestion",ques_number,"\n",u"\u001b[36m",temp[0],"\u001b[0m",temp[1])
            
            asnser= input("answer:").upper()
            while asnser not in Oopnion:asnser= input("aswer:").upper() 
            
                    
            if ans==asnser: right_answer+=1 
            else: 
                Mistake_arr.append({test:[ans,asnser]})
            if isshow:
                print(f"right_answer is -{ans} ")
                input("enter any key to continue")
        ##
        score=(right_answer/ques_amount)*100
        if score<70:color="31m"
        elif 80>score>70:color="33m"
        elif 90>score>80:color="34m"
        else :color="32m"
            
        print(f"\u001b[{color}------------------------------------------------end------------------------------------------------")
        print (f"\n\nwell done you finish the test \nyour answer right {right_answer} from {ques_amount} and scoreing {score}\n\n\n")
        print(u"\u001b[0m \u001b[31m")
        [print(list(i.keys())[0],"\n right answer is ",list(i.values())[0][0],"your answer was ",list(i.values())[0][1],end="\n\n\n") for i in Mistake_arr]
        
    except:
        print("------------------------------------------------end with eror------------------------------------------------")
        print (f"\n\nwell done you finish the test \nyour answer right {right_answer} from {ques_number} and scoreing {(right_answer/ques_number)*100}\n\n\n ")
        [print(list(i.keys())[0],"\n right answer is ",list(i.values())[0][0],"your answer was ",list(i.values())[0][1],end="\n\n\n") for i in Mistake_arr]
   
     
def main():
    #intilities
    filepath= "ques.json"
    filepath2="ParcticeTest/ques.json"
    file= open(filepath2,"r")
    data= json.load(file)
    
    
    #chosing test subjects
    input_test_options =["1","2","3"]
    print("welcome to gcpTest beta\n1.to ACE\n2.to PCA\n3.to exit")
    user_input= input("enter choice:")
    while user_input not in input_test_options:user_input=input("enter choice:")
    if user_input != "3":
        data=data[int(user_input)-1]
        os.system('clear')
        
    else:
        os.system('clear')
        print("good bye")
        return None
    
    #chosing test parm    
    input_options=["1","2"]
    print(f"welcome to gcpTest beta \nwe have {len(data)} questions \nenter 1 to show anser after ech questions \nenter 2 to show only scoring at the and ")
    
    user_input= input("enter choice:")
    while user_input not in input_options:user_input=input("enter choice:")
    if user_input == "1":
        print("choose questions amount")
        amount = input("enter amount:")
        while not amount.isdecimal() or not 0<int(amount)<len(data):amount = input("enter amount:") 
        isshow=True
    elif user_input == "2":
        print("choose questions amount")
        amount = input("enter amount:")
        while not amount.isdecimal() or not 0<int(amount)<len(data):amount = input("enter amount:") 
        isshow=False
    start_test(data,int(amount),isshow)
    

#main function    
if __name__=="__main__":
    main()