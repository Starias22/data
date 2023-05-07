import pandas as pd
info = pd.DataFrame({'X': range(1, 6),
                    'Y': range(10, 0, -2),
                    'Z': range(10, 5, -1)})
print(info)
print(info.query('X > Y'))
print(info.query('X ==5 or Y>8'))

print(info>0)