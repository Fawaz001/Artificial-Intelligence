planet(mercury, 36, no).
planet(venus, 67, no).
planet(earth, 93, yes).
planet(mars, 142, yes).
planet(jupiter, 484, yes).
planet(saturn, 886, yes).
planet(uranus, 1782, yes).
planet(neptune, 2793, yes).

distance_from_sun(Planet, Distance) :- planet(Planet, Distance, _).
has_moons(Planet) :- planet(Planet, _, yes).
no_moons(Planet) :- planet(Planet, _, no).