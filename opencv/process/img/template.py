import numpy as np
import cv2 as cv
import os
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt

blue=[255,0,0]

def selectMatch(imgsrc,imgTemplate,method=cv.TM_CCOEFF_NORMED,threshold=0.8,color=blue,thickness=2):
    try:
        #imgsrc=cv.cvtColor(cv.COLOR_BGR2GRAY)
        height,width=imgTemplate.shape[:2]
        tempRes=cv.matchTemplate(imgsrc,imgTemplate,method)
        loc=np.where(tempRes>=threshold)
        for (x,y) in zip(*loc[::-1]):
            cv.rectangle(imgsrc,(x,y),(x+width,y+height),color,thickness)
        return imgsrc
    except cv.error as e:
        print(e)
    except Exception as e:
        print(e)


def template(imgsrcPath,imgTemplatePath,outputPath,
            method=cv.TM_CCOEFF_NORMED,threshold=0.8,color=blue,thickness=2):
    try:
        wrtable=wrt.iswritable(outputPath)
        if  wrtable is None:
            return
        #try to read the img source
        imgsrc=reading.read(imgsrcPath)
        imgTemplate=reading.read(imgTemplatePath)
        #if failure
        if imgsrc is None or imgTemplate is None:
            #nothing else to do
            return
        #else
        print(imgTemplate)
        img=selectMatch(imgsrc,imgTemplate,method,threshold,color,thickness)
        #print("fine")
        if img is None :
            return
        if wt.imwrite(img, outputPath) is not None:
            print('Success')
    except cv.error as e:
        print(e)
    except Exception as e:
        print(e)

if __name__=='__main__':

    outputPath='fic.jpeg'
    src='../src/images/apple.jpeg'
    temp='../src/images/apple.jpeg'
    '../src/images/cat.jpeg'
    template(src,temp , outputPath)