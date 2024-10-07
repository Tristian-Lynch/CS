prodlist([], 1).
prodlist([H|T], P) :-
    prodlist(T, P1),
    P is H * P1.