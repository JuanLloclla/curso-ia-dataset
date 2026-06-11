import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../2020-Apr.csv", usecols=["event_time", "user_id"])

# Convertir a datetime
df['event_time'] = pd.to_datetime(df['event_time'], utc=True)
df['hour'] = df['event_time'].dt.hour
df['day_of_week'] = df['event_time'].dt.day_name()

# # Interacciones por hora (total)
# print("=== INTERACCIONES POR HORA ===")
# print(df.groupby('hour').size())

# # Interacciones por día de la semana (total)
# print("\n=== INTERACCIONES POR DÍA ===")
# orden = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# print(df.groupby('day_of_week').size().reindex(orden))

hora_counts = df.groupby('hour').size()
orden = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
dia_counts = df.groupby('day_of_week').size().reindex(orden)

# --- GRÁFICO 1: Por hora ---
plt.figure(figsize=(12, 6))
bars = plt.bar(hora_counts.index, hora_counts.values, color='steelblue')
plt.title('Interacciones por hora del día')
plt.xlabel('Hora del día')
plt.ylabel('Interacciones')
plt.xticks(range(24))
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))
# Anotación pico máximo
max_hora = hora_counts.idxmax()
plt.annotate(f'Pico máximo\n{hora_counts[max_hora]:,}\n({max_hora:02d}:00)',
             xy=(max_hora, hora_counts[max_hora]),
             xytext=(max_hora-3, hora_counts[max_hora]*0.95),
             arrowprops=dict(arrowstyle='->'), fontsize=9)
plt.tight_layout()
plt.savefig('../figuras/figura_hora.png', dpi=150)
plt.close()
print("figura_hora.png guardado")

# --- GRÁFICO 2: Por día ---
plt.figure(figsize=(10, 6))
plt.bar(dia_counts.index, dia_counts.values, color='mediumpurple')
plt.title('Interacciones por día de la semana')
plt.xlabel('Día de la semana')
plt.ylabel('Interacciones')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))
for i, (dia, val) in enumerate(dia_counts.items()):
    plt.text(i, val + 50000, f'{val:,}', ha='center', fontsize=7)
plt.tight_layout()
plt.savefig('../figuras/figura_dia.png', dpi=150)
plt.close()
print("figura_dia.png guardado")

