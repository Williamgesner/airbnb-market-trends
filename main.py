import pandas as pd
import numpy as np

df_tsv = pd.read_csv("airbnb_last_review.tsv", sep="\t")  # Importando arquivo TSV
df_csv = pd.read_csv("airbnb_price.csv")  # Importando arquivo CSV
df_xls = pd.read_excel("airbnb_room_type.xlsx")  # Importando arquivo XLSX

# Mesclando os DataFrames
merged_df = pd.merge(df_tsv, df_csv, on="listing_id")
merged_df = pd.merge(merged_df, df_xls, on="listing_id")

# Convertendo last_review em DateTime
merged_df["last_review"] = pd.to_datetime(merged_df["last_review"])

# Datas das avaliações (Mais antigas/ mais recentes - separando por variáveis)
oldest_review = merged_df["last_review"].min()
newest_review = merged_df["last_review"].max()
print(f"A avaliação mais antiga foi dia: {oldest_review.strftime("%d-%b-%Y")}")
print(f"A avaliação mais recente foi dia: {newest_review.strftime("%d-%b-%Y")}")

# Padronizando os dados de room_type e descobrindo quantos são quartos privativos
merged_df["room_type"] = merged_df["room_type"].str.lower()
count_room = (merged_df["room_type"] == "private room").sum()
print(f"Existem {count_room} quartos privativos")

# Padronizando os dados de price
merged_df["price"] = merged_df["price"].str.replace("dollars", "")
merged_df["price"] = merged_df["price"].astype(float)
avg_price = merged_df["price"].mean().round(2)  # Buscando a média dos preços
print(f"O preço médio de venda é de {avg_price} dollars")

merged_df.to_csv("merged_df.csv", index=False)

# Criando um novo DF
review_dates = pd.DataFrame(
    {
        "first_reviewed": [oldest_review.strftime("%d-%b-%Y")], # strftime é apenas para formatar a data
        "last_reviewed": [newest_review.strftime("%d-%b-%Y")],
        "nb_private_rooms": [count_room],
        "avg_price": [avg_price],
    }
)

print(review_dates)

review_dates.to_csv("review_dates.csv", index=False)