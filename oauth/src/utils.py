from urllib import parse as urlparse
from urllib.parse import urlencode


def append_params_to_uri(uri: str, params: dict) -> str:
    url = uri
    params = params
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    return urlparse.urlunparse(url_parts)