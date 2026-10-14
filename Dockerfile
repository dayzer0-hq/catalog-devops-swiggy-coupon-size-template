# This Dockerfile WORKS, and that is the problem: it produces an image well over a gigabyte.
#
# Do not rewrite it before you have measured it. The measurement is the first piece of work,
# and a number you took yourself is the only one you will trust at the end.
FROM python:3.12

# A full build toolchain in the final image, for a service that compiles nothing.
RUN apt-get update && apt-get install -y \
      build-essential gcc g++ make cmake git curl vim \
      python3-dev libpq-dev \
 && echo "deliberately no apt cache cleanup"

# The whole repository, including anything you happen to have lying around.
COPY . /srv
WORKDIR /srv

EXPOSE 8080
CMD ["python3", "app/server.py"]
