# Sample apps
This is a collection of sample apps, using OrientDB.
There is a directory for each sample app, including the subdirectories `databases` and `notebooks`. Providing these subdirectories is mandatory!
In some sample apps, there is a `libs.cnf` file included, which specifies the needed Python libraries. This libraries will be automatically installed on every boot of the Jupyter Docker container.

***App overview***

- Particulate Matter App from https://github.com/ChilliBits/particulate-matter-app collects particulate matter data from all over the world. With OrientDB the multimodel data (JSON documents and graph structure) can be efficiently analyzed using PyOrient and jupyter notebooks.
