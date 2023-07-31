import matplotlib.pyplot as plt
import ezdxf as dxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from time import time

from SI_lib.functions import *
from SI_lib.tLog import LogLine




tolerance = 3       # In base-units of the DXF (test-dxf was in [mm])

fName = r"TestDXFs/2x Line, 2x Poly, 2x Arc"
showDXFs = True


















######## DO NOT TOUCH AREA ########
t0 = time()
doc = dxf.readfile(f"{fName}.dxf")
LogLine(t0, "Read DXF")

## Vorher
if showDXFs:
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ctx = RenderContext(doc)
    out = MatplotlibBackend(ax)
    Frontend(ctx, out).draw_layout(doc.modelspace(), finalize=True)
    plt.show(block=False)
    # fig.suptitle("Original DXF (vorher)")
    # ax.set_xlabel("x")
    # ax.set_ylabel("y")
    # fig.savefig('your.png', dpi=300)
    LogLine(t0, "Drawed original DXF in a figure")

msp = doc.modelspace()
dxfEntities = msp.query("*").entities
LogLine(t0, "Extracted all entities")

dxfTypes = DetermineDXFTypes(dxfEntities)
print("Found this entity-types:")
for _iDXFType in range(len(dxfTypes["Types"])):
    _type = dxfTypes["Types"][_iDXFType]
    _cnt = dxfTypes["Counts"][_iDXFType]
    if handledEntities.__contains__(_type):
        print(f"- {Fore.YELLOW}Detected:{Fore.RESET}".ljust(15) + f"{Fore.BLUE}{_cnt:8d}x{Fore.RESET}".ljust(25) + f"\"{Fore.GREEN}{_type}{Fore.RESET}\"".ljust(20) +f"-entity".ljust(20) + f"({Fore.GREEN}OK{Fore.RESET})")
    else:
        print(f"- {Fore.YELLOW}Detected:{Fore.RESET}".ljust(15) + f"{Fore.BLUE}{_cnt:8d}x{Fore.RESET}".ljust(25) + f"\"{Fore.RED}{_type}{Fore.RESET}\"".ljust(20) +f"-entity".ljust(20) + f"({Fore.RED}No implemented, !!! MAY !!! cause problems{Fore.RESET})")

LogLine(t0, "Start with superimposing entities:")
dxfTypes = IterateThroughEntities(entities=dxfEntities, dTol=tolerance)
LogLine(t0, "Finished superimposing entities")


## Nachher
if showDXFs:
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ctx = RenderContext(doc)
    out = MatplotlibBackend(ax)
    Frontend(ctx, out).draw_layout(doc.modelspace(), finalize=True)
    plt.show(block=False)
    # fig.savefig('your.png', dpi=300)
    # fig.suptitle("Modified DXF (nachher)", color="white")
    # ax.set_xlabel("x")
    # ax.set_ylabel("y")
    LogLine(t0, "Drawed superimposed DXF in a figure")


sName = f"{fName}_Superimposed.dxf"
doc.saveas(filename=sName)
LogLine(t0, f"Saved superimposed dxf as: {sName}")



print("EOS")