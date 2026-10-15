import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("/Users/ansharora/Desktop/project/requirements/customer_shopping_behavior.csv")
# print(data.head())

# print(data.describe())
# print(data.shape)

data["Review Rating"]=data.groupby("Category")["Review Rating"].transform(lambda x:x.fillna(x.median()))
# print(data.isnull().sum())


# print(data.duplicated())

data.columns=data.columns.str.lower()
data.columns=data.columns.str.replace(" ","_")

data=data.rename(columns={"purchase_amount_(usd)":"purchase_amount"})



label=["Young","Adult","Middle","Senior"]
data["age_grouped"]=pd.qcut(data["age"],q=4 ,labels=label)
# print(data[["age","age_grouped"]].head())

frequency_maping={
"Fortnightly":14,
"Weekly":7,
"Bi-Weekly":14,
"Monthly":30,
"Quarterly":90,
"Annually":365
}
data["frequency_days"]=data["frequency_of_purchases"].map(frequency_maping)
# print(data[['frequency_of_purchases',"frequency_days"]].head(10))

print((data['discount_applied']==data['promo_code_used']).all())
data=data.drop("promo_code_used",axis=1)
print(data.columns)


data.to_csv(
    "/Users/ansharora/Desktop/project/requirements/cleaned_data.csv",
    index=False
)