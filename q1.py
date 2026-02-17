def calculate_total_bill(amount: float, tip_percent: int) -> float:
    total = float(amount) * (1 + float(tip_percent) / 100)
    return round(total, 2)
Team name - {Code Trio}
