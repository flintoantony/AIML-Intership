print("SMART DECISION SYSTEM ")


# MODULE 1: LIE DETECTOR
print("\n Module 1: Lie Detector ")

age = input("Enter your age: ")
birth_year = input("Enter your birth year: ")

if age.isdigit() and birth_year.isdigit():
    age = int(age)
    birth_year = int(birth_year)

    current_year = 2026
    calculated_age = current_year - birth_year

    if age == calculated_age:
        print(" Your data is consistent.")
    else:
        if age > calculated_age:
            print(" You might be lying about your age.")
        else:
            print(" Your birth year seems incorrect.")
else:
    print(" Invalid input! Age and birth year must be numbers.")

# MODULE 2: PERSONALITY TEST
print("\n Module 2: Personality Test ")

score = 0

q1 = input("Do you like socializing? (yes/no): ")
q2 = input("Do you enjoy solving problems? (yes/no): ")
q3 = input("Do you prefer planning over spontaneity? (yes/no): ")

if q1 == "yes":
    score += 2
else:
    score += 0

if q2 == "yes":
    score += 2
else:
    score += 0

if q3 == "yes":
    score += 1
else:
    score += 2

# Nested conditions
if score >= 5:
    if score == 6:
        print(" You are highly analytical and social!")
    else:
        print(" You are balanced and thoughtful.")
elif score >= 3:
    print(" You are practical and adaptable.")
else:
    print(" You are creative and spontaneous.")

# MODULE 3: RULE ENGINE 
print("\n Module 3: Rule Engine ")

income = input("Enter your monthly income: ")
credit_score = input("Enter your credit score: ")

if income.isdigit() and credit_score.isdigit():
    income = int(income)
    credit_score = int(credit_score)

    if income > 50000 and credit_score > 700:
        print(" Loan Approved")
    elif income > 30000 and credit_score > 650:
        print(" Loan Approved with Conditions")
    elif income > 20000:
        if credit_score > 600:
            print(" High Risk Approval")
        else:
            print(" Rejected due to low credit score")
    else:
        print(" Loan Rejected (Low Income)")
else:
    print(" Invalid input! Enter numeric values.")

# MODULE 4: DATA VALIDATION
print("\n Module 4: Data Validation ")

email = input("Enter your email: ")
password = input("Enter your password: ")

if "@" in email and "." in email:
    if len(password) >= 6:
        if len(password) >= 10:
            print(" Strong password and valid email")
        else:
            print(" Valid email but weak password")
    else:
        print(" Password too short")
else:
    print(" Invalid email format")


# MODULE 5: SIMULATION 
print("\n Module 5: Survival Simulation ")

health = 100
hunger = 0

while health > 0:
    print("\nHealth:", health, "| Hunger:", hunger)

    action = input("Choose action (eat/work/rest): ")

    if action == "eat":
        if hunger > 0:
            hunger -= 10
            print(" You ate food.")
        else:
            print(" You are not hungry.")
    elif action == "work":
        hunger += 15
        health -= 10
        print(" You worked hard.")
    elif action == "rest":
        health += 5
        hunger += 5
        print(" You rested.")
    else:
        print(" Invalid action.")

    # Conditions affecting health
    if hunger > 50:
        health -= 15
        print(" Too hungry! Health decreasing.")

    if hunger < 0:
        hunger = 0

    if health > 100:
        health = 100

    if health <= 0:
        print(" Game Over! You lost all health.")

print("\n END ")
