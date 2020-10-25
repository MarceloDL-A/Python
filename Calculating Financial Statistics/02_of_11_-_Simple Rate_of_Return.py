def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

# Write code here
def calculate_simple_return(start_price, end_price, dividend = 0):
  r = (end_price - start_price + dividend)/start_price
  return r
simple_return = calculate_simple_return(200, 250, 20)
print('The simple rate of return is ',(display_as_percentage(simple_return)))