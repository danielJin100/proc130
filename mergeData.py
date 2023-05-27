import pandas as pd
import numpy as np

stars = pd.read_csv("scraped_data.csv")
dwarfs = pd.read_csv("dwarf_data.csv")

stars.dropna(axis=0, inplace=True)
dwarfs.dropna(axis=0, inplace=True)

dwarfs.astype({"Mass": "float", "Radius": "float"})

dwarfs["Mass"] *= 0.102763
dwarfs["Radius"] *= 0.000954588

headers = ['id','name','dist', 'mass','rad','lum']
mergeFile = pd.DataFrame(columns=headers)
dwarfs.drop(columns=['Constellation','Right Ascension','Declination','Spectral Type','Date Discovered'], inplace=True)
dwarfs = dwarfs.rename({"Brown Dwarf": "name", "Distance": "dist", "Radius":"rad", 'Apparent Magnitude': "lum"}, axis="columns")
mergeFile = pd.concat([dwarfs, stars], axis=0)

mergeFile.drop(["lum"], inplace=True, axis="columns")
mergeFile.dropna(axis=1, inplace=True)
print(mergeFile.dtypes)

mergeFile.to_csv("merged_data.csv")