import sys
from datetime import date, time
import types

def ccyymmdd2date(ccyymmdd):
    if len(ccyymmdd) != 8:
        raise ValueError("invalid ccyymmdd date string [%s]" % ccyymmdd)
    year = int(ccyymmdd[0:4])
    month = int(ccyymmdd[4:6])
    day = int(ccyymmdd[6:8])

    if month < 1 or month > 12 or day < 1 or day > 31:
        raise ValueError("invalid date")

    return date(year, month, day)

def yymmdd2date(yymmdd):
    if len(yymmdd) != 6:
        raise ValueError("invalid yymmdd date string - [%s]" % yymmdd)
    year = int(yymmdd[0:2]) + 2000
    month = int(yymmdd[2:4])
    day = int(yymmdd[4:6])

    if month < 1 or month > 12 or day < 1 or day > 31:
        raise ValueError("invalid date - %s" % yymmdd)

    return date(year, month, day)

def splitdate(datestring):
    if len(datestring) == 6:
        return yymmdd2date(datestring)
    elif len(datestring) == 8:
        return ccyymmdd2date(datestring)
    else:
        raise ValueError("invalid date string [%s]" % datestring)

def hhmm2time(hhmm):
    if len(hhmm) != 4:
        raise ValueError("invalid string")
    hour = int(hhmm[0:2])
    min = int(hhmm[2:4])
    if hour < 0 or hour > 23 or min < 0 or min > 60:
        raise ValueError("invalid time")

    return time(hour=hour, minute=min)

class X12Segment(object):
    def __init__(self, name, elements):
        self.name = name
        self.elements = elements

        for e in elements:
            te = type(e)
            assert te == types.StringType or te == types.TupleType

    def isSegment(self):
        return True

    def isLoop(self):
        return False

    def dump(self, indent=0):
        print ("%s%s" % (("  " * indent), self.name))

    def getName(self):
        return self.name

    def getElement(self, index):
        return self.elements[index-1]

    def numElements(self):
        return len(self.elements)

    def getSubElement(self, index, sub_index):
        e = self.elements[index-1]
        if type(e) != types.TupleType:
            raise ValueError("%s%02d does not have sub-elements" % \
                    (self.name, index))
        return e[sub_index-1]

    def numSubElements(self, index):
        e = self.elements[index-1]
        if type(e) != types.TupleType:
            return 1
        else:
            return len(e)

class X12Loop(object):
    def __init__(self, loop_name):
        self.loop_name = loop_name

        # Each object in self.children must be either an X12Loop or X12Segment
        # object
        self.children = []

    def isSegment(self):
        return False

    def isLoop(self):
        return True

    def dump(self, indent = 0):
        assert len(self.children)
        pfx = "  " * indent
        print("%sLoop %s [" % (pfx, self.loop_name))
        for item in self.children:
            item.dump(indent + 1)
        print("%s]" % pfx)

    def getLoopName(self):
        return self.loop_name

    def add(self, segment_or_loop):
        if len(self.children) == 0:
            assert segment_or_loop.isSegment()
        else:
            assert segment_or_loop.isLoop() or segment_or_loop.isSegment()

        self.children.append(segment_or_loop)

    def getChildren(self):
        return self.children

    def getSubLoopsByName(self, loop_name):
        return [ c for c in self.children \
                if c.isLoop() and c.getLoopName() == loop_name ]

    def getSegmentsByName(self, seg_name):
        return [ c for c in self.children \
                if c.isSegment() and c.getName() == seg_name ]

class X12ParseError(ValueError):
    pass

class X12Handler(object):
    def startInterchangeControl(self, isa_segment):
        pass

    def endInterchangeControl(self, iea_segment):
        pass

    def startFunctionalGroup(self, gs_segment):
        pass

    def endFunctionalGroup(self, ge_segment):
        pass

    def startTransactionSet(self, st_segment):
        pass
    
    def endTransactionSet(self, se_segment):
        pass

    def interchangeAcknowledgment(self, ta1):
        pass

    def segment(self, segname, seg):
        pass

class SimpleHandler(X12Handler):
    def __init__(self):
        pass

    def startInterchangeControl(self, isa_segment):
        print "[ISA]"

    def endInterchangeControl(self, iea_segment):
        print "[IEA]"

    def startFunctionalGroup(self, gs_segment):
        print "  [GS]"

    def endFunctionalGroup(self, ge_segment):
        print "  [GE]"

    def startTransactionSet(self, st_segment):
        print "    [ST]"
    
    def endTransactionSet(self, se_segment):
        print "    [SE]"

    def interchangeAcknowledgment(self, ta1):
        print "  [TA1]"

    def segment(self, segname, seg):
        print "      [%s]" % segname()

