import ast
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
df = pd.read_csv("./Data/Transp.csv")
Product_ID = df["Product_ID"]
Product_ID = Product_ID.apply(ast.literal_eval)

te = TransactionEncoder()
te_ary = te.fit(Product_ID).transform(Product_ID)
df = pd.DataFrame(te_ary, columns=te.columns_)

frq_items = apriori(df, min_support = 0.006)
association = association_rules(frq_items, metric ="confidence", min_threshold = 0.085)

association["antecedents"] = association["antecedents"].apply(lambda x: list(x)[0]).astype("unicode")
association["consequents"] = association["consequents"].apply(lambda x: list(x)[0]).astype("unicode")

association.to_csv('./Data/Apriori.csv', index = False)
