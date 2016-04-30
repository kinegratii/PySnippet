
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import re
import copy
import collections
 
reobj = re.compile(r"\$([^$]*)\$")
tpldict = {}
TplClass = collections.namedtuple('TplClass', ['varpos', 'tplslice'])
 
def preproccess(tplid, tpl):
    results = reobj.finditer(tpl)
    obj = TplClass({}, [])
    start = 0
    end = 0
 
    for i in results:
        start = i.start(0)
        obj.tplslice.append(tpl[end:start])
        end = i.end(0)
        obj.varpos.setdefault(i.group(1), []).append(len(obj.tplslice))
        obj.tplslice.append(None)
 
    obj.tplslice.append(tpl[end:])
    tpldict[tplid] = obj
 
def make(tplid, tplvars):
    obj = tpldict[tplid]
    tplslice = copy.copy(obj.tplslice)
    for key, value in tplvars.iteritems():
        for idx in obj.varpos[key]:
            tplslice[idx] = value
            print tplslice
 
    return ''.join(tplslice)
 
if __name__ == '__main__':
    # preproccess
    tpl = "my name is $spname$, i'm $spage$ years old"
    tplid = 1
    preproccess(tplid, tpl)
 
    # make text
    print make(tplid, {'spname' : 'robin928', 'spage' : '29'})
