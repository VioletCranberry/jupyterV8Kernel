FROM python:3.12-slim

RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir poetry && poetry install --with base,dev

# Copy the kernel.json file to the Jupyter kernels directory
RUN mkdir -p /root/.local/share/jupyter/kernels/javascript_mini_racer/
COPY kernel.json /root/.local/share/jupyter/kernels/javascript_mini_racer/kernel.json

EXPOSE 8888
CMD ["poetry", "run", "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]
