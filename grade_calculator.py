marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Enter valid marks")
elif marks >= 91:
    print("Grade: AA")
elif marks >= 81:
    print("Grade: AB")
elif marks >= 71:
    print("Grade: BB")
elif marks >= 61:
    print("Grade: BC")
elif marks >= 51:
    print("Grade: CC")
elif marks >= 41:
    print("Grade: CD")
elif marks >= 31:
    print("Grade: DD")
else:
    print("Grade: FF")
