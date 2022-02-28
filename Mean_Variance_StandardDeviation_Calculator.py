import numpy as np

def calculate(list):
  
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
    
  calculations = {}
  # converting the values we have to a 3*3 matrix
  list = np.array(list)
  list = list.reshape(3,3)

  # Calculating mean
  mean_axis_1 = np.mean(list, 0).tolist()
  mean_axis_2 = np.mean(list, axis = 1).tolist()
  mean_axis = np.mean(list)

  # Calculating variance
  variance_axis_1 = np.var(list, 0).tolist()
  variance_axis_2 = np.var(list, 1).tolist()
  variance_axis = np.var(list).tolist()

  # Calculating standard deviation
  std_axis_1 = np.std(list, 0).tolist()
  std_axis_2 = np.std(list, 1).tolist()
  std_axis = np.std(list).tolist()
  
  # Calculating max
  max_axis_1 = np.max(list, 0).tolist()
  max_axis_2 = np.max(list, 1).tolist()
  max_axis = np.max(list).tolist()

  # Calculating min
  min_axis_1 = np.min(list, 0).tolist()
  min_axis_2 = np.min(list, 1).tolist()
  min_axis = np.min(list).tolist()

  # Calculating sum
  sum_axis_1 = np.sum(list, 0).tolist()
  sum_axis_2 = np.sum(list, 1).tolist()
  sum_axis = np.sum(list).tolist()

  # Adding the calculated values into the dictionary
  calculations["mean"] = [mean_axis_1,mean_axis_2,mean_axis]
  calculations["variance"] = [variance_axis_1,variance_axis_2,variance_axis]
  calculations["standard deviation"] = [std_axis_1,std_axis_2,std_axis]
  calculations["max"] = [max_axis_1,max_axis_2,max_axis]
  calculations["min"] = [min_axis_1,min_axis_2,min_axis]
  calculations["sum"] = [sum_axis_1,sum_axis_2,sum_axis]


  return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))