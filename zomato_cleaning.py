#ZOMATO ANALYSIS PROJECT

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

#importing data
dataframe= pd.read_csv("zomato.csv")
dataframe

#standardize column name
dataframe.columns = dataframe.columns.str.strip().str.lower().str.replace(' ', '_')

#filling missing 'cuisines' with placeholder
dataframe['cuisines'] = dataframe['cuisines'].fillna('Not Specified')

# Drop irrelevant or redundant columns
columns_to_drop = ['switch_to_order_menu', 'locality_verbose']
dataframe.drop(columns=columns_to_drop, inplace=True)

# Drop exact duplicate rows 
dataframe.drop_duplicates(inplace=True)

# Remove whitespace from string columns
str_cols = dataframe.select_dtypes(include='object').columns
dataframe[str_cols] = dataframe[str_cols].apply(lambda x: x.str.strip())

# Convert appropriate columns to category dtype
cat_cols = ['has_table_booking', 'has_online_delivery', 'is_delivering_now',
            'rating_color', 'rating_text', 'currency', 'city', 'locality']
for col in cat_cols:
    if col in dataframe.columns:
        dataframe[col] = dataframe[col].astype('category')
        
# Fix 'average_cost_for_two' and 'votes' if they contain outliers or negatives
df = dataframe[dataframe['average_cost_for_two'] >= 0]
df = df[df['votes'] >= 0]

# Fix 'average_cost_for_two' and 'votes' if they contain outliers or negatives
df = df[df['average_cost_for_two'] >= 0]
df = df[df['votes'] >= 0]

#standardize currency values if using global data
df['currency'] = df['currency'].replace({
    'Botswana Pula(P)': 'Pula',
    'Brazilian Real(R$)': 'Real',
    'Dollar($)': 'USD',
    'Emirati Diram(AED)': 'AED',
    'Indian Rupees(Rs.)': 'INR',
    'Indonesian Rupiah(IDR)': 'IDR',
    'NewZealand($)': 'NZD',
    'Pounds(£)': 'GBP',
    'Qatari Rial(QR)': 'QAR',
    'Rand(R)': 'ZAR',
    'Sri Lankan Rupee(LKR)': 'LKR',
    'Turkish Lira(TL)': 'TRY'
})

#Normalize text (e.g., lowercase restaurant names)
df['restaurant_name'] = df['restaurant_name'].str.title()

#Remove restaurants with invalid lat/long (e.g., 0 or out-of-bound)
df = df[(df['latitude'] != 0) & (df['longitude'] != 0)]

#Reset index after cleaning
df.reset_index(drop=True, inplace=True)

df= df.drop_duplicates()

columns_to_keep = ['restaurant_name', 'city', 'cuisines', 'average_cost_for_two', 'aggregate_rating', 'votes']
df = df[columns_to_keep]

#Display cleaned data info
print(df.info())
print(df.sample(5))

print(df.to_string)

df.to_csv("zomato_cleaned.csv", index=False)






