prodlist([], 1).
prodlist([X|Xs], P) :-
    prodlist(Xs, P1),
    P is X * P1.