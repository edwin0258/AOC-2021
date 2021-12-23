f = open('data.txt', 'r')

def genCaveConnections(data, caveObj):
    for l in data:
        # create an obj representing connections in cave system
        [p1, p2] = l.strip().split('-')
        if p1 in caveObj:
            caveObj[p1].append(p2)
        else:
            caveObj[p1] = [p2]

        if p2 in caveObj:
            caveObj[p2].append(p1)
        else:
            caveObj[p2] = [p1]

    return caveObj

# holds mappings of routes in cave
caveObj = genCaveConnections(f, {}) 
# cave paths
cavePaths = []


# check if end can be reached from this route
def canEnd(r, prevs):
    # for route in cave object
    prevs.append(r)
    if r in caveObj:
        if 'end' in caveObj[r]: # end found!
            return True
        else:
            childRouteEnds = []
            # child route
            for cr in caveObj[r]:
                if cr not in prevs: 
                    # check can end on each child r
                    childRouteEnds.append(canEnd(cr, prevs[:]))

            # does a child route have an end
            # or a child of that child?
            return True in childRouteEnds

    return False

# Note: list[:] is needed to pass lists by val instead of reference

# (current point in cave, previous points visited, complete route
# [designated two visit small cave for route, # uses])
def traverseCave(cur, prevs, route, twoUse):
    prevs.append(cur)
    if (twoUse[0] is not None):
        if (cur == twoUse[0]):
            twoUse[1] += 1

    if cur in caveObj:
        for r in caveObj[cur]:
            if r == 'end':
                cavePaths.append(route + '-end')
                continue

            # avoid going down a one way dead end..
            if (cur.islower() and (r.islower() and not canEnd(r, []))):
                # if cur can still be visited again
                # then continue is incorrect in that case
                if not (cur == twoUse[0] and twoUse[1] != 2):
                    continue

            # can't go back to a lowercase cave 2 times (small cave)
            # unless a special two visit small cave (one of these)
            if r.islower() and r in prevs:
                if not (r == twoUse[0] and twoUse[1] != 2):
                    continue

            traverseCave(r, prevs[:], route + '-' + r, twoUse[:])

            if r.islower() and twoUse[0] is None:
                if(r not in ['start', 'end']):
                    traverseCave(r, prevs[:], route + '-' + r, [r, 0])
                
    else:
        if cur == 'end':
            cavePaths.append(route)
        else:
            # go back 1, retrace steps
            traverseCave(prevs[-2], prevs[:], route + '-' + prevs[-2], twoUse[:])


# find all paths/routes in cave object
# start at cave start
traverseCave('start', [], 'start', [None, 0])

# print solution
print(len(set(cavePaths)))
