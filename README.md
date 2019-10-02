# AlphaZeroHex: Regular & Humanized 
Human players prefer training with human opponents over agents as the latter are distinctively different in level and style than humans. Agents designed for human-agent play are capable of adjusting their level, however their style is not aligned with that of human players. In this work, we implement approach for designing such agents with the game of hex.  

### Us
Modified by Avshalom Tam, Ori Fogler and Shlomo Rabinovich as undergraduates' final project at Bar Ilan University.

### Supervision and Original Paper
TODO

# Theoretical Background

## ResNet
ResNet, short for Residual Networks is a classic neural network used as a backbone for many computer vision tasks. This model was the winner of ImageNet challenge in 2015. The fundamental breakthrough with ResNet was it allowed us to train extremely deep neural networks with 150+layers successfully. Prior to ResNet training very deep neural networks was difficult due to the problem of vanishing gradients.

### Skip Connection
ResNet first introduced the concept of skip connection. We still stack convolution layers but we now also add the original input to the output of the convolution block. This is called skip connection.
It allows the model to learn an identity function which ensures that the higher layer will perform at least as good as the lower layer, and not worse.

## Reinforcement Learning
Reinforcement learning differs from the supervised learning in a way that in supervised learning the training data has the answer key with it so the model is trained with the correct answer itself whereas in reinforcement learning, there is no answer but the reinforcement agent decides what to do to perform the given task.  In the absence of training dataset, it is bound to learn from its experience.

## MCTS
Monte Carlo tree search is a heuristic search algorithm, most notably employed in game play.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
The focus of MCTS is on the analysis of the most promising moves, expanding the search tree based on random sampling of the search space. The application of Monte Carlo tree search in games is based on many playouts also called roll-outs. In each playout, the game is played out to the very end by selecting moves at random. The final game result of each playout is then used to weight the nodes in the game tree so that better nodes are more likely to be chosen in future playouts.

### Exploration & Exploitation Tradeoff
The main difficulty in selecting child nodes is maintaining some balance between the exploitation of deep variants after moves with high average win rate and the exploration of moves with few simulations. A formula for balancing exploitation and exploration in games called UCT.
* In the UCT formula:
  * wi stands for the number of wins for the node considered after the i-th move.
  * ni stands for the number of simulations for the node considered after the i-th move.
  * Ni stands for the total number of simulations after the i-th move ran by the parent node of the one considered.
  * c is the exploration parameter—theoretically equal to √2; in practice usually chosen empirically.
The first component of the formula above corresponds to exploitation; it is high for moves with high average win ratio. The second component corresponds to exploration; it is high for moves with few simulations.

### Creation of MCTS consists four stages:
* Selection  
  * Used for nodes we've seen before.  
  * Pick according to UCT.  
* Expansion  
  * Used when we reach the frontier.  
  * Add one node per playout.  
* Simulation  
  * Used beyond the search frontier.  
  * Don't bother with UCT, just play randomly.  
* Backpropagation  
  * After reaching a terminal node.  

## AlphaZero's Idea
Given enough playouts, UCT will be able to explore all of the important game positions in any game and determine their values using the Monte Carlo Method. But the amount of playouts needed in games like chess, Go, and Gomoku for this to happen is still computationally infeasible, even with UCT prioritization. Thus, most viable MCTS engines for these games end up exploiting a lot of domain-specific knowledge and heuristics.

Instead of memorizing a heuristic value for every game state, we can train a deep neural network to learn heuristic values from “images” of a game board. Adding in a deep neural network gives our models more of the learned “intuition” that human players often leverage.

Along with predicting the value of a given state, AlphaZero also tries to predict a probability distribution on the best moves from a given state (to combat overfitting), using a network with a “policy head” and a “value head”. These two measures cross-validate one another to ensure the network is rarely confident about wrong predictions.

As the deep neural network improves, it makes the MCTS search more efficient, which results in better state valuations to train the deep neural network with – causing a self-reinforcing cycle that can quickly snowball.

# This AlphaZero's Imlementation
TODO

###
`TrainAlphaHexZero.py` contains a script to self-play a specified number of iterations. In each iteration, the AlphaHex agent plays a specified number of games against itself, where it collects randomly 50% of the game data played in the iteration and saves it into a .npz file. It then trains the current best model on this game data for a specified number of epochs, and evaluates the new model against this previous model for a specified number of iterations, where the results are written to a .txt file. If the win rate is over a set threshold, than the new model will become the new current best model to be used in the next iteration of self play.  

###
`Hex.py` contains several functions to play against different players (Self, Random, HexPlayerBryce), where you can specify the number of games and who's player 1, and whether to show the game turn by turn. 

###
`AlphaHex.py` contains the actual agent that utilizes the general AlphaZero algorithm.

###
`hex_zero_model.py` contains the building of the Deep Neural Network used for policy and value prediction.
`sl_bootstrap.py` contains a script to bootstrap the neural network on existing hex data, calling on hex_zero_model to build the neural net before training the neural net for the specified epochs.

# Humanization

### Data
We found lists of ELO ranked players and their games (board size 11X11) at http://www.littlegolem.net/jsp/info/player_list.jsp?gtvar=hex_HEX11&countryid=&filter=&Send=submit.

### Original Representation Example
(;FF[4]EV[hex.mc.2010.oct.1.11]PB[Maciej Celuch]PW[pensando]SZ[13]RE[B]GC[ game #1254910]SO[http://www.littlegolem.com];W[mf];B[gg];W[de];B[df];W[ji];B[if];W[ld];B[jg];W[jf];B[ig];W[kg];B[kc];W[mb];B[ma];W[lb];B[la];W[kb];B[ka];W[jb];B[ja];W[hc];B[hb];W[fd];B[fc];W[ib];B[ia];W[gc];B[gb];W[cd];B[da];W[eb];B[dd];W[ce];B[dc];W[cc];B[db];W[bb];B[le];W[kf];B[ke];W[je];B[il];W[jj];B[kk];W[hk];B[resign])

### Our Representation
TODO

### More Sources
http://hex.kosmanor.com/hex-bin/board/.

###
todo

## Gui
Here you can find a gui that works with the agent - https://github.com/DebuggerOR/hexgui.

## About Us
Modified by Avshalom Tam, Ori Fogler and Shlomo Rabinovich as undergraduates' final project at Bar Ilan University.

## Read & Watch more
* https://nikcheerla.github.io/deeplearningschool/2018/01/01/AlphaZero-Explained/.
* https://www.biostat.wisc.edu/~craven/cs760/lectures/AlphaZero.pdf.
* https://www.youtube.com/watch?v=MgowR4pq3e8&t=492s.
* http://u.cs.biu.ac.il/~sarit/advai2018/MCTS.pdf.
* https://medium.com/oracledevs/lessons-from-implementing-alphazero-7e36e9054191 and more at medium.com.
* https://notes.jasonljin.com/projects/2018/05/20/Training-AlphaZero-To-Play-Hex.html.




