# -*- coding: utf-8 -*-
from internetarchive.cli.argparser import get_args_dict, get_xml_text


def test_get_xml_text():
    xml_str = ('<Error><Code>NoSuchBucket</Code>'
       '<Message>The specified bucket does not exist.</Message>'
       '<Resource>does-not-exist-! not found by Metadata::get_obj()[server]</Resource>'
       '<RequestId>d56bdc63-169b-4b4f-8c47-0fac6de39040</RequestId></Error>')
    assert get_xml_text(xml_str) == 'The specified bucket does not exist.'


def test_get_args_dict():
    test_input = [
            'collection:test_collection',
            "description: Attention: multiple colon's",
            'unicode_test:தமிழ்',
            'subject:subject1',
            'subject:subject2',
    ]
    test_output = {
            'collection': 'test_collection', 
            'description': " Attention: multiple colon's", 
            'unicode_test': '\xe0\xae\xa4\xe0\xae\xae\xe0\xae\xbf\xe0\xae\xb4\xe0\xaf\x8d', 
            'subject': ['subject1', 'subject2']
    }
    args_dict = get_args_dict(test_input)
    for key, value in args_dict.items():
        assert test_output[key] == value
