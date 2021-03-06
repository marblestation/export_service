
from flask import current_app
import requests

from exportsrv.client import client

def get_solr_data(bibcodes, fields, start=0, sort='date desc'):
    """
    
    :param bibcodes: 
    :param fields: 
    :param start: 
    :param sort: 
    :return: 
    """
    data = 'bibcode\n' + '\n'.join(bibcodes)

    rows = min(current_app.config['EXPORT_SERVICE_MAX_RECORDS_SOLR'], len(bibcodes))

    params = {
        'q': '*:*',
        'wt': 'json',
        'rows': rows,
        'start': start,
        'sort': sort,
        'fl': fields,
        'fq': '{!bitset}'
    }

    headers = {'Authorization':'Bearer '+current_app.config['EXPORT_SERVICE_ADSWS_API_TOKEN']}

    try:
        response = client().post(
            url=current_app.config['EXPORT_SOLRQUERY_URL'],
            params=params,
            data=data,
            headers=headers
        )
        if (response.status_code == 200):
            # make sure solr found the documents
            from_solr = response.json()
            if (from_solr.get('response')):
                num_docs = from_solr['response'].get('numFound', 0)
                if num_docs > 0:
                    return from_solr
        else:
            current_app.logger.error('Solr returned {response}.'.format(response=response))

        return None
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        current_app.logger.error('Solr exception. Terminated request.')
        current_app.logger.error(e)
        return None


def get_eprint(solr_doc):
    """

    :param a_doc:
    :return:
    """
    if 'eid' in solr_doc:
        eid = solr_doc.get('eid', '')
        if eid.startswith('arXiv') or eid.startswith('ascl'):
            return eid
    return ''



