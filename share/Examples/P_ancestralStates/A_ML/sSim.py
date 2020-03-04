var.verboseRead = 0
var.warnReadNoFile = 0
taxNames = list(string.ascii_uppercase[:5])
a = func.newEmptyAlignment(dataType='dna', taxNames=taxNames, length=5000)
d = Data([a])
read('((A:0.3, B:0.3):0.1, C:0.4, (D:0.3, E:0.3):0.1);')

t = var.trees[0]
t.data = d
c1 = t.newComp(free=0, spec='specified', val=[0.4, 0.1, 0.1])
c2 = t.newComp(free=0, spec='specified', val=[0.1, 0.2, 0.3])

# Put the c1 comp on all the nodes of the tree.  Then put c2 on the
# root, over-riding c1 that is already there.
t.setModelThing(c1, node=0, clade=1)
t.setModelThing(c2, node=0, clade=0)

t.newRMatrix(free=0, spec='ones')
t.setNGammaCat(nGammaCat=1)
t.setPInvar(free=0, val=0.0)
t.simulate()
# t.data.compoSummary()
d.writeNexus('d.nex')
t.writeNexus('simTree.nex')
