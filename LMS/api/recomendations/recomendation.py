import pandas as pd
from pandas.io.xml import preprocess_data
from api.recomendations.data_preprocessing import data_preprocessing,get_user_resources,get_resources




def recomendation_cluster_tabel():
   
    labeled_data = data_preprocessing() 

    group = labeled_data[['resource_id','label','rating']].groupby(['label','resource_id'])['rating'].agg(['mean','count'])
    
    group["obj"] = group["mean"]*group["count"]
    group = group[["obj"]].dropna()

    resources = pd.DataFrame(get_resources())


    labels = group.index.get_level_values(0).unique().tolist()
    recomendation = []

    for label in labels:

        sort =  group.loc[label].sort_values(by="obj",ascending=False).reset_index()
        sort = sort.join(resources[['resource_id','name']].set_index('resource_id'), on='resource_id')
        recomendation.append(sort["resource_id"].rename(label))

    recomendation_cluster_tabel = pd.concat(recomendation,axis=1)

    return recomendation_cluster_tabel


def get_recommendations(user_id):

    labeled_data = data_preprocessing() 

    group = labeled_data[['resource_id','label','rating']].groupby(['label','resource_id'])['rating'].agg(['mean','count'])
    
    group["obj"] = group["mean"]*group["count"]
    group = group[["obj"]].dropna()

    resources = pd.DataFrame(get_resources())

    user_data = labeled_data[labeled_data["user_id"] == user_id]
    user_data  = user_data["label"].iloc[0]

    user_obj = group.loc[user_data].sort_values(by="obj",ascending=False)
    recomendations = user_obj.join(resources.set_index('resource_id'), on='resource_id').reset_index()

    return recomendations

