from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("v1/books",views.BookViewSetView,basename="books")

router.register("v1/reviews",views.ReviewUpdateDestroyViewset,basename="reviews")


urlpatterns=[
    path("book/",views.BookCreateListView.as_view()),
    path("book/<int:pk>/",views.BookRetrieveUpdateDestroyView.as_view()),
    path("v2/books/",views.BookListView.as_view()),
    path("v2/books/<int:pk>/",views.BooksGenericView.as_view()),
    path("reviews/<int:pk>/",views.ReviewUpdateRetrieveDestroyView.as_view()),
    path("v2/books/<int:pk>/reviews/add/",views.ReviewCreateView.as_view())
]+router.urls