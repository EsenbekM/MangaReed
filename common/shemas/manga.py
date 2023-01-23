from rest_framework.schemas.coreapi import AutoSchema, coreapi, coreschema


class MangaListShema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "GET":
            api_fields = [
                coreapi.Field(
                    name="type",
                    required=False,
                    location="query",
                    schema=coreschema.String(
                        description="str - 'type' Filter by manga type"
                    ),
                ),
                coreapi.Field(
                    name="genre__title",
                    required=False,
                    location="query",
                    schema=coreschema.String(
                        description="str - 'genre__title' Filter by manga genre"
                    ),
                ),
                coreapi.Field(
                    name="en_name",
                    required=False,
                    location="query",
                    schema=coreschema.String(
                        description="str - 'en_name' Filter by manga en_name(Manga title in English)"
                    ),
                ),
                coreapi.Field(
                    name="ru_name",
                    required=False,
                    location="query",
                    schema=coreschema.String(
                        description="str - 'ru_name' Filter by manga ru_name(Manga title in Russian)"
                    ),
                ),
            ]
            return self._manual_fields + api_fields


class MangaDetailShema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "GET":
            api_fields = [
                coreapi.Field(
                    name="id",
                    required=False,
                    location="path",
                    schema=coreschema.String(
                        description="id - 'id(Primary key) of manga'"
                    ),
                ),
            ]
            return self._manual_fields + api_fields


class MangaAddCommentSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "POST":
            api_fields = [
                coreapi.Field(
                    name="id",
                    required=False,
                    location="path",
                    schema=coreschema.String(
                        description="id - 'id(Primary key) of manga'"
                    ),
                ),
                coreapi.Field(
                    name="text",
                    required=False,
                    location="form",
                    schema=coreschema.String(description="str - 'text'"),
                ),
            ]
            return self._manual_fields + api_fields


class MangaCommentsList(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "GET":
            api_fields = [
                coreapi.Field(
                    name="id",
                    required=False,
                    location="path",
                    schema=coreschema.String(
                        description="id - 'id(Primary key) of manga'"
                    ),
                ),
            ]

            return self._manual_fields + api_fields