class X12ElementSpec(object):
    def __init__(self, index, *values):
        self.index = index
        self.values = values

    def getIndex(self):
        return self.index

    def getValues(self):
        return self.values

class X12SegmentSpec(object):
    def __init__(self, name, usage = "R", max_repeat = 1, element_specs = []):
        self.name = name
        self.usage = usage
        self.max_repeat = max_repeat
        self.elem_specs = element_specs
        if len(name) < 2:
            raise ValueError("Invalid name")
        if usage not in "RSO":
            raise ValueError("Segment usage must be 'R', 'S', or 'O'")
        if max_repeat < 1:
            raise ValueError("Invalid max_repeat")

        assert(all([isinstance(es, X12ElementSpec) for es in element_specs]))

    def isSegmentSpec(self):
        return True

    def isLoopSpec(self):
        return False

    def getSegName(self):
        return self.name

    def getUsage(self):
        return self.usage

    def isRequired(self):
        return self.usage == "R"

    def getMaxSegmentRepeat(self):
        return self.max_repeat

    def getElementSpecs(self):
        return self.element_specs

    def matchesSegment(self, seg):
        if seg.name != self.name: return False
        for espec in self.elem_specs:
            if seg.getElement(espec.index) not in espec.values:
                return False
        return True

    def dump(self, indent = 0):
        print ("%s%s" % (("  " * indent), self.name))

class X12LoopSpec(object):
    def __init__(self, loop_name, loop_repeat, segment_and_loop_specs):
        self.loop_name = loop_name
        self.specs  = segment_and_loop_specs
        self.loop_repeat = loop_repeat

        assert self.specs[0].isSegmentSpec()
        assert self.specs[0].getMaxSegmentRepeat() == 1

        assert(all([isinstance(sl, X12LoopSpec) or isinstance(sl, X12SegmentSpec) \
                for sl in segment_and_loop_specs]))

    def getLoopName(self):
        return self.loop_name

    def getSpecs(self):
        return self.specs

    def getMaxLoopRepeat(self):
        return self.loop_repeat

    def getSegName(self):
        return self.specs[0].getSegName()

    def matchesSegment(self, seg):
        return self.specs[0].matchesSegment(seg)

    def isRequired(self):
        return self.specs[0].isRequired()

    def isSegmentSpec(self):
        return False

    def isLoopSpec(self):
        return True

    def dump(self, indent = 0):
        print ("%sLoop %s" % (("  " * indent), self.loop_name))
        for spec in self.specs:
            spec.dump(indent+1)
    
class X12Parser(object):
    def __init__(self):
        pass

    def parse(self, f, handler):
        self.num_segments_parsed = 0
        self.f = f
        self.elem_sep = None
        self.subelem_sep = None
        self.segment_sep = None
        self.handler = handler

        # ========= parse the ISA segment ==========

        # check that the first three bytes read "ISA"
        segname = f.read(3)
        if segname != "ISA":
            raise X12ParseError("Expected ISA, not \"%s\"" % segname)

        # the first element separator defines the element separator to be used
        # throughout the entire interchange
        self.elem_sep = f.read(1)
        
        # read the ISA fields into an array
        elements = []
        # read in the next 15 fields all at once.  Field lengths are defined in
        # ANSI X12 spec
        for i in [ 2, 10, 2, 10, 2, 15, 2, 15, 6, 4, 1, 5, 9, 1, 1 ]:
            s = f.read(i)
            c = f.read(1)
            if c != self.elem_sep: 
                raise X12ParseError("element separator not found! %s" % c)
            elements.append(s)
        elements.append(f.read(1))

#        authorization_information_qualifier = elements[0]
#        authorization_information = elements[1]
#        security_information_qualifier = self.isa[2]
#        self.senderid = self.isa[3]
#        self.receiverqual = self.isa[4]
#        self.receiverid = self.isa[5]
#        self.date = splitdate(self.isa[6])
#        self.time = hhmm2time(self.isa[7])
#        self.production = (self.isa[8] == "P")
        self.subelem_sep = elements[15]
        self.segment_sep = self.f.read(1)
