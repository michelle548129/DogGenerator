export MYSQL_ROOT_PASSWORD
docker stack deploy --compose-file docker-compose.yaml breed-name-stack
docker service update --replicas 3 breed-name-stack_front-end