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

marks={'english':15,'math':18,'chemistry':12,'french':17}
ms=pd.Series(marks)
def add2(x):
    if x<=18:
        x+=1
    return x



print('marks:',ms,sep='\n')
print('marks+2:',ms.map(add2),sep='\n')
