FROM fnndsc/python-poetry
WORKDIR .
COPY pyproject.toml poetry.lock /
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root
COPY src/ /src/
CMD ["poetry", "run", "src:app", "--host", "0.0.0.0"]
