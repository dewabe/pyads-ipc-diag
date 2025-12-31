pyads-ipc-diag
==============

Python library for reading Beckhoff IPC Diagnostics data via ADS using pyads.

.. note::

   This documentation is a work in progress.

Installation
------------

Install the package directly from PyPi:

.. code-block:: bash

   pip install pyads-ipc-diag


Getting started
---------------

**Command line usage**

.. code-block:: bash

   pyads-ipc-diag --ams-net-id [ams_net_id] --module [module] --json [output file]

Where

* ams_net_id is the AMS Net ID of the target device (you must have a router created!)
* module is the module you want to read, or use parameter 'all' to read all available ones
* output file is the file name you want to store the data in json format

For more information use

.. code-block:: bash

   pyads-ipc-diag --help


**Import the library**:

.. code-block:: python

   import pyads_ipc_diag as bhf


Create a connection
-------------------

Ensure you have created a route to your device.

Create an ADS connection using the IPC AMS Net ID:

.. code-block:: python

   with bhf.MDP("10.10.10.11.1.1") as ipc:


High-level diagnostics
----------------------

The library provides high-level access to common IPC Diagnostics modules.

Available modules:

* CPU
* Fan
* Mainboard
* Memory
* NIC
* OS
* Software
* Time
* TwinCAT
* UserManagement

Example to read TwinCAT information:

.. code-block:: python

   tc = bhf.TwinCAT(ipc)
   print(tc.info())

Low-level access
----------------

You can also read values directly by address using the low-level API:

.. code-block:: python

   value = ipc.read(module, table_base, subindex, plc_type)
