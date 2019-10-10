age = float(input("Write your age: ")) #appearently we do not have to take integer values,only.
if age > 19:
    print("Adult")
else:
    if age >= 10:
        print("Adolescent")
    else:
        if age >= 1:
            print("Child")
        else:
            print("Infant")
            
