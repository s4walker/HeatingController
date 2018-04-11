Development Guide
=================

The purpose of the Heating Controller project is to control a preparation
chamber for a scanning tunneling microscope. To do this, two problems were
identified.

1. Communicate with a heater and a pressure controller to read out meaningful
    values
2. Set up a series of tasks that the heater and pressure controller should
    do.

The First Problem
-----------------

In order to solve this problem, create a class for the ``TDKLambda`` heater
and the ``PhCiPressureController``. These will both be subclasses of an
``Instrument`` class. These classes will encapsulate the classes from
``instrumentkit``.

The Second Problem
------------------

Use the intepreter pattern to create a list of tasks that the system can
execute. These tasks make a monoid under composition. The basic list of tasks
that need to be done is the identity task, repeating task, and a conditional
instruction. Scheduling will need to be done carefully in order to run
everything in an executor.
