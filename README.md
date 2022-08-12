# Pima_Indians_Diabetes

Database

---------------------------------------------------------------------------

https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

---------------------------------------------------------------------------

Dataset details

=========================================================================

1: Pregnancies: Number of times pregnant

2: Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test.

3: BloodPressure: Diastolic blood pressure (mm Hg)

4: SkinThickness: Triceps skinfold thickness (mm)

5: Insulin: 2-Hour serum insulin (mu U/ml)

6: BMI: Body mass index (weight in kg/(height in m)²)

7: DiabetesPedigreeFunction: Diabetes pedigree function

8: Age: Age (years)

9: Outcome: Class variable (0 or 1) 268 of 768 are 1, the others are 0


=====================================================================================
=====================================================================================


                                             Approach 

====================================================================================

Data Exploration: 

1) The target variable is "Outcome".

2) There are nine categorical columns , which are in the numeric format.

3) The correlation of 'Outcome' with other columns are normal correlated. SO we cannot drop any of the columns form the data.

4) There are may zeroes appeared in most of the columns which has to beb replaced.

Feature Engineering:

1) First of all changed the zero values present in the column 'Glucose', 'Insulin', 'BMI', 'BloodPressure', 'SkinThickness'. Replaced them using median() on all of them.

2) The presence of outliers are high in the continuous columns. So, by standard deviation thr upper and lower limits were handled.

Building of the models:



Final Submission: 


