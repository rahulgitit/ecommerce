FROM python

# 3. Set the working directory in the container
WORKDIR /app

# 4. Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 5. Copy the project files into the container
COPY . /app

# 6. Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]