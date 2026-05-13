from django.urls import path
from .views import get_cetegory, create_cetegory, update_cetegory, get_cetegory_byid, delete_cetegory, get_books, add_books, update_books, book_id, del_books

urlpatterns =[

    path('all_cate',get_cetegory,name='books'),
    path('cate_create',create_cetegory,name='create'),
    path('cate_update/<int:pk>',update_cetegory,name='update'),
    path('get_cate/<int:pk>',get_cetegory_byid,name='getbooks'),
    path('delete_cate/<int:pk>',delete_cetegory,name='delete'),

    path('all_books',get_books,name='books',),
    path('books_add',add_books,name='add'),
    path('books_update/<int:pk>',update_books,name='update'),
    path('get_by_id/<int:pk>',book_id,name='get books'),
    path('books_delete/<int:pk>',del_books,name='delete')
]