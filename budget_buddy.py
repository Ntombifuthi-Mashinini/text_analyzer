monthly_income = float(input("Enter your total monthly income: R"))
daily_essentials = float(input("Enter your estimated daily cost for essentials: R"))

total_expenses = daily_essentials * 30
leftover_balance = monthly_income - total_expenses
daily_fun_budget = leftover_balance // 30

print("\n--- Your Monthly Budget Summary ---")
print(f"Total monthly expenses:  R{total_expenses:.2f}")
print(f"Leftover balance:        R{leftover_balance:.2f}")
print(f"Daily fun budget:        R{daily_fun_budget:.2f}")
