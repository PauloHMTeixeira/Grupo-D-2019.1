import pandas as pd
import json

with open("data_file.json", "r+") as f:
    data = json.load(f)
    df = pd.DataFrame(data)
    print(df)