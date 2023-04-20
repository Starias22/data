import cv2 as cv
import os
import numpy as np
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt

def split(img):
    b=img[:,:,0]
    g=img[:,:,1]
    r=img[:,:,2]
    size=img.size
    print('xxx',img.shape[0]*img.shape[1]*img.shape[2])
    print('size:',size)
    b=np.sum(b)
    g=np.sum(g)
    r=np.sum(r)
    #b,g,r=cv.split(img)
    return b,g,r
def cpt_bgr(inputPath):
    #try to read the image
    img=reading.read(inputPath)
    #if failure
    if img is None:
        return
    #else
    #img=cv.imread(inputPath)
    return split(img)
if __name__=='__main__':
    b,g,r=cpt_bgr('../src/images/apple.jpeg')
    print('blue:',b)
    print('green:',g)
    print('read:',r)