import os
import pandas as pd
import requests
from tqdm import tqdm

if not os.path.isdir('data/images'):
    os.makedirs('data/images')

df = pd.read_csv('data/metadata_public.csv', encoding='latin-1')
df = df[['File Name', 'Image Credits']]

for fname,url in tqdm(list(df.values)):
    pth = f'data/images/{fname}'
    r = requests.get(url)
    if r.status_code != 200: 
        print(f'failed to download {url}')
        continue
    open(pth, 'wb').write(r.content)

