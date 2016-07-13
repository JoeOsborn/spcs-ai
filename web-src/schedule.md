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
    * Topic 1: Posing problems as graph search. Example: PuzzleGraph. Heuristic search (A*). Exploit/explore.
    * Exercise:
        Pick an interesting problem and try to phrase it as "local search".
    * Topic 2: MCTS and back propagation
    * Topic 3: Reinforcement learning
    * Assignment
        ~ Individual or pair (long) assignment. (1) should be done by tomorrow, (2) and (3) by Monday.
        (1) Write a Python program to solve switch and door puzzles with one of the heuristic search algorithms
        described during the lecture. *(We'll provide a Puzzle class and sample puzzles, and maybe a function to draw puzzles or solution paths to the console or an image?)* Try it on the provided sample puzzles;
        if some puzzles give your program trouble, try to explain why that happens.

        (2) Once you have this working, write an agent which finds a policy for a "blind" puzzle using MCTS. "Blind" puzzles are just like the puzzles above, only (1) you don't get to see the whole puzzle or know the goal states in advance, and (2) some nodes are trap doors with a chance of dropping the player into a bottomless pit! Try different policies for deciding between exploit/explore and for doing rollouts and compare them. *(We'll provide a BlindPuzzle class and sample mazes, and maybe a function to draw mazes or maze paths to the console or an image?)*

        (3) Do (2) but with reinforcement learning. Compare state-value vs action-value learning vs MCTS in terms of iterations required to reach a certain score, etc.

        *(TAs could help with writing the code or understanding the algorithms. Eager students could implement multiple algorithms, select one on the fly, generate mazes, visualize the path-finding algorithms.)*
* Day 4: Probabilistic programming
    * __Note: also need to do intermediate evaluations at the end of the day__
    * Topic 1: Basic probability/Bayes rule
    * Topic 2: Probabilistic programming (pymc3)
    * Topic 3: Let's talk about projects
    * Assignment 1
        ~ Individual (small) assignment.

        Give me a list of three or more project ideas you might be interested in doing, either from the suggestions or your own idea. If you have a partner or partners in mind, let me know as well.
    * Assignment 2
        ~ Individual or pair (medium-length) assignment

        Write a probabilistic program that generates/runs/solves/represents/etc the mazes from before? Or somehow relates to the MCTS stuff?
* Day 5: Machine learning as function approximation
    * Topic 1: Error minimization and regression/gradient descent
        * Overfitting, linearity, curse of dimensionality ...
        * Test set vs validation set, generalizing, overgeneralizing...
    * Topic 2: Naive Bayes classifiers
    * Topic 3: Perceptrons
    * Assignment:
        ~ Write a perceptron or simple NN, classify something. We'll need to provide data sets!
* Day 6: Deep Neural Networks
    ~ __Note: need to finalize projects__
    * Reading
        ~ Primary sources on deep neural networks
    * Topic 1: Deep neural networks (and intro to scikit-neuralnetwork)
    * Topic 2: Image recognition and convolution
    * Topic 3: Auto-encoders
    * Assignment:
        ~ Write a image classifier or auto encoder?
* Day 7: Recurrent Neural Networks
    * _Finalize project ideas by end of today! or tomorrow!_
    * Reading
        ~ "The Unreasonable Effectiveness of RNNs" (Blog post)
    * Topic 1: String-to-string translation
    * Topic 2: Style Transfer
    * Topic 3: Deep Reinforcement Learning
    * Assignment:
        ~ Write a style transfer thing or string to string thing?
* Day 8: Formal Logic \& Prolog Crash Course
    * Topic 1: Propositional logic and inference
    * Topic 2: Prolog and proof search. "Old school" symbolic AI stuff.
    * Topic 3: Knowledge bases
    * Assignment:
        ~ Individual (medium-length) assignment.

        Todo: Some kind of knowledge base or expert system... or a maze generator-cum-solver... or something that shows how much more compact Prolog programs can be than Python ones? Two part thing with one part today and one part Monday (day 10). Or some of the 99 prolog problems?
* Day 9: Creative AI
    * Reading
        ~ Generative Methods paper [@compton2013generative] and Kate's PCG blog.
    * Topic: What is creative AI? Intro to Tracery.
    * Assignment:
        ~ Individual or pair (medium-length) assignment. Due Monday.

        Make a Tracery grammar to generate some interesting artifact: Genre stories, TV episodes, SVG images, Emoji compositions, musical leitmotifs, classified ads, inspirational quotes, fantasy game items, ... and put up a Twitter bot with it. Go as far as you can with this.

        *Todo:elaborate.*
* Day 10: Solving problems with logic
    * Topic 1: Planning with temporal logic and the event calculus. General game playing.
    * Topic 2: List/tree processing and meta-interpreters
    * Topic 3: DCGs?
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
