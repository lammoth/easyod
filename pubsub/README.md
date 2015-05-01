## Requirements

To deploy Pub/Sub service you'll need Kafka. We are using following docker:

[kafka + zookeeper + Exhibitor Docker](https://registry.hub.docker.com/u/sheeley/docker-kafka-exhibitor/)

### kafka docker
You need to install docker service. If you are runing in Mac, you will need [boot2docker](https://docs.docker.com/installation/mac/)

    brew install Caskroom/cask/boot2docker


Now you need instance kafka docker:

    docker pull sheeley/docker-kafka-exhibitor
    docker run -p 2181:2181 -p 9092:9092 -p 8181:8181 --env ADVERTISED_HOST=$BOOT2DOCKER_IP --env ADVERTISED_PORT=9092 sheeley/docker-kafka-exhibitor

The field ``$BOOT2DOCKER_IP` could contain your private docker host ip. You can get it running the command:

    boot2docker ip

You can add `-d` argument to detach the execution.

## TODO list
- [x] boot2docker docker config
- [ ] node.js client and server HelloWorld
- [ ] node.js kafka task queue
