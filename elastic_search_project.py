import elasticsearch

es = elasticsearch.Elasticsearch()
es.index(index='posts', doc_type='blog', id=1, body={
    'author':'Santa Clause',
    'blog':'Slave Based Shippers of the north',
    'title':'Using Celery for distributing gift dispatch',
    'topics':['slave labor', 'elves', 'python',
              'celery', 'antigravity reindeer'],
    'awesomeness':0.2
    })

es.get(index='posts', doc_type='blog', id=2)
    
es.search(index='posts', q='author:"Santa Clause"')


