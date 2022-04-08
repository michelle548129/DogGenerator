export MYSQL_ROOT_PASSWORD
docker stack deploy --compose-file docker-compose.yaml dog-stack
docker service update --replicas 3 dog-stack_front-end
docker service update --replicas 3 dog-stack_front-end