from urllib.error import URLError, HTTPError
from journal.nature import _nature, _nbt, _ng
from journal.oxford import _bioinformatics, _nar


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
    elif url.split('/')[2].split('.')[1] == "oxfordjournals":
        if url.split('/')[2].split('.')[0] == "bioinformatics":
            jounal_title = 'bioinformatics'
            meta_data, journal_data = _bioinformatics(url)
        elif url.split('/')[2].split('.')[0] == 'nar':
            jounal_title = "Nucleic Acids Research"
            meta_data, journal_data = _nar(url)
    else:
        raise URLError

    return jounal_title, meta_data, journal_data

