import pandas as pd
import numpy as np
import os

# TO DO: Import any additional packages



# TO DO: implement the entropy calculation for a given Series.
def entropy(S):
    # your implementation here
    return 0


# To Do: implement miscalculation loss for a given Series.
def misclassification(S):
    # your implementation here
    return 0


# To Do: implement gini (impurity) loss for a given Series.
def gini(S):
    # your implementation here
    return 1


# To Do: Implement the information gain that takes a set of splits using
#        a single feature and given loss criterion to provide the 
#        information gain.
def calculate_gain(subset_splits, criterion="gini"):
    # your implementation here
    return 0


# To Do: Implement a function that splits a dataset by a specific
#        feature.
def dataset_split_by_feature(dataset, feature, label):
    # your implementation here
    return []


# To Do: Fill find_best_split(dataset, label, criterion) function
#        which will find the best split for a given dataset, label,
#        and criterion. It should out using the given string output
#        format.
def find_best_split(dataset, label, criterion="gini"):
    # for each split calculate gain, return best feature to split and the gain
    best_feature = best_gain = 0
    return best_feature, best_gain, criterion


# If you used the starter code, you won't have to change any of the below
# code except for filling in your name and adjusting the criterion if you
# are in CS4361 and choose not to implement additional criterion.
if __name__ == '__main__':
  # read file
  name = "Doe_john"
  os.makedirs(name=name)
  data = pd.read_csv("agaricus-lepiota.csv")
  label = "class"
  
  # Find the best feature using suggested methods
  criteria = ["gini", "entropy", "misclassification"]
  f = open(f"{name}/mushrooms.txt", "w")
  for criterion in criteria:
    best_feature, best_gain, _ = find_best_split(data, "class", criterion)
    f.write(f"Best feature: {best_feature} Using: {criterion}-Gain: {best_gain:.2f}\n")
  f.close()