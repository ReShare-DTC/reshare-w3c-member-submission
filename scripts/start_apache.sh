#!/bin/bash
docker create -it --rm --name reshare-apache -p 8080:80 -v "$PWD"/public/:/usr/local/apache2/htdocs/ httpd:2.4
docker cp httpd.conf reshare-apache:/usr/local/apache2/conf/httpd.conf
docker start reshare-apache
