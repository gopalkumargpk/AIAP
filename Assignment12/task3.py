"""
Optimization problem:

Let:
  x = units of chocolate A
  y = units of chocolate B

Maximize profit:
  Z = 6x + 5y

Subject to resource constraints:
  Milk:  1x + 1y <= 5
  Choco: 3x + 2y <= 12
  x, y >= 0
"""

import pulp


def solve_chocolate_problem():
    # Define the LP problem: maximize profit
    problem = pulp.LpProblem("Chocolate_Profit_Maximization", pulp.LpMaximize)

    # Decision variables (non‑negative and integer, since units are countable)
    x = pulp.LpVariable("A_units", lowBound=0, cat="Integer")
    y = pulp.LpVariable("B_units", lowBound=0, cat="Integer")

    # Objective function: maximize 6x + 5y
    problem += 6 * x + 5 * y, "Total_Profit"

    # Constraints
    problem += x + y <= 5, "Milk_Constraint"
    problem += 3 * x + 2 * y <= 12, "Choco_Constraint"

    # Solve the problem
    problem.solve()

    # Extract solution
    optimal_x = int(pulp.value(x))
    optimal_y = int(pulp.value(y))
    max_profit = pulp.value(problem.objective)

    return optimal_x, optimal_y, max_profit


if __name__ == "__main__":
    A_units, B_units, profit = solve_chocolate_problem()
    print(f"Optimal units of A: {A_units}")
    print(f"Optimal units of B: {B_units}")
    print(f"Maximum profit: Rs {profit}")


