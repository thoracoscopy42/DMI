import pandas as pd

df = pd.read_csv("job_salary_prediction_dataset.csv")

#ilość rekordów 
print(df.shape)
#sprawdzamy czy nie ma wartości Null
print(df.isnull().sum())
#opis danych + wszystkie zmienne
print(df.describe())

