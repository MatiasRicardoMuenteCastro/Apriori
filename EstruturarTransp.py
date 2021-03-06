import numpy as np
import pandas as pd

texto = open('./Data/transp.txt','r')
textoLido = texto.read()

linhas = textoLido.split("\n")
vetorOrder_ID = []
vetorProduct_ID = []
for i in linhas:
    Order_ID = i.split(",")[0]
    vetorOrder_ID.append(Order_ID)
    Product_ID = i.split(",")[1:len(linhas)]
    vetorProduct_ID.append(Product_ID)

dicionario = {"Order_ID":vetorOrder_ID,"Product_ID":vetorProduct_ID}
df = pd.DataFrame(dicionario)

df["Order_ID"] = df["Order_ID"].replace('"order_id"',np.nan)
df = df.replace("",np.nan)
df = df.dropna().reset_index(drop = True)

intVetorOrder_ID = []
intVetorProduct_ID = []

for i in df["Order_ID"]:
    intVetorOrder_ID.append(int(i))

for i in df["Product_ID"]:
    tempArray = []
    for j in i:
        tempArray.append(int(j))
    
    intVetorProduct_ID.append(tempArray)

dfTratado = pd.DataFrame({"Order_ID": intVetorOrder_ID, "Product_ID": intVetorProduct_ID})

dfTratado.to_csv("./Data/Transp.csv", index = False)




