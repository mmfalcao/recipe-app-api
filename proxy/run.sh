#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/default.conf
nginx -g 'daemon off;'