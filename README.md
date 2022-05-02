# AB-Testing

What is AB testing known as A/B testing? A/B testing is a methodology that reveals the user experience. With this methodology, it is tried to measure the interactions of users over two variables. It measures 2 different variables with systematic and theoretical analysis, leaving other factors the same. It is quite common to use these statistical values to measure advertising performance.

# Business Problem

Facebook recently available alternative to the bidding type called "maximumbidding"
Introduced a new type of bid, "average bidding" as  One of our customers, ......com,
decided to test this new feature and found that average bidding converts more than maximum bidding
He wants to do an A/B test to see if it returns. A/B testing continues for 1 month and
........com is now waiting for us to analyze the results of this A/B test. ultimate success criterion is Purchase. Therefore, the focus should be on the Purchase metric for statistical testing.

# Dataset Story
What users see and click on in this dataset, which includes a company's website information
In addition to information such as the number of advertisements, there are earnings information from here. There are two separate data sets, the Control and Test group. These datasets are on separate sheets of the ab_testing.xlsx excel. Maximum Bidding was applied to the control group and Average Bidding was applied to the test group..

Impression: Ad impressions

Click: Number of clicks on the displayed ad

Purchase: The number of products purchased after the ads clicked

Earning: Earnings after purchased products

# Analysis of Results


Firstly, normality test was applied to both groups. Since it was observed that the normal distribution was observed in both groups, the second assumption was made and the homogeneity of the variance was examined. Since the variances are homogeneous
"Independent Two-Sample T-Test" was applied. As a result of the application, it was observed that the p-value was greater than 0.05.
and H0 hypothesis could not be rejected.


Since there is no significant difference in terms of purchase, the customer can choose one of the two methods, but here are the other statistics.
differences will also matter. The differences in Click, Engagement, Earnings and Conversion Rates are evaluated and which
method can be found to be more profitable. Which method is clicked, especially since Facebook is paid per click?
It can be determined that the rate is lower and the CTR (Click Through Rate) rate can be checked.
