import matplotlib.pyplot as plt
import ezdxf as dxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from time import time
from os.path import join, dirname, basename

from SI_lib.functions import *
from SI_lib.tLog import LogLine




tolerance = 1e-3                                # In base-units of the DXF (test-dxf was in [mm])
fNames = [                                      # Append your DXF-files here (".dxf" extension is optional!)
r".\TestDXFs\2x Arc defined angles.dxf",
r".\TestDXFs\2x Line, 2x Poly, 2x Arc.dxf",
r".\TestDXFs\EasyTri.dxf",
r".\TestDXFs\TestDrawOpened.dxf",
]
showDXFs = False                                # Open figures showing the changes (before/after) -> normally only used for debug puposes






























######## DO NOT TOUCH AREA ########
for _fName in fNames:
    # t0 = time()
    fName = join(dirname(_fName), basename(_fName))
    fName = fName.removesuffix(".dxf")
    lName = fName + ".dxf"
    LogLine(f"Applying DXF-superimposer on {lName}")
    doc = dxf.readfile(lName)
    LogLine("Read DXF")

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
        LogLine("Drawed original DXF in a figure")

    msp = doc.modelspace()
    dxfEntities = msp.query("*").entities
    LogLine("Extracted all entities")

    dxfTypes = DetermineDXFTypes(dxfEntities)
    LogLine("Found this entity-types:")
    for _iDXFType in range(len(dxfTypes["Types"])):
        _type = dxfTypes["Types"][_iDXFType]
        _cnt = dxfTypes["Counts"][_iDXFType]
        if handledEntities.__contains__(_type):
            print(f"- {Fore.YELLOW}Detected:{Fore.RESET}".ljust(31) + f"{Fore.BLUE}{_cnt:8d}x{Fore.RESET}".ljust(25) + f"\"{Fore.GREEN}{_type}{Fore.RESET}\"".ljust(20) +f"-entity".ljust(10) + f"({Fore.GREEN}OK{Fore.RESET})")
        else:
            print(f"- {Fore.YELLOW}Detected:{Fore.RESET}".ljust(31) + f"{Fore.BLUE}{_cnt:8d}x{Fore.RESET}".ljust(25) + f"\"{Fore.RED}{_type}{Fore.RESET}\"".ljust(20) +f"-entity".ljust(10) + f"({Fore.RED}Not implemented -> skipped{Fore.RESET})")
    print(f"Entities found:".ljust(28) + f"{Fore.BLUE}{dxfTypes['CountAll']}{Fore.RESET}")

    LogLine("Start with superimposing entities:")
    dxfTypes = IterateThroughEntities(entities=dxfEntities, dTol=tolerance)
    LogLine("Finished superimposing entities")


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
        LogLine("Drawed superimposed DXF in a figure")


    sName = fName + "-Superimposed.dxf"
    doc.saveas(filename=sName)
    LogLine(f"Saved superimposed dxf as: {sName}")



print("EOS")