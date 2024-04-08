import pandas as pd
import numpy as np
import sklearn as sk
import csv 
from .algorithm import KMEANS 
from ..models import UserResourceInteraction,Resources


def get_resources(): 
    output = []
    resources = Resources.objects.all()
    for resource in resources:
        data = {
                'resource_id': resource.resource_id,
                'name': resource.name,
                'tags': resource.tags.all(),
                }
        output.append(data)
    return output

def get_user_resources(): 
    output = []
    user_resources = UserResourceInteraction.objects.all()
    for user_resource in user_resources:
        data = {
                'user_id': user_resource.user_id.id,
                'resource_id': user_resource.resource_id.resource_id,
                'rating': user_resource.rating,
                }
        output.append(data)
    return output



def tag_expansion(x): 
    tags = x["tags"]
    if tags: 
        for tag in tags:
            x[tag.tag_name] = 1
    return x







def data_preprocessing(): 
    data = pd.DataFrame(get_resources())
    data = data.drop(columns = ["name"])
        
    slice = data.copy()

    slice = slice.apply(tag_expansion, axis=1)

    slice = slice.drop(columns = ["tags"])

    user_resources = pd.DataFrame(get_user_resources())
    user_resources = user_resources.join(slice.set_index('resource_id'), on='resource_id')
    
    user_resources.to_csv("user_resources.csv")
    
    user_resources = user_resources.drop(columns = ["resource_id"])

    columns = user_resources.columns.tolist()

    columns.remove("rating")
    columns.remove('user_id')

    for column in columns:
        user_resources[column] = user_resources[column].mul(user_resources["rating"],axis=0)
    user_resources = user_resources.groupby(by="user_id").mean()
    user_resources = user_resources.fillna(value=0)
    user_resources.head() 
    

    kmeans = KMEANS(n_clusters=4,random_state=10,max_iter=300)
    users_with_label = pd.DataFrame(user_resources)
    users_with_label["label"]= kmeans.fit(users_with_label.values)

    users_with_label = pd.DataFrame(get_user_resources()).join(users_with_label['label'], on='user_id')
    
    return users_with_label
