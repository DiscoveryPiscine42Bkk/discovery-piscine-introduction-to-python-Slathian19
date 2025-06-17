for multiplier in range(11):  # 0 ถึง 10 รวม 11 ตัว
    print(f"Table de {multiplier}:", end=" ")

   
    for number in range(11):
        print(f"{multiplier * number}", end=" " if number < 10 else "")

    
    print()