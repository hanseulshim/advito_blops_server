
def object_to_dict(obj):

    """
    Converts an object to a python dictionaryself.
    Ignores fields starting with the underscore character.
    Primarily used for updates on db sessions as that function requires a dictionary rather than an ORM object.
    """

    dict = vars(obj)
    return { key:value for (key,value) in dict.items() if not key.startswith('_') }
