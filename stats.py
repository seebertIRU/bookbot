def convert_dict_to_list_of_dicts(dict):
    list_of_dicts = [{'key':k,'value':v} for k,v in dict.items()]
    return list_of_dicts

def sort_on_value(dict):
    return dict['value']

def sort_dict_by_value(dict,reverse):
    lod=convert_dict_to_list_of_dicts(dict)
    sl=lod.sort(reverse=reverse, key=sort_on_value)
    return lod

def count_lower_case_characters(strdata):
    da={ '~':0 }
    char_list=list(strdata)
    for c in char_list:
        tc=c.lower()
        da.update({tc:da.get(tc,0)+1})
    del da['~']
    return da

def get_book_text(filepath):
    with open (filepath) as f:
        file_contents=f.read()
    return file_contents

def get_num_words(data):
    dl=data.split()
    return len(dl)
