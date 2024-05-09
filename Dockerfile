FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /scripts

# Install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install psycopg2
RUN pip install --no-cache-dir psycopg2-binary

# Copy scripts directory into the container
COPY . /scripts/

# Expose the port that the application runs on
EXPOSE 8000


CMD ["python", "manage.py"]
