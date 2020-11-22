#!/bin/bash

docker-compose exec -e "TERM=$TERM" backend python3 /nebula/data_import.py
