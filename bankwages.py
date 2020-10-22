import pandas as pd 
import seaborn as sns

dfwages = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/AER/BankWages.csv")
dfwages 

sns.pairplot(dfwages, hue="")

