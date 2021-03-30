Nebula 6
========

Pre-pre-pre-pre alpha of the next generation of Nebula (2022)
This repository is so far only for testing the stack. No serious stuff yet.

 - PostgreSQL for relations and primary data storage
 - Redis for caching and sessions store
 - Elastic search
 - Async API server

Core
----

Set of command-line scripts to deploy Nebula instance as a docker stack (swarm?).

Backend
-------

Asyncio based API server (HUB replacement).

 - Use Redis to store session data.
 - Load-balanced, HA done by Traefik or Caddy

Frontend
--------

 - React web app
 - Desktop app (Firefly)

Playout
-------

Bare metal playout server - Debian CasparCG box /w ccg-companion-app (storage monitor,
ws2amcp, osc2ws, metrics...)
