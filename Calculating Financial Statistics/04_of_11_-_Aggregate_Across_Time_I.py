def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

daily_return_a = 0.001
monthly_return_b = 0.022

# Write code here
print("The daily rate of return for Investment A is ", str(display_as_percentage(daily_return_a)))
print("The monthly rate of return for Investment B is ", str(display_as_percentage(monthly_return_b)))

def annualize_return(log_return, t):
  r = log_return*t
  return r

annual_return_a = annualize_return(daily_return_a, 252)
print("The annual rate of return for Investment A is ", str(display_as_percentage(annual_return_a)))

annual_return_b = annualize_return(monthly_return_b, 12)
print("The annual rate of return for Investment B is ", str(display_as_percentage(annual_return_b)))