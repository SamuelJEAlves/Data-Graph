import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("VendasAleatorio.xlsx")

df.plot(kind="line", x="MESES", y="VENDAS")

plt.xlabel("Meses")
plt.ylabel("Quantidade de Vendas")

plt.title("Gráfico de Vendas 23/24/25")

plt.grid(True)
plt.show()


