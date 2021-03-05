import pandas as pd
from matplotlib import pyplot as plt

def mean_price(df,column):
    df["{}".format(column)] = df["{}".format(column)].str.split("-")
    df["{}".format(column)] = df["{}".format(column)].apply(lambda x:  [x[0][:-3]] if len(x) ==1 else [x[0][:-4], x[1][:-3]])
    df["{}".format(column)] = df["{}".format(column)].apply(lambda x: (float(x[0])+float(x[1]))/2 if len(x) != 1 else float(x[0]))

def clean_sells(df,column):
    df["{}".format(column)] = df["{}".format(column)].fillna(0)
    df["{}".format(column)] = df["{}".format(column)].apply(lambda x: str(x)[1:-1] if x !=0 else x)

def To_int(df,column):
    df["{}".format(column)] = df["{}".format(column)].astype(int)

def To_float(df,column):
    df["{}".format(column)] = df["{}".format(column)].astype(float)

def clean_stars(df,column):
    df["{}".format(column)] = df["{}".format(column)].fillna(0)
    df["{}".format(column)] = df["{}".format(column)].apply(lambda x: str(x)[:3] if x !=0 else x)
    df["{}".format(column)] = df["{}".format(column)].apply(lambda x: x[0] if " " in str(x) else x)

def mean_price_1(df,column):
    df["{}".format(column)] = df["{}".format(column)].str.split("-")
    df["{}".format(column)] = df["{}".format(column)].apply(lambda x:  [x[0][:-3]] if len(x) ==1 else [x[0][:-4], x[1][:-4]])
    df["{}".format(column)] = df["{}".format(column)].apply(
        lambda x: x[0][0]+x[0][2:] if len(x)==1 and "," in str(x) else x)
    df["{}".format(column)] = df["{}".format(column)].apply(lambda x: (float(x[0])+float(x[1]))/2 if len(x) != 1 else float(x[0]))



if __name__ == '__main__':

################################## Cleaning Femme.csv

    data = pd.read_csv('Files/Femme.csv')
    df = data.drop(['product_information'],axis=1)
    df = df.dropna(axis='index', how='all')
    mean_price(df,"price")
    clean_sells(df,"sells")
    To_int(df,"sells")
    clean_stars(df,"stars")
    To_float(df,"stars")
    print(df.head())

################################## Cleaning Jumia_sport.csv

    data1 = pd.read_csv('Files/Jumia_sport.csv')
    df1 = data1.drop(['product_information'], axis=1)
    df1 = df1.dropna(axis='index', how='all')
    mean_price_1(df1,"price")

    clean_sells(df1,"sells")
    To_int(df1,"sells")
    clean_stars(df1,"stars")
    To_float(df1,"stars")
    print(df1.head())

################################## Visualasing

    plt.style.use("fivethirtyeight")
    df_price_sells = df1.drop("product",axis=1).drop("stars",axis=1)
    plt.bar(df_price_sells.price,df_price_sells.sells,color="k",label="test",width=2)
    print(df_price_sells.head())
    plt.legend()
    plt.title("Sells by price")
    plt.xlabel("price")
    plt.ylabel("sells")
    plt.show()

###########################################



