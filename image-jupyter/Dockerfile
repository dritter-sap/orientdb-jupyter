FROM jupyter/minimal-notebook:latest
USER root

RUN apt-get update
RUN apt-get upgrade -y
RUN pip install git+https://github.com/orientechnologies/pyorient.git#egg=pyorient

EXPOSE 8888

COPY apply-config.sh /run/apply-config.sh
COPY install-dependencies.sh /run/install-dependencies.sh
COPY base-libs.cnf /base-libs.cnf
RUN sed -i -e 's/\r$//' /run/apply-config.sh
RUN sed -i -e 's/\r$//' /run/install-dependencies.sh
RUN /run/install-dependencies.sh "/base-libs.cnf"
CMD ["sh", "-c", "/run/apply-config.sh && /usr/local/bin/start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''"]