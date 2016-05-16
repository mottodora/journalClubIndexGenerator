from journal.nature import _nature, _nbt, _ng


def generate(url):
    if url.split('/')[2] == "www.nature.com":
        if url.split('/')[3] == 'nature':
            jounal_title = 'Nature'
            meta_data, journal_data = _nature(url)
        elif url.split('/')[3] == 'nbt':
            jounal_title = 'Nature Biotechnology'
            meta_data, journal_data = _nbt(url)
        elif url.split('/')[3] == 'ng':
            jounal_title = 'Nature Genetics'
            meta_data, journal_data = _ng(url)

    return jounal_title, meta_data, journal_data

