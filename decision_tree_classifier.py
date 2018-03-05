# -*- coding: utf-8 -*-
"""
Created on Mar 2018

@author: Shimin
"""

from sklearn.tree import DecisionTreeClassifier

# decision tree induction
def dtree_classifer(X,y):

    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(dtree_train_X, dtree_train_y)

    return clf

if __name__ == "__main__":

    dtree_train_X = [[1,1,0],
         [0,1,1],
         [0,0,1],
         [0,0,1],
         [1,0,0],
         [1,0,0],
         [1,0,0],
         [0,0,0]]

    dtree_train_y = [1,1,1,1,0,0,0,0]

    dtree_test_X = [[0,1,0]]

    clf =dtree_classifer(dtree_train_X, dtree_train_y)

    print (clf.predict(dtree_test_X))