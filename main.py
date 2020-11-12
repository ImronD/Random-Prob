import random

def randomProb():
  # This function will take your reward to risk ratio, accuracy, frequency and number of tests to give you a realistic outcome of your trading system.

  # Get input from user and define variables.
  numTests = int(input("How many tests would you like to run?:\n"))
  rRatio = float(input("What is your reward:risk ratio?:\n"))
  accuracy = float(input("What is your accuracy in decimal?:\n"))
  trades = int(input("How many trades would you like to take each run?:\n"))
  total = 0
  allTimeHigh = 0
  maxDrawdown = 0

  # For every trade in every test
  for test in range(numTests):
    streak = []
    testSum=0
    for trade in range(trades):
      # Determine if trade is a winner or loser.
      tradeOutcome = random.randint(0,1000)
      if tradeOutcome <= (accuracy * 1000):
        testSum += rRatio
        total += rRatio
        streak.append('W')
      else:
        testSum -= 1
        total -=1
        streak.append('L')
      # Cheack if your P/L is at an all time high.  
      if total > allTimeHigh:
        allTimeHigh = total
      # Calculate maximum drawdown.
      if maxDrawdown < allTimeHigh - total:
        maxDrawdown = abs(total-allTimeHigh)
    # Results of every individual test run.
    print("\n",streak)
    print("Your total for this run was",round(testSum,2),'R\n')

  # Results of all tests combined.
  print ("After",numTests*trades,"trades, you've netted",round(total,2),"R's.")
  print ("Your maximum drawdown was",round(maxDrawdown,2),"R.")

randomProb()
 