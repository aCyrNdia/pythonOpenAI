FROM python:3.7

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENV OPENAI_API_KEY=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

CMD ["python3", "python-chatgpt.py"]
