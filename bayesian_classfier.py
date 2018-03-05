# -*- coding: utf-8 -*-
"""
Created on Mar 2018

@author: Shimin
"""


from sklearn.naive_bayes import MultinomialNB

# naive bayesian classifier
def nb_classifer(X,y):

    clf = MultinomialNB()
    clf.fit(X, y)

    return clf


if __name__ == '__main__':



    nb_train_X = [[1, 1, 0],
                     [0, 1, 1],
                     [0, 0, 1],
                     [0, 0, 1],
                     [1, 0, 0],
                     [1, 0, 0],
                     [1, 0, 0],
                     [0, 0, 0]]

    nb_train_y = [1, 1, 1, 1, 0, 0, 0, 0]

    nb_test_X = [[0, 1, 0]]

    clf = nb_classifer(nb_train_X, nb_train_y)

    print (clf.predict(nb_test_X))
