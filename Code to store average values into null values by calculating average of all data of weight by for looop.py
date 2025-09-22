import pandas as pd
df = pd.read_csv(r"C:\Users\Abdullah\Downloads\nba.csv")
c = avg = 0
for ele in df['Weight']:
    if str(ele).isnumeric():
        c += 1
        avg += ele
if c > 0:
    avg /= c
else:
    avg = float('nan')
df = df.replace(to_replace='nan', value=avg)
print(df)

