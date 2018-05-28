FROM alpine:latest

COPY . /var/app

RUN chmod +x /var/app/run.sh

WORKDIR /var/app/

RUN apk update && \
 apk add python3 libffi libjpeg && \
 apk add --virtual .build-deps gcc jpeg-dev openjpeg-dev python3-dev zlib-dev libffi-dev musl-dev  curl && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

EXPOSE 8080

WORKDIR /var/app/

CMD /var/app/run.sh
