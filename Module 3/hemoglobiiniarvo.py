sex = input("Enter biological gender (male/female): ").lower()
hemoglobiini = float(input("Enter hemoglobin value (g/l): "))

if sex == "female" and 117 <= hemoglobiini <= 155:
    print("Your hemoglobin is normal.")
elif sex == "female" and hemoglobiini <= 117:
    print("Your hemoglobin is low.")
elif sex == "female" and hemoglobiini >= 155:
    print("Your hemoglobin is high.")
elif sex == "male" and 134 <= hemoglobiini <= 167:
    print("Your hemoglobin is normal.")
elif sex == "male" and hemoglobiini < 134:
    print("Your hemoglobin is low.")
elif sex == "male" and hemoglobiini > 167:
    print("Your hemoglobin is high.")
else:
    print("Invalid gender.")