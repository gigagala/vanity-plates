def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# bicho bicho bocho




def is_valid(s):
    
    valid = True
    
    # sigrzis shemocmeba
    if not 2 <= len(s) <= 6:
        valid = False
        
    # unda shedgebodes mxolod asoebisgan da cifrebisgan
    for char in s:
        if not (char.isalpha() or char.isnumeric()):
            valid = False
    
    indicator = False
    # cifrebis shemdeg aso ar sheizleba
    for char in s:
        if char.isnumeric():
            
            if indicator == False and char == '0':
                valid = False
            
            indicator = True
            
            
            
        if indicator == True and char.isalpha():
            valid = False

        
        
    # pirveli ori simbolo unda iyos aso
    for char in s[:2]:
        
        if not char.isalpha():
            valid = False
        
    return valid


main()