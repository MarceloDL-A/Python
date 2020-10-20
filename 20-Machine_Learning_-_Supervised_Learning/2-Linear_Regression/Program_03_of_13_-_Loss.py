x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0
y_predicted1 = [m1*x_valor + b1 for x_valor in x]
#y = 0.5x + 1
m2 = 0.5
b2 = 1
y_predicted2 = [m2*x_valor + b2 for x_valor in x]

total_loss1 = 0
total_loss2 = 0
for i in range(len(y_predicted1)):
  total_loss1 += (y[i]-y_predicted1[i])**2
  total_loss2 += (y[i]-y_predicted2[i])**2

print("total_loss1: " + str(total_loss1))
print("total_loss2: " + str(total_loss2))

better_fit = 2

