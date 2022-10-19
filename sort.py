import pandas as pd
from datetime import datetime

now = datetime.utcnow()

temp = pd.read_csv('/Users/viking/Documents/github/mmev/txn.csv')
temp.drop_duplicates(keep='first', inplace=True)
temp.sort_values(by='block_number', ascending=True, inplace=True)
temp.reset_index(drop=True, inplace=True)

temp.to_csv('/Users/viking/Documents/github/mmev/txn.csv', index=False)

temp = pd.read_csv('/Users/viking/Documents/github/mmev/blocks.csv')
temp.drop_duplicates(keep='first', inplace=True)
temp.sort_values(by='block_number', ascending=True, inplace=True)
temp.reset_index(drop=True, inplace=True)

temp.to_csv('/Users/viking/Documents/github/mmev/blocks.csv', index=False)


current_time = now.strftime("%H:%M:%S")
print(current_time)
