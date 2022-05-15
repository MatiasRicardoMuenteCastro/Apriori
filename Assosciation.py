import pandas as pd

def mergeProducts():
    products = pd.read_csv("./Datasets/products.csv")
    aisles = pd.read_csv("./Datasets/aisles.csv")
    for aisle_id in products["aisle_id"]:
        count = 0
        for product_aisle_id in aisles["aisle_id"]:
            if aisle_id == product_aisle_id:
                products['aisle_id'] = products['aisle_id'].replace(aisle_id,aisles["aisle"][count])
            count = count+1
    products.rename(columns = {'aisle_id':'aisle'}, inplace = True)
    return products
            

def associateNameID(products, association):
    antecedent_aisles = []
    for antecedent_ID in association["antecedents"]:
        for ProductID in products["product_id"]:
            if antecedent_ID == ProductID:
                association['antecedents'] = association['antecedents'].replace(antecedent_ID,products["product_name"].loc[antecedent_ID-1])
                antecedent_aisles.append(products["aisle"].loc[antecedent_ID-1])
    
    association["aisle_antecedent"] = antecedent_aisles

    consequent_aisles = []
    for consequent_ID in association["consequents"]:
        for ProductID in products["product_id"]:
            if consequent_ID == ProductID:
                association['consequents'] = association['consequents'].replace(consequent_ID,products["product_name"].loc[consequent_ID-1])
                consequent_aisles.append(products["aisle"].loc[consequent_ID-1])
    
    association["aisle_consequent"] = consequent_aisles
    return association

association = pd.read_csv("./Data/Apriori.csv")
products = mergeProducts()
df = associateNameID(products = products, association = association)
finalDF = pd.DataFrame({"antecedents":df["antecedents"],"consequents":df["consequents"],"aisle_antecedents":df["aisle_antecedent"],"aisle_consequents":df["aisle_consequent"],"support":df["support"],"confidence":df["confidence"]})
finalDF["confidence"] = finalDF["confidence"].apply(lambda x: f"{x*100:0.2f}%")
finalDF.to_csv("./Data/FinalAssociation.csv",sep = ";",index = False)