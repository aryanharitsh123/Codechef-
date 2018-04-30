import sys
data = sys.stdin.read()
to_withdraw, initial_balance = data.rstrip().split(" ")
initial_amount = float(initial_amount)
to_withdraw=int(to_withdraw)
if to_withdraw % 5 == 0 and initial_amount >= to_withdraw + 0.50:
    print(round(initial_balance - to_withdraw - 0.50,2))
else:
    print(round(initial_balance,2))