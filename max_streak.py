def max_streak(num_employees, data):

    full_attend = 'Y' * num_employees
    current = 0
    count = 0
    
    for day in data:
        if day == full_attend:
            current += 1
        else:
            count = max(count, current)
            current = 0
            
    return max(count, current_streak)

