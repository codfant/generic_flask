# generic_flask

## About ##

This is a generic Flask app for use as an example of how to build an opensource project.

## How to run the Flask app ##

codfant@blah $ python3.6 flask_app.py
 * Running on http://0.0.0.0:32989/ (Press CTRL+C to quit)


## How to generate a self signed cert... ##

As a side note, if you are going to use HTTPS, as best practice please generate a new certificate. Don't use the one included with this project. The certificate is merely included to give an example of a working HTTPS version.

openssl genrsa -out server.key 1024  

openssl req -new -key server.key -out server.csr  

openssl x509 -req -days 3650 -in server.csr -signkey server.key -out server.crt  


EXAMPLE:
codfant@blah $ openssl genrsa -out server.key 1024

codfant@blah $ openssl req -new -key server.key -out server.csr

You are about to be asked to enter information that will be incorporated

into your certificate request.

What you are about to enter is what is called a Distinguished Name or a DN.

There are quite a few fields but you can leave some blank

For some fields there will be a default value,

If you enter '.', the field will be left blank.

Country Name (2 letter code) [AU]:

State or Province Name (full name) [Some-State]:

Locality Name (eg, city) []:

Organization Name (eg, company) [Internet Widgits Pty Ltd]:

Organizational Unit Name (eg, section) []:

Common Name (e.g. server FQDN or YOUR name) []:

Email Address []:


Please enter the following 'extra' attributes

to be sent with your certificate request

A challenge password []:

An optional company name []:

codfant@blah $ openssl x509 -req -days 3650 -in server.csr -signkey server.key -out server.crt
