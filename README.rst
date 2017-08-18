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

**OR**

#. Run a task without the remote scheduler

   ::

     $ docker run -v $(pwd):/pipedream -p 8082:8082 pipedream luigi --module<module_name> --local-scheduler <task_name>
 

Tests
-----

To run the tests for this app's "business logic"...

::

  $ docker run pipedream pytest


**OR** for a running ``pipedream`` container...

::

  $ docker exec -it pipedream pytest

Writing Unit Tests
~~~~~~~~~~~~~~~~~~

You *should avoid embedding business logic in your Luigi tasks*! This means any tests you run against your Luigi tasks are *technically not* "Unit" tests.

The best practice for testing your Luigi code would be to break out the business logic into a different module and unit test *that*.

The closest a Luigi task can get to unit tests would be testing that ``Task.run()`` calls the correct "business logic" modules.


Writing Functional Tests
~~~~~~~~~~~~~~~~~~~~~~~~

It's not infeasable to write Functional test for Luigi tasks!

Just remember that, if you're running functional tests, you're taking a much bigger bite out of your resources than your unit tests. 

One test might look like...

#. Initialize a task
#. Mock some data/services
#. Check the result of the run task
    
   **e.g.** Check that a CSV was written to, check that a postgres mock was called, check that a file was created
