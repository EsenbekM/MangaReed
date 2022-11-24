import coreapi
from rest_framework.schemas.coreapi import AutoSchema
import coreschema


class GetMangaSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "GET":
            api_fields = [
                coreapi.Field(name='id', required=True, location='path',
                              schema=coreschema.String(description='str (id)')),
                coreapi.Field(name='page', required=False, location='query',
                              schema=coreschema.String(description='int (default=0)')),
                coreapi.Field(name='count', required=False, location='query',
                              schema=coreschema.String(description='int (default=15)')),
            ]
        return self._manual_fields + api_fields