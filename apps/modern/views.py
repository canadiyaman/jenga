from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from apps.helpers import get_adapter



class BoooksViewset(viewsets.GenericViewSet):
    def get(self, request, *args, **kwargs):
        adapter = get_adapter()
        results = adapter.books()
        return Response(results)

    @action(methods=['get'], detail='search')
    def search(self, request):
        q = request.query_params.get('q')
        adapter = get_adapter()
        results = adapter.search(q)
        return Response(results)



class BookSearchAPIView(APIView):
    def get(self, request):
        q = request.query_params.get('q')
        adapter = get_adapter()
        results = adapter.search(q)
        return Response(results)


class BookDetailAPIView(APIView):
    def get(self, request, isbn13):
        adapter = get_adapter()
        results = adapter.book(isbn13)
        return Response(results)


class BookListAPIView(APIView):
    def get(self, request):
        adapter = get_adapter()
        results = adapter.books(paginated=False)
        return Response({"books": results})
