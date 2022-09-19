#!/bin/bash

pass=$(cat /opt/stfu/.env | grep SQLALCHEMY_DATABASE_URI | awk -F':' '{ print $3 }' | awk -F'@' '{ print $1 }')
host=$(cat /opt/stfu/.env | grep SQLALCHEMY_DATABASE_URI | awk -F'@' '{ print $2 }' | awk -F':' '{ print $1 }')

set -x

dbp() {
  PGPASSWORD=$pass psql --user=stfu --host=$host postgres -c "$@"
}
dbp "SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE pid <> pg_backend_pid()
AND datname = 'stfu'"
dbp "DROP DATABASE stfu"
dbp "CREATE DATABASE stfu WITH OWNER stfu"

PGPASSWORD=$pass psql --user=stfu --host=$host stfu < backup.sql
