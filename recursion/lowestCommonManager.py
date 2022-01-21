class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

    def __repr__(self):
        return str(self.name)

    def addDirectReport(self, node):
        self.directReports.append(node)


class OrgChartInfo:
    def __init__(self, lowestCommonManager, numImportantReports):
        self.lowestCommonManager = lowestCommonManager
        self.numImportantReports = numImportantReports


# O(n) time | O(d) space - where n is the people in the org chart and
# d is the depth of the org chart.
def aeSolution(topManager, reportOne, reportTwo):
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager


def getOrgInfo(manager, reportOne, reportTwo):
    numImportantReports = 0
    for directReport in manager.directReports:
        orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
        if orgInfo.lowestCommonManager is not None:
            return orgInfo
        numImportantReports += orgInfo.numImportantReports
    if manager == reportOne or manager == reportTwo:
        numImportantReports += 1
    lowestCommonManager = manager if numImportantReports == 2 else None 
    return OrgChartInfo(lowestCommonManager, numImportantReports)





if __name__ == '__main__':
    rb = OrgChart('B')
    rc = OrgChart('C')

    rd = OrgChart('D')
    re = OrgChart('E')

    rf = OrgChart('F')
    rg = OrgChart('G')

    rh = OrgChart('H')
    ri = OrgChart('I')

    topManager = OrgChart('A')
    topManager.addDirectReport(rb)
    topManager.addDirectReport(rc)

    rb.addDirectReport(rd)
    rb.addDirectReport(re)

    rc.addDirectReport(rf)
    rc.addDirectReport(rg)

    rd.addDirectReport(rh)
    rd.addDirectReport(ri)

    print(aeSolution(topManager, re, ri))