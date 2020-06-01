mylist = [10, 40, 30, 20]

import pandas as pd
s = pd.Series(mylist)
print(pd.Series(mylist))

print(s.value_counts())