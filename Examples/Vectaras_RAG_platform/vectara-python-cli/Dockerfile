FROM python:3.8-slim

ENV VECTARA_CUSTOMER_ID=123
ENV VECTARA_CLIENT_ID=abc
ENV VECTARA_CLIENT_SECRET=xyz
# Optional for using a proxy like LlaMasterKey
# ENV VECTARA_BASE_URL=http://127.0.0.1:8000/vectara

WORKDIR /src

COPY . /src

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

ENV NAME World

CMD ["funix" , "src/vectara/__init__.py "]
