#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
knn.py
~~~~~~
@Author: Patrick Spencer

Implementation of KNN

# make two points with a known l2 distance
# answer is 5
from sklearn.model_selection import train_test_split

p1 = np.array([0., 4.])
p2 = np.array([3., 0.])
X = np.random.normal(size=[10, 2])
y = np.random.randint(0, 2, 10)  # y is the array of classes


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

knn = Knn(X_train, y_train)
type(knn.dist_np(p1, p2))
"""
from typing import Optional
from collections import defaultdict, Counter
import numpy as np
import numpy.typing as npt

"""
TODO:
Change fit function to accept batch points
"""


class Point:
    """Abstracting Point as a class makes label and data easier
    to keep track of
    """

    def __init__(self, data: npt.ArrayLike, label: int = None):
        self.data = data
        self.label = label


class Knn:
    """main knn class"""

    def __init__(self, X_train: npt.ArrayLike, y_train: npt.ArrayLike, k=5):
        self.k = k
        self.points = []
        self.nn = defaultdict(list)
        for data, label in zip(X_train, y_train):
            self.points.append(Point(data, label))

    def dist(self, p1: Point, p2: Point) -> np.float64:
        """Compute the distance between two Point instances. Defaults to
        L2 distance"""
        return np.linalg.norm(p1.data - p2.data)

    def fit(self, p: npt.ArrayLike) -> None:
        q = Point(p)
        # O(nlog(n))
        tmp = sorted(self.points, key=lambda x: self.dist(q, x))[:self.k]
        self.nn[tuple(p)] = tmp

    def predict(self, p: npt.ArrayLike) -> Optional[int]:
        t = tuple(p.tolist())
        c = Counter([q.label for q in self.nn[t]]).most_common()
        return c[0][0] if c else None

    def knn_all_points(self):
        self.distances = {}
        for p in self.points:
            self.distance[p] = self.sort_points(p)
