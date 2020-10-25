# Import library here
from math import log

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

# Write code here
def calculate_log_return(start_price, end_price):
  r = log(end_price/start_price)
  return r

log_return = calculate_log_return(200, 250)
print('The value formatted as a percentage is', display_as_percentage(log_return))