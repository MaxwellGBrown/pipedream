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


#. Start the remote scheduler

   ::

     $ docker run -v $(pwd):/pipedream -p 8082:8082 -d --name pipedream pipedream

#. Run a task using the remote scheduler

   ::

     $ docker exec -it pipedream luigi --module <module_name> <task_name>

*OR*

#. Run a task without the remote scheduler

   ::

     $ docker run -v $(pwd):/pipedream -p 8082:8082 pipedream luigi --module<module_name> --local-scheduler <task_name>
 
