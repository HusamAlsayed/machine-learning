import os
import shutil
class SpamClassifier:
  def __init__(self):
    self.labels =  ['spam','ham']
  
  def train(self,X_train , Y_train):
    for l in self.labels:
      name = l + '.txt'
      if os.path.exists(name):
        print(name)
        os.remove(name)
    for content,label in zip(X_train,Y_train):
      with open(label + '.txt','a') as f:
        f.write(' ' + content)

  def score(self,X_test,Y_test):
    ans = 0
    for index,(content,label) in enumerate(zip(X_test,Y_test)):
      sz = []
      for l in self.labels:
        old_size = os.path.getsize('/content/{}.zip'.format(l))
        with open(l + '.txt','a') as f:
          f.write(' ' + content)
        shutil.make_archive(l,'zip','/content/{}'.format(l))
        new_size = os.path.getsize('/content/{}.zip'.format(l))
        sz.append(new_size - old_size)
        with open(l + '.txt','rb+') as f:
          f.seek(-len(content) - 1,os.SEEK_END)
          f.truncate()
      predict_value = 'ham'
      if sz[0] > sz[1]:
        predict_value = 'spam'
      if predict_value == label:
        ans+=1
    return round(ans/len(X_test),3)

  def predict(self,X_test):
    for index,content in enumerate(X_test):
      sz = []
      for l in self.labels:
        old_size = os.path.getsize('/content/{}.zip'.format(l))
        with open(l + '.txt','a') as f:
          f.write(' ' + content)
        shutil.make_archive(l,'zip','/content/{}'.format(l))
        new_size = os.path.getsize('/content/{}.zip'.format(l))
        sz.append(new_size - old_size)
        with open(l + '.txt','rb+') as f:
          f.seek(-len(content) - 1,os.SEEK_END)
          f.truncate()
      predict_value = 'ham'
      if sz[0] > sz[1]:
        predict_value = 'spam'
      return predict_value
   
