###########
# BUILDER #
###########
FROM python:3.9-slim-buster as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    netcat \
    python3-dev

# Create user for building and installing pip packages inside its home for security purposes
RUN useradd --create-home appbuilder
ENV BUILDER_HOME=/home/appbuilder
WORKDIR $BUILDER_HOME
USER appbuilder

# Install dependencies and create layer cache of them
COPY requirements.txt .
RUN pip install --user -r requirements.txt

######################################
# RUNNER IMAGE: For running the code #
######################################
FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends netcat

RUN groupadd -g 2000 apigroup && \
    useradd -u 2000 -g apigroup --create-home apiuser

ENV USER_HOME=/home/apiuser
WORKDIR $USER_HOME
USER apiuser

# Copy pip install results from builder image
COPY --from=builder --chown=apiuser /home/appbuilder/.local $USER_HOME/.local

# Make sure scripts installed by pip in .local are usable:
ENV PATH=$USER_HOME/.local/bin:$PATH

# Setup workdir
RUN mkdir app
WORKDIR $USER_HOME/app

# Copy project files
COPY --chown=apiuser project/ project/
COPY --chown=apiuser manage.py manage.py
COPY --chown=apiuser scripts/ scripts/
