# Method 1
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    ds_dict = {}
    for i in range(len(daily_sales)):
        d = daily_sales['date_id'][i]
        m = daily_sales['make_name'][i]
        l = daily_sales['lead_id'][i]
        p = daily_sales['partner_id'][i]

        if (d,m) not in ds_dict:
            ds_dict[(d,m)] = [set(),set()]
        ds_dict[(d,m)][0].add(l)
        ds_dict[(d,m)][1].add(p)

    result = []
    for k,v in ds_dict.items():
        result.append([k[0], k[1], len(v[0]), len(v[1])])
    
    return pd.DataFrame(result, columns = ['date_id','make_name','unique_leads','unique_partners'])


# Method 2
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df = daily_sales.groupby(['date_id','make_name']).agg(
        unique_leads = ('lead_id','nunique'),
        unique_partners = ('partner_id','nunique')
    ).reset_index()

    return df


# Method 3
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df = daily_sales.groupby(['date_id','make_name']).nunique().reset_index()

    return df.rename(columns = {'lead_id':'unique_leads','partner_id':'unique_partners'})