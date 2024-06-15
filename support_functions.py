

import numpy as np

def calculate_accuracy(predicted, actual):
  
  correct = 0
  for i in range(len(predicted)):
    if predicted[i] == actual[i]:
      correct += 1
  
  accuracy = correct/len(predicted)
  
  return accuracy

# copy your splitdata_train_test function here
def splitdata_train_test(data, fraction_training):
  # complete this function
  np.random.shuffle(data)
  split = int(len(data)*fraction_training)
  return data[:split], data[split:]

# copy your generate_features_targets function here
def generate_features_targets(data):
  # complete the function by calculating the concentrations
  
  targets = data['class']

  features = np.empty(shape=(len(data), 13))
  features[:, 0] = data['u-g']
  features[:, 1] = data['g-r']
  features[:, 2] = data['r-i']
  features[:, 3] = data['i-z']
  features[:, 4] = data['ecc']
  features[:, 5] = data['m4_u']
  features[:, 6] = data['m4_g']
  features[:, 7] = data['m4_r']
  features[:, 8] = data['m4_i']
  features[:, 9] = data['m4_z']

  # fill the remaining 3 columns with concentrations in the u, r and z filters
  # concentration in u filter
  features[:, 10] = data['petroR50_u']/data['petroR90_u']
  # concentration in r filter
  features[:, 11] = data['petroR50_r']/data['petroR90_r']
  # concentration in z filter
  features[:, 12] = data['petroR50_z']/data['petroR90_z']

  return features, targets