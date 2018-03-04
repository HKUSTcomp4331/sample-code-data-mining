# -*- coding: utf-8 -*-
"""
Created on Mar 2018

@author: Shimin
"""

from sklearn.neighbors import KNeighborsClassifier

# KNN classifier
def KNN(X,y,k):

    neigh = KNeighborsClassifier(n_neighbors=k)
    neigh.fit(X, y)

    return neigh


if __name__ == '__main__':


    knn_train_X = [[1, 1, 1, 0],
         [1, 1, 1, 1],
         [2, 1, 1, 0],
         [3, 2, 1, 0],
         [3, 3, 2, 0],
         [3, 3, 2, 1],
         [2, 3, 2, 1]]

    knn_train_y = [0,0,1,1,1,0,1]

    knn_test_X = [[3,2,1,1]]

    knn_k = 3

    knn_classifier = KNN(knn_train_X,knn_train_y,knn_k)

    print(knn_classifier.predict(knn_test_X))