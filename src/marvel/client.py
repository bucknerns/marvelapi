from hashlib import md5
import time

from requests import Session


class MarvelClient(Session):
    def __init__(self, url, api_key, api_secret):
        super(MarvelClient, self).__init__()
        ts = str(time.time())
        hash_str = md5(f"{ts}{api_secret}{api_key}".encode("utf8")).hexdigest()
        self.params = {"hash": hash_str, "apikey": api_key, "ts": ts}
        self.url = url

    def get_story(self, story_id):
        url = f"{self.url}/v1/public/stories/{story_id}"
        return self.get(url)

    def get_single_series(self, series_id):
        """Changed to get_single_series since series is singular and plural"""
        url = f"{self.url}/v1/public/series/{series_id}"
        return self.get(url)

    def get_event(self, event_id):
        url = f"{self.url}/v1/public/events/{event_id}"
        return self.get(url)

    def get_creator(self, creator_id):
        url = f"{self.url}/v1/public/creators/{creator_id}"
        return self.get(url)

    def get_comic(self, comic_id):
        url = f"{self.url}/v1/public/comics/{comic_id}"
        return self.get(url)

    def get_character(self, character_id):
        url = f"{self.url}/v1/public/characters/{character_id}"
        return self.get(url)

    def get_story_comics(
        self, story_id, format=None, format_type=None, no_variants=None,
        date_descriptor=None, date_range=None, title=None,
        title_starts_with=None, start_year=None, issue_number=None,
        diamond_code=None, digital_id=None, upc=None, isbn=None, ean=None,
        issn=None, has_digital_issue=None, modified_since=None, creators=None,
        characters=None, series=None, events=None, shared_appearances=None,
            collaborators=None, order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/stories/{story_id}/comics"
        params = {
            "format": format, "formatType": format_type,
            "noVariants": no_variants, "dateDescriptor": date_descriptor,
            "dateRange": date_range, "title": title,
            "titleStartsWith": title_starts_with, "startYear": start_year,
            "issueNumber": issue_number, "diamondCode": diamond_code,
            "digitalId": digital_id, "upc": upc, "isbn": isbn, "ean": ean,
            "issn": issn, "hasDigitalIssue": has_digital_issue,
            "modifiedSince": modified_since, "creators": creators,
            "characters": characters, "series": series, "events": events,
            "sharedAppearances": shared_appearances,
            "collaborators": collaborators, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_series_comics(
        self, series_id, format=None, format_type=None, no_variants=None,
        date_descriptor=None, date_range=None, title=None,
        title_starts_with=None, start_year=None, issue_number=None,
        diamond_code=None, digital_id=None, upc=None, isbn=None, ean=None,
        issn=None, has_digital_issue=None, modified_since=None, creators=None,
        characters=None, events=None, stories=None, shared_appearances=None,
            collaborators=None, order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/series/{series_id}/comics"
        params = {
            "format": format, "formatType": format_type,
            "noVariants": no_variants, "dateDescriptor": date_descriptor,
            "dateRange": date_range, "title": title,
            "titleStartsWith": title_starts_with, "startYear": start_year,
            "issueNumber": issue_number, "diamondCode": diamond_code,
            "digitalId": digital_id, "upc": upc, "isbn": isbn, "ean": ean,
            "issn": issn, "hasDigitalIssue": has_digital_issue,
            "modifiedSince": modified_since, "creators": creators,
            "characters": characters, "events": events, "stories": stories,
            "sharedAppearances": shared_appearances,
            "collaborators": collaborators, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_event_comics(
        self, event_id, format=None, format_type=None, no_variants=None,
        date_descriptor=None, date_range=None, title=None,
        title_starts_with=None, start_year=None, issue_number=None,
        diamond_code=None, digital_id=None, upc=None, isbn=None, ean=None,
        issn=None, has_digital_issue=None, modified_since=None, creators=None,
        characters=None, series=None, events=None, stories=None,
        shared_appearances=None, collaborators=None, order_by=None,
            limit=None, offset=None):
        url = f"{self.url}/v1/public/events/{event_id}/comics"
        params = {
            "format": format, "formatType": format_type,
            "noVariants": no_variants, "dateDescriptor": date_descriptor,
            "dateRange": date_range, "title": title,
            "titleStartsWith": title_starts_with, "startYear": start_year,
            "issueNumber": issue_number, "diamondCode": diamond_code,
            "digitalId": digital_id, "upc": upc, "isbn": isbn, "ean": ean,
            "issn": issn, "hasDigitalIssue": has_digital_issue,
            "modifiedSince": modified_since, "creators": creators,
            "characters": characters, "series": series, "events": events,
            "stories": stories, "sharedAppearances": shared_appearances,
            "collaborators": collaborators, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_creator_comics(
        self, creator_id, format=None, format_type=None, no_variants=None,
        date_descriptor=None, date_range=None, title=None,
        title_starts_with=None, start_year=None, issue_number=None,
        diamond_code=None, digital_id=None, upc=None, isbn=None, ean=None,
        issn=None, has_digital_issue=None, modified_since=None,
        characters=None, series=None, events=None, stories=None,
        shared_appearances=None, collaborators=None, order_by=None,
            limit=None, offset=None):
        url = f"{self.url}/v1/public/creators/{creator_id}/comics"
        params = {
            "format": format, "formatType": format_type,
            "noVariants": no_variants, "dateDescriptor": date_descriptor,
            "dateRange": date_range, "title": title,
            "titleStartsWith": title_starts_with, "startYear": start_year,
            "issueNumber": issue_number, "diamondCode": diamond_code,
            "digitalId": digital_id, "upc": upc, "isbn": isbn, "ean": ean,
            "issn": issn, "hasDigitalIssue": has_digital_issue,
            "modifiedSince": modified_since, "characters": characters,
            "series": series, "events": events, "stories": stories,
            "sharedAppearances": shared_appearances,
            "collaborators": collaborators, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_comics(
        self, format=None, format_type=None, no_variants=None,
        date_descriptor=None, date_range=None, title=None,
        title_starts_with=None, start_year=None, issue_number=None,
        diamond_code=None, digital_id=None, upc=None, isbn=None, ean=None,
        issn=None, has_digital_issue=None, modified_since=None, creators=None,
        characters=None, series=None, events=None, stories=None,
        shared_appearances=None, collaborators=None, order_by=None, limit=None,
            offset=None):
        url = f"{self.url}/v1/public/comics"
        params = {
            "format": format, "formatType": format_type,
            "noVariants": no_variants, "dateDescriptor": date_descriptor,
            "dateRange": date_range, "title": title,
            "titleStartsWith": title_starts_with, "startYear": start_year,
            "issueNumber": issue_number, "diamondCode": diamond_code,
            "digitalId": digital_id, "upc": upc, "isbn": isbn, "ean": ean,
            "issn": issn, "hasDigitalIssue": has_digital_issue,
            "modifiedSince": modified_since, "creators": creators,
            "characters": characters, "series": series, "events": events,
            "stories": stories, "sharedAppearances": shared_appearances,
            "collaborators": collaborators, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_character_comics(
        self, character_id, format=None, format_type=None, no_variants=None,
        date_descriptor=None, date_range=None, title=None,
        title_starts_with=None, start_year=None, issue_number=None,
        diamond_code=None, digital_id=None, upc=None, isbn=None, ean=None,
        issn=None, has_digital_issue=None, modified_since=None, creators=None,
        series=None, events=None, stories=None, shared_appearances=None,
            collaborators=None, order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/characters/{character_id}/comics"
        params = {
            "format": format, "formatType": format_type,
            "noVariants": no_variants, "dateDescriptor": date_descriptor,
            "dateRange": date_range, "title": title,
            "titleStartsWith": title_starts_with, "startYear": start_year,
            "issueNumber": issue_number, "diamondCode": diamond_code,
            "digitalId": digital_id, "upc": upc, "isbn": isbn, "ean": ean,
            "issn": issn, "hasDigitalIssue": has_digital_issue,
            "modifiedSince": modified_since, "creators": creators,
            "series": series, "events": events, "stories": stories,
            "sharedAppearances": shared_appearances,
            "collaborators": collaborators, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_story_series(
        self, story_id, events=None, title=None, title_starts_with=None,
        start_year=None, modified_since=None, comics=None, creators=None,
        characters=None, series_type=None, contains=None, order_by=None,
            limit=None, offset=None):
        url = f"{self.url}/v1/public/stories/{story_id}/series"
        params = {
            "events": events, "title": title,
            "titleStartsWith": title_starts_with, "startYear": start_year,
            "modifiedSince": modified_since, "comics": comics,
            "creators": creators, "characters": characters,
            "seriesType": series_type, "contains": contains,
            "orderBy": order_by, "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_story_events(
        self, story_id, name=None, name_starts_with=None, modified_since=None,
        creators=None, characters=None, series=None, comics=None,
            order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/stories/{story_id}/events"
        params = {
            "name": name, "nameStartsWith": name_starts_with,
            "modifiedSince": modified_since, "creators": creators,
            "characters": characters, "series": series, "comics": comics,
            "orderBy": order_by, "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_story_creators(
        self, story_id, first_name=None, middle_name=None, last_name=None,
        suffix=None, name_starts_with=None, first_name_starts_with=None,
        middle_name_starts_with=None, last_name_starts_with=None,
        modified_since=None, comics=None, series=None, events=None,
            order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/stories/{story_id}/creators"
        params = {
            "firstName": first_name, "middleName": middle_name,
            "lastName": last_name, "suffix": suffix,
            "nameStartsWith": name_starts_with,
            "firstNameStartsWith": first_name_starts_with,
            "middleNameStartsWith": middle_name_starts_with,
            "lastNameStartsWith": last_name_starts_with,
            "modifiedSince": modified_since, "comics": comics,
            "series": series, "events": events, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_story_characters(
        self, story_id, name=None, name_starts_with=None, modified_since=None,
        comics=None, series=None, events=None, order_by=None, limit=None,
            offset=None):
        url = f"{self.url}/v1/public/stories/{story_id}/characters"
        params = {
            "name": name, "nameStartsWith": name_starts_with,
            "modifiedSince": modified_since, "comics": comics,
            "series": series, "events": events, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_stories(
        self, modified_since=None, comics=None, series=None, events=None,
        creators=None, characters=None, order_by=None, limit=None,
            offset=None):
        url = f"{self.url}/v1/public/stories"
        params = {
            "modifiedSince": modified_since, "comics": comics,
            "series": series, "events": events, "creators": creators,
            "characters": characters, "orderBy": order_by, "limit": limit,
            "offset": offset}
        return self.get(url, params=params)

    def get_series_stories(
        self, series_id, modified_since=None, comics=None, events=None,
        creators=None, characters=None, order_by=None, limit=None,
            offset=None):
        url = f"{self.url}/v1/public/series/{series_id}/stories"
        params = {
            "modifiedSince": modified_since, "comics": comics,
            "events": events, "creators": creators, "characters": characters,
            "orderBy": order_by, "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_series_events(
        self, series_id, name=None, name_starts_with=None, modified_since=None,
        creators=None, characters=None, comics=None, stories=None,
            order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/series/{series_id}/events"
        params = {
            "name": name, "nameStartsWith": name_starts_with,
            "modifiedSince": modified_since, "creators": creators,
            "characters": characters, "comics": comics, "stories": stories,
            "orderBy": order_by, "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_serices_creators(
        self, series_id, first_name=None, middle_name=None, last_name=None,
        suffix=None, name_starts_with=None, first_name_starts_with=None,
        middle_name_starts_with=None, last_name_starts_with=None,
        modified_since=None, comics=None, events=None, stories=None,
            order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/series/{series_id}/creators"
        params = {
            "firstName": first_name, "middleName": middle_name,
            "lastName": last_name, "suffix": suffix,
            "nameStartsWith": name_starts_with,
            "firstNameStartsWith": first_name_starts_with,
            "middleNameStartsWith": middle_name_starts_with,
            "lastNameStartsWith": last_name_starts_with,
            "modifiedSince": modified_since, "comics": comics,
            "events": events, "stories": stories, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_series_characters(
        self, series_id, name=None, name_starts_with=None, modified_since=None,
        comics=None, events=None, stories=None, order_by=None, limit=None,
            offset=None):
        url = f"{self.url}/v1/public/series/{series_id}/characters"
        params = {
            "name": name, "nameStartsWith": name_starts_with,
            "modifiedSince": modified_since, "comics": comics,
            "events": events, "stories": stories, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_series(
        self, title=None, title_starts_with=None, start_year=None,
        modified_since=None, comics=None, stories=None, events=None,
        creators=None, characters=None, series_type=None, contains=None,
            order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/series"
        params = {
            "title": title, "titleStartsWith": title_starts_with,
            "startYear": start_year, "modifiedSince": modified_since,
            "comics": comics, "stories": stories, "events": events,
            "creators": creators, "characters": characters,
            "seriesType": series_type, "contains": contains,
            "orderBy": order_by, "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_event_stories(
        self, event_id, modified_since=None, comics=None, series=None,
        creators=None, characters=None, order_by=None, limit=None,
            offset=None):
        url = f"{self.url}/v1/public/events/{event_id}/stories"
        params = {
            "modifiedSince": modified_since, "comics": comics,
            "series": series, "creators": creators,
            "characters": characters, "orderBy": order_by, "limit": limit,
            "offset": offset}
        return self.get(url, params=params)

    def get_event_series(
        self, event_id, title=None, title_starts_with=None, start_year=None,
        modified_since=None, comics=None, stories=None, creators=None,
        characters=None, series_type=None, contains=None, order_by=None,
            limit=None, offset=None):
        url = f"{self.url}/v1/public/events/{event_id}/series"
        params = {
            "title": title, "titleStartsWith": title_starts_with,
            "startYear": start_year, "modifiedSince": modified_since,
            "comics": comics, "stories": stories, "creators": creators,
            "characters": characters, "seriesType": series_type,
            "contains": contains, "orderBy": order_by, "limit": limit,
            "offset": offset}
        return self.get(url, params=params)

    def get_event_creators(
        self, event_id, first_name=None, middle_name=None, last_name=None,
        suffix=None, name_starts_with=None, first_name_starts_with=None,
        middle_name_starts_with=None, last_name_starts_with=None,
        modified_since=None, comics=None, series=None, stories=None,
            order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/events/{event_id}/creators"
        params = {
            "firstName": first_name, "middleName": middle_name,
            "lastName": last_name, "suffix": suffix,
            "nameStartsWith": name_starts_with,
            "firstNameStartsWith": first_name_starts_with,
            "middleNameStartsWith": middle_name_starts_with,
            "lastNameStartsWith": last_name_starts_with,
            "modifiedSince": modified_since, "comics": comics,
            "series": series, "stories": stories, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_event_characters(
        self, event_id, name=None, name_starts_with=None, modified_since=None,
        comics=None, series=None, stories=None, order_by=None, limit=None,
            offset=None):
        url = f"{self.url}/v1/public/events/{event_id}/characters"
        params = {
            "name": name, "nameStartsWith": name_starts_with,
            "modifiedSince": modified_since, "comics": comics,
            "series": series, "stories": stories, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_events(
        self, name=None, name_starts_with=None, modified_since=None,
        creators=None, characters=None, series=None, comics=None, stories=None,
            order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/events"
        params = {
            "name": name, "nameStartsWith": name_starts_with,
            "modifiedSince": modified_since, "creators": creators,
            "characters": characters, "series": series, "comics": comics,
            "stories": stories, "orderBy": order_by, "limit": limit,
            "offset": offset}
        return self.get(url, params=params)

    def get_creator_stories(
        self, creator_id, modified_since=None, comics=None, series=None,
        events=None, characters=None, order_by=None, limit=None,
            offset=None):
        url = f"{self.url}/v1/public/creators/{creator_id}/stories"
        params = {
            "modifiedSince": modified_since, "comics": comics,
            "series": series, "events": events, "characters": characters,
            "orderBy": order_by, "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_creator_series(
        self, creator_id, title=None, title_starts_with=None, start_year=None,
        modified_since=None, comics=None, stories=None, events=None,
        characters=None, series_type=None, contains=None, order_by=None,
            limit=None, offset=None):
        url = f"{self.url}/v1/public/creators/{creator_id}/series"
        params = {
            "title": title, "titleStartsWith": title_starts_with,
            "startYear": start_year, "modifiedSince": modified_since,
            "comics": comics, "stories": stories, "events": events,
            "characters": characters, "seriesType": series_type,
            "contains": contains, "orderBy": order_by, "limit": limit,
            "offset": offset}
        return self.get(url, params=params)

    def get_creator_events(
        self, creator_id, name=None, name_starts_with=None,
        modified_since=None, characters=None, series=None, comics=None,
            stories=None, order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/creators/{creator_id}/events"
        params = {
            "name": name, "nameStartsWith": name_starts_with,
            "modifiedSince": modified_since, "characters": characters,
            "series": series, "comics": comics, "stories": stories,
            "orderBy": order_by, "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_creators(
        self, first_name=None, middle_name=None, last_name=None,
        suffix=None, name_starts_with=None, first_name_starts_with=None,
        middle_name_starts_with=None, last_name_starts_with=None,
        modified_since=None, comics=None, series=None, events=None,
            stories=None, order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/creators"
        params = {
            "firstName": first_name, "middleName": middle_name,
            "lastName": last_name, "suffix": suffix,
            "nameStartsWith": name_starts_with,
            "firstNameStartsWith": first_name_starts_with,
            "middleNameStartsWith": middle_name_starts_with,
            "lastNameStartsWith": last_name_starts_with,
            "modifiedSince": modified_since, "comics": comics,
            "series": series, "events": events, "stories": stories,
            "orderBy": order_by, "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_comic_stories(
        self, comic_id, modified_since=None, series=None, events=None,
        creators=None, characters=None, order_by=None, limit=None,
            offset=None):
        url = f"{self.url}/v1/public/comics/{comic_id}/stories"
        params = {
            "modifiedSince": modified_since, "series": series,
            "events": events, "creators": creators, "characters": characters,
            "orderBy": order_by, "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_comic_events(
        self, comic_id, name=None, name_starts_with=None, modified_since=None,
        creators=None, characters=None, series=None, stories=None,
            order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/comics/{comic_id}/events"
        params = {
            "name": name, "nameStartsWith": name_starts_with,
            "modifiedSince": modified_since, "creators": creators,
            "characters": characters, "series": series, "stories": stories,
            "orderBy": order_by, "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_comic_creators(
        self, comic_id, first_name=None, middle_name=None, last_name=None,
        suffix=None, name_starts_with=None, first_name_starts_with=None,
        middle_name_starts_with=None, last_name_starts_with=None,
        modified_since=None, comics=None, series=None, stories=None,
            order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/comics/{comic_id}/creators"
        params = {
            "firstName": first_name, "middleName": middle_name,
            "lastName": last_name, "suffix": suffix,
            "nameStartsWith": name_starts_with,
            "firstNameStartsWith": first_name_starts_with,
            "middleNameStartsWith": middle_name_starts_with,
            "lastNameStartsWith": last_name_starts_with,
            "modifiedSince": modified_since, "comics": comics,
            "series": series, "stories": stories, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_comic_characters(
        self, comic_id, name=None, name_starts_with=None,
        modified_since=None, series=None, events=None, stories=None,
            order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/comics/{comic_id}/characters"
        params = {
            "name": name, "nameStartsWith": name_starts_with,
            "modifiedSince": modified_since, "series": series,
            "events": events, "stories": stories, "orderBy": order_by,
            "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_character_stories(
        self, character_id, modified_since=None, comics=None, series=None,
        events=None, creators=None, order_by=None, limit=None,
            offset=None):
        url = f"{self.url}/v1/public/characters/{character_id}/stories"
        params = {
            "modifiedSince": modified_since, "comics": comics,
            "series": series, "events": events, "creators": creators,
            "orderBy": order_by, "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_character_series(
        self, character_id, title=None, title_starts_with=None,
        start_year=None, modified_since=None, comics=None, stories=None,
        events=None, creators=None, series_type=None, contains=None,
            order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/characters/{character_id}/series"
        params = {
            "title": title, "titleStartsWith": title_starts_with,
            "startYear": start_year, "modifiedSince": modified_since,
            "comics": comics, "stories": stories, "events": events,
            "creators": creators, "seriesType": series_type,
            "contains": contains, "orderBy": order_by, "limit": limit,
            "offset": offset}
        return self.get(url, params=params)

    def get_character_events(
        self, character_id, name=None, name_starts_with=None,
        modified_since=None, creators=None, series=None, comics=None,
            stories=None, order_by=None, limit=None, offset=None):
        url = f"{self.url}/v1/public/characters/{character_id}/events"
        params = {
            "name": name, "nameStartsWith": name_starts_with,
            "modifiedSince": modified_since, "creators": creators,
            "series": series, "comics": comics, "stories": stories,
            "orderBy": order_by, "limit": limit, "offset": offset}
        return self.get(url, params=params)

    def get_characters(
        self, name=None, name_starts_with=None, modified_since=None,
        comics=None, series=None, events=None, stories=None, order_by=None,
            limit=None, offset=None):
        url = f"{self.url}/v1/public/characters"
        params = {
            "name": name, "nameStartsWith": name_starts_with,
            "modifiedSince": modified_since, "comics": comics,
            "series": series, "events": events, "stories": stories,
            "orderBy": order_by, "limit": limit, "offset": offset}
        return self.get(url, params=params)
