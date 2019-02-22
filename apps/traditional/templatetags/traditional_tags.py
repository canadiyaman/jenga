from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag()
def book_details_breadcumbs(book):
    return [
        {
            "title": "Books",
            "url": reverse('traditional:books')
        },
        {
            "title": book['title'],
            "url": reverse('traditional:book', kwargs={"isbn13": book['isbn13']})
        }
    ]


@register.simple_tag()
def books_breadcumbs():
    return [
        {
            "title": "Books",
            "url": reverse('traditional:books')
        }
    ]
