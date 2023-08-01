from ezdxf.math import ConstructionArc
from colorama import Fore

ljustLen = 20
ljustLen2 = 35
handledEntities = ["LINE", "POLYLINE", "ARC"]


def CheckVec3InRange(start, end, dTol):
    dVec = start - end
    if dVec.magnitude <= dTol:
        return end.copy(), True
    return start.copy(), False


def LineOnLine(Line1, Line2, dTol):
    replCnt = 0
    Line1.dxf.start, replaced = CheckVec3InRange(start=Line1.dxf.start, end=Line2.dxf.start, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Line1}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}startpoint{Fore.RESET}")

    Line1.dxf.start, replaced = CheckVec3InRange(start=Line1.dxf.start, end=Line2.dxf.  end, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Line1}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}startpoint{Fore.RESET}")
        
    Line1.dxf.  end, replaced = CheckVec3InRange(start=Line1.dxf.  end, end=Line2.dxf.start, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Line1}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}endpoint{Fore.RESET}")
        
    Line1.dxf.  end, replaced = CheckVec3InRange(start=Line1.dxf.  end, end=Line2.dxf.  end, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Line1}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}endpoint{Fore.RESET}")
        
    return replCnt

def LineOnPolyline(Line, Polyline, dTol):
    replCnt = 0
    pV = Polyline.vertices
    Line.dxf.start, replaced = CheckVec3InRange(start=Line.dxf.start, end=pV[ 0].dxf.location, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Line}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}startpoint{Fore.RESET}")

    Line.dxf.start, replaced = CheckVec3InRange(start=Line.dxf.start, end=pV[-1].dxf.location, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Line}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}startpoint{Fore.RESET}")

    Line.dxf.  end, replaced = CheckVec3InRange(start=Line.dxf.  end, end=pV[ 0].dxf.location, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Line}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}endpoint{Fore.RESET}")

    Line.dxf.  end, replaced = CheckVec3InRange(start=Line.dxf.  end, end=pV[-1].dxf.location, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Line}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}endpoint{Fore.RESET}")

    return replCnt

def LineOnArc(Line, Arc, dTol):
    replCnt = 0
    Line.dxf.start, replaced = CheckVec3InRange(start=Line.dxf.start, end=Arc.start_point, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Line}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}startpoint{Fore.RESET}")

    Line.dxf.start, replaced = CheckVec3InRange(start=Line.dxf.start, end=Arc.  end_point, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Line}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}startpoint{Fore.RESET}")

    Line.dxf.  end, replaced = CheckVec3InRange(start=Line.dxf.  end, end=Arc.start_point, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Line}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}endpoint{Fore.RESET}")

    Line.dxf.  end, replaced = CheckVec3InRange(start=Line.dxf.  end, end=Arc.  end_point, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Line}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}endpoint{Fore.RESET}")

    return replCnt

def PolyOnPoly(Polyline1, Polyline2, dTol):
    replCnt = 0
    pV1 = Polyline1.vertices
    pV2 = Polyline2.vertices
    pV1[ 0].dxf.location, replaced = CheckVec3InRange(start=pV1[ 0].dxf.location, end=pV2[ 0].dxf.location, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Polyline1}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}first vertex{Fore.RESET}")

    pV1[ 0].dxf.location, replaced = CheckVec3InRange(start=pV1[ 0].dxf.location, end=pV2[-1].dxf.location, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Polyline1}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}first vertex{Fore.RESET}")

    pV1[-1].dxf.location, replaced = CheckVec3InRange(start=pV1[-1].dxf.location, end=pV2[ 0].dxf.location, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Polyline1}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}last vertex{Fore.RESET}")

    pV1[-1].dxf.location, replaced = CheckVec3InRange(start=pV1[-1].dxf.location, end=pV2[-1].dxf.location, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Polyline1}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}last vertex{Fore.RESET}")

    return replCnt

