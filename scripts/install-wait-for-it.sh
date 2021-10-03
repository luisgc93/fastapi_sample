#!/bin/sh


set -e # Exit immediately if a command exits with a non-zero status.
set -x # Print commands and their arguments as they are executed.
apt-get -y update
apt-get -y install wait-for-it