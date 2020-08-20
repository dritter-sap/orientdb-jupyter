FROM jupyter/minimal-notebook:latest
USER root

RUN apt-get update
RUN apt-get upgrade -y
RUN pip install git+https://github.com/orientechnologies/pyorient.git#egg=pyorient

EXPOSE 8888

COPY apply-config.sh /run/apply-config.sh
RUN sed -i -e 's/\r$//' /run/apply-config.sh
CMD ["sh", "-c", "/run/apply-config.sh && /usr/local/bin/start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''"]