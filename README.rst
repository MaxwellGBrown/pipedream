==========
Pipe Dream
==========

A demo of the python package Luigi

Development Quickstart
----------------------

Use `Docker <https://www.docker.com>`__ to develop!

#. Build the docker image

   :: 
   
     $ docker build -t pipedream .


#. Use the docker image to run commands

   ::

     $ docker run -v $(pwd):/pipedream pipedream <do a thing> 
