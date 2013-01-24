pythongrid overview

This module provides high level functionality for cluster computing in python using the Sun Grid Engine. As some cluster environments are notoriously unreliable, pythongrid attempts to handle job monitoring and resubmission (in case of sudden death of nodes) under the hood, while providing the user with a simple map-reduce like interface.

Main features:
- Uses ZMQ-based heart-beat to monitor job status
- Robust error detection (out-of-memory, node failure)
- Automated resubmission in case of unexpected failure
- Error emails, including CPU/MEM statistics
- Optional web-interface to monitor jobs
- Let's you easily switch between local multiprocessing and cluster computing

Dependencies
- pyZMQ
- drmaa-python

related projects
- ruffus
