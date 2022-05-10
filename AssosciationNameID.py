import pandas as pd

def associateNameID(products, association):
    
    for antecedent_ID in association["antecedents"]:
        for ProductID in products["product_id"]:
            if antecedent_ID == ProductID:
                association['antecedents'] = association['antecedents'].replace(antecedent_ID,products["product_name"].loc[antecedent_ID-1])

    for consequent_ID in association["consequents"]:
        for ProductID in products["product_id"]:
            if consequent_ID == ProductID:
                association['consequents'] = association['consequents'].replace(consequent_ID,products["product_name"].loc[consequent_ID-1])
    
    return association

products = pd.read_csv("./Datasets/products.csv")
association = pd.read_csv("./Apriori.csv")

df = associateNameID(products,association)
print(df)
df.to_csv("FinalAssociation.csv",index = False)