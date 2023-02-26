from __future__ import division, print_function, unicode_literals
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Xử lý loại bỏ các line dữ liệu thừa
from sklearn.naive_bayes import GaussianNB

with open('datacum.txt', 'r') as oFile, open('rawData.csv', 'w') as nFile:
    for line in oFile:
        if not line.startswith('#') and not line.startswith('\n'):
            nFile.write(line)
data = pd.read_csv('rawData.csv', header=None)
#chọn mẫu test
uBenign = data[data[1] == 2]  # u lành tính
uMalignant = data[data[1] == 4]  # u ác tính
testData = pd.concat([uBenign.sample(n=80, random_state=42), uMalignant.sample(n=40, random_state=42)])
trainData = data.drop(testData.index)
#training dữ liệu
X_train = trainData.drop([1], axis=1)
y_train = trainData[1]
gnb = GaussianNB()
gnb.fit(X_train, y_train)
X_test = testData.drop([1], axis=1)
y_test = testData[1]

y_pred = gnb.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy: {:.2f}%".format(accuracy * 100))

precision = precision_score(y_test, y_pred, pos_label=2)
print("Precision: {:.2f}%".format(precision * 100))
#
recall = recall_score(y_test, y_pred, pos_label=4)
print("Recall: {:.2f}%".format(recall * 100))
