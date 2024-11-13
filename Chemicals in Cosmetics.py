import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno

df = pd.read_csv('dataset.csv', encoding=('ISO-8859-1'))

# print(df.head(),"\n")
# print(df.describe().transpose(),"\n")
# print(df.info(),"\n")
# print(df.shape,"\n")
# print(df.isnull().sum(),"\n")
# print(df.select_dtypes(include=['int64']).columns,"\n")
# print(df.select_dtypes(include=['object']).columns,"\n")
# print(df.drop_duplicates(),"\n")

# print(df['ChemicalName'].value_counts(),"\n")

# 將Chemicalcount小於5和大於5的的產品分類，按照化學，按照化學成分排序
# below_5 = df[df['ChemicalCount'] < 5]
# above_5 = df[df['ChemicalCount'] >= 5]
# sorted_above_5 = above_5.sort_values(by='ChemicalCount', ascending=False)
# plt.barh(sorted_above_5['ProductName'], sorted_above_5['ChemicalCount'])
# plt.xlabel("Number of Chemicals used")
# plt.title("Cosmetics with more than 5 chemicals")
# plt.show()

# 根據 CompanyName 計算產品數量，篩選ProductCount大於4000的併用長條圖顯示
# df['ProductCount'] = df.groupby('CompanyName')['CompanyName'].transform('count')  # 計算每家公司產品的數量，並將結果存入新欄位 'ProductCount'
# no_of_products = df[df['ProductCount'] > 4000]  # 篩選出產品數量超過4000的公司
# no_of_products.groupby('CompanyName').size().plot(kind='barh')  # 將這些公司的數量以橫向長條圖的形式繪製出來
# plt.title("Companies with more than 4000 products")  # 設定圖表標題為「產品數量超過4000的公司」
# plt.show()

def insert_line_breaks(name, max_length=15):
    return '\n'.join([name[i:i+max_length] for i in range(0, len(name), max_length)])

# 根據 BrandName 計算產品數量，篩選ProductCount大於3000的併用長條圖顯示
# df['ProductCount'] = df.groupby('BrandName')['BrandName'].transform('count')
# no_of_products_brand = df[df['ProductCount'] > 3000]
# no_of_products_brand.groupby('CompanyName').size().plot(kind='barh')
# plt.title("Brand with more than 3000 products")
# plt.show()

# # 根據 ChemicalName 計算產品數量，篩選ProductCount大於1000的併用長條圖顯示
# df['ProductCount'] = df.groupby('ChemicalName')['ChemicalName'].transform('count')
# no_of_products_chemical = df[df['ProductCount'] > 1000]
# no_of_products_chemical.groupby('ChemicalName').size().plot(kind='barh')
# plt.title("Chemical with more than 1000 products")
# plt.show()

# 根據 ChemicalName 計算產品數量，篩選ProductCount大於1000的併用長條圖顯示，做成函式
def plot_product_count(df, column, count):
    df['ProductCount'] = df.groupby(column)[column].transform('count')
    no_of_products = df[df['ProductCount'] > count]
    no_of_products.groupby(column).size().plot(kind='barh')
    plt.title(f"{column} with more than {count} products")
    plt.show()

# 根據 ChemicalName 計算產品數量，篩選ProductCount大於1000的併用長條圖顯示
plot_product_count(df, 'ChemicalName', 1000)
# 根據 BrandName 計算產品數量，篩選ProductCount大於3000的併用長條圖顯示
plot_product_count(df, 'BrandName', 3000)
# 根據 CompanyName 計算產品數量，篩選ProductCount大於4000的併用長條圖顯示
plot_product_count(df, 'CompanyName', 4000)

# 修改plot_product_count函式，if條件布林可以選擇大於或小於
# def plot_product_count(df, column, count, greater_than=True):
#     df['ProductCount'] = df.groupby(column)[column].transform('count')
#     if greater_than:
#         no_of_products = df[df['ProductCount'] > count]
#     else:
#         no_of_products = df[df['ProductCount'] < count]
#     no_of_products.groupby(column).size().plot(kind='barh')
#     plt.title(f"{column} with {'more' if greater_than else 'less'} than {count} products")
#     plt.show()

# 根據 ChemicalName 計算產品數量，篩選ProductCount大於1000的併用長條圖顯示