def PolyOnArc(Polyline, Arc, dTol):
    replCnt = 0
    pV = Polyline.vertices
    pV[ 0].dxf.location, replaced = CheckVec3InRange(start=pV[ 0].dxf.location, end=Arc.start_point, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Polyline}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}first vertex{Fore.RESET}")

    pV[ 0].dxf.location, replaced = CheckVec3InRange(start=pV[ 0].dxf.location, end=Arc.  end_point, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Polyline}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}first vertex{Fore.RESET}")

    pV[-1].dxf.location, replaced = CheckVec3InRange(start=pV[-1].dxf.location, end=Arc.start_point, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Polyline}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}last vertex{Fore.RESET}")

    pV[-1].dxf.location, replaced = CheckVec3InRange(start=pV[-1].dxf.location, end=Arc.  end_point, dTol=dTol)
    if replaced:
        replCnt += 1
        print(f"{Polyline}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}last vertex{Fore.RESET}")

    return replCnt

def ArcOnArc(Arc1, Arc2, dTol):
    replCnt = 0
    tPnt, replaced = CheckVec3InRange(start=Arc1.start_point, end=Arc2.start_point, dTol=dTol)
    if replaced:
        replCnt += 1
        cArc = DetermineNewConstructionArc(Arc=Arc1, Pnt=tPnt, PntIsStart=True)
        Arc1.dxf.center         = cArc.center
        Arc1.dxf.radius         = cArc.radius
        Arc1.dxf.start_angle    = cArc.start_angle
        Arc1.dxf.end_angle      = cArc.end_angle
        print(f"{Arc1}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}startpoint {Fore.RESET}& {Fore.YELLOW}center{Fore.RESET}")


    tPnt, replaced = CheckVec3InRange(start=Arc1.start_point, end=Arc2.  end_point, dTol=dTol)
    if replaced:
        replCnt += 1
        cArc = DetermineNewConstructionArc(Arc=Arc1, Pnt=tPnt, PntIsStart=True)
        Arc1.dxf.center         = cArc.center
        Arc1.dxf.radius         = cArc.radius
        Arc1.dxf.start_angle    = cArc.start_angle
        Arc1.dxf.end_angle      = cArc.end_angle
        print(f"{Arc1}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}startpoint {Fore.RESET}& {Fore.YELLOW}center{Fore.RESET}")

    tPnt, replaced = CheckVec3InRange(start=Arc1.  end_point, end=Arc2.start_point, dTol=dTol)
    if replaced:
        replCnt += 1
        cArc = DetermineNewConstructionArc(Arc=Arc1, Pnt=tPnt, PntIsStart=False)
        Arc1.dxf.center         = cArc.center
        Arc1.dxf.radius         = cArc.radius
        Arc1.dxf.start_angle    = cArc.start_angle
        Arc1.dxf.end_angle      = cArc.end_angle
        print(f"{Arc1}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}endpoint {Fore.RESET}& {Fore.YELLOW}center{Fore.RESET}")

    tPnt, replaced = CheckVec3InRange(start=Arc1.  end_point, end=Arc2.  end_point, dTol=dTol)
    if replaced:
        replCnt += 1
        cArc = DetermineNewConstructionArc(Arc=Arc1, Pnt=tPnt, PntIsStart=False)
        Arc1.dxf.center         = cArc.center
        Arc1.dxf.radius         = cArc.radius
        Arc1.dxf.start_angle    = cArc.start_angle
        Arc1.dxf.end_angle      = cArc.end_angle
        print(f"{Arc1}:".ljust(ljustLen) + f"{Fore.GREEN}Superimposed ".ljust(ljustLen2) + f"{Fore.YELLOW}endpoint {Fore.RESET}& {Fore.YELLOW}center{Fore.RESET}")
        
    return replCnt


def DetermineNewConstructionArc(Arc, Pnt, PntIsStart):
    arcR     = Arc.dxf.radius
    arcStrtP = Arc.start_point
    arcEndP  = Arc.end_point

    if PntIsStart:
        cArc = ConstructionArc.from_2p_radius(start_point=Pnt, end_point=arcEndP, radius=arcR)
    else:
        cArc = ConstructionArc.from_2p_radius(start_point=arcStrtP, end_point=Pnt, radius=arcR)
    
    return cArc







    dummy, replaced = CheckVec3InRange(start=Arc1.  end_point, end=Arc2.start_point, dTol=dTol)
    dummy, replaced = CheckVec3InRange(start=Arc1.  end_point, end=Arc2.  end_point, dTol=dTol)



    return


