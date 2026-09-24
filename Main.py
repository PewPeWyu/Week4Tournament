#############################################
# Name: alyana
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################


print("What is the first team name?")
team1 = input()
print("How many wins did they get?")
wins1 = int(input())
print("how many ties did they get?")
ties1 = int(input())
team1_points = (wins1*2) + (ties1*1)

print("What is the second team's name?")
team2 = input()
print("How many wins did they get?")
wins2 = int(input())
print("how many ties did they get?")
ties2 = int(input())
team2_points = (wins2*2) + (ties2*1)

print("What is the third team's name?")
team3 = input()
print("How many wins did they get?")
wins3 = int(input())
print("how many ties did they get?")
ties3 = int(input())
team3_points = (wins3*2) + (ties3*1)

print("What is the fourth team's name?")
team4 = input()
print("How many wins did they get?")
wins4 = int(input())
print("how many ties did they get?")
ties4 = int(input())
team4_points = (wins4*2) + (ties4*1)

print("What is the fifth team's name?")
team5 = input()
print("How many wins did they get?")
wins5 = int(input())
print("how many ties did they get?")
ties5 = int(input())
team5_points = (wins5*2) + (ties5*1)

print("What is the sixth team's name?")
team6 = input()
print("How many wins did they get?")
wins6 = int(input())
print("how many ties did they get?")
ties6 = int(input())
team6_points = (wins6*2) + (ties6*1)

print("scoreboard")
print("",team1,"points: " , team1_points)
print("",team2,"points: " , team2_points)
print("",team3,"points: " , team3_points)
print("",team4,"points: " , team4_points)
print("",team5,"points: " , team5_points)
print("",team6,"points: " , team6_points)


if team1_points > team2_points and team1_points > team3_points and team1_points > team4_points and team1_points > team5_points and team1_points > team6_points:
    print(team1, "is the winner")
elif team2_points > team1_points and team2_points > team3_points and team2_points > team4_points and team2_points > team5_points and team2_points > team6_points:
    print(team2, " is the winner")
elif team3_points > team1_points and team3_points > team2_points and team3_points > team4_points and team3_points > team5_points and team3_points > team6_points:
    print(team3, "is the winner")
elif team4_points > team1_points and team4_points > team2_points and team4_points > team3_points and team4_points > team5_points and team4_points > team6_points:
    print(team4, "is the winner")
elif team5_points > team1_points and team5_points > team2_points and team5_points > team3_points and team5_points > team4_points and team5_points > team6_points:
    print(team5, "is the winner")
elif team6_points > team1_points and team6_points > team2_points and team6_points > team3_points and team6_points > team4_points and team6_points > team5_points:
    print(team6, "is the winner")

