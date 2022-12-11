n=int(input()) # total num of order
for i in range(n):
    eater_id=int(input())
    foodmenu_id=input()
    if(foodmenu_id>1):
        foodmenu_id+=1
    print(foodmenu_id)


