# Use a Python 3.10 base image
FROM python:3.10-slim
LABEL maintainer Synkevych Roman "synkevych.roman@gmail.com"

# Set working directory
WORKDIR /app

COPY .cdsapirc /root/.cdsapirc

# Create a volume named "data" to persist data outside the container
# VOLUME /data

# Install cdsapi library
RUN pip install cdsapi

# Copy your Python code to the container
COPY . .

# Set the entrypoint to run your script
ENTRYPOINT ["python", "multi_level_data_manager.py"]
