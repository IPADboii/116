from google.colab import files
data_to_load = files.upload()

"""plotting data on scatter plot"""

import pandas as pd
import plotly.express as px

df = pd.read_csv("Admission_Predict.csv")

toefl_score = df["TOEFL Score"].tolist()
result = df["Chance of admit"].tolist()



fig = px.scatter(x=toefl_score, y=result)
fig.show()

"""plotting the scatter plot with all the variables to see how the different variables affect the results"""

import plotly.graph_objects as go

toefl_score = df["TOEFL Score"].tolist()
gre_score = df["GRE Score"].tolist()

results = df["Chance of admit"].tolist()
colors=[]
for data in results:
  if data == 1:
    colors.append("green")
  else:
    colors.append("red")



fig = go.Figure(data=go.Scatter(
    x=toefl_score,
    y=gre_score,
    mode='markers',
    marker=dict(color=colors)
))
fig.show()

"""Splitting the data into two parts . Using a part of this data to train the prediction model and other part to test the prediction model."""

#scores and chances of admit
scores = df[["GRE Score", "TOEFL Score"]]

#results
results = df["Chance of admit"]

"""splitting the data into 75% and 25%. 75% data for training and then we will test our model on the remaining 25% percent of the data to test and determine the accuracy of our model."""

from sklearn.model_selection import train_test_split 

score_train, score_test, results_train, results_test = train_test_split(scores, results, test_size = 0.25, random_state = 0)

"""Training the logistic Regression model"""

from sklearn.linear_model import LogisticRegression 

classifier = LogisticRegression(random_state = 0) 
classifier.fit(score_train, results_train)

"""Testing the accuracy of the prediction"""

results_pred = classifier.predict(score_test)

from sklearn.metrics import accuracy_score 
print ("Accuracy : ", accuracy_score(results_test, results_pred))

"""tesiting the prediction model"""

from sklearn.preprocessing import StandardScaler 
sc_x = StandardScaler() 

score_train = sc_x.fit_transform(score_train)  

user_gre_score = int(input("Enter the GRE score -> "))
user_toefl_score = int(input("Enter the TOEFL Score -> "))

user_test = sc_x.transform([[user_gre_score, user_toefl_score]])

user_result_pred = classifier.predict(user_test)

if user_result_pred[0] == 1:
  print("This user may pass!")
else:
  print("This user may not pass!")