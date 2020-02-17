# -*- coding: utf-8 -*-

import unittest
from abc import ABCMeta
from datetime import datetime

import elasticsearch

from elasticmock import elasticmock

INDEX_NAME = 'test_index'
DOC_TYPE = 'doc-Type'
BODY = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}


class TestElasticmock(unittest.TestCase, metaclass=ABCMeta):

    @elasticmock
    def setUp(self):
        self.es = elasticsearch.Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
