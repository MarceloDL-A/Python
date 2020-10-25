def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

daily_returns = [0.002, -0.002, 0.003, 0.002, -0.001]

# Write code here
def convert_returns(log_returns, t):
  r = sum(log_returns)*t/len(log_returns)
  return r

annual_return = convert_returns(daily_returns, 252)
print('The annual rate of return is', display_as_percentage(annual_return))


weekly_return = sum(daily_returns)
print('The weekly rate of return is', display_as_percentage(weekly_return))
weekly_return = convert_returns(daily_returns, 5)
print('The weekly rate of return is', display_as_percentage(weekly_return))


