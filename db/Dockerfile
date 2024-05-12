FROM postgres:16

WORKDIR /var/lib/postgresql/data

COPY create_table.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_DB=example
ENV POSTGRES_HOST_AUTH_METHOD=trust

EXPOSE 5432

HEALTHCHECK --interval=10s --timeout=5s --retries=5 CMD pg_isready

CMD ["postgres"]