import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("spam.csv", encoding='cp1252')
spam_df = df[["v1", "v2"]]


def detect(message):
    pd_df = _create_df(message)
    count_vect = CountVectorizer()
    count_vect.fit_transform(spam_df["v2"])
    X_transformed_train = count_vect.transform(spam_df["v2"])
    X_transformed_test = count_vect.transform(pd_df["v2"])
    ui_mnb = MultinomialNB()
    ui_mnb.fit(X_transformed_train, spam_df["v1"])
    predictions = ui_mnb.predict(X_transformed_test)
    return None if len(predictions)==0 else predictions[0]

def _create_df(inputted):
    pd_df = pd.DataFrame(
        {
            "v1" : ['idk'],
            "v2" : [inputted]
        }
    )
    return pd_df


