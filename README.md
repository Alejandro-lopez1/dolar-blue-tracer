# Dolar Blue Tracker AR
Un **script en Python** que consulta la cotización del **dólar blue** en Argentina, guarda los datos en una CSV y genera un gráfico de su evolución. Ideal para seguir la cotización diariamente y practicar Python y análisis de datos.

---

##Características:
-Consulta en tiempo real de **compra y venta** desde la API de [dolarapi.com](https://dolarapi.com/).
-Guarda cada registro con **fecha y hora** en 'dolar_blue.csv'
-Genera un **gráfico de evolución** con 'Matplotlib'.
-Fácil de ejecutar en **Windows, Linus o Google Colab**.

---

#Requisitos:
-Python 3.x
Librerías: 'requests', 'pandas', 'matplotlib'

Instalación rápida: 
```bash
pip install requests pandas matplotlib
```

#Uso: 
##1: Clonar el repositorio:
```bash
git clone https://github.com/TU_USUARIO/dolar-blue-tracker.git
cd dolar-blue-tracker
```

##2: Ejecutar el Script:
```
python dolar.py
```
##3: Cada vez que se ejecuta:
    -Se guardará un nuevo registro en 'dolar_blue.csv'
    -Se mostrará un gráfico de Compra vs Venta.

```
Autor: Alejandro Lopez
Fecha: 2025
```
