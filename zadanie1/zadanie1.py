import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport


# df = pd.read_csv("dataset_fixed.csv",sep=";")

# df = pd.read_csv("medical_insurance.csv",sep=",")
df = pd.read_csv("StudentPerformanceFactors.csv",sep=",")


"""
# Ile rekordów zawiera? 
print(df.shape)
# Jakie są typy danych tworzących atrybuty (cechy) w zbiorze danych? 
print(df.info())
#sprawdzamy czy nie ma wartości Null
print(df.isnull().sum())
#opis danych + wszystkie zmienne
print(df.describe())
"""

# print(df.describe(include="all"))

# for col in df.columns:
#     print(f"Dla kolumny: {col}")
#     print(df[col].value_counts(normalize=True))

# pandas_profiling.ProfileReport(df)

# profile = ProfileReport(df)
# profile.to_file("raport.html")





