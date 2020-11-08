Nebula 6
========

The next generation of Nebula (2022)

 - PostgreSQL for relations and primary data storage
 - Redis for asset caching and sessions
 - Elastic search
 - Sanic as an API server


Nb (Niobium)
------------

Set of command-line scripts to deploy Nebula instance as a docker stack (swarm?).

Be (Beryllium)
---------------

A.K.A. Backend - stateless, Sanic/async based API server (HUB replacement). 

 - Use Redis to store session data. 
 - Load-balanced, HA done by Traefik

Fe (Ferrum)
-----------

A.K.A. Frontend - TBD. Options:

 - Pure javascript web app
 - Hybrid app (similar to hub)
 - Desktop app (Firefly)
 - Desktop environment (multiple desktop apps within a dedicated desktop environment)


P (Platinum)
------------

A.K.A. Playout - Bare metal playout server - Debian CasparCG box /w ccg-companion-app (storage monitor,
ws2amcp, osc2ws, metrics...)