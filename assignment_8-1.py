def convert_grade():
    print("What grade did you get?")
    grade_percentage = float(input())
    if grade_percentage >= 95:
        return "Congrats! you got a A+"
    elif grade_percentage >= 92 and grade_percentage < 95:
        return "Congrats! you got a A"
    elif grade_percentage >= 89 and grade_percentage < 92:
        return "Congrats! you got a A-"
    elif grade_percentage >= 87 and grade_percentage < 89:
        return "Congrats! you got a B+"
    elif grade_percentage >= 84 and grade_percentage < 87:
        return "Congrats! you got a B"
    elif grade_percentage >= 81 and grade_percentage < 84:
        return "Congrats! you got a B-"
    elif grade_percentage >= 77 and grade_percentage < 81:
        return "You got a C+, it's ok, try a little harder next time :)"
    elif grade_percentage >= 74 and grade_percentage < 77:
        return "You got a C, it's ok, try a little harder next time :)"
    elif grade_percentage >= 70 and grade_percentage < 74:
        return "You got a C-, it's ok, try a little harder next time :)"
    elif grade_percentage >= 60 and grade_percentage < 70:
        return "You got a D, I think you need to study a lot harder next time"
    elif grade_percentage < 60:
        return "See me after class :("

print(convert_grade())