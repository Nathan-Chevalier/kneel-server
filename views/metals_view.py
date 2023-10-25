import json
from nss_handler import status
from repository import db_get_single, db_get_all

class MetalsView:
    def get(self, handler, pk):
        if pk != 0:
            sql = """
                SELECT
                    m.id,
                    m.metal,
                    m.price
                FROM Metals m
                WHERE m.id = ?
                """
            query_results = db_get_single(sql, pk)
            serialized_metal = json.dumps(dict(query_results))

            return handler.response(serialized_metal, status.HTTP_200_SUCCESS.value)
        else:

            query_results = db_get_all("SELECT m.id, m.metal, m.price FROM Metals m")
            metals = [dict(row) for row in query_results]
            serialized_metals = json.dumps(metals)

            return handler.response(serialized_metals, status.HTTP_200_SUCCESS.value)
    
    def add(self, handler, data):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)