import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
from tabulate import tabulate
import os
file_path_1 = os.path.dirname(os.path.abspath('heard.xlsx'))
file_path_2 = os.path.dirname(os.path.abspath('techvschatgpt.xlsx'))
# Table 1: counts the number of people who heard of chat GPT
def table_1():
    var1 = pd.read_excel(file_path_1)
    question = list(var1['Have you heard of ChatGPT?']) # made list from column responses
    myres = list(var1[' is cheating?'])
    mycount_yes = 0 # counts the number of people who said yes to the question "Do you think using chatGPT is considered cheating"
    mycount_no = 0 # counts the number of people who said no to the question above
    myyes = 0 # counts the number of people who have used chatGPT before

    # used a for loop to tally up the responses to the options we gave in the survey
    for j in range(len(question)):
        if question[j] == "Yes, I have used it before":
            myyes +=1
    for i in range(len(question)):
        if question[i] == "Yes, I have used it before" and myres[i] == "Yes":
            mycount_yes +=1
        elif question[i] == "Yes, I have used it before" and myres[i] == "No":
            mycount_no +=1
    data = [['Yes, I have used ChatGPT before', myyes],['yes, using chatGPT is considered cheating',mycount_yes],['No,using chatGPT is not considered cheating',mycount_no]]
    col_name = ['Question asked', 'Responses']
    # a table to print out the number of responses to each option given in the survey
    print(tabulate(data, headers=col_name, tablefmt="fancy_grid"))


#Table 2: counts the number of people who heard of chat GPT but never used it
def table_2():
    var1 = pd.read_excel(file_path_1)
    myh = list(var1['Have you heard of ChatGPT?'])
    myres = list(var1[' is cheating?'])
    mycount_yes = 0 # counts the number of people who said yes to the question "Do you think using chatGPT is considered cheating"
    mycount_no = 0 # counts the number of people who said no to the question above
    myyes = 0 # counts the number of people who have used heard of chatGPT before but never used it
    for j in range(len(myh)):
        if myh[j] == "Yes, I have heard of it, but never used it":
            myyes +=1
    for i in range(len(myh)):
        if myh[i] == "Yes, I have heard of it, but never used it" and myres[i] == "Yes":
            mycount_yes +=1
        elif myh[i] == "Yes, I have heard of it, but never used it" and myres[i] == "No":
            mycount_no +=1
    data = [['Yes, I have heard of ChatGPT before but never used it', myyes],['yes, using chatGPT is considered cheating',mycount_yes],['No,using chatGPT is not considered cheating',mycount_no]]
    col_name = ['Question asked', 'Responses']
    print(tabulate(data, headers=col_name, tablefmt="fancy_grid"))


#Table 3: counts the number of people who never heard of chat GPT
def table_3():
    var1 = pd.read_excel(file_path_1)
    myh = list(var1['Have you heard of ChatGPT?'])
    myres = list(var1[' is cheating?'])
    mycount_yes = 0 # counts the number of people who said yes to the question "Do you think using chatGPT is considered cheating"
    mycount_no = 0 # counts the number of people who said no to the question above
    myyes = 0# counts the number of people who have not used ChatGPT before
    for j in range(len(myh)):
        if myh[j] == "No, I have not heard of it before":
            myyes +=1
    for i in range(len(myh)):
        if myh[i] == "No, I have not heard of it before" and myres[i] == "Yes":
            mycount_yes +=1
        elif myh[i] == "No, I have not heard of it before" and myres[i] == "No":
            mycount_no +=1
    data = [['No,I have not heard of it before', myyes],['yes, using chatGPT is considered cheating',mycount_yes],['No,using chatGPT is not considered cheating',mycount_no]]
    col_name = ['Question asked', 'Responses']
    print(tabulate(data, headers=col_name, tablefmt="fancy_grid"))

#Table 4: the career paths/fields selected
def table_4():
    var1 = pd.read_excel(file_path_2)
    myh = list(var1['Stream'])
    arts = 0
    tech = 0
    buisness = 0
    rec = 0
    ss = 0
    lc = 0
    math = 0
    science = 0
    law =0
    for i in range(len(myh)):
        if myh[i] == "Arts (ex. Music, Fashion, Interior Design)":
            arts +=1
        elif myh[i] == "Technology (ex. Computer Science, Engineering, Robotics)":
            tech +=1
        elif myh[i] == "Business (ex. Marketing, Human Resource Management)":
            buisness +=1
        elif myh[i] == "Recreation (ex Entertainment, Communication, media)":
            rec +=1
        elif myh[i] == "Social Science (ex. History, Geography, Psychology, Philosophy, Politics)":
            ss +=1
        elif myh[i] == "Language/Culture":
            lc +=1
        elif myh[i] == "Mathematics":
            math +=1
        elif myh[i] == "Science (ex. Biology, Chemistry, Physics)":
            science +=1
        elif myh[i] == "Criminology/Law":
            law +=1

    data = [['Arts', arts],['Technology',tech],['Business',buisness],['Recreation',rec],['Social Science',ss],['Language/Culture',lc],['Mathematics',math],['Sciences',science],['Law/Criminology',law]]
    col_name = ['field of study', 'representation']

    print(tabulate(data, headers=col_name, tablefmt="fancy_grid"))

