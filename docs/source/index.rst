.. tutorial documentation master file, created by
   sphinx-quickstart on Sun Mar 19 14:56:00 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to tutorial's documentation!
====================================
Shown above is a typical respiratory waveform (without averaging) as produced with PVP1. Blue is the recorded pressure, orange is the flow out of the system. Note that airflow (and also oxygen concentration) are only measured during expiration, so that the main control-loop during inspiration runs as fast as possible, and is not slowed down by communication delays. Pressure is recorded continuously. Empirically, the Raspberry pi allowed for the primary control loop to run at speeds of ~5ms per loop, which was considerably faster than all hardware delays (i.e. the time it takes for a mechanical, physical valve to open or close; see main manuscript).

The purpose of the controller is to produce a breath waveform, as the one shown above. More specifically, it’s job is to reach a certain target-pressure (PIP), and to hold that pressure for a certain amount of time. These numbers are provided by the user via thee UI. Exhalation is passive, and PEEP pressure is mechanically controlled with a spring-valve.

Conceptually, the controller is written as a hybrid system of state and PID control. During inspiration, it actively controls pressure with a simple
Shown above is a typical respiratory waveform (without averaging) as produced with PVP1. Blue is the recorded pressure, orange is the flow out of the system. Note that airflow (and also oxygen concentration) are only measured during expiration, so that the main control-loop during inspiration runs as fast as possible, and is not slowed down by communication delays. Pressure is recorded continuously. Empirically, the Raspberry pi allowed for the primary control loop to run at speeds of ~5ms per loop, which was considerably faster than all hardware delays (i.e. the time it takes for a mechanical, physical valve to open or close; see main manuscript).

The purpose of the controller is to produce a breath waveform, as the one shown above. More specifically, it’s job is to reach a certain target-pressure (PIP), and to hold that pressure for a certain amount of time. These numbers are provided by the user via thee UI. Exhalation is passive, and PEEP pressure is mechanically controlled with a spring-valve.

Conceptually, the controller is written as a hybrid system of state and PID control. During inspiration, it actively controls pressure with a simple

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Our class
==================

.. automodule:: tutorialclass
    :members:
    :undoc-members:
    :inherited-members:
    :show-inheritance:

Testcode
==================
We can write some text. Blablabla.

.. automodule:: test_tutorialclass
    :members:
    :undoc-members:
    :inherited-members:
    :show-inheritance:

This is to show possibilities
====================================
Today we're doin a tutorial on documentation and coding. This is fun