burger_calories = [461, 431, 420, 0]
drink_calories = [130, 160, 118, 0]
side_calories = [100, 57, 70, 0]
dessert_calories = [167, 266, 75, 0]

burger_choice = int(input()) - 1
side_choice = int(input()) - 1
drink_choice = int(input()) - 1
dessert_choice = int(input()) - 1

total_calories = (burger_calories[burger_choice] +
                  side_calories[side_choice] +
                  drink_calories[drink_choice] +
                  dessert_calories[dessert_choice])

print("Your total Calorie count is {total_calories}.")
