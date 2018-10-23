
.. code:: ipython3

    from marvel.client import MarvelClient

.. code:: ipython3

    client = MarvelClient("http://gateway.marvel.com", "<api_key>", "<api_secret>")

.. code:: ipython3

    resp = client.get_comic(16246)

.. code:: ipython3

    resp.json()




.. parsed-literal::

    {'code': 200,
     'status': 'Ok',
     'copyright': '© 2018 MARVEL',
     'attributionText': 'Data provided by Marvel. © 2018 MARVEL',
     'attributionHTML': '<a href="http://marvel.com">Data provided by Marvel. © 2018 MARVEL</a>',
     'etag': '0ee715261c97423ba6caa142956a1194d5ad3d66',
     'data': {'offset': 0,
      'limit': 20,
      'total': 1,
      'count': 1,
      'results': [{'id': 16246,
        'digitalId': 0,
        'title': 'Cap Transport (2005) #7',
        'issueNumber': 7,
        'variantDescription': '',
        'description': None,
        'modified': '-0001-11-30T00:00:00-0500',
        'isbn': '',
        'upc': '',
        'diamondCode': '',
        'ean': '',
        'issn': '',
        'format': 'Comic',
        'pageCount': 0,
        'textObjects': [],
        'resourceURI': 'http://gateway.marvel.com/v1/public/comics/16246',
        'urls': [{'type': 'detail',
          'url': 'http://marvel.com/comics/issue/16246/cap_transport_2005_7?utm_campaign=apiRef&utm_source=a1b984315df89963191b79f350c37f60'}],
        'series': {'resourceURI': 'http://gateway.marvel.com/v1/public/series/2722',
         'name': 'Cap Transport (2005 - 2006)'},
        'variants': [],
        'collections': [],
        'collectedIssues': [],
        'dates': [{'type': 'onsaleDate', 'date': '2029-12-31T00:00:00-0500'},
         {'type': 'focDate', 'date': '-0001-11-30T00:00:00-0500'}],
        'prices': [{'type': 'printPrice', 'price': 0}],
        'thumbnail': {'path': 'http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available',
         'extension': 'jpg'},
        'images': [],
        'creators': {'available': 9,
         'collectionURI': 'http://gateway.marvel.com/v1/public/comics/16246/creators',
         'items': [{'resourceURI': 'http://gateway.marvel.com/v1/public/creators/2133',
           'name': 'Tom Brevoort',
           'role': 'editor'},
          {'resourceURI': 'http://gateway.marvel.com/v1/public/creators/5248',
           'name': 'Molly Lazer',
           'role': 'editor'},
          {'resourceURI': 'http://gateway.marvel.com/v1/public/creators/4371',
           'name': 'Andy Schmidt',
           'role': 'editor'},
          {'resourceURI': 'http://gateway.marvel.com/v1/public/creators/367',
           'name': 'Ed Brubaker',
           'role': 'writer'},
          {'resourceURI': 'http://gateway.marvel.com/v1/public/creators/7129',
           'name': 'Virtual Calligraphy',
           'role': 'letterer'},
          {'resourceURI': 'http://gateway.marvel.com/v1/public/creators/8635',
           'name': 'Vc Randy Gentile',
           'role': 'letterer'},
          {'resourceURI': 'http://gateway.marvel.com/v1/public/creators/8504',
           'name': "Frank D'ARMATA",
           'role': 'colorist'},
          {'resourceURI': 'http://gateway.marvel.com/v1/public/creators/374',
           'name': 'Steve Epting',
           'role': 'penciler'},
          {'resourceURI': 'http://gateway.marvel.com/v1/public/creators/127',
           'name': 'John Paul Leon',
           'role': 'penciler'}],
         'returned': 9},
        'characters': {'available': 4,
         'collectionURI': 'http://gateway.marvel.com/v1/public/comics/16246/characters',
         'items': [{'resourceURI': 'http://gateway.marvel.com/v1/public/characters/1009220',
           'name': 'Captain America'},
          {'resourceURI': 'http://gateway.marvel.com/v1/public/characters/1009475',
           'name': 'Nomad'},
          {'resourceURI': 'http://gateway.marvel.com/v1/public/characters/1009565',
           'name': 'Scourge'},
          {'resourceURI': 'http://gateway.marvel.com/v1/public/characters/1010791',
           'name': 'Sub-Mariner'}],
         'returned': 4},
        'stories': {'available': 3,
         'collectionURI': 'http://gateway.marvel.com/v1/public/comics/16246/stories',
         'items': [{'resourceURI': 'http://gateway.marvel.com/v1/public/stories/34018',
           'name': 'Cover #34018',
           'type': 'cover'},
          {'resourceURI': 'http://gateway.marvel.com/v1/public/stories/34019',
           'name': 'The Lonesome Death of Jack Monroe',
           'type': 'interiorStory'},
          {'resourceURI': 'http://gateway.marvel.com/v1/public/stories/34020',
           'name': 'Freedom of Speech',
           'type': 'letters'}],
         'returned': 3},
        'events': {'available': 0,
         'collectionURI': 'http://gateway.marvel.com/v1/public/comics/16246/events',
         'items': [],
         'returned': 0}}]}}

