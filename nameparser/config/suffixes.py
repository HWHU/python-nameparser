# -*- coding: utf-8 -*-
from __future__ import unicode_literals

SUFFIX_NOT_ACRONYMS = set([
    'esq',
    'esquire',
    'jr',
    'jnr',
    'sr',
    'snr',
    '2',
    'i',
    'ii',
    'iii',
    'iv',
    'v',
])
SUFFIX_ACRONYMS = set([
    'ae',
    'afc',
    'afm',
    'arrc',
    'bart',
    'bem',
    'bt',
    'cb',
    'cbe',
    'cfp',
    'cgc',
    'cgm',
    'ch',
    'chfc',
    'cie',
    'clu',
    'cmg',
    'cpa',
    'cpm',
    'csi',
    'csm',
    'cvo',
    'dbe',
    'dcb',
    'dcm',
    'dcmg',
    'dcvo',
    'dds',
    'dfc',
    'dfm',
    'dmd',
    'do',
    'dpm',
    'dsc',
    'dsm',
    'dso',
    'dvm',
    'ed',
    'erd',
    'gbe',
    'gc',
    'gcb',
    'gcie',
    'gcmg',
    'gcsi',
    'gcvo',
    'gm',
    'idsm',
    'iom',
    'iso',
    'kbe',
    'kcb',
    'kcie',
    'kcmg',
    'kcsi',
    'kcvo',
    'kg',
    'kp',
    'kt',
    'lg',
    'lt',
    'lvo',
    'ma',
    'mba',
    'mbe',
    'mc',
    'md',
    'mm',
    'mp',
    'msm',
    'mvo',
    'obe',
    'obi',
    'om',
    'phd',
    'phr',
    'pmp',
    'qam',
    'qc',
    'qfsm',
    'qgm',
    'qpm',
    'rd',
    'rrc',
    'rvm',
    'sgm',
    'td',
    'ud',
    'vc',
    'vd',
    'vrd',
])
SUFFIXES = SUFFIX_ACRONYMS | SUFFIX_NOT_ACRONYMS
"""

Pieces that come at the end of the name but are not last names. These potentially
conflict with initials that might be at the end of the name.

These may be updated in the future because some of them are actually titles that just
come at the end of the name, so semantically this is wrong. Positionally, it's correct.

"""