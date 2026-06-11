import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.read_csv('../2020-Apr.csv', usecols=['category_code'])

print("Generando Figura 4...")
df_apparel = df[df['category_code'].str.contains('apparel', na=False)].copy()
top_categories = df_apparel['category_code'].value_counts().head(15)

plt.figure(figsize=(12, 8))
top_categories.plot(kind='barh', color='salmon')
plt.gca().invert_yaxis()
plt.title('Top 15 subcategorías de Apparel (Urban Soul)')

# Etiquetas en cada barra
for i, val in enumerate(top_categories.values):
    plt.text(val + 5000, i, f'{val:,}', va='center', fontsize=8)

# Espacio y formato eje X
plt.xlim(0, top_categories.max() * 1.15)
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

plt.tight_layout()
plt.savefig('../figuras/figura4_apparel.png', dpi=150)
plt.close()
print("figura guardado")

