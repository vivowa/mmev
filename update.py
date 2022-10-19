import requests
import pandas as pd
from datetime import datetime

now = datetime.utcnow()

url = f'https://blocks.flashbots.net/v1/blocks?limit=350'

response = requests.get(url)

raw = response.json()
raw = raw['blocks']

df_raw = pd.DataFrame.from_dict(raw)
df_raw.sort_values(by='block_number', ascending=True, inplace=True)
df_raw.reset_index(drop=True, inplace=True)


def create_transactions(raw):
    txn = []
    for i in range(0, len(raw)):
        txn.append(raw[i]['transactions'])

    txn = [item for sublist in txn for item in sublist]
    return txn

txn = create_transactions(raw)

df_txn = pd.DataFrame.from_dict(txn)

df_txn.to_csv('/Users/viking/Documents/github/mmev/txn.csv', mode='a', index=False, header=False)

df_raw.drop(columns=['transactions'], inplace=True)
df_raw.to_csv('/Users/viking/Documents/github/mmev/blocks.csv', mode='a', index=False, header=False)

current_time = now.strftime("%H:%M:%S")
print(current_time)
print(df_raw['block_number'].iloc[0] , 'to ', df_raw['block_number'].iloc[-1], 'updated ')


