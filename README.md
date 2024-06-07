# Jupyter JavaScript (MiniRacer) Kernel

This repository contains a custom Jupyter kernel that allows you to run JavaScript 
code using the V8 engine via the [PyMiniRacer](https://github.com/bpcreech/PyMiniRacer)
library. The kernel is containerized using Docker and managed with Poetry for dependency
management.

## Features

- Run JavaScript code within Jupyter notebooks.
- Uses the V8 engine through `py_mini_racer`.
- Containerized with Docker for easy deployment.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Poetry](https://python-poetry.org/docs/#installation)

## Run the Docker Container

```bash
docker build -t jupyter-v8-kernel && docker run -p 8888:8888 -v $(pwd):/app jupyter-v8-kernel
```

## Access Jupyter Notebook

Open your web browser and navigate to http://localhost:8888. 
You should see the Jupyter Notebook interface.

	1.	In the Jupyter interface, open the examples/example.ipynb file.
	2.	Select the “JavaScript (MiniRacer)” kernel from the kernel menu.
	3.	Run the cells to execute JavaScript code.

