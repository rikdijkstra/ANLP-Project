import pandas as pd

def double_tweet(tweet):
    for index, row in trumpdf2.iterrows():
        if tweet == row['content']:
            return True
    return False


trumpdf = pd.read_csv('realdonaldtrump.csv')
trumpdf2 = pd.read_csv('trumptweets.csv')
counter = 0

for index, row in trumpdf.iterrows():
    if double_tweet(row['content']):
        counter = counter+1
        trumpdf.drop(index, inplace=True)

final_list = [trumpdf, trumpdf2]
final = pd.concat(final_list)
print(counter, " amount of double tweets")
final.to_csv (r'Trump.csv', index = False)
