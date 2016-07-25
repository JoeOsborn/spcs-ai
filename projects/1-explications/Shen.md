Comparison between Deep Blue and AlphaGo
========
Deep Blue is the chess playing AI developed in the mid 1990 by IBM. It had two versions, Deep Blue I and Deep Blue II(DB), in witch Deep Blue II has stronger chips and better algorisms that it beat all human players. The speed of the AI has linear positive correlation with the calculation speed of the chips, however, good algorisms could could increase the efficiency exponentially. The makers of DB did make good algorisms such as Hybrid software/hardware search and Massively parallel search \[1\], but these algorisms are totally *knowledge-based techniques* that DB can’t grow stronger as it plays more games. 

AlphaGo(AG) is a go AI developed by Google. Go was such very complex game: the number of possible boards for chess is 10^47, and for go is 10^171. For both AG and DB beat the very top human players, people should expect AG with much more and stronger chips thank DB, but in fact, AG (in the match) has about the same calculation power as DB. This is mainly because of the different type of algorism AG uses. AG uses a combination of tree search techniques and machine learning \[2\], which is *statistic-based technique*. In this way it studies from previous matches played by people and the matches it played with itself. It is notable that AG has 176 GPUs: the major innovation by AG is that it analysis the graphic of the games and find the most possible step a professional player would play next and do calculations on those steps. This largely reduced the total calculation, and could only realized by machine learning. 

As a conclusion, I believe the future of AI would use more statistic-based technique. Let’s take an extreme example: if people try to build a human-like AI, it is impossible to pre-code every situation it could face, but give it the capability to learn everything based on some algorisms (maybe quantum physics based chips are need for that).

Reference:

\[1\] Murray Campbell, A. Joseph Hoane Jr., Feng-hsiung Hsu, Deep Blue, Artificial Intelligence 134 (2002) 57–83 [link](http://ac.els-cdn.com/S0004370201001291/1-s2.0-S0004370201001291-main.pdf?_tid=3e0d7242-4875-11e6-9aeb-00000aacb361&acdnat=1468358087_0d298efddcf6f972b6c181c24ad96491)

\[2\] David Silver etc., Mastering the game of Go with deep neural networks and tree search, Nature. Retrieved 27 January 2016  [link](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html)

PS: I don't know why markdown didn't run in this file but on notebook format so I get a copy on notebook.