
import pandas as pd
import numpy as np
info = pd.DataFrame([[4, 9,2,25]] * 4, columns=['P', 'Q','R','S'])
print(info)
sq=info.apply(np.sqrt)

print(sq)

sm=info.apply(sum)
print(sm)

prod=info.apply(np.product,axis=1)
print(prod)
xx=info.apply(lambda x: [1, 2], axis='columns')
print(xx)

xx=info.apply(lambda x: [1, 2], axis='index')
print(xx)

xx=info.apply(lambda x: [1, 2], axis=1, result_type='expand')
print(xx)



