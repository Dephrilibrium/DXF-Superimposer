# DXF-Superimposer

At the OTH we design lithography-masks for clean room exposure processes. They are written, using a HEIDELBERG DWL 66+. The mask-designs are typically created with AutoCAD (2D) and exported as DXF (version r12). For some reason, sometimes the design-entities (LINE, POLYLINE, ARC) not forming only closed circumfences. As the mask-design needs to be converted from DXF into for the DWL understandable files, open circumfences disables the conversion of the DXF-mask.

Therefore this script was developed. It searches for implemented  and possibly open entities and superimposes close located start- and endpoints, which is done by:
* 1\.) Build a list of all supported entities (LINE, POLYLINE, ARC)
* 2\.) Grab a main entity `ent` and remove it from the list (this one gets modified)
* 3\.) Check its DXF-type (LINE, POLYLINE, ARC)
* 4\.) Iterate through the residual compare-entities (compare-entity-variable `ent2`) and check if the any distance between their start- and end-points are smaller than the tolerance. If this applies, the point of `ent`, which fulfills that condition is overwritten with the corresponding coordinate of `ent2`
* 5\.) 4.) is repeating until 2 superimposings were done (each entity only have 2 points), the compare-entity iteration is stopped, the script restarts at 2\.) using the next main-entity.
 
Thereby, the distance (max. tolerance between 2 points) can be adjusted. The value needs to be slightly higher than the biggest estimated distance between 2 points which should be on the exact same location.


### How to setup

* 1\.) Install Python3 ([Python3])__
  * 1\.1\.) Make sure, pip is working too
* 2\.) Install IDE (e.g.: [VSCode])
  * 2\.1\.) Install Python Extensions
* 3\.) Install python packages `pip install matplotlib ezdxf colorama`

### How to use
* 1\.) Create your mask-design and make sure, there are not groups or blocks
* 2\.) Export your mask-design as DXF (tested with: AutoCAD DXF version r12)
* 3\.) Use this script on your DXF
  * 3\.1\.) Estimate your tolerance correctly, otherwise that can cause some exceptions!<br />
    *  Is a tolerance to high, then you will may face wrong superimposed points or even an exception.<br />
    *  Is your tolerance too small, may not all entities will be superimposed.
* 4\.) Reload the superimposed DXF by your DXF-tool
* 5\.) Connect the separated entities to one closed circumfence

### Pre- and Post-image of the test-DXF "2x Line, 2x Poly, 2x Arc.dxf"
![2x Line, 2x Poly, 2x Arc - Pre-Superimpose](https://github.com/Dephrilibrium/DXF-Superimposer/assets/89015665/48e9a234-f01c-45b5-8632-5831ccbcfd60)
![2x Line, 2x Poly, 2x Arc - Post-Superimpose](https://github.com/Dephrilibrium/DXF-Superimposer/assets/89015665/2f216e73-21f3-422b-ad36-dc8cd61c8605)



code by haum(2023)


[VSCode]: [https://code.visualstudio.com/#alt-downloads]
[Python3]: [https://www.python.org/downloads/]