# Importar a biblioteca que irá ler a planilha, pandas é o nome e 'pd'
# é a variável que utilizará as funções
import pandas as pd

# essa função lê a planilha para dentro da variável data como um DataFrame
# (diferente da lista e string), então para modificar e fazer as alterações deve-se
# usar as funções do pandas
data = pd.read_csv("Popular_Movies.csv", delimiter=";")


# printar a tabela, só que ela é muito grande e precisa ser ajustada
print(data)
