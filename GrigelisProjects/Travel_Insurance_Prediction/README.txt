Travel Insurance

Project description
A Tour & Travels Company Is Offering Travel Insurance Package To Their Customers. The New Insurance Package Also Includes Covid Cover. The Company Requires To Know The Which Customers Would Be Interested To Buy It Based On Its Database History. The Insurance Was Offered To Some Of The Customers In 2019 And The Given Data Has Been Extracted From The Performance/Sales Of The Package During That Period.

Dataset
Age - age of the customer.
Employment Type - the sector in which customer is employed: Government Sector or Private Sector/Self Employed.
GraduateOrNot- whether the customer is college graduate or not
AnnualIncome- the yearly income of the customer in indian rupees[rounded to nearest 50 thousand rupees]
FamilyMembers- number of members in customer's family
ChronicDisease- whether the customer suffers from any major disease or conditions like diabetes/high bp or asthama,etc.
FrequentFlyer- derived data based on customer's history of booking air tickets on at least 4 different instances in the last 2 years[2017-2019].
EverTravelledAbroad- has the customer ever travelled to a foreign country[not necessarily using the company's services]
TravelInsurance- did the customer buy travel insurance package during introductory offering held in the year 2019.
Goal
Predict whether a given customer would like to buy the insurance package, once the corona lockdown ends and travelling resumes.

Hypothesis 1
Null hypothesis: Family size has no impact for purchase of Travel insurance.
Alternative hypothesis: Family size has impact for purchase of Travel insurance.

Hypothesis 1 interpretation
Mann-Whitney U statistics: 151330.5
p-value: 0.03752688801410266
We reject the null hypothesis that family size has an effect on travel insurance.

Hypothesis 2
Null hypothesis: ChronicDisease has no impact for purchase of Travel insurance.
Alternative hypothesis: ChronicDisease has impact for purchase of Travel insurance.

Hypothesis 2 interpretation
Mann-Whitney U statistics: 161136.0
p-value: 0.6809240702889678
There is insufficient evidence to reject the null hypothesis that family size has no significant effect.

Results
          precision    recall  f1-score   support

       0       0.77      0.27      0.40       256
       1       0.39      0.85      0.54       142

accuracy                           0.48       398
macro avg 0.58 0.56 0.47 398 weighted avg 0.64 0.48 0.45 398

[[ 70 186] [ 21 121]] Class 1 (positive): High recall (0.85) remains — most positive cases are detected, but precision remains low (0.39) — almost 6 out of 10 positive predictions are false.
Class 0 (negative): Only 27% of true negatives are classified correctly. Many false positives — too sensitive threshold.
Overall accuracy: 48%, but this is not the most important criterion when trying to catch as many positive cases as possible.

The model correctly predicts 85% of positive cases, which is the most important aspect. It is better to offer travel insurance to someone who is not interested, than to miss offering it to someone who is willing to buy — and risk losing a customer.

Suggestions for future
Include more/other parameters to the model.
To test other models.