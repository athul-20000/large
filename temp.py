def faranheit_to_celcious(faranheit):
    return (faranheit-32)*5/9
def celcious_to_faranheit(celcious):
    return(celcious*9/5)+32
def celcious_to_kelvin(celcious):
    return(celcious+273)

print("\nTemperature conversion menu")
print("1.faranheit to celcious")
print("2.celcious to faranheit")
print("3.celcious to kelvin")
print("4.Exit")
choice= int (input("Enter your choice(1/2/3/4):"))
if choice==1:
    faranheit=float(input("Enter the temperature in faranheit:"))
    celcious=faranheit_to_celcious(faranheit)
    print(f"{faranheit}degree F is equal to{celcious:.2f} degree C")
elif choice==2:
    celcious=float(input("Enter the temperature in celcious:"))
    faranheit=celcious_to_faranheit(celcious)
    print(f"{celcious}degree C is equal to{faranheit:.2f} degree F")
elif choice==3:
    celcious=float(input("Enter the temperature in celcious:"))
    kelvin=celcious_to_kelvin(celcious)
    print(f"{celcious}degree C is equal to{kelvin:.2f} degree F")
elif choice==4:
       print("Exiting the program ,Goodbye")

else:
     print("Invalid choice,please try again")
