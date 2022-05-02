import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro, levene, ttest_ind

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# The data set consisting of control and test group data named ab_testing_data.xlsx was read.
# Control and test group data were assigned to separate variables.

df_control = pd.read_excel("databases/ab_testing.xlsx",sheet_name='Control Group')
df_test = pd.read_excel("databases/ab_testing.xlsx",sheet_name='Test Group')

#Analyze control and test group data.

def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head())
    print("##################### Tail #####################")
    print(dataframe.tail())
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df_control)
check_df(df_test)


# After the analysis, the control and test group data were combined using the concat method.

df_new=pd.concat([df_control, df_test], axis=1)
df_new.columns=['ImpressionControl', 'ClickControl', 'PurchaseControl', 'EarningControl', 'ImpressionTest', 'ClickTest',
       'PurchaseTest', 'EarningTest']

#Defining the A/B Test Hypothesis

# Defining the hypothesis.

# H0 : M1 = M2 (There is no difference between the control group and test group purchasing averages.)
# H1 : M1!= M2 (There is a difference between the purchasing averages of the control group and test group.)

# Analyze the purchase (gain) averages for the control and test group


df_new.groupby("group").agg({"Purchase": "mean"})

#Performing Hypothesis Testing

# Assumption checks are done before hypothesis testing is done. These are Assumption of Normality and Homogeneity of Variance.

# Whether the control and test groups comply with the normality assumption was tested separately over the Purchase variable.
# Normality Assumption :
# H0: Assumption of normal distribution is provided.
# H1: Normal distribution assumption not provided
# p < 0.05 H0 RED
# p > 0.05 H0 CANNOT BE REJECTED
# According to the test result, whether the assumption of normality is provided for the control and test groups.
# interpreted according to the p-values obtained.

test_stat, pvalue = shapiro(df_new["PurchaseControl"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


# p-value=0.5891
# HO cannot be denied. The values of the control group provide the assumption of normal distribution.



test_stat, pvalue = shapiro(df_new["PurchaseTest"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value=0.1541
# HO cannot be denied. The values of the control group provide the assumption of normal distribution.

# Variance Homogeneity:
# The variance is the sum of the squares of the deviations of the data from the arithmetic mean. In other words, it is the standard deviation without the square root.
# H0: Variances are homogeneous.
# H1: The variances are not homogeneous.
# p < 0.05 H0 RED
# p > 0.05 H0 CANNOT BE REJECTED
# Test whether the homogeneity of variance is provided for the control and test groups over the Purchase variable.
# Is the assumption of normality provided according to the test result? Interpret the p-values obtained.

test_stat, pvalue = levene(df_new["PurchaseControl"],
                           df_new["PurchaseTest"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value=0.1083
# HO cannot be denied. The values of the Control and Test groups provide the assumption of variance homogeneity.
# Variances are Homogeneous.

#  The appropriate test is selected according to the Normality Assumption and Variance Homogeneity results

# Since assumptions are provided, independent two-sample t-test (parametric test) is performed.
# H0: M1 = M2 (There is no statistically significant difference between the control group and test group purchasing averages.)
# H1: M1 != M2 (There is a statistically significant difference between the control group and test group purchasing averages)
# p<0.05 HO RED , p>0.05 HO CANNOT BE REJECTED

test_stat, pvalue = ttest_ind(df_new["PurchaseControl"],
                           df_new["PurchaseTest"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#  Purchasing the control and test group by considering the p_value obtained as a result of the test
#It was interpreted whether there was a statistically significant difference between the averages.

# p-value=0.3493
# HO cannot be denied. There is no statistically significant difference between the purchasing averages of the control and test groups.