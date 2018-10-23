player_data={"chelsea":"hazard","juventus":"ronaldo", "barcelona":"messi"}
user_team = input("enter your team's name:")

if user_team in  player_data.keys():
    player_name= player_data.get(user_team)
    print("most important player of",user_team," is :",player_name)
else:
    print("Enter from the given teams: ")
    for key in player_data.keys():
        print(key)

