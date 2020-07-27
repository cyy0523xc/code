# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2019年08月14日 星期三 18时03分41秒
import whoosh
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.query import *
from whoosh.qparser import QueryParser

schema = Schema(name=TEXT(stored=True))
idx = create_in("/tmp/test_idx", schema, "idx_name")
writer = idx.writer()
#writer.add_document(name="惠 州")
#writer.add_document(name="惠 城")
#writer.add_document(name="惠 州 惠 城")
writer.add_document(name="hello world")
writer.commit()

s = idx.searcher()
print("Fields: ", list(s.lexicon("name")))
qp = QueryParser("name", schema=schema, termclass=FuzzyTerm)
for i in range(1,40):
    #res = s.search(FuzzyTerm("name", "惠 城", maxdist=i, prefixlength=0))
    res = s.search(FuzzyTerm("name", "hello world test", maxdist=i, prefixlength=0))
    if len(res) > 0:
        for r in res:
            print("Potential match ( %s ): [  %s  ]" % ( i, r["name"] ))
    else:
        print("Pass: %s" % i)

s.close()
