import json
from collections import OrderedDict

from description import (
    operation_description_map,
    tag_description_map,
    parameter_description_map
)

from name import (
    tag_map,
    singular_name_map,
    plural_name_map
)


def get_model_list():
    l = [k for k in tag_description_map.keys()]
    l.sort()
    return l

def get_key(description, i):
    if i in description.keys():
        return description[i]
    else:
        return {}

def get_operation_description(i):
    origin_dict = operation_description_map.get(i, {})
    origin_list = [(k, v) for k, v in origin_dict.iteritems() ]
    origin_list.sort()
    return OrderedDict(origin_list)

def get_parameter_description(i):

    origin_dict = parameter_description_map.get(i, {})

    path_list = []
    query_list = []
    post_list = []
    put_list = []
    response_list = []
    generic_list = []

    if type(origin_dict) == dict:
        for k,v in origin_dict.items():
            if k.startswith('discover-') or \
                k.startswith('get-') or \
                k.startswith('list-') or \
                k.startswith('delete-') or \
                k.startswith('update-') or \
                k.startswith('add-'):
                    path_list.append((k, v))
            elif k.startswith('query-'):
                query_list.append((k, v))
            elif k.startswith('post-'):
                post_list.append((k, v))
            elif k.startswith('put-'):
                put_list.append((k, v))
            elif k.startswith('response-'):
                response_list.append((k, v))
            else:
                generic_list.append((k, v))
    else:
        print(i)


    def path_cmp(a, b):
        path_sequence = ['list-container', 'discover-container', 'get-name',
                         'update-name', 'delete-name', 'delete-version', 'add-name']
        tmp_a = path_sequence.index(a[0])
        tmp_b = path_sequence.index(b[0])

        if tmp_a > tmp_b:
            return 0
        else:
            return -1

    path_list.sort(cmp=lambda a, b: path_cmp(a, b))

    query_list.sort()
    post_list.sort()
    put_list.sort()
    response_list.sort()
    generic_list.sort()

    sequence_dict = OrderedDict(
        [
            ('path-parameter-description', OrderedDict(path_list)),
            ('query-parameter-description', OrderedDict(query_list)),
            ('post-body-parameter-description', OrderedDict(post_list)),
            ('put-body-parameter-description', OrderedDict(put_list)),
            ('response-body-parameter-description', OrderedDict(response_list)),
            ('generic-description', OrderedDict(generic_list)),
        ]
    )

    return sequence_dict

def generator():
    info = []
    for i in get_model_list():
        value = [
            ('tag-name', tag_map.get(i, '')),
            ('tag-description', tag_description_map.get(i, '')),
            ('sigular-name', singular_name_map.get(i, '')),
            ('plural-name', plural_name_map.get(i, '')),
            ('operation-description', get_operation_description(i)),
            ('parameter-description', get_parameter_description(i)),
        ]
        value = OrderedDict(value)
        info.append((i, value))

    with open('description.json', 'w') as f:
        json.dump(OrderedDict(info), f, indent=4)

if __name__ == '__main__':
    generator()
