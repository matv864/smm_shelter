FROM fedora:latest

WORKDIR /backend
COPY . .

RUN dnf install -y make python postgresql zip
RUN python -m ensurepip

RUN make deps

CMD make run