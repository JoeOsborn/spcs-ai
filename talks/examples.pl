edge(a,b).
% PYTHON:edges = [("a","b"), ...]
edge(a,c).
edge(b,d).
edge(d,e).
edge(b,a).
edge(f,f).
edge(c,d).

reach(A,A,[A]).
reach(A,Z,[A|P]) :-
    edge(A,B),
    reach(B,Z,P).

% Big database of people and demographic data
% Gossip or conspiracy theory database
% (Romantic pairing database)
% Recipe knowledge base -- relating ingredients and outputs via recipe predicates
% Car buying guide, features safety rating, option packages, prices, insurance rates, overall ratings, stats like performance handling etc
% Medical diagnosis
% "guess the animal"


% HOSPITAL
%  facts: patients and their diseases, medicines used for which diseases, which diseases are contagious, special care instructions for patients
% can_stay(A,B) :-
%     disease(A,D), disease(B,D),
%     normal_care(A), normal_care(B).
% can_stay(A,B) :-
%     disease(A,D1), not_contagious(D1),
%     disease(B,D2), not_contagious(D2),
%     normal_care(A), normal_care(B).
% queries: who can stay with whom, what medicine should each patient have, special case,

% Netflix knowledge base : choosing a show
% facts: movie genres, ratings, age recs, media type, actors, language, trending, viewing history, user age
% rules: similar(M1,M2), suggested(M), disallowed(M)
% queries: pick something to watch to pass time, find an agreeable movie for two+ people

% Fruit knowledge base
% facts: colors, sizes, nutrition?, taste?, durability?, shelf life?, textures,
% rules: complementary fruits, what can be stacked on top of other fruits
% queries: unknown fruit classification, meal planning for nutrition (given nutrient info), fruit arrangement, grocery store/pantry purchasing

% memb will be recursive.
memb(Elt, [Elt|_Rest]).
memb(Elt, [_Elt2|Rest]) :-
    memb(Elt, Rest).

% L3 == L1 followed by L2
% L3 is all the elements of L1 followed by all the elements of L2
append1([],L2,L2).
append1([H|T], L2, [H|L3]) :-
    append1(T,L2,L3).

each_sorted([H|T],Current) :-
    Current > H,
    each_sorted(T,H).
sorted(L1, L2) :-
    perm(L1,L2),
    L2 = [First|Rest],
    each_sorted(L2,First).

%William Byrd
eval(A + B, C) :-
    number(A), number(B),
    C #= A + B.
eval((A + B) + C, D) :-
    eval(A + B, Q),
    eval(Q + C, D).

% (4 + 3) + 2 = 9
% 7 + 2 = 9
% eval(expression, value) -->
%   does this expression have this value?
%   do two expressions have the same value?
%   generate expressions that produce a value
%   eval((4 + X) + Y, 10)
