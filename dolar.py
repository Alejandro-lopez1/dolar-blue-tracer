import requests
import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt

# URL de la API del dólar blue
url = 'https://dolarapi.com/v1/dolares/blue'

# Pedimos la data
response = requests.get(url)
data = response.json()

# Extraemos los valores
fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
compra = data['compra']
venta = data['venta']

# Mostramos en consola
print(f'{fecha} | Dólar Blue -> Compra: {compra} | Venta: {venta}')

# Guardamos en un CSV
file_name = 'dolar_blue.csv'

# Si existe, leemos; si no, creamos DataFrame vacío
if os.path.exists(file_name):
    df = pd.read_csv(file_name)
else:
    df = pd.DataFrame(columns=['Fecha', 'Compra', 'Venta'])

# Agregamos la nueva fila con los valores correctos
nueva_fila = {'Fecha': fecha, 'Compra': compra, 'Venta': venta}
df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)

# Guardamos actualizado
df.to_csv(file_name, index=False, encoding='utf-8')
print(f"Registro guardado en {file_name}")

# -----------------------------
# GRÁFICO DE EVOLUCIÓN
# -----------------------------
df['Fecha'] = pd.to_datetime(df['Fecha'])
plt.figure(figsize=(8, 4))
plt.plot(df['Fecha'], df['Venta'], marker='o', label='Venta')
plt.plot(df['Fecha'], df['Compra'], marker='x', label='Compra')
plt.title('Evolución del Dólar Blue')
plt.xlabel('Fecha')
plt.ylabel('Valor (ARS)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
