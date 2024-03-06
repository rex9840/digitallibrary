import pandas as pd
import numpy as np
import sklearn as sk
import csv 

from ..models import UserResourceInteraction,Users,Resources


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
                'user_id': user_resource.user_id,
                'resource_id': user_resource.resource_id,
                'rating': user_resource.rating,
                }
        output.append(data)
    return output 


def data_preprocessing(): 
    data = pd.DataFrame(get_resources())
    data = data.drop(columns = ["name"])
    
    slice = data.copy()

    def func(x):
        if x['tags'] is np.nan:
            return x
        else: 
            tags = x['tags']
            for g in tags:
                x[g] = 1
        return x

    slice = slice.apply(func, axis=1)

    slice = slice.drop(columns = ["tags"])
    
    user_resources = pd.DataFrame(get_user_resources())
    
    user_resources.to_csv('user_resources.csv')

    return slice["tags"]
