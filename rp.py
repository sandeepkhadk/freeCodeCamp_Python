full_dot = '●'
empty_dot = '○'
def create_character(name,strength,intelligence,charisma):
    if not isinstance(name,str):
        return "The character name should be a string"
    if len(name)>10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if not all(isinstance(x,int)for x in (strength,intelligence,charisma)):
        return "All stats should be integers"
    if any (x<1 for x in (strength,intelligence,charisma)):
        return "All stats should be no less than 1"
    if any(x>4 for x in (strength,intelligence,charisma)):
        return "All stats should be no more than 4"
    sum=strength+intelligence+charisma
    if sum !=7 :
        return "The character should start with 7 points"
    return(
    f"{name}\n"
    f"STR {full_dot * strength}{empty_dot * (10 - strength)}\n"
    f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\n"
    f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}\n"
   
   )
print(create_character("ren", 4, 2, 1))   
