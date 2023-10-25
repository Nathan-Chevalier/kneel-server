import json
from nss_handler import status
from repository import db_get_single, db_get_all

class SizesView:
    def get(self, handler, pk):
        if pk != 0:
            sql = """
                SELECT
                    s.id,
                    s.carats,
                    s.price
                FROM Sizes s
                WHERE s.id = ?
                """
            query_results = db_get_single(sql, pk)
            serialized_size = json.dumps(dict(query_results))

            return handler.response(serialized_size, status.HTTP_200_SUCCESS.value)
        else:

            query_results = db_get_all("SELECT s.id, s.carats, s.price FROM Sizes s")
            sizes = [dict(row) for row in query_results]
            serialized_sizes = json.dumps(sizes)

            return handler.response(serialized_sizes, status.HTTP_200_SUCCESS.value)
    
    def add(self, handler, data):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    
    def update(self, handler, data, pk):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    
    def delete(self, handler, pk):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)