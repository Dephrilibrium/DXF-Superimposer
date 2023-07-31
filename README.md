# DXF-Superimposer

When designing masks for wafer exposure processes, we are using DXFs. For some reason, sometimes the DXF-mask entities not completely closed, even if they should be. Therefore this script was developed. It searches for possibly open entities and superimposes all start- and endpoints with neighbour entities, so that the circumfences can be closed by the designer-tools (AutoCAD for instance).
This script was more or less done quick and dirty, which is why it not catches all problems. You may need to play bit around with your tolerance, until it works

### How to setup

* 1\. Install Python3 ([Python3])__
  * 1\.1\. Make sure, pip is working too
* 2\. Install IDE (e.g.: [VSCode])
  * 2\.1\. Install Python Extensions
* 3\. Install python packages `pip install matplotlib ezdxf colorama`

### How to use
* 1\. Create your mask (e.g. AutoCAD)
* 2\. Export your mask as DXF (tested with r12 version, as our mask writer use this format)
* 3\. Use this script on your DXF
  * 3\.1\. Estimate your tolerance correctly, otherwise that can cause some exceptions!
      Try to give a tolerance value just slightly higher than the biggest distance you try to close!
* 4\. Reload the superimposed DXF by your DXF-tool
* 5\. Connect the separated entities to one closed circumfence





code by haum(2023)


[VSCode]: [https://code.visualstudio.com/#alt-downloads]
[Python3]: [https://www.python.org/downloads/]