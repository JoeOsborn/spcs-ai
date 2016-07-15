---
title: AI, Knowledge Representation, and Machine Learning
author: Joseph C. Osborn
bibliography: bibliography.bib
---

>"It's part of the history of the field of artificial intelligence that every time somebody figured out how to make a computer do something---play good checkers, solve simple but relatively informal problems---there was a chorus of critics to say, "that's not thinking"...
>Practical AI successes, computational programs that actually achieved intelligent behavior, were soon assimilated into whatever application domain they were found to be useful in, and became silent partners alongside other problem-solving approaches, which left AI researchers to deal only with the "failures," the tough nuts that couldn't yet be cracked." [@McCorduck:2004:MTP:983115]

This course surveys the field of artificial intelligence and its two main threads: symbolic/knowledge-based and statistical/machine-learning approaches.
We will pay special attention to how AI systems reflect and reify not just the knowledge of their creators, but also their values and implicit biases.
In recent years we have seen a proliferation of AI systems that filter news feeds, hyper-target advertisements, act as personal assistants, determine apartment rental rates, and even attempt to identify suspected terrorists or decide parole terms and sentencing.
Whenever we build an AI system, we choose how to represent the world and the problem we want to solve, and this decision must consider ethics as much as the performance of the resulting algorithm.
On the positive side, if AI systems can encode values, then we can also use them to creative or socially beneficial ends!
AI systems can generate novel stories and works of art, provide compelling opponents in games, and personalize education for individual learners.

This course will engage with active research in deep learning, computational creativity, video game AI, natural language understanding, and the ethics of AI.
Students will learn the core principles of AI with worked examples, writing programs in Prolog and Python to apply the techniques shown in lectures and readings.
We will also critically analyze commercial and research AI projects to understand how they function (building smaller versions on the way), the extent to which they are successful at their stated aims, how they fit into the history of AI, and what they say about their creators and society at large.

#Objective

Students will finish the course with an appreciation of the ethical, social, and historical aspects of artificial intelligence, as well as concrete experience building small AI systems in two radically different programming environments.
Automated algorithmic decision-making is only becoming more pervasive, and this course should prepare students to observe, critique, create, and (potentially) counteract such systems.

#Format

Each day's lecture will be broken up into three main topics.
The morning schedule will generally follow this pattern:

* 9:00-9:15: Introductions and logistics. Q\&A for previous day's reading or work.
* 9:15-9:35: The first topic of the morning.
* 9:35-9:45: A small group exercise, followed by a short break.
* 9:50-10:00: Review and discussion of the results of the exercise.
* 10:00-10:30: The second topic of the morning.
* 10:40-11:10: The third topic of the morning.
* 11:10-11:30: Introduction to the day's assignment. Q\&A.

Each day will have a reading along with a programming assignment.
There will also be a final project comprising either a larger AI programming project or a research paper deeply or broadly exploring some AI system(s), topic(s), or technique(s).
This final project may be tackled alone or in a group of no more than 3 students.

Coursework will be submitted via GitHub, and on the first day we will ensure that all students have an account with the service.
An understanding of version control is vital for working on software projects in teams, and this will also give us a persistent record of project work suitable for use in portfolios or to share with family and friends.

#Topics

This course will move very quickly.
Each week we will consider four or five topics.
Each topic stands as a milestone in a particular tradition, and most remain active research areas---in fact, each would justify a three-week course on its own!

* Foundations
    * What is AI?
    * Critical technical practice
    * Introduction to Python programming
    * State machines and basic CS theory
    * Search, planning, and game AI
* Statistical techniques
    * Probabilistic programming
        * Probabilistic inference
        * Bayes Theorem
    * Machine learning as function approximation
        * Error minimization and regression
        * Perceptrons
    * Deep Neural Networks
    * Recurrent Neural Networks
* Knowledge-based techniques
    * Introduction to logic and Prolog programming
    * Rule-based systems and grammars
    * Planning with logic
    * Non-monotonic logics

#Project ideas

* Game-related AI
    * Video game character AI/social simulation
    * Automated "Heads Up" player
    * Realtime game AI
    * Guess game from level, generate level given game
    * GVGAI competition bot (or Arcade Learning Environment)
    * Learn game rules (GDL/VGDL) from forward model
    * Survey or deep-dive papers from recent AIIDE/EXAG/CIG/TCIAIG etc conferences/workshops/journals
    * Deep analysis/historical study/etc of some game AI system(s) or survey of techniques
    * ...
* General AI
    * Source repository mining/bug prediction
    * Any Kaggle competition
    * An AI system (expert system or machine learning) for some diagnosis or support task
        * Or for playing Heads Up?
    * Survey or deep-dive papers from recent AAAI/IJCAI/NIPS/etc conferences or arxiv publications in machine learning/AI/etc
    * Deep analysis/historical study/etc of some AI system(s) or survey of techniques
    * Use a probabilistic programming language to encode one or more interesting models
        * E.g. http://webppl.org (book at http://dippl.org), or PyMC3 for Python
    * Program synthesis --- given a specification or a set of examples or a partially implemented program, come up with a function implementing it
    * ...

#References
