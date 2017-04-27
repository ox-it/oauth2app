#-*- coding: utf-8 -*-


"""OAuth 2.0 URI Helper Functions"""


from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode
 
 
def add_parameters(url, parameters):
    """Parses URL and appends parameters. 

    **Args:**

    * *url:* URL string.
    * *parameters:* Dict of parameters

    *Returns str*"""
    parts = list(urlparse(url))
    parts[4] = urlencode(parse_qsl(parts[4]) + list(parameters.items()))
    return urlunparse(parts)
    

def add_fragments(url, fragments):
    """Parses URL and appends fragments. 

    **Args:**

    * *url:* URL string.
    * *fragments:* Dict of fragments

    *Returns str*"""
    parts = list(urlparse(url))
    parts[5] = urlencode(parse_qsl(parts[5]) + list(fragments.items()))
    return urlunparse(parts)
