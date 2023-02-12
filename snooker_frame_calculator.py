print("Welcome to the Snooker Frame Calculator. This program calculates the total scores of two snooker players playing in a frame.")
print("The winner will be revealed, after the program calculates the points earned in the first and last phase of the frame, as well as any points rewarded due to your opponent's fouls.")
print("In a frame of Snooker, there are two phases: The first phase involving potting reds and the colours. The last phase involving potting the remaining colours.")

#Value of each ball:
#red_ball = 1
#yellow_ball = 2
#green_ball = 3
#brown_ball = 4
#blue_ball = 5
#pink_ball = 6
#black_ball = 7

#Value of points rewarded by oppenent's foul:
#four_point_foul = 4
#five_point_foul = 5
#six_point_foul = 6
#seven_point_foul = 7

#Version 1 without input value (must fill in how many balls potted by replace the zeros, before running the program)
#player_1_frame_points = (red_ball * 0) + (yellow_ball * 0) + (green_ball * 0) + (brown_ball * 0) + (blue_ball * 0) + (pink_ball * 0) + (black_ball * 0)
#player_1_rewarded_points = (four_point_foul * 0) + (five_point_foul * 0) + (six_point_foul * 0) + (seven_point_foul * 0)
#player_1_total_score = player_1_frame_points + player_1_rewarded_points

#player_2_frame_points = (red_ball * 0) + (yellow_ball * 0) + (green_ball * 0) + (brown_ball * 0) + (blue_ball * 0) + (pink_ball * 0) + (black_ball * 0)
#player_2_rewarded_points = (four_point_foul * 0) + (five_point_foul * 0) + (six_point_foul * 0) + (seven_point_foul * 0)
#player_2_total_score = player_2_frame_points + player_2_rewarded_points

#if player_1_total_score > player_2_total_score:
    #print("Player 1 wins the frame by " + str(player_1_total_score - player_2_total_score) + " points!")
#if player_2_total_score > player_1_total_score:
    #print("Player 2 wins the frame by " + str(player_2_total_score - player_1_total_score) + " points!")

#Version 2 with input values
print("For the first phase of the frame, please input the number of reds and colours Player 1 potted.")
player_1_first_phase_points = (int(input("How many red balls Player 1 potted in first phase of the frame?:")) * 1) + (int(input("How many yellow balls Player 1 potted in first phase of the frame?:")) * 2) + (int(input("How many green balls Player 1 potted in the first phase of the frame?:")) * 3) + (int(input("How many brown balls Player 1 potted in the first phase of the frame?:")) * 4) + (int(input("How many blue balls Player 1 potted in the first phase of the frame?:")) * 5) + (int(input("How mnay pink balls Player 1 potted in the first phase of the frame?:")) * 6) + (int(input("How many black balls Player 1 potted in the first phase of the frame?:")) * 7)
print("For the last phase of the frame, once a colour is potted, it is not put back on the table. Please input either 0 or 1, for each remaining colour potted by Player 1.")
player_1_last_phase_points = (int(input("How many yellow balls Player 1 potted in the last phase of the frame?:")) * 2) + (int(input("How many green balls Player 1 potted in the last phase of the frame?:")) * 3) + (int(input("How many brown balls Player 1 potted in the last phase of the frame?:")) * 4) + (int(input("How many blue balls Player 1 potted in the last phase of the frame?:")) * 5) + (int(input("How mnay pink balls Player 1 potted in the last phase of the frame?:")) * 6) + (int(input("How many black balls Player 1 potted in the last phase of the frame?:")) * 7)
print("Please input the number of fouls made by Player 2 in the frame.")
player_1_rewarded_points = (int(input("How many four point fouls rewarded to Player 1 in the frame?:")) * 4 ) + (int(input("How many five point fouls rewarded to Player 1 in the frame?:")) * 5) + (int(input("How mnay six point fouls rewarded to Player 1 in the frame?:")) * 6) + (int(input("How many seven point fouls rewarded to Player 1 in the frame?:")) * 7)
player_1_total_score = player_1_first_phase_points + player_1_last_phase_points + player_1_rewarded_points

print("For the first phase of the frame, please input the number of reds and colours Player 2 potted.")
player_2_first_phase_points = (int(input("How many red balls Player 2 potted in first phase of the frame?:")) * 1) + (int(input("How many yellow balls Player 2 potted in first phase of the frame?:")) * 2) + (int(input("How many green balls Player 2 potted in the first phase of the frame?:")) * 3) + (int(input("How many brown balls Player 2 potted in the first phase of the frame?:")) * 4) + (int(input("How many blue balls Player 2 potted in the first phase of the frame?:")) * 5) + (int(input("How mnay pink balls Player 2 potted in the first phase of the frame?:")) * 6) + (int(input("How many black balls Player 2 potted in the first phase of the frame?:")) * 7)
print("For the last phase of the frame, once a colour is potted, it is not put back on the table. Please input either 0 or 1, for each remaining colour potted by Player 2.")
player_2_last_phase_points = (int(input("How many yellow balls Player 2 potted in the last phase of the frame?:")) * 2) + (int(input("How many green balls Player 2 potted in the last phase of the frame?:")) * 3) + (int(input("How many brown balls Player 2 potted in the last phase of the frame?:")) * 4) + (int(input("How many blue balls Player 2 potted in the last phase of the frame?:")) * 5) + (int(input("How mnay pink balls Player 2 potted in the last phase of the frame?:")) * 6) + (int(input("How many black balls Player 2 potted in the last phase of the frame?:")) * 7)
print("Please input the number of fouls made by Player 1 in the frame.")
player_2_rewarded_points = (int(input("How many four point fouls rewarded to Player 2 in the frame?:")) * 4 ) + (int(input("How many five point fouls rewarded to Player 2 in the frame?:")) * 5) + (int(input("How mnay six point fouls rewarded to Player 2 in the frame?:")) * 6) + (int(input("How many seven point fouls rewarded to Player 2 in the frame?:")) * 7)
player_2_total_score = player_2_first_phase_points + player_2_last_phase_points + player_2_rewarded_points

if player_1_total_score > player_2_total_score:
    print("Final score of the frame: " + str(player_1_total_score) + " - " + str(player_2_total_score) + ":" + " Player 1 wins the frame by " + str(player_1_total_score - player_2_total_score) + " points!")
if player_2_total_score > player_1_total_score:
    print("Final score of the frame: " + str(player_1_total_score) + " - " + str(player_2_total_score) + ":" + " Player 2 wins the frame by " + str(player_2_total_score - player_1_total_score) + " points!")