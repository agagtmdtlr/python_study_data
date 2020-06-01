import numpy as np
import pandas as pd



myframe = pd.DataFrame([[np.nan,0,0],[0,np.nan,0],[0,0,0]])

print(myframe.dropna(axis=0))
print(myframe.dropna(axis=1,how=))