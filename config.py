# -*- coding: utf-8 -*-

import os
# This is the URL to communicate with ADS Classic
EXPORT_SERVICE_CLASSIC_EXPORT_URL = 'http://adsabs.harvard.edu/cgi-bin/nph-abs_connect'

# In what environment are we?
ENVIRONMENT = os.getenv('ENVIRONMENT', 'staging').lower()
# Configure logging
EXPORT_SERVICE_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s\t%(process)d '
                      '[%(asctime)s]:\t%(message)s',
            'datefmt': '%m/%d/%Y %H:%M:%S',
        }
    },
    'handlers': {
        'file': {
            'formatter': 'default',
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/tmp/export_service_app.{}.log'.format(ENVIRONMENT),
        },
        'console': {
            'formatter': 'default',
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        '': {
            'handlers': ['file','console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}


#This section configures this application to act as a client, for example to query solr
#EXPORT_SERVICE_BIGQUERY_PATH = None
#EXPORT_SERVICE_ADSWS_API_TOKEN = 'this is a secret api token!'

# curl -H 'Authorization: Bearer:rCCi5v3Xb3eReNsG5mTz7tWBNh4Z2rPMGNShne2d' 'http://devapi.adsabs.harvard.edu/v1/search/query?q=star&fl=bibcode'
#EXPORT_SERVICE_BIGQUERY_PATH = 'https://devapi.adsabs.harvard.edu/v1/search/bigquery'
#EXPORT_SERVICE_ADSWS_API_TOKEN = 'Bearer:rCCi5v3Xb3eReNsG5mTz7tWBNh4Z2rPMGNShne2d'
EXPORT_SERVICE_BIGQUERY_PATH = 'http://api.adsabs.harvard.edu/v1/search/bigquery'
EXPORT_SERVICE_ADSWS_API_TOKEN = 'Bearer:eQhhOLITyCD1B2Afuxf2b5LdTpFTl5WaepVI7Dn0'


EXPORT_SERVICE_QUERY_DEFAULT_FIELDS = 'author,title,year,date,pub,pub_raw,issue,volume,page,aff,doi,abstract,eid,' \
                                      'citation_count,read_count,bibcode,identification,copyright,keyword,doctype,' \
                                      'links_data,reference,comment'

EXPORT_SERVICE_BBB_PATH = 'https://ui.adsabs.harvard.edu/#abs'
EXPORT_SERVICE_ADS_NOTES = 'Provided by the SAO/NASA Astrophysics Data System'

EXPORT_SERVICE_RECORDS_SET_XML = [('xmlns','http://ads.harvard.edu/schema/abs/1.1/abstracts'),
                                  ('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance'),
                                  ('xsi:schemaLocation','http://ads.harvard.edu/schema/abs/1.1/abstracts http://ads.harvard.edu/schema/abs/1.1/abstracts.xsd')]

EXPORT_SERVICE_LINK_URL_FORMAT = 'https://ui.adsabs.harvard.edu/#abs/{}/{}'
EXPORT_SERVICE_LINK_LINKS_DATA_URL_FORMAT = 'https://ui.adsabs.harvard.edu/#abs/{}{}{}'

EXPORT_SERVICE_LATEX_ACCENT = [
    [u"à", "\\`a"],  # Grave accent
    [u"è", "\\`e"],
    [u"ì", "\\`{\\i}"],
    [u"ò", "\\`o"],
    [u"ù", "\\`u"],
    [u"ỳ", "\\`y"],
    [u"À", "\\`A"],
    [u"È", "\\`E"],
    [u"Ì", "\\`{\\I}"],
    [u"Ò", "\\`O"],
    [u"Ù", "\\`U"],
    [u"Ỳ", "\\`Y"],
    [u"á", "\\'a"],  # Acute accent
    [u"ć", "\\'c"],
    [u"é", "\\'e"],
    [u"í", "\\'{\\i}"],
    [u"ó", "\\'o"],
    [u"ú", "\\'u"],
    [u"ý", "\\'y"],
    [u"Á", "\\'A"],
    [u"É", "\\'E"],
    [u"Í", "\\'{\\I}"],
    [u"Ó", "\\'O"],
    [u"Ú", "\\'U"],
    [u"Ý", "\\'Y"],
    [u"ő", "\\Ho"],  # Double Acute accent
    [u"ű", "\\Hu"],
    [u"ӳ", "\\Hy"],
    [u"Ő", "\\HO"],
    [u"Ű", "\\HU"],
    [u"Ӳ", "\\HY"],
    [u"â", "\\^a"],  # Circumflex
    [u"ê", "\\^e"],
    [u"î", "\\^{\\i}"],
    [u"ô", "\\^o"],
    [u"û", "\\^u"],
    [u"ŷ", "\\^y"],
    [u"Â", "\\^A"],
    [u"Ê", "\\^E"],
    [u"Î", "\\^{\\I}"],
    [u"Ô", "\\^O"],
    [u"Û", "\\^U"],
    [u"Ŷ", "\\^Y"],
    [u"ä", "\\\"a"],  # Umlaut or dieresis
    [u"ë", "\\\"e"],
    [u"ï", "\\\"{\\i}"],
    [u"ö", "\\\"o"],
    [u"ü", "\\\"u"],
    [u"ÿ", "\\\"y"],
    [u"Ä", "\\\"A"],
    [u"Ë", "\\\"E"],
    [u"Ï", "\\\"{\\I}"],
    [u"Ö", "\\\"O"],
    [u"Ü", "\\\"U"],
    [u"Ÿ", "\\\"Y"],
    [u"ã", "\\~{a}"],  # Tilde
    [u"ñ", "\\~{n}"],
    [u"õ", "\\~{o}"],
    [u"Ã", "\\~{A}"],
    [u"Ñ", "\\~{N}"],
    [u"Õ", "\\~{O}"],
    [u"ċ", "\\.{c}"],   # Dot above
    [u"ė", "\\.{e}"],
    [u"ġ", "\\.{g}"],
    [u"ṁ", "\\.{m}"],
    [u"ṅ", "\\.{n}"],
    [u"ṙ", "\\.{r}"],
    [u"ṡ", "\\.{s}"],
    [u"ẏ", "\\.{y}"],
    [u"ż", "\\.{z}"],
    [u"Ċ", "\\.{C}"],
    [u"Ė", "\\.{E}"],
    [u"İ", "\\.{I}"],
    [u"Ġ", "\\.{G}"],
    [u"Ṁ", "\\.{M}"],
    [u"Ṅ", "\\.{N}"],
    [u"Ṙ", "\\.{R}"],
    [u"Ṡ", "\\.{S}"],
    [u"Ẏ", "\\.{Y}"],
    [u"Ż", "\\.{Z}"],
    [u"ạ", "\\d{a}"],   # Dot below
    [u"ḅ", "\\d{b}"],
    [u"ḍ", "\\d{d}"],
    [u"ẹ", "\\d{e}"],
    [u"ḥ", "\\d{h}"],
    [u"ị", "\\d{i}"],
    [u"ḳ", "\\d{k}"],
    [u"ḷ", "\\d{l}"],
    [u"ṃ", "\\d{m}"],
    [u"ṇ", "\\d{n}"],
    [u"ọ", "\\d{o}"],
    [u"ṛ", "\\d{r}"],
    [u"ṣ", "\\d{s}"],
    [u"ṭ", "\\d{t}"],
    [u"ụ", "\\d{u}"],
    [u"ỵ", "\\d{y}"],
    [u"ẓ", "\\d{z}"],
    [u"Ạ", "\\d{A}"],
    [u"Ḅ", "\\d{B}"],
    [u"Ḍ", "\\d{D}"],
    [u"Ẹ", "\\d{E}"],
    [u"Ḥ", "\\d{H}"],
    [u"Ị", "\\d{I}"],
    [u"Ḳ", "\\d{K}"],
    [u"Ḷ", "\\d{L}"],
    [u"Ṃ", "\\d{M}"],
    [u"Ṇ", "\\d{N}"],
    [u"Ọ", "\\d{O}"],
    [u"Ṛ", "\\d{R}"],
    [u"Ṣ", "\\d{S}"],
    [u"Ṭ", "\\d{T}"],
    [u"Ụ", "\\d{U}"],
    [u"Ỵ", "\\d{Y}"],
    [u"Ẓ", "\\d{Z}"],
    [u"ă", "\\u{a}"],  # Breve
    [u"ĕ", "\\u{e}"],
    [u"ŏ", "\\u{o}"],
    [u"š", "\\v{s}"],  # Caron
    [u"č", "\\v{c}"],
    [u"æ", "{\\ae}"],
    [u"Æ", "{\\AE}"],
    [u"å", "{\\aa}"],
    [u"Å", "{\\AA}"],
    [u"ç", "\\c{c}"],   # Cedilla
    [u"Ç", "\\c{C}"],
    [u"œ", "{\\oe}"],   # Ligatures
    [u"Œ", "{\\OE}"],
    [u"æ", "{\\ae}"],   # AElig
    [u"Æ", "{\\AE}"],
    [u"œ", "{\\oe}"],  # OElig
    [u"Œ", "{\\OE}"],
    [u"å", "{\\aa}"],   # Ring
    [u"Å", "{\\AA}"],
    [u"ů", "{\\uu}"],
    [u"Ů", "{\\UU}"],
    [u"ḇ", "\\b{b}"],   # Underbar
    [u"ḏ", "\\b{d}"],
    [u"ẖ", "\\b{h}"],
    [u"ḵ", "\\b{k}"],
    [u"ḻ", "\\b{l}"],
    [u"ṉ", "\\b{n}"],
    [u"ṟ", "\\b{r}"],
    [u"ṯ", "\\b{t}"],
    [u"ẕ", "\\b{z}"],
    [u"Ḇ", "\\b{B}"],
    [u"Ḏ", "\\b{D}"],
    # [u"H̱", "\\b{H}"],
    [u"Ḵ", "\\b{K}"],
    [u"Ḻ", "\\b{L}"],
    [u"Ṉ", "\\b{N}"],
    [u"Ṟ", "\\b{R}"],
    [u"Ṯ", "\\b{T}"],
    [u"Ẕ", "\\b{Z}"],
    [u"ā", "\\=a"],  # Macron accent
    [u"ē", "\\=e"],
    [u"ī", "\\={\\i}"],
    [u"ō", "\\=o"],
    [u"ū", "\\=u"],
    [u"Ā", "\\=A"],
    [u"Ē", "\\=E"],
    [u"Ī", "\\={\\I}"],
    [u"Ō", "\\=O"],
    [u"Ū", "\\=U"],
    [u"–", "--"],       # Dashes
    [u"—", "---"],
    [u"ø", "{\\o}"],    # strok
    [u"ł", "\\l"],
    [u"Ø", "{\\O}"],
    [u"Ł", "\\L"],
    [u"ß", "{\\ss}"],   # szlig
    [u"¡", "{!`}"],
    [u"¿", "{?`}"],
    [u"\\", "\\\\"],    # Characters that should be quoted
    [u"~", "\\~"],
    [u"&", "\\&"],
    [u"$", "\\$"],
    [u"{", "\\{"],
    [u"}", "\\}"],
    [u"%", "\\%"],
    [u"#", "\\#"],
    [u"_", "\\_"],
    [u"≥", "$\\ge$"],  # Math operators
    [u"≤", "$\\le$"],
    [u"≠", "$\\neq$"],
    [u">", "$\\gt$"],
    [u"<", "$\\lt$"],
    [u"≠", "$\\neq$"],
    [u"〉", "$\\gt$"],
    [u"〈", "$\\lt$"],
    [u"\u3008", "$\\lt$"],  # European/Spanish style single angle quote mark.
    [u"\u3009", "$\\gt$"],
    [u"©", "\copyright"],  # Misc
    [u"ı", "{\\i}"],
    [u"µ", "$\\mu$"],
    [u"°", "$\\deg$"],
    [u"‘", "`"],        # Quotes
    [u"’", "'"],
    [u"′", "$^\\prime$"],
    [u"“", "``"],
    [u"”", "''"],
    [u"‚", ","],
    [u"„", ",,"],
    [u"\xa0", " "],  # Unprintable characters
    [u"ı", "{\\i}"],
    [u"α", "$\\alpha$"],
    [u"β", "$\\beta$"],
    [u"γ", "$\\gamma$"],
    [u"δ", "$\\delta$"],
    [u"ε", "$\\epsilon$"],
    [u"ζ", "$\\zeta$"],
    [u"η", "$\\eta$"],
    [u"θ", "$\\theta$"],
    [u"ι", "$\\iota$"],
    [u"κ", "$\\kappa$"],
    [u"λ", "$\\lambda$"],
    [u"µ", "$\\mu$"],
    [u"ν", "$\\nu$"],
    [u"ξ", "$\\xi$"],
    [u"ο", "$\\omicron$"],
    [u"π", "$\\pi$"],
    [u"ρ", "$\\rho$"],
    [u"σ", "$\\sigma$"],
    [u"ς", "$\\sigma$"],
    [u"τ", "$\\tau$"],
    [u"υ", "$\\upsilon$"],
    [u"φ", "$\\phi$"],
    [u"χ", "$\\chi$"],
    [u"ψ", "$\\psi$"],
    [u"ω", "$\\omega$"],
    [u"Α", "$\\Alpha$"],
    [u"Β", "$\\Beta$"],
    [u"Γ", "$\\Gamma$"],
    [u"Δ", "$\\Delta$"],
    [u"Ε", "$\\Epsilon$"],
    [u"Ζ", "$\\Zeta$"],
    [u"Η", "$\\Eta$"],
    [u"Θ", "$\\Theta$"],
    [u"Ι", "$\\Iota$"],
    [u"Κ", "$\\Kappa$"],
    [u"Λ", "$\\Lambda$"],
    [u"Μ", "$\\Mu$"],
    [u"Ν", "$\\Nu$"],
    [u"Ξ", "$\\Xi$"],
    [u"Ο", "$\\omicron$"],
    [u"Π", "$\\Pi$"],
    [u"Ρ", "$\\Rho$"],
    [u"Σ", "$\\Sigma$"],
    [u"Τ", "$\\Tau$"],
    [u"Υ", "$\\Upsilon$"],
    [u"Φ", "$\\Phi$"],
    [u"Χ", "$\\Chi$"],
    [u"Ψ", "$\\Psi$"],
    [u"Ω", "$\\Omega$"]
]

# Journal Abbreviations used in the ADS BibTeX entries
# From http://adsabs.harvard.edu/abs_doc/aas_macros.html
# Journal name   TeX macro
EXPORT_SERVICE_AASTEX_JOURNAL_MACRO = [
    ['Astronomical Journal',r'\aj'],
    ['Acta Astronomica',r'\actaa'],
    ['Annual Review of Astron and Astrophys',r'\araa'],
    ['Astrophysical Journal',r'\apj'],
    ['Astrophysical Journal, Letters',r'\apjl'],
    ['Astrophysical Journal, Supplement',r'\apjs'],
    ['Applied Optics',r'\ao'],
    ['Astrophysics and Space Science',r'\apss'],
    ['Astronomy and Astrophysics',r'\aap'],
    ['Astronomy and Astrophysics Reviews',r'\aapr'],
    ['Astronomy and Astrophysics, Supplement',r'\aaps'],
    ['Astronomicheskii Zhurnal',r'\azh'],
    ['Bulletin of the AAS',r'\baas'],
    ['Chinese Astronomy and Astrophysics',r'\caa'],
    ['Chinese Journal of Astronomy and Astrophysics',r'\cjaa'],
    ['Icarus',r'\icarus'],
    ['Journal of Cosmology and Astroparticle Physics',r'\jcap'],
    ['Journal of the RAS of Canada',r'\jrasc'],
    ['Memoirs of the RAS',r'\memras'],
    ['Monthly Notices of the RAS',r'\mnras'],
    ['New Astronomy',r'\na'],
    ['New Astronomy Review',r'\nar'],
    ['Physical Review A: General Physics',r'\pra'],
    ['Physical Review B: Solid State',r'\prb'],
    ['Physical Review C',r'\prc'],
    ['Physical Review D',r'\prd'],
    ['Physical Review E',r'\pre'],
    ['Physical Review Letters',r'\prl'],
    ['Publications of the Astron. Soc. of Australia',r'\pasa'],
    ['Publications of the ASP',r'\pasp'],
    ['Publications of the ASJ',r'\pasj'],
    ['Revista Mexicana de Astronomia y Astrofisica',r'\rmxaa'],
    ['Quarterly Journal of the RAS',r'\qjras'],
    ['Sky and Telescope',r'\skytel'],
    ['Solar Physics',r'\solphys'],
    ['Soviet Astronomy',r'\sovast'],
    ['Space Science Reviews',r'\ssr'],
    ['Zeitschrift fuer Astrophysik',r'\zap'],
    ['Nature',r'\nat'],
    ['IAU Cirulars',r'\iaucirc'],
    ['Astrophysics Letters',r'\aplett'],
    ['Astrophysics Space Physics Research',r'\apspr'],
    ['Bulletin Astronomical Institute of the Netherlands',r'\bain'],
    ['Fundamental Cosmic Physics',r'\fcp'],
    ['Geochimica Cosmochimica Acta',r'\gca'],
    ['Geophysics Research Letters',r'\grl'],
    ['Journal of Chemical Physics',r'\jcp'],
    ['Journal of Geophysics Research',r'\jgr'],
    ['Journal of Quantitiative Spectroscopy and Radiative Transfer',r'\jqsrt'],
    ['Mem. Societa Astronomica Italiana',r'\memsai'],
    ['Nuclear Physics A',r'\nphysa'],
    ['Physics Reports',r'\physrep'],
    ['Physica Scripta',r'\physscr'],
    ['Planetary Space Science',r'\planss'],
    ['Proceedings of the SPIE',r'\procspie'],
]