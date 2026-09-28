   # SAID MAMMADRZAYEV 

# ---------- 1. Grading System (if-elif-else) ----------
marks = float(input("Enter your exam marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")


# ---------- 2. Multiplication Table (for loop) ----------
number = int(input("\nEnter a number: "))  # \n  arada bir sətir buraxsın deyə yazmışam

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# ---------- 3. Password Retry System (while loop) ----------
correct_password = "python123"
attempts = 0

while True:
    password = input("\nEnter the password: ")
    attempts += 1

    if password == correct_password:
        print("Access granted! ✅ ")
        break

    print(f"Wrong password ❌. {3 - attempts} attempts left.")

    if attempts == 3:
        print("Too many attempts. Access denied.")
        break
