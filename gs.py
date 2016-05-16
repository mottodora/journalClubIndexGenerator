from journal.nature import _nature, _nbt


def generate(url):
    if url.split('/')[2] == "www.nature.com":
        if url.split('/')[3] == 'nature':
            jounal_title = 'Nature'
            meta_data, jounal_data = _nature(url)
        elif url.split('/')[3] == 'nbt':
            jounal_title = 'Nature Biotechnology'
            meta_data, jounal_data = _nbt(url)

    return jounal_title, meta_data, jounal_data

