FROM ubuntu:18.04

LABEL maintainer="Kofi Oghenerukevwe"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y php7.2 php7.2-xdebug curl \
       php-dom \
       php-mbstring \
       php-zip \
    && curl -sS https://getcomposer.org/installer | php -- --filename=composer --install-dir=/bin

ENV PATH /root/.composer/vendor/bin:$PATH

EXPOSE 80

WORKDIR /var/www/html
