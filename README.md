About this tutorial
-------------------
This tutorial is aimed to show you the basics of DDS data-centric model.

For the sake of simplicity, this tutorial is based on the Python RTI Connector API,
which simplifies the development and let the user focus on the basic concepts rather
than learning a complex API.

Requirements
------------
- python
- virtualenv package
- git (to download RTI Connector)

Preparing your environment
--------------------------
Run the ./setup script. This will download the RTI Connector API from
the repository and create a python virtual environment

The script performs the following tasks:

- Clone RTI Connector from the official github repository
- Create a python virtual environment under rticonnectorenv/
- Installs the RTI Connector in the rticonnectorenv environment

Exercises
-------------------------
This tutorial contans the following exercises

- ex1-basic: Basic communication using publish/subscribe
- ex2-filtering: Filtering
	- Time Based Filtering
	- Content Based Filtering
- ex3-ha: High Availability: 
	- Ownership
- ex4-durability: Late Joiners
- ex5-isolation: Partitioning/Isolation

Running the exercises
---------------------
To avoid requiring administrator rights to install RTI Connector in
your system, the examples are prepared to be run using a python virtual
environment. For this reason, it is important to run the following command
in each terminal window you open before running the scripts:

  source rticonnectorenv/bin/activate




