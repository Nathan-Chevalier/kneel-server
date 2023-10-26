import json
from nss_handler import status
from repository import db_get_single, db_get_all

class OrdersView:
    def get(self, handler, pk):
        parsed_url = handler.parse_url(handler.path)
        if pk != 0:
            base_sql = """SELECT
                o.id,
                o.styleId,
                o.sizeId,
                o.metalId
                FROM Orders o
                WHERE o.id = ?
                """
            query_results = db_get_single(base_sql, pk)
            dictionary_order = dict(query_results)

            if '_expand' in parsed_url['query_params'] and 'metal' in parsed_url['query_params']['_expand']:
                fk = dictionary_order['metalId']
                sql = """SELECT
                m.id,
                m.metal,
                m.price
                FROM Metals m
                WHERE m.id = ?
                    """
                single_metal = db_get_single(sql, fk)
                metal = {
                    "id": single_metal['id'],
                    "metal": single_metal['metal'],
                    "price": single_metal['price']
                }
                dictionary_order['metal'] = metal
            if '_expand' in parsed_url['query_params'] and 'style' in parsed_url['query_params']['_expand']:
                fk = dictionary_order['styleId']
                sql = """SELECT
                s.id,
                s.style,
                s.price
                FROM Styles s
                WHERE s.id = ?
                """
                single_style = db_get_single(sql, fk)
                style = {
                    "id": single_style['id'],
                    "style": single_style['style'],
                    "price": single_style['price']
                }
                dictionary_order['style'] = style
            if '_expand' in parsed_url['query_params'] and 'size' in parsed_url['query_params']['_expand']:
                fk = dictionary_order['sizeId']
                sql = """SELECT
                s.id,
                s.carats,
                s.price
                FROM Sizes s
                WHERE s.id = ?
                """
                single_size = db_get_single(sql, fk)
                size = {
                    "id": single_size['id'],
                    "carats": single_size['carats'],
                    "price": single_size['price']
                }
                dictionary_order['size'] = size
            serialized_order = json.dumps(dictionary_order)
            return handler.response(serialized_order, status.HTTP_200_SUCCESS.value)
        else:

            query_results = db_get_all("SELECT o.id, o.styleId, o.sizeId, o.metalId FROM Orders o")
            orders = [dict(row) for row in query_results]
            serialized_orders = json.dumps(orders)

            return handler.response(serialized_orders, status.HTTP_200_SUCCESS.value)
    
    def add(self, handler, data):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    
    def update(self, handler, data, pk):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    
    def delete(self, handler, pk):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)