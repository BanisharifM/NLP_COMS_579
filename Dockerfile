# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container to /app
WORKDIR /

# Copy the current directory contents into the container at /app
COPY . /

# Create virtual environment and install dependencies
# RUN python -m venv /openai-env && \
#     /openai-env/bin/pip install --upgrade pip && \
#     /openai-env/bin/pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Use bash to source the virtual environment
# Note: RUN commands are not affected by sourcing in previous layers
# SHELL ["/bin/bash", "-c"]
# RUN source /openai-env/bin/activate

# EXPOSE the port where Streamlit will run
EXPOSE 8501

# Update PATH environment variable to include the virtual environment
# ENV PATH="/openai-env/bin:$PATH"

# Define command to run the application
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
