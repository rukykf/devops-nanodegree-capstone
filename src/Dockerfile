FROM php:7.3-apache

LABEL maintainer="Kofi Oghenerukevwe"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y curl zip unzip\
    && curl -sS https://getcomposer.org/installer | php -- --filename=composer --install-dir=/bin \
    && apt install -y finger

RUN apt install -y nano

ENV PATH /root/.composer/vendor/bin:$PATH
COPY . /var/www/html/
EXPOSE 80

WORKDIR /var/www/html
RUN composer install
RUN rm /etc/apache2/sites-enabled/000-default.conf \
    && mv 000-default.conf /etc/apache2/sites-enabled/000-default.conf
