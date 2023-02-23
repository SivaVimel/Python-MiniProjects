import random

print("Welcome to Rock vs Paper vs Scissors \nRockVSPaper -> Paper \nPaperVSScissor -> Scissor \nScissorVSRock -> Rock")
while True:
    print("\nEnter : \n1 - Rock \n2 - Paper \n3 - Scissor")
    ans=int(input("Enter the number : "))
    comp = random.randint(1,3)
    if ans == comp:
        print("Draw")
    if ans == 1 and comp == 2:
        print(f'You Choose {ans} and Computer Choose {comp}')
        print(f"{comp} : Computer is the winner")
    if ans == 2 and comp == 3:
        print(f'You Choose {ans} and Computer Choose {comp}')
        print(f"{comp} : Computer is the winner")
    if ans == 3 and comp == 1:
        print(f'You Choose {ans} and Computer Choose {comp}')
        print(f"{comp} : Computer is the winner")
    if comp == 1 and ans == 2:
        print(f'You Choose {ans} and Computer Choose {comp}')
        print(f"{ans} : You are the winner")
    if comp == 2 and ans == 3:
        print(f'You Choose {ans} and Computer Choose {comp}')
        print(f"{ans} : You are the winner")
    if comp == 3 and ans == 1:
        print(f'You Choose {ans} and Computer Choose {comp}')
        print(f"{ans} : You are the winner")
    print("\nDo you want to continue ? \nYes or No")
    ans = input().lower()
    if ans=="no":
        break
print("\nThanks for playing ^.^")
        