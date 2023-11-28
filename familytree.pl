parent(john, jim).
parent(john, ann).
parent(jane, jim).
parent(jane, ann).
parent(jim, tom).
parent(ann, sara).
male(john).
male(jim).
male(tom).
female(jane).
female(ann).
female(sara).

father(Father, Child) :-
    parent(Father, Child),
    male(Father).

mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

sibling(Sibling1, Sibling2) :-
    parent(Parent, Sibling1),
    parent(Parent, Sibling2),
    Sibling1 \= Sibling2.
 
