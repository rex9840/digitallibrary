import pandas as pd
import numpy as np
import sklearn as sk


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



def data_preprocessing(): 
    data = pd.DataFrame(get_resources())
    return data
