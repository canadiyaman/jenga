from json import loads


class BookSerializer(object):
    def __init__(self, initial_data, request):
        self.initial_data = initial_data
        self.bookmak_set = request.user.bookmark_set.all().values_list('isbn13', flat=True)

    def is_bookmarked(self, isbn13):
        return isbn13 in self.bookmak_set

    def chlid_serializer(self, data):
        data.update({
            "bookmarked": self.is_bookmarked(data['isbn13'])
        })
        return data

    @property
    def data(self):
        return self.chlid_serializer(self.initial_data)


class BookListSerializer(BookSerializer):

    @property
    def data(self):
        book_list = list()
        for _book in self.initial_data:
            book_list.append(self.chlid_serializer(_book))
        return book_list


class BookmarkListSerializer(object):
    def __init__(self, initial_data):
        self.initial_data = initial_data

    def child_serializer(self, bookmark):
        return loads(bookmark.data)

    @property
    def data(self):
        bookmark_list = list()
        for _bookmark in self.initial_data:
            bookmark_list.append(self.child_serializer(_bookmark))
        return bookmark_list
