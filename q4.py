def average_passing_grades(grades: list[int]) -> float:
    total = 0
    count = 0
    for grade in grades:
        if grade >= 50:
            total += grade
            count += 1
    return total / count if count > 0 else 0.0


