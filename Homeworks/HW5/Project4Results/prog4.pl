%Bailey Kocin and Ryan Reynolds 2693018
%****************************
%***********FACTS************
%****************************

%*******QUESTION 1 FACTS*********
male(mushu).
male(tangdee).
female(mulan).
female(beumei).
female(gugu).

father(baba,mushu).
father(baba,mulan).
father(yeye,baba).
father(yeye,gugu).
father(yeye,susu).
father(susu,tangdee).
father(zengzufu,yeye).
father(jojo,beumei).

mother(mama,mushu).
mother(mama,mulan).
mother(popo,mama).
mother(popo,jojo).

%********QUESTION 1 RULES************
parent(X,Y):- father(X,Y).
parent(X,Y):- mother(X,Y).
sibling(X,Y):- parent(Z,X), parent(Z,Y), not(X=Y).
brother(X,Y):- sibling(X,Y), male(X).
aunt(X,Y):- sibling(X,Z), father(Z, Y), female(X).
granddaughter(X,Y):- parent(Y, Z), parent(Z, X), female(X).
descendent(A,D):-parent(D,A).
descendent(A,D):-parent(P,A),descendent(P,D).

%********QUESTION 2***********
getlast([L],L).
getlast([_|T],X):-getlast(T,X).

%*******QUESTION 3******************

%match function to iterate a match is found
match(X, [X|T], T).

%<S>--> x<X>
ns(X0,X):-match(x,X0,X1),nx(X1,X).

%<X>--> x<X> % | <Y>
nx(X0,X):-match(x,X0,X1),nx(X1,X).
nx(X0,X):- ny(X1,X).

%<Y>--> y<Z>
ny(X0,X):-match(y,X0,X1),nz(X1,X).

%<Z>--> empty % |y<Z>
nz([],[]):-!.
nz(X0,X):-match(y,X0,X1),nz(X1,X).	



%*******QUESTION 4************

%FACTS
democrats([alice, bill, claire, diane, emily]).
smart([bill, claire, emily]).
not_corrupt([alice, claire, bill]).

%RULES
%A candidate is A good candidate if they are smart and not corrupt
%Dem candidate without a cut in the member function
tests(X):-smart(L), not_corrupt(L2), member(X,L), member(X,L2).
member(E, [E | _]).
member(E, [_ | L]) :- member(E, L).
dem_candidate(X) :- democrats(L), member(X, L), tests(X).

%Dem candidate a cut in the member function
tests_cut(X):-smart(L),not_corrupt(L2), member_cut(X,L), member_cut(X,L2).
member_cut(E,[]):-!,fail.
member_cut(E, [E | _]) :- !.
member_cut(E, [_ | L]) :- member_cut(E, L).
dem_candidate_cut(X) :- democrats(L), member_cut(X, L), tests_cut(X).
