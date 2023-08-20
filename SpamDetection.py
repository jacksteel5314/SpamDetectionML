import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer


value_input = str(input("Input a Message: "))
X_test_cv = pd.DataFrame(
    {
        "v1" : ['idk'], 
        "v2" : [value_input]
    }
)


# Data Frame
df = pd.read_csv("spam.csv", encoding='cp1252')
spam_df = df[["v1", "v2"]]

# Count Vectorizer 
count_vect = CountVectorizer()
X_train_trans = count_vect.transform(spam_df["v2"])
X_test_trans = count_vect.transform(spam_df["v1"])
cv_mnb = MultinomialNB()
cv_mnb.fit(X_train_trans, spam_df["v1"])
cv_mnb_y_pred = cv_mnb.predict(X_test_trans)
print(cv_mnb_y_pred)