#        if authorization_information_qualifier not in ("00", "03"):
#            self.__warn("invalid ISA01")

        # TODO validation

        # ========== remaining segments =============

        self.num_segments_parsed += 1
        self.handler.startInterchangeControl(X12Segment("ISA", elements))

        n_functional_groups = 0
        while True:
            # expect GS on first loop.  On subsequent loops, IEA is ok.  
            # TA1 is also ok
            seg = self.__readSegment()
            if seg.getName() == "GS":
                self.handler.startFunctionalGroup(seg)
                n_functional_groups += 1
            elif seg.getName() == "TA1":
                self.handler.interchangeAcknowledgment(seg)
                continue
            elif n_functional_groups == 0:
                self.__fail("Expected GS segment, got [%s]\n" % seg.getName())
            elif seg.getName() == "IEA":
                self.handler.endInterchangeControl(seg)
                break
            else:
                self.__fail("Expected GS or IEA segment, got [%s]\n" % seg.getName())

            # count the number of transaction sets within a functional group
            n_transaction_sets = 0

            while True:
                # expect ST on first loop.  On subsequent loops, GT is ok
                seg = self.__readSegment()
                if seg.getName() == "ST":
                    self.handler.startTransactionSet(seg)
                    n_transaction_sets += 1
                elif n_transaction_sets == 0:
                    self.__fail("Expected ST segment, got [%s]\n" % seg.getName())
                elif seg.getName() == "GE":
                    self.handler.endFunctionalGroup(seg)
                    break
                else:
                    self.__fail("Expected ST or GE segment, got [%s]\n" % seg.getName())

                while True:
                    seg = self.__readSegment()
                    if seg.getName() == "SE":
                        self.handler.endTransactionSet(seg)
                        break
                    else:
                        self.handler.segment(seg.getName(), seg)

    def __readSegment(self):
        """assumes that self.f is positioned on the beginning of a segment
        (i.e. right after a segment terminator).  Reads the entire segment, 
        and returns with self.f positioned at the beginning of the next
        segment.  Returns an array, one entry per segment element.  
        """
        segname = None
        elements = []
        self.num_segments_parsed += 1
        more_elements = True
        while more_elements:
            elem_chars = []
            has_subelems = False
            c = ""
            while True:
                c = self.f.read(1)
                if len(c) != 1:
                    self.__fail("error reading element/segment separator")
                if c == self.elem_sep:
                    break
                elif c == self.segment_sep:
                    more_elements = False
                    break
                elif c == self.subelem_sep:
                    has_subelems = True
                elem_chars.append(c)

            if has_subelems:
                elem = tuple("".join(elem_chars).split(self.subelem_sep))
            else:
                elem = "".join(elem_chars)

            if segname is None:
                segname = elem
            else:
                elements.append(elem)

        return X12Segment(segname, elements)

    def __warn(self, txt):
        # TODO
        sys.stderr.write("%s\n" % txt)
        pass

    def __fail(self, txt):
        raise X12ParseError("segment %d:  %s\n" % \
                (self.num_segments_parsed, txt))

class _LoopParseStatus(object):
    def __init__(self, loopSpec, loop):
        self.loopSpec = loopSpec
        self.index = 0
        self.loop_repeat = 1
        self.loop = loop
        self.segment_repeat = 0

