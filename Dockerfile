FROM python:3.10

WORKDIR /usr/src/app

COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements

# Run bot.py when the container launches
CMD ["python", "./bot.py"]
