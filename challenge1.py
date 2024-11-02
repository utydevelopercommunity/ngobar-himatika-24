import random

# prepare for the answer
answer = random.randint(1, 50)

# prepare for the chance
chance = 5

while chance > 0:
    print("Kesempatan tersisa: ", chance)

    user_input = int(input("Masukkan jawaban anda: "))

    if user_input == answer:
        print("Jawaban anda benar!")
        break;
    elif user_input < answer:
        print("Jawaban anda terlalu kecil")
    elif user_input > answer:
        print("Jawaban anda terlalu besar")
        
    chance -= 1
    if chance == 0:
        print("Kesempatan anda telah habis. Jawabannya adalah", answer)
    




