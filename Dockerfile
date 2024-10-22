FROM python:3.10

WORKDIR /app

COPY README.md pyproject.toml pdm.lock ./
COPY tests/test_*.py /app/tests/
COPY .github/workflows/build.yaml /app/.github/workflows/
COPY .github/workflows/task_2_test.yaml /app/.github/workflows/

RUN python3 -m pip install --upgrade pip setuptools wheel pdm
RUN pdm lock --check \
    && pdm export -f requirements --without-hashes > requirements.txt \
    && python3 -m pip install --no-cache-dir -r requirements.txt

    
COPY dist/ /tmp/dist/
RUN python3 -m pip install --no-cache-dir /tmp/dist/*.whl

COPY src/hw5_yu_stas/python_script.py /app/
CMD ["python", "python_script.py"]