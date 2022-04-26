==================
Pipeline Framework
==================

Core Layer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generally you will never need to touch these plugins in order to customize Connect 2.


ftrack-connect-pipeline

The core plugin that runs the framework Host - responsible for loading and validating schema definitions and running pipeline plugins. Does not require a user interface, can be run isolated within a DCC application in remote mode.

Here would be a good place to put shared integration code that will be used across all DCC applications, for example functions that apply statuses and resolve paths to work scenes.

Definition layer
^^^^^^^^^^^^^^^^
ftrack-connect-pipeline-definition

A set of JSON definition schemas and corresponding framework plugins, where each definition defines loading or publishing of a certain ftrack asset type.

This is the repository you customise to your studio needs, together with the integration plugins when the DCC app needs bootstrapping or further extension.

UI layer
^^^^^^^^

ftrack-connect-pipeline-qt
The Qt/PySide2 abstraction layer plugin, driving user interface widgets inside DCC apps.