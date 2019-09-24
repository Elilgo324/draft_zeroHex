# AlphaZeroHex Regular & Humanized 

### TODO
describe more and better.

## Data
Lists of ELO ranked players and their games (size 11X11).
http://www.littlegolem.net/jsp/info/player_list.jsp?gtvar=hex_HEX11&countryid=&filter=&Send=submit.

### Original representation
(;FF[4]EV[hex.mc.2010.oct.1.11]PB[Maciej Celuch]PW[pensando]SZ[13]RE[B]GC[ game #1254910]SO[http://www.littlegolem.com];W[mf];B[gg];W[de];B[df];W[ji];B[if];W[ld];B[jg];W[jf];B[ig];W[kg];B[kc];W[mb];B[ma];W[lb];B[la];W[kb];B[ka];W[jb];B[ja];W[hc];B[hb];W[fd];B[fc];W[ib];B[ia];W[gc];B[gb];W[cd];B[da];W[eb];B[dd];W[ce];B[dc];W[cc];B[db];W[bb];B[le];W[kf];B[ke];W[je];B[il];W[jj];B[kk];W[hk];B[resign])


## Training the neural network
`hex_zero_model.py` contains the building of the Deep Neural Network used for policy and value prediction.
`sl_bootstrap.py` contains a script to bootstrap the neural network on existing hex data, calling on hex_zero_model to build the neural net before training the neural net for the specified epochs.

### Instructions
`python3 sl_bootstrap.py`

## Evaluating against various players
`Hex.py` contains several functions to play against different players (Self, Random, HexPlayerBryce), where you can specify the number of games and who's player 1, and whether to show the game turn by turn. 

### Instructions
`python3 Hex.py`

## AlphaHex Agent
`AlphaHex.py` contains the actual agent that utilizes the general AlphaZero algorithm. 

## Self-Play & Reinforcement Learning
`TrainAlphaHexZero.py` contains a script to self-play a specified number of iterations. In each iteration, the AlphaHex agent plays a specified number of games against itself, where it collects randomly 50% of the game data played in the iteration and saves it into a .npz file. It then trains the current best model on this game data for a specified number of epochs, and evaluates the new model against this previous model for a specified number of iterations, where the results are written to a .txt file. If the win rate is over a set threshold, than the new model will become the new current best model to be used in the next iteration of self play.  

### Instructions
`python3 TrainAlphaHexZero.py`

## Us:
Modified by Avshalom Tam, Ori Fogler and Shlomo Rabinovich as undergraduates' final project at BIU.

## Read & Watch more:
https://notes.jasonljin.com/projects/2018/05/20/Training-AlphaZero-To-Play-Hex.html:.

https://www.youtube.com/watch?v=MgowR4pq3e8&t=492s.


