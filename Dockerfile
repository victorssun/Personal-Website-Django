FROM python:3.7

WORKDIR /home/code

COPY . /home/code/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

# ADD start.sh /home/code
# RUN chmod +x /home/code/start.sh
# CMD ["/home/code/start.sh"]
