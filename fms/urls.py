from django.urls import path
from . import views
urlpatterns = [

   # path('view-pdf/<str:filename>/', views.PDFView.as_view(), name='pdf'),
    #received
   

   path('home',views.DashboardView.as_view(),name='dashboard'),
#    path('pdf',views.DisplayPdfView.as_view(),name='pdf'),
#RECEIVED URLS
   path('received',views.ReceivedListView.as_view(),name='received'),
   path('search',views.SearchReceivedListView.as_view(),name='search'),
   path('addreceived',views.ReceivedAddView.as_view(),name='addreceived'),
   path('edit-received/<int:file_id>',views.UpdateReceived.as_view(),name='edit-received'),
   path('delete-received/<int:file_id>',views.DeleteReceived.as_view(),name='delete-received'),
   path('view-file/<int:file_id>/', views.ReceivedViewFile.as_view(), name='view-file'),

   #Sent URLS
   path('sent',views.SentListView.as_view(),name='sent'),
   path('addsent',views.SentAddView.as_view(),name='addsent'),
   path('sentsearch',views.SearchSentListView.as_view(),name='sentsearch'),
   path('edit-sent/<int:file_id>',views.UpdateSent.as_view(),name='edit-sent'),
   path('delete-sent/<int:file_id>',views.DeleteSent.as_view(),name='delete-sent'),
   path('file/<int:file_id>/', views.SentViewFile.as_view(), name='file'),

   path('download/<int:file_id>/', views.SentDownloadFileView.as_view(), name='sent_download_file'),
   path('received-download/<int:file_id>/', views.ReceivedDownloadFileView.as_view(), name='received-download'),

  
]