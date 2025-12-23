pyads-ipc-diag
==============

Python library for reading Beckhoff IPC Diagnostics data via ADS using pyads.

.. note::

   This documentation is a work in progress.

Installation
------------

Install the package directly from GitHub:

.. code-block:: bash

   pip install git+https://github.com/dewabe/pyads-ipc-diag.git


Getting started
---------------

Import the library:

.. code-block:: python

   import pyads_ipc_diag


Create a connection
-------------------

Create an ADS connection using the IPC AMS Net ID:

.. code-block:: python

   with pyads_ipc_diag.MDP("10.10.10.11.1.1") as ipc:
       ipc.update_modules()


High-level diagnostics
----------------------

The library provides high-level access to common IPC Diagnostics modules.

TwinCAT information:

.. code-block:: python

   tc = pyads_ipc_diag.TwinCAT(ipc)


CPU information:

.. code-block:: python

   cpu = pyads_ipc_diag.CPU(ipc)


Memory information:

.. code-block:: python

   memory = pyads_ipc_diag.Memory(ipc)


Mainboard information:

.. code-block:: python

   mainboard = pyads_ipc_diag.Mainboard(ipc)


Low-level access
----------------

You can also read values directly by address using the low-level API:

.. code-block:: python

   value = ipc.read(module, table_base, subindex, plc_type)