class _X12DocumentHandler(X12Handler):
    def __init__(self, document, spec):
        self.doc = document
        self.spec = spec

        self.loopStack = [ _LoopParseStatus(spec, self.doc.loop0) ]

    def __warn(self, msg):
        sys.stderr.write("WARNING: %s\n" % msg)

    def startInterchangeControl(self, isa):
        self.doc.isaSenderIDType = isa.getElement(5)
        self.doc.isaSenderID = isa.getElement(6)
        self.doc.isaReceiverIDType = isa.getElement(7)
        self.doc.isaReceiverID = isa.getElement(8)
        self.doc.isaDate = yymmdd2date(isa.getElement(9))
        self.doc.isaTime = hhmm2time(isa.getElement(10))
        
        icsi = isa.getElement(11)
        if icsi != "U":
            raise X12ParseError("Invalid ISA11: [%s]" % icsi)

        icvn = isa.getElement(12)
        if icvn != "00401":
            raise X12ParseError("Invalid ISA12: [%s]" % icvn)

        self.doc.isaID = isa.getElement(13)

        ui = isa.getElement(15)
        if ui not in "PT":
            raise X12ParseError("Invalid ISA15: [%s]" % ui)
        self.doc.isaProduction = (ui == "P")
        pass

    def endInterchangeControl(self, iea):
        # TODO check number of functional groups

        icn = iea.getElement(2)
        if icn != self.doc.isaID:
            self.__warn("IEA02 does not match ISA13: %s / %s" % \
                    (icn, self.doc.isaID))

    def startTransactionSet(self, st):
        self.segment(st.getName(), st)
    def endTransactionSet(self, se):
        self.segment(se.getName(), se)

    def matchSegment(self, segname, seg, lp):
        # is there more in this loop?
        specs = lp.loopSpec.getSpecs()
        while lp.index < len(specs):
            spec = specs[lp.index]

            if spec.matchesSegment(seg):
                # matched the next spec.

                if spec.isLoopSpec():
                    dbg("   entering loop %s" % spec.getLoopName())
                    newloop = X12Loop(spec.getLoopName())
                    newloop.add(seg)
                    newlp = _LoopParseStatus(spec, newloop)
                    newlp.index += 1
                    newlp.segment_repeat = 0

                    lp.loop.add(newloop)
                    self.loopStack.append(newlp)
                else:
                    lp.loop.add(seg)
                    lp.segment_repeat += 1
                    if lp.segment_repeat >= spec.getMaxSegmentRepeat():
                        lp.segment_repeat = 0
                        lp.index += 1

                return True
            elif spec.isRequired() and lp.segment_repeat == 0:
                # a segment can only be required once

                # uh oh.  did not match a required segment.
#                print "  Unable to match %s to a loop" % segname
                raise X12ParseError("In loop %s - expected %s, got %s" % \
                        (lp.loopSpec.getLoopName(), spec.getSegName(), segname))
            else:
#                dbg("  skipping [%s]" % spec.getSegName())
                # did not match, but the next segment was not required
                # try the next spec in this loop (or bottom out of the loop)
                lp.index += 1

        # reached the end of the loop.  Can either repeat, or pop out
        if lp.loop_repeat >= lp.loopSpec.getMaxLoopRepeat():
            # hit repeat limit.  do not try to repeat the loop
            return False
        else:
            if lp.loopSpec.matchesSegment(seg):
                lp.loop_repeat += 1
                lp.index = 1
                lp.segment_repeat = 0
                
                newloop = X12Loop(lp.loopSpec.getLoopName())
                newloop.add(seg)
                self.loopStack[-2].loop.add(newloop)
                lp.loop = newloop
                return True

    def segment(self, segname, seg):
        dbg("[%s]" % segname)
        # is there more in this loop?
        while not self.matchSegment(segname, seg, self.loopStack[-1]):
            dbg("   leaving loop %s" % self.loopStack[-1].loopSpec.getLoopName())
            self.loopStack.pop(-1)

            if len(self.loopStack) == 0:
                raise X12ParseError("Don't know what to do with segment %s" % \
                        segname)
            else:
                self.loopStack[-1].index += 1

class X12Document(object):
    def __init__(self, f, spec):
        self.loop0 = X12Loop("0")

        self.isaSenderID = None
        self.isaSenderIDType = "ZZ"
        self.isaReceiverID = None
        self.isaReceiverIDType = "ZZ"
        self.isaDate = None
        self.isaTime = None
        self.isaID = None
        self.isaProduction = False

        handler = _X12DocumentHandler(self, spec)

        parser = X12Parser()
        parser.parse(f, handler)

    def getDocumentDate(self):
        return self.isaDate

    def getDocumentTime(self):
        return self.isaTime

    def getSenderID(self):
        return self.isaSenderID

    def getSenderIDType(self):
        return self.isaSenderIDType

    def getReceiverID(self):
        return self.isaReceiverID

    def getReceiverIDType(self):
        return self.isaReceiverIDType

    def getDocumentID(self):
        return self.isaID

    def isProductionMode(self):
        return self.isaProduction

    def getRootLoop(self):
        return self.loop0

    def dump(self):
        self.loop0.dump()

def dbg(text):
    pass
#    sys.stderr.write("%s\n" % text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("usage: x12.py <edifact_file>\n")
        sys.exit(1)

    f = file(sys.argv[1], "r")
    p = X12Parser()
    p.parse(f, SimpleHandler())
