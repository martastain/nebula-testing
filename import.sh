#!/bin/bash

docker-compose exec -e "TERM=$TERM" backend /nebula/import.sh
