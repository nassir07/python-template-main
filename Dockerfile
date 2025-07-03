From registry.git.technica-engineering.net/data/templates/python-template/base_image:1.0.0
# Set the working directory to /app
RUN odbcinst -q -d -n

WORKDIR /app

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock /app/

# Install Python dependencies from the Pipfile
RUN pipenv install --system --deploy --extra-pip-args="--index-url https://nexus.technica-engineering.net/repository/pypi-group/simple --proxy http://squid.technica-engineering.net:3128"


# Copy the rest of the application files
COPY . /app/

# Default command (you can override this in Jenkins)
CMD ["python"]
