Check any credit card number to test if it is Valid or Invalid.

Luhn's Algorithm:
  1. Take every alternate digit of card number starting from penultimate position
  2. Multiply each one of these digits by 2
  3. Calculate sum of all indivisual digits after multiplication
  4. Calculate sum of every other remaining digit of card number (i.e. every alternate digit starting from last position)
  5. Add the sum values from step_3 and step_4
  6. If the number obtained from step_5 is divisible by 10, then the entered card number is VALID otherwise INVALID
