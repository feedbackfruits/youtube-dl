# coding: utf-8
from __future__ import unicode_literals
from .common import InfoExtractor


class AmaraIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?amara\.org/(?:\w+/)?videos/(?P<id>\w+).*'
    _TESTS = [
        {
            'url': 'https://amara.org/en/videos/jVx79ZKGK1ky/info/why-jury-trials-are-becoming-less-common/?tab=video',
            'md5': 'ea10daf2b6154b8c1ecf9922aca5e8ae',
            'info_dict': {
                'id': 'h6ZuVdvYnfE',
                'ext': 'mp4',
                'title': 'Why jury trials are becoming less common',
                'description': 'md5:a61811c319943960b6ab1c23e0cbc2c1',
                'thumbnail': r're:^https?://.*\.jpg$',
                'subtitles': dict,
                'upload_date': '20160813',
                'uploader': 'PBS NewsHour',
                'uploader_id': 'PBSNewsHour'
            }
        },
        {
            'url': 'https://amara.org/en/videos/ZEVX7U5OT6UU/info/native-linkedin-video/',
            'md5': 'e792f0b86fc75705801573b33d5f9594',
            'info_dict': {
                'id': '330482296',
                'ext': 'mp4',
                'title': 'Native LinkedIn Video',
                'description': 'md5:64fa074587187194903c6f267c7544c6',
                'thumbnail': r're:^https?://.*\.jpg$',
                'subtitles': dict,
                'timestamp': 1555320305,
                'upload_date': '20190415',
                'uploader': 'Vormats',
                'uploader_id': 'user85377268'
            }
        },
        {
            'url': 'https://amara.org/en/videos/s8KL7I3jLmh6/info/the-danger-of-a-single-story/',
            'md5': 'd3970f08512738ee60c5807311ff5d3f',
            'info_dict': {
                'id': 'ChimamandaAdichie_2009G-transcript',
                'ext': 'mp4',
                'title': 'The danger of a single story',
                'description': 'md5:d769b31139c3b8bb5be9177f62ea3f23',
                'thumbnail': r're:^https?://.*\.jpg$',
                'subtitles': dict,
                'upload_date': '20131206'
            }
        }
    ]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        meta = self._download_json('https://amara.org/api/videos/%s/' % video_id, video_id, query={'format': 'json'})

        video_url = meta.get('all_urls')[0]
        subtitles = dict(map(lambda language: [
            language['code'],
            [
                {
                    'ext': 'vtt',
                    'url': language['subtitles_uri'].replace('format=json', 'format=vtt')
                }, {
                    'ext': 'srt',
                    'url': language['subtitles_uri'].replace('format=json', 'format=srt')
                },
            ]
        ], filter(lambda language: language['published'], meta.get('languages', []))))

        return {
            '_type': 'url_transparent',
            'url': video_url,
            'id': video_id,
            'subtitles': subtitles,
            'title': meta['title'],
            'description': meta['description'],
            'thumbnail': meta['thumbnail']
        }
