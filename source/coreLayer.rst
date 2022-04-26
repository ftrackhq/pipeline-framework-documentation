==========
Core Layer
==========


Generally you will never need to touch these plugins in order to customize Connect 2.

.. autosummary::
   :toctree: generated

   ftrack-connect-pipeline

The core plugin that runs the framework Host - responsible for loading and validating schema definitions and running pipeline plugins. Does not require a user interface, can be run isolated within a DCC application in remote mode.

Here would be a good place to put shared integration code that will be used across all DCC applications, for example functions that apply statuses and resolve paths to work scenes.
