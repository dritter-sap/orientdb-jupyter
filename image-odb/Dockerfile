FROM orientdb:3.1.1
USER root

RUN apt-get update
RUN apt-get upgrade -y

EXPOSE 2424
EXPOSE 2480

COPY apply-config.sh /run/apply-config.sh
RUN sed -i -e 's/\r$//' /run/apply-config.sh
CMD ["sh", "-c", "/run/apply-config.sh && /orientdb/bin/server.sh"]