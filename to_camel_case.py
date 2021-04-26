#Complete the method/function so that it converts dash/underscore
#delimited words into camel casing. The first word within the output
#should be capitalized only if the original word was capitalized (known as
#Upper Camel Case, also often referred to as Pascal case).


def to_camel_case(text):
    #your code here
    new_string = ""

    if text =="":
        return ""
    if "-" in text or "_":
        new_string = text.replace("-"," ").replace("_"," ").title().replace(" ","")
        return text[0] + new_string[1:]
        

print(to_camel_case("the_stealth_warrior")) #should print theStealthWarrior
print(to_camel_case("The-Stealth-Warrior")) #should print TheStealthWarrior
print(to_camel_case(''))    #should print 
print(to_camel_case("A-B-C")) #should print ABC
