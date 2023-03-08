FROM python:3.7

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENV OPENAI_API_KEY

CMD ["python3", "python-chatgpt.py"]
