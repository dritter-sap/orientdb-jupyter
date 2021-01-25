# OrientDB Data Analysis -- Jupyter Notebooks

Orientdb-jupyter gives an idea on how to use [Jupyter notebooks](https://jupyter.org/) to analyze data stored in [OrientDB](https://orientdb.org/) accessed via PyOrient.
This is particularily interesting due to OrientDB's multimodel nature, allowing to do combined document and graph analytics.
The Docker files and scripts for Jupyter and OrientDB (incl. PyOrient) are generic and can be seen as blueprint for a "Jupyter on OrientDB" setup.
The applications in the `apps` folder denote examples on how to use this blueprint.
Subsequently we describe how to setup the example apps step-by-step, which should give an impression on how to add and run your own app.

> **Note:** PyOrient is only available for OrientDB version [2.2.x](https://github.com/orientechnologies/pyorient/tree/2.2.x). The support for OrientDB version [3.1.x](https://github.com/orientechnologies/pyorient/tree/3.1.x) is work in progress.
 
## Setup the demo environment

### Clone this repository

```console
user@local:~$ git clone https://github.com/orientechnologies/orientdb-jupyter.git orientdb-jupyter-demos
```
### Setup Docker & Docker Compose

To install Docker on your system, please follow the [installation guide](https://docs.docker.com/get-docker) from the official Docker documentation.<br>
After installing Docker, you need to install Docker Compose to orchestrate containers locally. Therefor, please use the [installation guide for Docker Compose](https://docs.docker.com/compose/install) from the official Docker documentation.

> installation of python basis takes a while, hence docker images are provided as packages.

## Configure demo apps

You can specify, which demo projects you want to load into the demo environment.
Therefor, you can edit the `apps.cnf` file in the root directory of this repo.
Within the specific app folder a `libs.cnf` can be used to specify required Python dependencies.
The application-specific libraries are dynamically added and can be used in the notebook of this application.

> Note: If you altered the configuration file, use the command `docker-compose restart` to apply the changes for the Docker containers.

## Start the environment

To start the environment, you have to execute following command in the root directory of the cloned repository:
```console
user@local:~$ docker-compose up -d
```
Depending on the number of python libs, specified with the selected apps, it can take a few seconds / minutes for jupyter to come up.

> Note: If changed, use `docker-compose build` to rebuild. The try again.

## Work with notebooks

OrientDB Studio will be available here: [http://localhost:2480](http://localhost:2480/studio/index.html)<br>
Jupyter will be available here: [http://localhost](http://localhost)

Find the notebook configured in the `.cnf` file in the `root` directory.

For example (particle matter emission app):

```
particulate-matter-app
* emission-data-science.ipynb
* emission-forecast.ipynb
```

> Hint: The emission app notebooks contain examples on how to use `PyOrient` (cf. https://github.com/orientechnologies/pyorient/tree/master/pyorient).
