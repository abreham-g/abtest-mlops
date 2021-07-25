# A/B Hypothesis Testing: Ad campaign performance

# Classic and sequential A/B testing analysis

performming data exploration to count unique values of categorical variables, 
making histogram, relational, and other necessary plots to help understand the data. For
each of the plots we produce, We will write a description of what the plot shows in
markdown cells.

performming hypothesis testing: we will apply the classical p-value based algorithm and the
sequential A/B testing algorithm for which a starter code is provided.

    - Are the number of data points in the experiment enough to make a reasonable
      judgement or should the company run a longer experiment? Remember that
      running the experiment longer may be costly for many reasons, so you should
      always optimize the number of samples to make a statistically sound decision.
    - What does your A/B testing analysis tell you? Is brand awareness increased for
      the exposed group?
# A/B testing with Machine Learning
we Split data by browser and platform_os, and version each split as a new version of
the data in dvc.

    - For each version of the data do the following
    - Split the data into 70% training, 20% validation, and 10% test sets.
    - Based on the reading material provided, apply machine learning to the
      training data. Train a machine learning model using 5-fold cross validation
      using the following 3 different algorithms:
            - Logistic Regression
            - Decision Trees
            - XGBoost
# conclusion
We discovered that the system is affected by hours in logistic regression.
Magnitude and direction of effect that We discovered the impact each features had on the awareness of the users and wether it is positive or not




