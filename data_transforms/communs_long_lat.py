import pandas as pd

df = pd.read_csv("/home/lt/Cost_estimator/docs/communes-departement-region.csv")
auction_data = pd.read_csv("/home/lt/Cost_estimator/project/filtered_data.csv")

filter_on_region = df [df['nom_region']=='Île-de-France']

#filter_on_region.to_csv("/home/lt/Cost_estimator/docs/communes-departement-iles-de-france.csv")


auction_commun = auction_data['commune']

def get_lat_long(x):
    res=filter_on_region[filter_on_region["nom_commune_complet"]==x]
    res = res["latitude"]
    print("for ", x , "found " , str(res))

auction_commun.apply(get_lat_long)