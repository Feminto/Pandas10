# Method 1
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    act_dict = {}
    for i in range(len(actor_director)):
        a = actor_director['actor_id'][i]
        d = actor_director['director_id'][i]

        if (a,d) in act_dict:
            act_dict[(a,d)] += 1
        else:
            act_dict[(a,d)] = 1
    
    result = []
    for k,v in act_dict.items():
        if v >= 3:
            result.append([k[0],k[1]])
    
    return pd.DataFrame(result, columns = ['actor_id','director_id'])


# Method 2
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id','director_id']).size().reset_index(name = 'cnt')
    
    return df[df['cnt'] >= 3][['actor_id','director_id']]