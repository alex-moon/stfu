#!/bin/bash

pass=$(cat /opt/stfu/.env | grep SQLALCHEMY_DATABASE_URI | awk -F':' '{ print $3 }' | awk -F'@' '{ print $1 }')
host=$(cat /opt/stfu/.env | grep SQLALCHEMY_DATABASE_URI | awk -F'@' '{ print $2 }' | awk -F':' '{ print $1 }')

echo "Connecting to $host"

PGPASSWORD=$pass psql --user=stfu --host=$host stfu
