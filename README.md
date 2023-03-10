# snooker-frame-calculator

The purpose of this application is to calculate the scores of both players, based on the number of balls potted each player, and any fouls rewarded during a frame. Afterwards, the program determines the final score of the frame, the winner, and the difference of both players’ scores.

I used Python 3 to write the program, making it user-input based, so the program can ask how many balls were potted, and if there were any points rewarded because of fouls. The challenges I faced was figuring out a systematic approach to calculating the scores of both players. I settled on dividing the frame into two phases, the first phase with potting reds and colours, and the last phase with the remaining colours on the table. Each player’s score is made of three parts: the score during the first phase, the score during the last phase, and any points rewards due to fouls. For the two scenarios, where Player 1 or Player 2 wins the frame, I used if-then statements. If the user made a mistake during the input process, the user must restart the program again.

Please read LICENSE for more information.