#Table 5: level of education selected
def table_5():
    var1 = pd.read_excel(file_path_2)
    myres = list(var1['level of edu'])
    bachelors = 0
    masters = 0
    diploma = 0
    highschool = 0
    phd = 0
    for i in range(len(myres)):
            if myres[i] == "Bachelors degree":
                    bachelors +=1
            if myres[i] == "Masters degree":
                    masters +=1
            if myres[i] == "Highschool Diploma":
                    highschool +=1
            if myres[i] == "Diploma":
                    diploma +=1
            if myres[i] == "Doctorate/PHD or higher":
                    phd +=1
    data = [['bachelors degree',bachelors],['masters degree',masters],['diploma',diploma],["High school diploma", highschool],["Doctorate/PhD or higher",phd]]
    col_name = ['Degree','data']
    print(tabulate(data, headers=col_name, tablefmt="fancy_grid"))

#Table 6: what is chat GPT used for
def table_6():
    var1 = pd.read_excel(file_path_2)
    myres = list(var1['What do you use ChatGPT for? (Select all that apply)'])
    gq = 0
    entertainment = 0
    homework = 0
    research = 0
    socials = 0
    for i in range(len(myres)):
        mylist = str(myres[i]).split(",")
        for i in range(len(mylist)):
            if mylist[i] == "General Questions (ex. Assistance in fixing a problem)":
                gq +=1
            if mylist[i] == "Entertainment":
                entertainment +=1
            if mylist[i] == "Homework help":
                homework +=1
            if mylist[i] == "Research (ex. academic/work)":
                research +=1
            if mylist[i] == "Social Media":
                socials +=1
    data = [['General question',gq],['Entertainment',entertainment],['Homework Help',homework],["Research", research],["Social Media",socials]]
    col_name = ['Options','data']
    print(tabulate(data, headers=col_name, tablefmt="fancy_grid"))

#Table 7: opinions of chat GPT outside of tech
def table_7():
    var1 = pd.read_excel(file_path_2)
    myh = list(var1['Stream'])
    myres = list(var1['Have you heard of ChatGPT?'])
    mych = list(var1[' is cheating?'])
    myin = list(var1['inhibit education?'])
    others = 0 # total responses in tech
    others_used = 0 # counter to count the number of people from tech who used chatGPT
    others_no = 0 # counter to count the number of people from tech who used chatGPT and think using chatGPT is not an inhibition to education
    others_yes=0 # counter to count the number of people from tech who used chatGPT and think using chatGPT is an inhibition to education
    for i in range(len(myh)):
        if myh[i] != "Technology (ex. Computer Science, Engineering, Robotics)":
            others +=1
        if myh[i] != "Technology (ex. Computer Science, Engineering, Robotics)" and myres[i] == "Yes, I have used it before":
            others_used +=1
        if myh[i] != "Technology (ex. Computer Science, Engineering, Robotics)" and myres[i] == "Yes, I have used it before" and  myin[i] == "No" :
            others_no +=1
        if myh[i] != "Technology (ex. Computer Science, Engineering, Robotics)" and myres[i] == "Yes, I have used it before" and  myin[i] == "Yes" :
            others_yes +=1
    data = [['total responses from outside of Tech',others],['people who used ChatGPT',others_used],['Those who do not consider inhibition to education',others_no],["Those who do consider it as inhibition to education", others_yes]]
    col_name = ['Other field responses','data']
    print(tabulate(data, headers=col_name, tablefmt="fancy_grid"))


#Table 8: opinions of chat GPT in tech
def table_8():
    var1 = pd.read_excel(file_path_2)
    myh = list(var1['Stream'])
    myres = list(var1['Have you heard of ChatGPT?'])
    mych = list(var1[' is cheating?'])
    myin = list(var1['inhibit education?'])
    tech = 0 # total responses in tech
    tech_used = 0 # counter to count the number of people from tech who used chatGPT
    tech_no = 0 # counter to count the number of people from tech who used chatGPT and think using chatGPT is not an inhibition to education
    tech_yes=0 # counter to count the number of people from tech who used chatGPT and think using chatGPT is an inhibition to education
    for i in range(len(myh)):
        if myh[i] == "Technology (ex. Computer Science, Engineering, Robotics)":
            tech +=1
        if myh[i] == "Technology (ex. Computer Science, Engineering, Robotics)" and myres[i] == "Yes, I have used it before":
            tech_used +=1
        if myh[i] == "Technology (ex. Computer Science, Engineering, Robotics)" and myres[i] == "Yes, I have used it before" and  myin[i] == "No" :
            tech_no +=1
        if myh[i] == "Technology (ex. Computer Science, Engineering, Robotics)" and myres[i] == "Yes, I have used it before" and  myin[i] == "Yes" :
            tech_yes +=1
    data = [['total responses from tech',tech],['people who used ChatGPT',tech_used],['Those who do not consider inhibition to education',tech_no],["Those who do consider it as inhibition to education", tech_yes]]
    col_name = ['tech responses','data']
    print(tabulate(data, headers=col_name, tablefmt="fancy_grid"))

if __name__ == "__main__":
    table_1()
    table_2()
    table_3()
    table_4()
    table_5()
    table_6()
    table_7()
    table_8()


