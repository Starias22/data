# Descriptive statistics

Descriptive statistics is a branch of statistics that deals with the collection, analysis, interpretation, and presentation of data. It provides a way to summarize and describe important features of a dataset, such as its central tendency, variability, and correlation.

## Central tendancy

Central tendency is a measure of the "typical" or "central" value of a dataset. The most commonly used measures of central tendency are:

* Mean
* Weighted mean
* Geometric mean
* Harmonic mean
* Mode

### Mean

It's the arithmetic average of a dataset. It is calculated by summing all the values in the dataset and dividing by the number of observations.

#### mean and fmean

#### Weighted mean

Weighted mean is a variation of the mean that takes into account the importance or weight of each value in the dataset. It is calculated by multiplying each value by its weight, summing the products, and dividing by the sum of the weights.

#### Geometric mean

Geometric mean is a type of mean that is calculated by taking the nth root of the product of n values. It is commonly used for datasets that exhibit exponential growth or decay.

#### Harmonic mean

Harmonic mean is a type of mean that is calculated by taking the reciprocal of each value, calculating the mean of the reciprocals, and taking the reciprocal of the result. It is commonly used for datasets that involve rates or ratios.

### Median

It's the middle value of a dataset. It is calculated by ordering the values in the dataset and selecting the value that is in the middle.

Median can be further divided into low median and high median, depending on whether the middle value is included in the dataset or not.

#### median

#### Low median

The low median is the median of the lower half of the dataset.

#### High median

The high median is the median of the upper half.

### Mode

The mode of a data set is the value that appears most frequently in that data set.
Mean can be calculated using different functions in Python, such as the mean function from the statistics module, or the mean function from the numpy module. The fmean function from the math module is a faster implementation of the mean function that only works with floats.

Mode can also be further divided into different types, such as mode and multimode.

#### mode

For datasets with one mode

#### multimode

For datasets with multiple modes

## Variability

Variability is a measure of how spread out or dispersed the values in a dataset are. The most commonly used measures of variability are:

* Variance
* Standard deviation
* Population variance and standard deviation
* Range
* Correlation

### Variance

Variance: a measure of how much the values in a dataset deviate from the mean. It is calculated by taking the sum of the squared deviations from the mean and dividing by the number of observations minus one.

### Standard deviation

Standard deviation: the square root of the variance. It represents the typical amount of deviation from the mean in a dataset.

### Population variance and standard deviation

Population variance and standard deviation are similar to variance and standard deviation, but they are calculated using the entire population of observations, rather than a sample of the population.

#### pvariance

#### pstdev

### Range

Ranges are measures of the spread of a dataset, calculated as the difference between the maximum and minimum values.

## Correlation

Correlation consit to study relationship between two ore several data sets

### covariance

### correlation coefficient

The correlation coefficient is a measure of the strength and direction of the linear relationship between two variables. It ranges from -1 to 1, with values close to -1 indicating a strong negative correlation, values close to 1 indicating a strong positive correlation.
