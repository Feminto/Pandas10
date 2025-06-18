# Method 1
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    adict = {}
    for i in range(len(activities)):
        s = activities['sell_date'][i]
        p = activities['product'][i]

        if s not in adict:
            adict[s] = set()
        adict[s].add(p)

    result = []
    for k,v in adict.items():
        result.append([k, len(v), ','.join(sorted(v))])
    
    return pd.DataFrame(result, columns = ['sell_date','num_sold','products']).sort_values('sell_date')


# Method 2
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # df = activities.groupby('sell_date').nunique().reset_index()
    df = activities.groupby('sell_date').agg(
            num_sold = ('product','nunique'),
            products = ('product', lambda x : ','.join(sorted(x.drop_duplicates()))) # or you can also take set(x) which gives distinct values
            ).reset_index()
    
    return df