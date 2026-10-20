This is a readme file for a quick intro inside the code and idea behind it

A small Python project that turns a chess position into a heatmap showing which side controls each square.

The idea
For each of the 64 squares: (standard chess board)

net control = (White attackers - Black attackers) x centre weight(this formula is indeed a important one)

- Red means White controls the square more, blue means Black does, and zero means balanced or untouched.
- Squares near the centre get a larger weight (1.0 on the edges, up to 1.5 on d4, e4, d5 and e5).
- All four heatmaps share one colour scale (-6 to +6), so they can be compared fairly.

You can think of the pieces as sources of a field on an 8x8 lattice. Each piece contributes to the squares it attacks, White positive and Black negative, and the contributions simply add up (superposition). The two squares ringed below are attacked once by each side, so they cancel to 0.0.

These are the positions i tested this python on

Position | White total | Black total | What stands out |
| Najdorf Sicilian | 55.5 | 42.5 | The strongest squares, e2 (+5.5) and d7 (-5.5), are each covered by five of one side's own pieces |
| Starting position | 41.6 | 41.6 | Exact mirror image; ranks 4 and 5 are zero |
| Opera Game (before 16.Qb8+) | 42.3 | 31.4 | b8 reads 0.0 even though White wins by force |
| Bare endgame | 13.7 | 11.3 | Only kings and pawns, so only a few squares light up |

The result i learned
**A sanity check passes.** A mirror-image position should give a mirror-image map, and the starting position does (41.6 against 41.6).
 **The map measures coverage, not advantage.** A square defended five times looks like a stronghold even if no enemy piece is nearby, because a side's own defenders count as control.
**Counting attackers cannot see tactics.** In Morphy's Opera Game, White wins with 16.Qb8+ Nxb8 17.Rd8#, yet b8 scores 0.0: White's queen and Black's knight each attack it once.

 I tested it on Paul Morphy’s famous 1858 Opera Game. White wins with a forced Queen sacrifice on b8. However, my static model evaluated the b8 square as a perfectly balanced 0.0. It proved exactly what a good unit test should: a static scalar field measures potential coverage, but it is blind to dynamic time evolution and tactical x-rays.

 
 

Well ofcourse there are limitations its not a new model or anything it just a computational based type model i tested on standard 8x8 chess board

 Every attacker counts the same, so a pawn and a queen contribute equally.
 One position gives one map, so there is no notion of what happens next.
 The centre weights are hand-picked, not fitted to data.
 Four positions are an illustration, not a sample, so no statistical conclusion can be drawn yet.

 THERE CAN BE MORE LIMITATIONS So if you wish to point out it would be a great help

What's next with this?
 We can Compare the maps with an engine evaluation on many real games (for example from the Lichess database) to train our own database but that is alot work I aint doing that
 Why i Code this anyways?

As a physics major 3rd sem there is a topic of thermal energy potential , Proffessor told everything radiate energy and i love chess (not that i am good at it but yes i love chess) I chess is also kinda similar at center you have more move set than at edges i thought aint that a similar concept i then googled found a concept of heatmap i then searched library in python found 2 new interesting ones 
import chess    
import seaborn as sns 

Well if you like this idea or suggest changes queries feel free to ask I will be posting this on github and linkdin 
bye!
