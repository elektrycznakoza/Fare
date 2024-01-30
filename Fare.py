import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Załaduj dane (pobierz dane lub dostosuj do swojego zbioru danych)
# Przykładowe dane
data = {
    'Fare': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

df = pd.DataFrame(data)

# Oblicz statystyki opisowe
mean_fare = df['Fare'].mean()
median_fare = df['Fare'].median()
q1 = df['Fare'].quantile(0.25)
q3 = df['Fare'].quantile(0.75)

# Wydrukuj statystyki
print(f'Średnia opłata: {mean_fare}')
print(f'Mediana opłaty: {median_fare}')
print(f'Kwartyl dolny: {q1}')
print(f'Kwartyl górny: {q3}')

# Wygeneruj wykres pudełkowy
plt.boxplot(df['Fare'])
plt.title('Wykres pudełkowy dla opłat')
plt.ylabel('Opłata')
plt.show()
