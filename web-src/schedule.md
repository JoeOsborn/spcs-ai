---
title: Schedule
author: Joseph C. Osborn
bibliography: bibliography.bib
---

This document is intended for use by the instructor and TAs, since we don't want to commit to a firm schedule or show the readings/assignments too far in advance (it might be confusing).

* Day 1: What is AI?
    * Reading
        ~ Before doing today's assignment, students should read the excerpts from Philip Agre's "Computation and Human Experience" as well as the D.\ Fox Harrell paper in the reader.
    * Topic 1: What is AI?
        ~ Hi, who am I?
        ~ Introduction to main threads of AI research. What is and is not AI. Historical and present uses of the term. AI winter. Sidestepping "what is 'intelligence'"? Creative and commercial uses of AI. Generative methods. Modern AI as a set of techniques, rather than an attempt to simulate the brain. "Getting good results" vs "learning/claiming something about cognition".
        ~ (If possible, include some Game AI, some mixed initiative stuff (Tanagra), some of my research area here.)
        * Knowledge based
            * Grammars, logical systems, argumentation, social simulations, explicit representation of knowledge...
            * Expense, fragility, rhetorical purpose, ...
        * Statistical
            * Genetic algorithms/programming, neural nets, machine learning ...
            * Choice of loss function, metrics, overfitting, "money laundering for bias" ...
    * Exercise
        ~ Identify three "AI" systems.
        For each one, discuss and decide whether it is mainly knowledge-based or mainly statistical/machine-learning-based.
    * Topic 2: Critical Technical Practice \& the Ethics of AI
        ~ Explanation of Agre's and Harrell's work. Examples from recent high-profile AI incidents including Microsoft's "Tay" chatbot, noise-based attacks on Google's image classifiers, MaxMind's IP mapping, Facebook's algorithmic feed emotion manipulation research, automated sentencing/parole...
    * Topic 3: IPython. How to submit assignments. Q\&A.
    * What worked:
        * AI and ethics examples, group activity, pretty much every active learning segment got some response except "name some AI techniques", ethics material.
    * What didn't work:
        * Arriving late (ugh), rushing through critical technical practice material.
    * What to change for next time:
        * More active learning and student-driven exampling, less lecture, shorter reading addressed across more days.
    * Assignment 1
        ~ Individual (short) assignment.

        Pick an AI system, describe it briefly, and explain its "perspective." Who wrote
        this system and for what purpose? Who uses the system---are their goals aligned
        with those of the system authors? From a knowledge representation standpoint,
        how does it view the world? Which concepts are central, and which concepts are
        peripheral? How does this system interact with humans, and what does it know or
        assume about the humans who use it? How could a hostile user or third party
        subvert this system and break it or harrass/injure other users? Consult the
        documentation of this system, or articles written about it, if necessary. Write
        at least 300 words.

        *TAs could help students think of or explicate AI systems and draw out answers to these questions. Enterprising students could write more, engaging with the subject more deeply; or compare two or more different AI approaches to the same problem, with respect to the criteria above.*
    * Assignment 2
        ~ Individual (short) assignment.

        Submit an IPython notebook with a Markdown cell briefly introducing yourself: your background in programming and/or AI, what you hope to gain from this course, and your favorite hobby or hobbies outside of programming (and even outside of computing).

        Also include a Python cell which prints out your name using the `print()` function.
