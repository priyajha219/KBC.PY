questions=[
    ["which language use in creating fb?"
            ,"python","french","javascript","php",4],
            ["which language use in creating fb?"
            ,"python","french","javascript","php",4],
            ["which language use in creating fb?"
            ,"python","french","javascript","php",4],
            ["which language use in creating fb?"
            ,"python","french","javascript","php",4],
            ["which language use in creating fb?"
            ,"python","french","javascript","php",4],
            ["which language use in creating fb?"
            ,"python","french","javascript","php",4],
            ["which language use in creating fb?"
            ,"python","french","javascript","php",4],
            ["which language use in creating fb?"
            ,"python","french","javascript","php",4],
            ]
    
     

levels=[1000,2000,3000,5000,10000,20000,40000,80000,16000,32000]
money=0
for i in range(0,(len(questions))):
    question=questions[i]
    print(f"\n\nquestion for Rs.{levels[i]}")
    print(f"a.{questions[i][1]}        b.{questions[i][2]}")
    print(f"c. {questions[i][3]}       d.{questions[i][4]} ")
    reply=int(input("Enter your answer (1-4)"))
    if(reply==question[-1]):
        print(f"Correct answer, you have won Rs.{levels[i]} ")
        if(i==4):
            money=10000
        elif (i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("Wrong answer!")
        break
print(f"your take home money is {money}")
    
    

