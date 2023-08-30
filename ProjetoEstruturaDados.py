# Importar a biblioteca que irá ler a planilha, pandas é o nome e 'pd'
# é a variável que utilizará as funções
import pandas as pd
import Functions as func

class Filmes:
   #Construtor da classe com as variáveis
   def __init__(self,budget,genres,id,overview,orinal_Language,popularity,production_companies,release_Date,revenue,runtime,tagline,title,vote_average,vote_count):
       self.budget = budget
       self.genres = genres
       self.id = id
       self.overview = overview
       self.original_Language = orinal_Language
       self.popularity = popularity
       self.production_companies = production_companies
       self.release_Date = release_Date
       self.revenue = revenue
       self.runtime = runtime
       self.tagline = tagline
       self.title = title
       self.vote_average = vote_average
       self.vote_count = vote_count#Criando objeto da classe filme     
meu_Filme = Filmes(0,"",0,"","",0,"","",0.0,0,"","",0,0)



# essa função lê a planilha para dentro da variável data como um DataFrame
# (diferente da lista e string), então para modificar e fazer as alterações deve-se
# usar as funções do pandas
# O delimiter=';' serve para dizer o que separa uma celula de outra, pq por padrão é ','
data = pd.read_csv("Popular_Movies.csv", delimiter=";")


# printar a tabela, só que ela é muito grande e precisa ser ajustada
print(data)