def IterateThroughEntities(entities, dTol):
    _nEntities = len(entities)
    if _nEntities <= 0:
        return

    _dPerc = 1/_nEntities * 100

    _nCount = 0
    _perDone = 0
    for ent in entities:
        entities.remove(ent)
        _perDone += _dPerc
        print(f"{Fore.BLUE}Checking entity[{_nCount}]:".ljust(32) + f" {Fore.RED}{ent}{Fore.RESET}".ljust(25) + f"({_nCount+1:7d}/{_nEntities:7d} = {_perDone:3.3f}%)")
        _nCount += 1

        _replaceCount = 0 # Each element (LINE; POLYLINE; ARC) only have start_point and end_point -> Therefore it can only be 2x a superimpose happen. If they are done, all other compares are nonsense -> Directly head on to the next entity for "ent"
        if ent.DXFTYPE == "LINE":
            for ent2 in entities:
                if _replaceCount >= 2:
                    print(f"{ent}:".ljust(ljustLen) + f"{Fore.GREEN}2 replacements done ".ljust(ljustLen2) + f"{Fore.YELLOW}Skipping the rest of the compares!{Fore.RESET}")
                    break

                if ent2.DXFTYPE == "LINE":
                    _replaceCount += LineOnLine(Line1=ent, Line2=ent2, dTol=dTol)
                elif ent2.DXFTYPE == "POLYLINE":
                    _replaceCount += LineOnPolyline(Line=ent, Polyline=ent2, dTol=dTol)
                elif ent2.DXFTYPE == "ARC":
                    _replaceCount += LineOnArc(Line=ent, Arc=ent2, dTol=dTol)
                else:
                    continue


        elif ent.DXFTYPE == "POLYLINE":
            for ent2 in entities:
                if _replaceCount >= 2:
                    print(f"{ent}:".ljust(ljustLen) + f"{Fore.GREEN}2 replacements done ".ljust(ljustLen2) + f"{Fore.YELLOW}Skipping the rest of the compares!{Fore.RESET}")
                    break

                if ent2.DXFTYPE == "LINE":
                    _replaceCount += LineOnPolyline(Line=ent2, Polyline=ent, dTol=dTol)
                elif ent2.DXFTYPE == "POLYLINE":
                    _replaceCount += PolyOnPoly(Polyline1=ent, Polyline2=ent2, dTol=dTol)
                elif ent2.DXFTYPE == "ARC":
                    _replaceCount += PolyOnArc(Polyline=ent, Arc=ent2, dTol=dTol)
                else:
                    continue


        elif ent.DXFTYPE == "ARC":
            for ent2 in entities:
                if _replaceCount >= 2:
                    print(f"{ent}:".ljust(ljustLen) + f"{Fore.GREEN}2 replacements done ".ljust(ljustLen2) + f"{Fore.YELLOW}Skipping the rest of the compares!{Fore.RESET}")
                    break

                if ent2.DXFTYPE == "LINE":
                    _replaceCount += LineOnArc(Line=ent2, Arc=ent, dTol=dTol)
                elif ent2.DXFTYPE == "POLYLINE":
                    _replaceCount += PolyOnArc(Polyline=ent2, Arc=ent, dTol=dTol)
                elif ent2.DXFTYPE == "ARC":
                    _replaceCount += ArcOnArc(Arc1=ent, Arc2=ent2, dTol=dTol)
                else:
                    continue
        print("") # Add a new line
    return



def DetermineDXFTypes(entities):
    dxfStats = {}
    dxfStats["Types"] = []
    dxfStats["Counts"] = []
    dxfStats["CountAll"] = len(entities)
    for ent in entities:
        if not (dxfStats["Types"].__contains__(ent.DXFTYPE)):
            dxfStats["Types"].append(ent.DXFTYPE)
            dxfStats["Counts"].append(1)
        else:
            _iEnt = dxfStats["Types"].index(ent.DXFTYPE)
            dxfStats["Counts"][_iEnt] += 1

    return dxfStats