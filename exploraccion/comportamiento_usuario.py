import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.read_csv("../2020-Apr.csv", usecols=["user_id"])
user_counts = df['user_id'].value_counts()

powerlaw = user_counts.value_counts().sort_index()
print(powerlaw)

plt.figure(figsize=(14, 7))
counts, edges, bars = plt.hist(user_counts, bins=100, log=True, color='skyblue', edgecolor='black')

# Etiqueta
for bar, val in zip(bars, counts):
    if val > 0:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.3,
                 f'{int(val):,}', ha='center', va='bottom', fontsize=6)

plt.title('Distribución de interacciones por usuario (Power Law)')
plt.xlabel('Interacciones por usuario')
plt.ylabel('Cantidad de usuarios (Log)')
plt.tight_layout()
plt.savefig('../figuras/figura3_powerlaw.png', dpi=150)
plt.close()
print("figura guardado")

