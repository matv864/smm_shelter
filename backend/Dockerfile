FROM python:3.12

WORKDIR /backend

RUN apt-get update && apt-get install make
COPY Makefile requirements.lock pyproject.toml README.md /backend/
RUN make deps

COPY . /backend/

CMD ["make", "run"]
