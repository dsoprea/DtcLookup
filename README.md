Diagnostic Trouble Code (DTC) Lookup
====================================

Description
-----------

    This website is a simple lookup utility for SAE (automotive) DTC codes. It can be accessed by hand, but is intended to be implemented by software utilities as a tool to produce meaningful messages from codes read from vehicles via OBDII diagnostic hardware.


Usage
-----

    http://localhost:8080/lookup/dtc/code/<code>


Example
-------

    http://localhost:8080/lookup/dtc/code/P0442


Sample Result
-------------

```{ "Data": [["Generic", 
            "Evaporative Emission Control System Leak Detected (small leak)"], 
           ["Landrover", 
            "Evap System Small Leak Detected Fault"]], 

  "Error": null }
```
    
    The result is a JSON-encoded dictionary with the members "Data" and "Error". "Data" is a list of lists, where the latter always has a length of two. The first item is a category (usually the make of the vehicle, or "Generic"), and the second is the description.

    If "Error" is not NULL, then an error occurred.


Notes
-----

The dtcdatabase.com website runs using this project.

The DTC lists used for this project are courtesy of the "scantool" (http://www.scantool.net/downloads/archive/diagnostic-software) project.


