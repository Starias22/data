import statistics  as stat
import numpy as np
# lists of  numbers
dataset = [5, 2, 7, 4, 2, 7, 8,-2.58]
data=[5,5,3,1,11]


print('(dataset, data):',(dataset,data))

# Central tendance
##Mean

### arithmetic average or arithmetic mean
#### using sum and len
print('(mean of dataset, mean of data):',(sum(dataset)/len(dataset),sum(data)/len(data)))


####using mean
print('(mean of dataset, mean of data):',(stat.mean(dataset),stat.mean(data)))

####using fmean
print('(mean of dataset, mean of data):',(stat.mean(dataset),stat.mean(data)))

### Weighted mean

x=[5,10,22,7,5,7,22,5,1,5]

marks=[15,12,13,18,20]
coeffs=[3,4,5,5,2]

####implementation

def weightedMean(dset,weights=None):
    if weights==None:
        return stat.fmean(dset)
    sm=sum(weights)
    if sm !=1:
        weights=[x/sm for x in weights]
    wm=sum(weights[i]* dset[i] for i in range(len(dset)))
    return wm


wm=weightedMean(x)
print(wm)

####using numpy

print(np.average(x))
print(stat.mean(x))


wm=weightedMean(marks,coeffs)
print('Your weighted average:',wm)
m=np.average(marks,weights=coeffs)
print('Your weighted average:',m)

### Geometric mean
y=[4,5,61,22,3,12,15]
print('y:',y)
####implementation

def geometricMean(dset):
    import math
    for item in dset:
        if item<=0:
            return
    return math.prod(dset)**(1/len(dset))
print('Geometric mean of y:',geometricMean(y))

####using geometric_mean

print('Geometric mean of y:',stat.geometric_mean(y))


### Harmonic mean
y=[4,5,61,22,3,12,15]
print('y:',y)
####implementation

def harmonicMean(dset):

    if 0 in dset:
        return
    return sum(1/x for x in dset)*len(dset)

print('Harmonic mean of y:',harmonicMean(y))

####using harmonic_mean

print('Harmoric mean of y:',stat.harmonic_mean(y))

## Median

###median
####implementing

def median(dset):
    sdset=sorted(dset)
    n=len(dset)
    if n%2!=0:
        return sdset[n//2]
    else:
        return 0.5*(sdset[n//2-1]+sdset[n//2])

print('(median of dataset, median of data):',(median(dataset),median(data)))

####using median
print('(median of dataset, median of data):',(stat.median(dataset),stat.median(data)))

### high median

#### implementation

def highMedian(dset):
    sdset=sorted(dset)
    n=len(dset)
    if n%2!=0:
        return sdset[n//2]
    else:
        return max( [sdset[n//2-1], sdset[n//2] ])

print('(high median of dataset, high median of data):',(highMedian(dataset),highMedian(data)))

#### using high_median

print('(high median of dataset, high median of data):',(stat.median_high(dataset),stat.median_high(data)))

### low median

#### implementation

def lowMedian(dset):
    sdset=sorted(dset)
    n=len(dset)
    if n%2!=0:
        return sdset[n//2]
    else:
        return min( [sdset[n//2-1], sdset[n//2] ])

print('(low median of dataset, low median of data):',(lowMedian(dataset),lowMedian(data)))

#### using low_median

print('(low median of dataset, low median of data):',(stat.median_low(dataset),stat.median_low(data)))

## Mode

## mode
###implementation

def mode(dset):
    # Convert the input list to a set to get unique values, then convert it back to a list
    sample=set(dset)
    sample=list(sample)

    # Count the occurrences of each value in the input list and store the counts in a separate list
    x=[dset.count(x) for x in sample]

    # Find the maximum count (the count of the mode)
    max_count=max(x)

    # Find the index of the mode in the sample list (where the count is equal to the maximum count)
    mode_index=x.index(max_count)

    # Return the mode (the value at the mode index in the sample list)
    md=sample[mode_index]
    return md

print('(mode of dataset, mode of data):',(mode(dataset),mode(data)))

###using mode()
print('(mode of dataset, mode of data):',(stat.mode(dataset),stat.mode(data)))

## multimode

###implementation

###using multimode()

print('(mode of dataset, mode of data):',(stat.multimode(dataset),stat.multimode(data)))


## Variability

### Variance

####implementation

def variance(dset):
    n=len(dset)
    if n<2:
        return
    mn=stat.fmean(dset)
    return sum( (item-mn)**2 for item in dset)/(n-1)

print('(variance of dataset, variance of data):',(variance(dataset),variance(data)))

####using stat.variance()
print('(variance of dataset, variance of data):',(stat.variance(dataset),stat.variance(data)))

### standard deviation

####implementation

def stdev(dset):
    import math
    return math.sqrt(stat.variance(dset))

print('(stdev of dataset, stdev of data):',(stdev(dataset),stdev(data)))

####using stat.stdev()
print('( stdev of dataset, stdev data):',(stat.stdev(dataset),stat.stdev(data)))

### Population variance and standar deviation

####Population variance
#####implementation

def pvariance(dset):
    n=len(dset)
    if n<2:
        return
    mn=stat.fmean(dset)
    return sum( (item-mn)**2 for item in dset)/n

print('(pvariance of dataset, pvariance of data):',(pvariance(dataset),pvariance(data)))

#####using pvariance
print('(pvariance of dataset, pvariance of data):',(stat.pvariance(dataset),stat.pvariance(data)))

####Population standard deviation
#####implementation
def pstdev(dset):
    import math
    return math.sqrt(stat.pvariance(dset))

print('(pstdev of dataset, pstdev of data):',(pstdev(dataset),pstdev(data)))

#####using stat.pstdev()
print('( pstdev of dataset, pstdev of data):',(stat.stdev(dataset),stat.stdev(data)))

### Range

####implementation

def myrange(dset):
    return max(dset)- min(dset)

print('( range of dataset, range of data):',(myrange(dataset),myrange(data)))

## Correlation

x=[5, 2, 7, 4, 2, 7, 8,-2.58,0,5]
y=[4,-8,9,4.5,8,9,10,17,56,-5]
print(len(x),len(y))

print('x:',x)
print('y:',y)

### covariance

####implementation

def covariance(dset1,dset2):
    n=len(dset1)
    if n!=len(dset2) or n<2:
        return
    mean1=stat.fmean(dset1)
    mean2=stat.fmean(dset2)
    return sum( (dset1[i]-mean1)*(dset2[i]-mean1) for i in range(n))/(n-1)

print('( cov(x,y)):',covariance(x,y))

#### using stat.covariance()

print('( cov(x,y)):',stat.covariance(x,y))

### correlation coefficient



####implementation

def corr(dset1,dset2):
    n=len(dset1)
    if n!=len(dset2) or n<2:
        return
    return stat.covariance(dset1, dset2)/(stat.stdev(dset1)*stat.stdev(dset2))

print('( cor(x,y)):',corr(x,y))

#### using stat.corellation()
print('( cor(x,y)):',stat.correlation(x, y))
