import math

def calculate_eoq(demand, ordering_cost, holding_cost):
    """
    EOQ = sqrt((2 * D * S) / H)
    """
    if holding_cost == 0:
        return 0

    eoq = math.sqrt((2 * demand * ordering_cost) / holding_cost)

    # Total Cost = Ordering Cost + Holding Cost
    ordering_cost_total = (demand / eoq) * ordering_cost
    holding_cost_total = (eoq / 2) * holding_cost

    total_cost = ordering_cost_total + holding_cost_total

    return round(eoq, 2), round(total_cost, 2)