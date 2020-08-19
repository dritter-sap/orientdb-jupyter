# OrientDB Jupyter Notebooks

In this repository, we show how to use Jupyter notebooks to analyze data stored in OrientDB.

## Setup the demo environment

### Clone this repository
```console
user@local:~$ git clone https://github.com/orientechnologies/orientdb-jupyter.git orientdb-demos
```
### Setup Docker & Docker Compose
*Insert references to guides to install Docker with Docker Compose*

## Configure demo apps
You can specify, which demo projects you want to load into the demo environment. Therefor, you can edit the `apps.cnf` file in the root directory of this repo.

## Start the environment
To start the environment, you have to execute following command in the root directory of the cloned repository:
```console
user@local:~$ docker-compose up -d
```
