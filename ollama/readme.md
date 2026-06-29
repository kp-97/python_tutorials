# Ollama API Interaction Examples

This repository provides examples of how to interact with the local Ollama API using different methods in Python.

## Project Overview

The following scripts demonstrate two different ways to query a local Ollama instance:

- **`sample_request_1.py`**: Shows how to use the standard `requests` and `json` libraries to query the Ollama API directly.
- **`sample_request_2.py`**: Shows how to achieve the same result using the dedicated `Ollama` Python package.

## Usage Examples

### Using Standard Libraries
To see how to interact with the API using only standard tools, refer to:
`python sample_request_1.py`

### Using the Ollama Package
To see the implementation using the official library, refer to:
`python sample_request_2.py`

## Custom Models

You can create and register custom models using a `Modelfile`. For example, to create a model named "mario":

```bash
ollama create mario -f ./Modelfile