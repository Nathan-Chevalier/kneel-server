import json
from nss_handler import status
from repository import db_get_single, db_get_all

class StylesView:
    def get(self, handler, pk):
        if pk != 0:
            sql = """
                SELECT
                    s.id,
                    s.style,
                    s.price
                FROM Styles s
                WHERE s.id = ?
                """
            query_results = db_get_single(sql, pk)
            serialized_style = json.dumps(dict(query_results))

            return handler.response(serialized_style, status.HTTP_200_SUCCESS.value)
        else:

            query_results = db_get_all("SELECT s.id, s.style, s.price FROM Styles s")
            styles = [dict(row) for row in query_results]
            serialized_styles = json.dumps(styles)

            return handler.response(serialized_styles, status.HTTP_200_SUCCESS.value)
    
    def add(self, handler, data):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    
    def update(self, handler, data, pk):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    
    def delete(self, handler, pk):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)