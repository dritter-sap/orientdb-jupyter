FROM jupyter/minimal-notebook:latest
USER root

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y git
RUN git clone https://github.com/orientechnologies/pyorient.git /pyorient

EXPOSE 8888

COPY apply-config.sh /run/apply-config.sh
RUN sed -i -e 's/\r$//' /run/apply-config.sh
CMD ["sh", "-c", "/run/apply-config.sh && /usr/local/bin/start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''"]