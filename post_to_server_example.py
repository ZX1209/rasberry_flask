import json
import request

posts=[
            {'key':'test1',
             'value':10
             },
             {'key':'test2',
             'value':11
             },
             {'key':'test3',
             'value':12
             },
             {'key':'test4',
             'value':13
             },
             {'key':'test5',
             'value':14
             },
             {'key':'test6',
             'value':15
             },
             {'key':'test6',
             'value':15
             }
           ]

json_data=json.dumps(posts)

request.post('http://159.89.155.162:5000/info',data=json_data)