* Day 2: Python, data structures, and algorithms
    * Topic 1: Building and processing interesting data structures
        * Get students to do the typing as much as possible
        * Python basics
            * Print each number between 1 and 10
                * for x in range
            * Functions with ordered and keyword arguments
            * Draw an image in IPython
            * Random numbers
        * Tuples, arrays, dicts
            * reverse a list, animal sounds
            * plot a graph in IPython
            * For x in y
        * Classes
            * define and use custom objects
            * animal sounds 2---but don't worry about inheritance for now, just polymorphism and info hiding
        * Iterative functions (and stacks/queues/pointers)
        * Recursive functions (and accumulators)
    * Topic 2: State machines and string recognizers
        * CS theory basics
        * Languages, intersection and union
        * Finite (word) automata
        * Deterministic vs nondeterministic
        * Extensions (symbolic FA, pushdown automata, counter automata, timed automata)
        * "Inspired by" (behavior trees, ...)
    * Exercise:
        * Pair up
        * Pick an agent from your experience (video game character, routine worker, animal, robot, ...) and write out (possibly repetitive) sequences of actions they might perform (it's okay to indicate cycles or similar with "..." or what-have-you) OR pick a string language and enumerate examples
        * What are the "letters"---basic actions---and what are the states?
        * Draw a state machine that captures that language of actions
    * Topic 3: Graph traversal
        * (Quick: state machine implementation strategies)
        * Basic graph theory (trees)
        * Depth-first vs breadth-first
            * Ask for pseudocode (recursive AND iterative)
        * Directed graphs, DAGs, and general graphs
        * Complications for depth- and breadth-first in presence of cycles
            * Ask for pseudocode (recursive AND iterative)
    * What worked:
        * State machine exercise. Many students knew Python already so that material was successful.
    * What didn't work:
        * Rushing through tree/graph material, not having a 100% prepared set of examples for Python learning.
    * What to change for next time:
        * More active learning and student-driven exampling, a little less state machine theory material (save it for a subsequent day) and a little more tree/graph material, maybe even before the state machines.
    * Assignment
        ~ Individual (short) assignment.
        Write two state machine evaluators for deterministic finite word automata: one which takes a state machine representing a language along with a string, and checks whether the machine accepts the string; and another which takes such a state machine and generates strings from it.

        *We'll provide the state machine data structures. Students with extra time could write a regular expression parser, or write functions to take the intersection or union of two languages, or visualize the evaluation steps using e.g.\ `pillow`.*
* Day 3: Search and Planning
    * Reading
        * Red Blob Games' [A* tutorial](http://www.redblobgames.com/pathfinding/a-star/introduction.html)
        * Excerpts from Sutton \& Barto's reinforcement learning book [-@sutton1998reinforcement] (available [here](https://webdocs.cs.ualberta.ca/~sutton/book/ebook/the-book.html)):
            * Sections 1.1--1.5
            * Section 2.1
            * Sections 3.1--3.3 (and as much of chapter 3 as you have time for)
        * At least section 3 ("MONTE CARLO TREE SEARCH") of Cameron Browne et al's [survey of MCTS methods](http://repository.essex.ac.uk/4117/1/MCTS-Survey.pdf)
    * Topic 1: Posing problems as graph search. Example: PuzzleGraph. Heuristic search (A*). Exploit/explore. Discrete constraint problems too (n-queens). Graph vs grid representations of space.
        * Recommend following the links from RedBlobGames' tutorial as well.
    * Exercise:
        Pair up. Pick an interesting problem and try to phrase it as "search" or planning. What are the operators at a given state? What are reward values at the end? Do operators have costs? Etc. Candidates include: transforming mathematical formulae, solving some logic puzzle, graph coloring, cooking...
    * Topic 2: MCTS, expected value, and backpropagation of reward
        * How do I calculate expected value?
        * Tree policy: How do I pick action? uniform random, weighted random, random among untried possibilities, ... balancing exploit/explore
        * Default policy: How do I pick action? Want to explore as much as possible?
        * Backpropagation: max, decay, ...
    * Topic 3: Reinforcement learning: the problem, the basic idea, how it differs from MCTS (MCTS is a special case)
        * "MCTS estimates temporary state values in order to decide the next move, whereas TDL learns the long-term value of each state that then guides future behaviour"---mcts guesses more
    * What worked:
        * Graph search, A* material, MCTS explanation, small-group activity
    * What didn't work:
        * RL material wasn't prepared thoroughly enough
        * Maze should have been an immutable value object!
    * What to change:
        * Needed more active learning opportunities, more specific RL material, too many different topics in one day (nobody had time to do enough reading).
    * Assignment
        ~ Individual or pair (long) assignment. (1) should be done by tomorrow, (2) and (3) by Monday.
        (1) Write a Python program to solve switch and door puzzles with one of the heuristic search algorithms
        described during the lecture. *(We'll provide a Puzzle class and sample puzzles, and maybe a function to draw puzzles or solution paths to the console or an image?)* Try it on the provided sample puzzles;
        if some puzzles give your program trouble, try to explain why that happens.

        (2) Once you have this working, write an agent which finds a policy for a "blind" puzzle using MCTS. "Blind" puzzles are just like the puzzles above, only (1) you don't get to see the whole puzzle or know the goal states in advance, and (2) some nodes are trap doors with a chance of dropping the player into a bottomless pit! Try different policies for deciding between exploit/explore and for doing rollouts and compare them. *(We'll provide a BlindPuzzle class and sample mazes, and maybe a function to draw mazes or maze paths to the console or an image?)*

        (3) Do (2) but with reinforcement learning. Compare state-value vs action-value learning vs MCTS in terms of iterations required to reach a certain score, etc.

        *(TAs could help with writing the code or understanding the algorithms. Eager students could implement multiple algorithms, select one on the fly, generate mazes, visualize the path-finding algorithms.)*
* Day 4: Intro to probability and probabilistic programming
    * __Note: also need to do intermediate evaluations at the end of the day__
    * Topic 0: Feedback/notes on yesterday's assignment
        * Ask the TAs for code to let you put Maze objects into sets or use them as keys in dicts. I meant to include that from the start. This lets you avoid tricks like turning the Maze into a string for this purpose.
        * NOTE: If you put a Maze into a set or use it as a dict key, don't modify it at all afterwards (e.g. via `move_player`, `toggle`, or setting its variables)! Only clone it and change the clones---otherwise the set/dict will break in super confusing ways.
        1. Should use `m.move_player()` and `m.toggle()` to modify game state and not e.g. check if `m.grid[y][x] == "#"`
        2. Since this is destructive, they should copy the maze using `m.clone()` before making a move
        3. They can’t (easily) use a distance grid because switching switches changes which doors are open and closed, so player position doesn't suffice to represent world state, so:
        4. They need to track whether a maze has been seen before. One way is to use a set to track seen mazes.
        5. They need to track the cost and predecessor state along with Maze states. Some ways of doing that include:
        	* Add `cost` and `predecessor` properties to maze objects.
        	* Include `cost` and `predecessor` with the maze in the frontier in a tuple. Of course, using priority queues the tuple's first element should be `g(n) + h(n)` where `g(n)` is the real cost to reach node `n` and `h(n)` is the heuristic value (e.g. Manhattan distance from goal) at `n`.
            * Keep a `costs` dict and a `predecessors` dict or a `best_paths` dict keyed by Maze objects.
    * Topic 1: Basic probability/Bayes rule
        * what probability of an event means
        * P(X) -- cases where X happens / all possible cases
        * P(X, Y) -- cases where both X and Y happen / all possible cases
        * If X,Y independent, then P(X,Y) = P(X) P(Y)
        * P(X | Y) = P(Y|X) P(X) / P(Y) -- or equivalently, P(Y,X) = P(X|Y) P(Y) / P(X)
        * Chaining: P(G,S,R)=P(G | S,R) P(S | R) P(R)
        * I like the [wikipedia page](https://en.wikipedia.org/wiki/Conditional_probability) on conditional probability too
        * Bayesian statistics
            * Prior (background belief) and posterior (after considering prior) probability
            * Not, "What is the chance of X happening", but "Given my background knowledge/superstition/experience, what is the chance of X happening?"
            * Example priors: Uniform/flat prior; or:
                * "An example is a prior distribution for the temperature at noon tomorrow. A reasonable approach is to make the prior a normal distribution with expected value equal to today's noontime temperature, with variance equal to the day-to-day variance of atmospheric temperature, or a distribution of the temperature for that day of the year."
            * Priors are really important but we don't have time to get too deeply into them
        * Bayes nets
        * Given P(X | Y), P(X), and P(Y), we can find P(Y | X) with Bayes rule
        * P(X)="Chance of rain", P(Y)="chance of clouds": "Chance of rain when it's cloudy = chance of clouds * chance of clouds given rain / chance of rain"
        * Bayes nets
        * Random variables and expected value
            * P(X=x)
            * "probability-weighted average of all possible values"
        * Distributions (normal, poisson, negative binomial), mean/variance, and PDFs
    * Exercise: Make a bayes net for some situation. It's okay to use e.g. "low/medium/high" for the probabilities in the tables.
    * Topic 2: Probabilistic programming
        * Programming with distribution variables
        * "probabilistic programming languages extend a well-specified deterministic programming language with primitive constructs for random choice" [@dippl]
        * "If we view the semantics of the underlying deterministic language as a map from programs to executions of the program, the semantics of a PPL built on it will be a map from programs to distributions over executions. When the program halts with probability one, this induces a proper distribution over return values." [@dippl]
        * WebPPL examples
    * Topic 3: Let's talk about projects
        * Project format
        * Project suggestions
    * What went well:
        * Basic probability, Bayes nets and exercise, connection to ML, WebPPL
    * What went poorly:
        * Bayes rule. Typo in my notes, stumbled, ended up with a result I couldn't interpret well.
    * What to do next time:
        * Should have practiced the Bayes Rule part of the lecture specifically!
        * Should have had more examples of belief nets in the bag.
    * Assignment 1
        ~ Individual (small) assignment.

        Give me a list of three or more project ideas you might be interested in doing, either from the suggestions or your own idea. If you have a partner or partners in mind, let me know as well. Submit them (as Markdown `.md` files) in the folder `projects/4-project-ideas`.
    * Assignment 2
        ~ Individual (small) assignment.

        Fill out the preliminary evaluation form and send it to a TA. They'll anonymize them and send them on to me so I can adjust the course based on your feedback. You can find the form in the `projects/4-evaluations` folder.
    * Assignment 3: MCTS and Reinforcement Learning agents for maze solving.
    * Assignment 4 (Optional)
        ~ Individual or pair (small) assignment.

        Make a probabilistic program expressing your Bayesian model from earlier today. Try to give it a prior based on your intuition, or by loading up a dataset. Either PyMC3 or WebPPL is fine.

        Submit it as an `.ipynb` or a `.wppl` file in `projects/4-probabilistic`.
* Day 5: Creative AI
    * Reading (do it this afternoon/tonight, since I didn't get it ready in advance. It will help with the assignment!)
        ~ Kate Comptons's classic [procedural content generation post](http://galaxykate0.tumblr.com/post/139774965871/so-you-want-to-build-a-generator) and [tracery tutorial](http://www.crystalcodepalace.com/tracery)
        ~ Look at some [cheap bots done quick](http://cheapbotsdonequick.com) bots
        ~ Look at [emoji world](http://ncase.me/simulating)
        ~ Look at some [deep forger](https://twitter.com/deepforger?lang=en) examples
    * Note: [Nucl.ai](http://events.nucl.ai/program/tracks/) just started streaming! Check it out in your down time.
    * Topic 0: MCTS/RL recap
    * Topic 1: What is creative AI? Let's go through some examples.
        * Importance of framing, anthropomorphizability
        * Not about "right answers", but "feels right" or "interesting" or "visualizing possibilities" or "helping creators"
    * Exercise: Think of examples?
    * Topic 2: Planning, hierarchical planning, and planning for story/music/etc generation
        * World model
        * Hierarchical decomposition
    * Exercise: Break down a storyworld/genre/music-style/art-composition/etc into planning operators/world models?
    * Topic 3: Grammars (special case of above) and Tracery
        * Grammars + objectives ~~ planning
    * Topic 4: Artificial life: Cellular automata and genetic algorithms/evolutionary search
        * CAs, what they are, how they work
        * GAs, special type of search, how they work
    * What went well:
        * ALife, GAs, MCTS recap, idea of creative AI and overview, planning domains
    * What went poorly:
        * Grammar overview, group "creative AI" exercise didn't go as deep as I'd hoped, didn't get to the planning exercise
    * What to do next time:
        * Planning exercise; more grammar examples prepared
    * Assignment 1:
        ~ Individual or pair (medium-length) assignment. Get it started today and try to finish it by the end of the week. Go as far as you can with it.

        Make a Tracery grammar to generate some interesting artifact: Genre stories, TV episodes, SVG images, Emoji compositions, musical leitmotifs, classified ads, inspirational quotes, fantasy game items, small programs... and use it somehow, maybe in a Twitter bot (using cheapbotsdonequick) or in some other context.

        AND/OR

        Make an emoji world simulation, under similar constraints as above: go as far as you can!
* Day 6: Formal Logic \& Prolog Crash Course
    * Reading, in this order:
        * Art of Prolog, chapter 1
        * Kowalski's "Algorithm = Logic + Control"
        * Art of Prolog, chapter 6 if you have time
    * Topic 1: Propositional logic and inference
        * Why logic?
        * Propositional logic basics: propositional variables, and, or, not, implies
        * Queries
        * Horn logic and resolution: mechanical proof
        * Existential and universal quantifiers
        * Queries with logic variables, and uninterpreted functions
    * Topic 2: Prolog and proof search. "Old school" symbolic AI stuff.
        * First, mention Prolog is used in Watson and other query answering systems
        * Prolog rules and queries
        * Logic variables again
        * Knowledge bases
        * Graphs
        * Planning with temporal logic and event calculus
        * General game playing
    * Exercise:
        * Pair up. Pick a domain distinct from the family tree example and write some first-order logic/Prolog rules (on paper) for a knowledge base about that domain. Include facts, some rules, and some example queries. Some example domains:
            * Romantic interests/dating compatibility
            * Car features, options, prices, and ratings
            * Types of animals/animal-guessing game knowledge base
            * ...
    * Topic 3: Prolog data structures
        * Lists and recursion
            * member/2
                * member(E,[E|_]). member(E,[_|L]) :- member(E,L).
            * append/3
                * append([],L,L). append([H|T],L,[H|L2]) :- append(T,L,L2).
            * path/3
                * path1(E,E,[]). path1(S,E,[S|P]) :- edge(S,M), path1(M,E,P).
                    * but: cycles in DFS! let's do iterative deepening instead by fixing path length each time:
                * path2(S,E,P) :- length(P,_), path1(S,E,P).
        * Numerical operations, math, and constraints: #=, #\=, #>, #<, #>=, #=<
        * Functors, including ","
    * What went well:
        * Knowledge bases, basic propositional logic, derivations, starter Prolog, KB exercise
    * What went poorly:
        * Framing narrative, deductive rules, advanced propositional logic, CLP
    * What to do next time:
        * Real logic intro, real first order stuff, don't mix syllogistic stuff and propositional stuff, prepare CLP examples
    * Assignment:
        ~ Individual or pair (medium-length) assignment. (SKIPPED, maybe something like this on Monday)

        Write a maze solver or other planning problem in Prolog. It's OK if it's simpler than the Python maze or doesn't return paths; the key thing is to specify what movement through a maze means, and derive the solution algorithm automatically from that. Good starting points might be, "recognizing a tweet of up to 140 characters" or "confirming a maze solution of fewer than N steps".
* Day 7: Machine learning as function approximation
    * Topic 1: Error minimization and regression/gradient descent
        * Today we're focusing on supervised learning.
        * Inputs, outputs/labeling, function approximation, feature design, curse of dimensionality, ...
        * Separability, linearity, ...
        * Test set vs validation set, dropout, overfitting, stochastic gradient descent, ...
        * What does this have in common with MCTS?
    * Exercise: Pick a data set and design some features/inputs/outputs. Is your data easy or hard to collect?
    * Topic 2: Perceptrons and perceptron learning
        * Perceptron: vector of inputs -> output boolean, learn vector of weights and bias y = (wx+b > 0); usually formulated with input x0 = 1 and w0 = b and y = (wx > 0)
            * Classification problem
            * Initialize all weights to small random values (used to suggest all zeroes, but this suggestion works better with the stochastic gradient descent methods used for training bigger NNs)
            * cost function: How to score a predicted output vs the actual labeled output
            * learning = descending the gradient of the cost function
            * Perceptron is a linear function, so it's differentiable.
        * Learning algorithm: For each sample input/output, evaluate y = wx (no > 0 here); compare y vs desired output d; update each weight wi += c(d, y) * xi. (e.g. c(a,b) = a - b)
            * Example on some linear thing
            * Will it converge? Yes, iff linearly separable.
            * Let's try it on XOR and see
            * If not linearly separable, will it get close to an approximate answer? NO
    * Topic 3: Multilayer perceptrons, if there's time:
    * Assignment:
        ~ Write a perceptron yourself, classify something.
            * Possible data sets:
                * Custom sequence of numbers to boolean labels
                * http://archive.ics.uci.edu/ml/datasets/StoneFlakes , with outputs being "is it flint" or "is it found in a quarry" or...
                * http://archive.ics.uci.edu/ml/datasets/Wholesale+customers , with prediction being "channel" or "region" or...
        ~ Install scikit-neuralnetwork or Keras
* Day 8: Deep Neural Networks
    * __Note: need to finalize projects by end of today or tomorrow__
    * Reading
        ~ http://deeplearningbook.org, especially chapters 6, 9, 14
        ~ Side references: NEAT, https://nucl.ai/blog/extreme-style-machines/
    * Topic 1: Deep neural networks (and intro to scikit-neuralnetwork)
        * Most neural networks have many "hidden" layers between the inputs and outputs, not just the one layer described yesterday
            * The "> 0" bit is a kind of "output transformation" from activation values to classes.
        * Are those networks made out of linear perceptrons like yesterday, or something else?
            * Something else --- why?
            * ((TODO: UNSURE:: Because stacking linear classifiers just gives you linear separation in increasing numbers of dimensions. But this can get really inefficient?))
            * By analogy to non-linear neuron firing "activation", we use activation functions that are "nearly" linear. The default suggestion is ReLU (rectified linear units) because they're simple and cheap to calculate and don't have the same saturation issues as sigmoids (becoming insensitive to inputs)
            * However, for output units sigmoids are still used in predicting binary variables (and softmax for multi-class prediction): ensure there's always a strong gradient when you have a wrong answer.
            * The loss function has to be designed with the output layer in mind
            * [Citations for above](http://www.deeplearningbook.org/contents/mlp.html)
        * Learning in deep networks
            * Backpropagation, similar to RL/MCTS but using derivatives
            * "back-propagation refers only to the method for computing the gradient, while another algorithm, such as stochastic gradient descent, is used to perform learning using this gradient"
            * Find gradient (partial derivative) of cost function WRT parameters, then try to climb down that gradient by tweaking parameters.
            * TODO: Worked example? More detailed algorithm pseudocode?
    * TODO: Exercise? Or do it after topic 2?
    * Topic 2: Image recognition and convolution
        * LeCun, 1989
        * Useful if your data has a grid topology, e.g. time series (1d) or image data (2d) or video (3d) or ...
        * Anyone know what convolution is? It's a kind of operation on matrices, and convolutional nets "just" use convolutions instead of multiplications in one or more of their layers.
        * Convolution is more or less a weighted average considering nearby elements more strongly than far-away ones.
        * For example, for a 2D image there's a nested sum and a 2D weight function
            * "kernel", like in image processing
            * What happens at the edges of the image?
        * If a regular neural network lets every input unit react with every output unit equally, convolutions enforce some locality and admit smaller, more efficient networks (or equivalently, similarly sized networks that extract more medium-level features)
            * Multiple convolution layers can build up high level structures starting from the low level inputs
        * One layer: Convolve to linear activations->Run through nonlinear activation function like ReLU ("detector")->pool local groups into summary statistics (to achieve e.g. translation invariance)
    * Topic 3: Auto-encoders
        * Probably won't have time...?
        * (1987 and onwards)
        * Neural net trained to try copying input to output
        * Design them to be unable to learn perfect copying, so that their approximate copies only "resemble" the inputs, to learn useful/typical/important properties of the data
        * Often, we care more about the learned parameters than the actual outputs
        * Why is this useful?
            * Dimensionality reduction, feature learning...
            * Denoising, reconstruction, ...
            * A colleague uses these for Magic: The Gathering card generation from partial examples
    * Assignment:
        ~ Write an image classifier or auto encoder?
* Day 9: Computer History Museum
    * Assignment: Explication of a historical AI system
* Day 10: Prolog techniques; recurrent neural networks.
    * Reading
        ~ ML:
            * "The Unreasonable Effectiveness of RNNs" (Blog post)
            * deeplearning.org chapter 10, 11
            * http://karpathy.github.io/2016/05/31/rl/
        ~ Prolog:
            * Art of Prolog, chapter 14
    * Topic 1: List/tree processing and meta-interpreters
    * Topic 2: RNNs and string-to-string translation
        * Recurrent NNs: NNs with cycles.
        * Unrolling. Show diagram.
        * backpropagation through time.
        * LSTM
            * Input, output, forget gates collect activations from inside and outside the block, and control the activation of the cell via multiplications (small black circles). The input and output gates multiply the input and output of the cell while the forget gate multiplies the cell’s previous state. No activation function is applied within the cell. Gate activations usually logistic sigmoid, cell input and output usually logistic sigmoid but sometimes output is identity function.
    * Topic 3: Deep Reinforcement Learning
        * learning a policy by learning state-action function, approximating rather than filling in a table
    * Assignment:
        ~ Individual or pair (short) assignment.
        ~ symbolic manipulation stuff, NLP, ...?
* Day 11: Argumentation and Non-Monotonic Logics
    * Reading
        ~ At least Nute's defeasible logic paper.
    * Topic 1: Reasoning with exceptions; non-binary logic; defeasible logic, deontic logic, ...
    * Topic 2: Reasoning about counterfactuals
    * Topic 3: Evaluating arguments
    * Assignment:
        ~ Individual (medium-length) assignment.

        *Todo: clean up.*

        Encode some argumentation logic or legal thing or social thing or artistic thing or...

        Generate argument trees using a meta-interpreter and evaluate their quality. Provide a writeup describing your rationale and showing some example claims, arguments, and evaluations. There should be a couple of arguments generated for each claim so we (human readers) can see differences in the evaluations. If there's no "subjectivity" in the argumentation, you're probably not doing it right!
* Day 12: Project workshopping and research talk. Or more Prolog stuff, general game playing? Or other topics related to the projects?
* Day 13: Presentations 1. New directions in AI.
* Day 14: Presentations 2.

#References
