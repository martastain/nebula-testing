Nebula 6
========

Pre-pre-pre-pre alpha of the next generation of Nebula (2022)
This repository is so far only for testing the stack. No serious stuff yet.

 - PostgreSQL for relations and primary data storage
 - Redis for asset caching and sessions store
 - Elastic search
 - Sanic as an API server


Core
----

Set of command-line scripts to deploy Nebula instance as a docker stack (swarm?).

Backend
-------

Sanic/async based API server (HUB replacement).

 - Use Redis to store session data.
 - Load-balanced, HA done by Traefik

Frontend
--------

 - React web app
 - Desktop app (Firefly)
 - Desktop environment (multiple desktop apps within a dedicated desktop environment)

Playout
-------

Bare metal playout server - Debian CasparCG box /w ccg-companion-app (storage monitor,
ws2amcp, osc2ws, metrics...)
