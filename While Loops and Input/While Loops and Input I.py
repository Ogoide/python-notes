# A while loop tests an initial condition.
# If that condition is true, the loop starts executing. Every time the loop finishes, the condition is reevaluated.
# As long as the condition remains true, the loop keeps executing.
# As soon as the condition becomes false, the loop stops executing.

# Setting an initial condition
loop_active = True

# Setting the loop
while loop_active:
    #Execute code within the loop
    user_input = input()
    if user_input.lower().strip() == "exit":
        loop_active = False
        print("Loop exited")
    else:
        print(f"Input: {user_input}")

# Run any desired code after the loop finishes
print("Pretty neat, huh?\n")
print("_" * 100, "\n")

# Another example
# The player's power starts out at 5.
power = 5

# The player is allowed to keep playing as long as their power is over 0.
while power > 0:
    print("You are still playing, because your power is %d." % power)
    # Your game code would go here, which includes challenges that make it
    #   possible to lose power.
    # We can represent that by just taking away from the power.
    power = power - 1

print("\nOh no, your power dropped to 0! Game Over.")