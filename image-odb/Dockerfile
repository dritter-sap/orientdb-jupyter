FROM orientdb:3.1.1
COPY apply-config.sh /run/apply-config.sh
EXPOSE 2424
EXPOSE 2480
CMD ["sh", "-c", "/run/apply-config.sh && /orientdb/bin/server.sh"]