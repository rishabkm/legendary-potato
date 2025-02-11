quarters = int(input())  # Initial number of quarters
first = int(input())  # First slot machine counter
second = int(input())  # Second slot machine counter
third = int(input())  # Third slot machine counter

plays = 0
machine = 0  # Keeps track of which machine Martha is playing

while quarters >= 1:  # Continue until she runs out of quarters
    quarters -= 1  # Each play costs 1 quarter

    if machine == 0:  
        first += 1
        if first == 35:
            first = 0
            quarters += 30  # Wins 30 quarters

    elif machine == 1:
        second += 1
        if second == 100:
            second = 0
            quarters += 60  # Wins 60 quarters

    elif machine == 2:
        third += 1
        if third == 10:
            third = 0
            quarters += 9  # Wins 9 quarters

    plays += 1  # Increase play count
    machine = (machine + 1) % 3  # Cycle through machines (0 → 1 → 2 → 0)

print('Martha plays', plays, 'times before going broke.')
