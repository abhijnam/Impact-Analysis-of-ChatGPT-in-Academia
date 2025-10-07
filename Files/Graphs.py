import pandas as pd
import matplotlib.pyplot as plt
import plotly
#graph to show the data from the tech sector on their opinion on whether using chatGPT is an inhibition to education
def graph_1():
   myres = ['total responses from tech','who used ChatGPT before','is not an inhibition to education', 'is inhibition to education']
   data = [87,37,19,18]
   plt.rcParams["figure.figsize"] = [4.00, 2.50]
   plt.rcParams["figure.autolayout"] = True
   ax = plt.bar(myres, data, width = 0.3)
   for myres, data,data in zip(myres,data,data):
      plt.text(myres, data, data)
   plt.title("Responses from Tech")
   plt.ylabel("Responses gathered from Survey")
   plt.show()

#graph to show the different fields of study / career paths of the respondents

def graph_2():
   myres = ['Arts','Technology','Business','Recreation','Social Science','Language/Culture','Mathematics','Sciences','Law/Criminology']
   data = [8,87,16,1,7,3,2,14,1]
   plt.rcParams["figure.figsize"] = [4.00, 2.50]
   plt.rcParams["figure.autolayout"] = True
   ax = plt.bar(myres, data, width = 0.5)
   for myres, data,data in zip(myres,data,data):
      plt.text(myres, data, data)
   plt.title("Field of Study")
   plt.xlabel("fields")
   plt.ylabel("Responses gathered from Survey")
   plt.show()

# graphs to show if chatGPT is considered cheating taking the entire range of respondents
def graph_3():
   myres = ['No, I have not heard of ChatGPT before', 'Yes, using chatGPT is considered cheating','No,using chatGPT is not considered cheating']
   data = [19,5,14]
   plt.rcParams["figure.figsize"] = [4.00, 2.50]
   plt.rcParams["figure.autolayout"] = True
   ax = plt.bar(myres, data, width = 0.3, color = 'orange')
   for myres, data,data in zip(myres,data,data):
      plt.text(myres, data, data)
   plt.title("Is chatGPT considered cheating?")
   plt.xlabel("Options given")
   plt.ylabel("Responses gathered from Survey")
   plt.show()

def graph_4():
   myres = ['Yes I have heard of ChatGPT, but never used it', 'Yes, using chatGPT is considered cheating','No,using chatGPT is not considered cheating']
   data = [71,37,34]
   plt.rcParams["figure.figsize"] = [4.00, 2.50]
   plt.rcParams["figure.autolayout"] = True
   ax = plt.bar(myres, data, width = 0.3, color = 'green')
   for myres, data,data in zip(myres,data,data):
      plt.text(myres, data, data)
   plt.title("Is chatGPT considered cheating?")
   plt.xlabel("Options given")
   plt.ylabel("Responses gathered from Survey")
   plt.show()


def graph_5():
   myres = ['Yes I have used ChatGPT before', 'Yes, using chatGPT is considered cheating','No,using chatGPT is not considered cheating']
   data = [49,22,27]
   plt.rcParams["figure.figsize"] = [4.00, 2.50]
   plt.rcParams["figure.autolayout"] = True
   ax = plt.bar(myres, data, width = 0.3, color = 'red')
   for myres, data,data in zip(myres,data,data):
      plt.text(myres, data, data)
   plt.title("Is chatGPT considered cheating?")
   plt.xlabel("Options given")
   plt.ylabel("Responses gathered from Survey")
   plt.show()

# graph to show the level of education of respondents
def graph_6():
   myres = ['Bachelors Degree', 'Masters Degree','Diploma','Highschool Diploma','Doctorate/PhD or higher']
   data = [97,25,7,10,1]
   plt.rcParams["figure.figsize"] = [4.00, 2.50]
   plt.rcParams["figure.autolayout"] = True
   ax = plt.bar(myres, data, width = 0.3, color = 'blue')
   for myres, data,data in zip(myres,data,data):
      plt.text(myres, data, data)
   plt.title("Level of education")
   plt.xlabel("Options given")
   plt.ylabel("Responses gathered from Survey")
   plt.show()

#graph to show for what reasons people in academia use ChatGPT
def graph_7():
   myres = ['General Questions','Entertainment','Homework Help','Research','Social media']
   data = [30,1,2,16,1]
   plt.rcParams["figure.figsize"] = [4.00, 2.50]
   plt.rcParams["figure.autolayout"] = True
   ax = plt.bar(myres, data, width = 0.3)
   for myres, data,data in zip(myres,data,data):
      plt.text(myres, data, data)
   plt.title("For what reason ChatGPT is used")
   plt.xlabel("Options")
   plt.ylabel("Responses gathered from Survey")
   plt.show()


# graph to show other fields excluding the tech opinions on chat GPT
def graph_8():
   myres = ['total responses from other fields','who used ChatGPT','not an inhibition to education','is an inhibition to education']
   data = [52,12,7,5]
   plt.rcParams["figure.figsize"] = [4.00, 2.50]
   plt.rcParams["figure.autolayout"] = True
   ax = plt.bar(myres, data, width = 0.3)
   for myres, data,data in zip(myres,data,data):
      plt.text(myres, data, data)
   plt.title("Responses from other fields of study on ChatGPT")
   plt.xlabel("Options")
   plt.ylabel("Responses gathered from Survey")
   plt.show()

if __name__ == "__main__":
   graph_1()
   #graph_2()
   #graph_3()
   #graph_4()
   #graph_5()
   #graph_6()
   #graph_7()
   #graph_8()
