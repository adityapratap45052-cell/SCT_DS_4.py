
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Accident dataset
df = pd.read_csv('accidents.csv')

# -----------------------------
# Exploratory Data Analysis
# -----------------------------

# Accidents by Weather Condition
sns.countplot(x='Weather_Condition', data=df, order=df['Weather_Condition'].value_counts().index)
plt.xticks(rotation=45)
plt.title('Accidents by Weather Condition')
plt.show()

# Accidents by Time of Day
sns.countplot(x='Time', data=df, order=df['Time'].value_counts().index)
plt.xticks(rotation=45)
plt.title('Accidents by Time of Day')
plt.show()

# Accidents by Road Condition
sns.countplot(x='Road_Condition', data=df, order=df['Road_Condition'].value_counts().index)
plt.xticks(rotation=45)
plt.title('Accidents by Road Condition')
plt.show()
