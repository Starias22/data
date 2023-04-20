import pandas as pd
import numpy as np
lang = pd.Series(['Java', 'C', 'C++', 'Python'])
desc=lang.map({'Java': 'Android development','Python':'Data science language','C++':'So fast'})
print(lang)
print(desc)

lang[4]='Perl'
lang[5]=np.nan
print(lang)
likeLang=lang.map('I like {} programming language'.format)
print(likeLang)

likeLang=lang.map('I like {} programming language'.format,na_action='ignore')
print(likeLang)
