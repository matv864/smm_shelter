FROM fedora:latest

WORKDIR /backend

RUN dnf install -y make python poetry postgresql zip

COPY Makefile pyproject.toml README.md .

COPY . .

RUN make deps

CMD make run