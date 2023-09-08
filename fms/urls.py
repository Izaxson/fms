from django.urls import path
from . import views
urlpatterns = [

   # path('view-pdf/<str:filename>/', views.PDFView.as_view(), name='pdf'),
    #received
   path('',views.DashboardView.as_view(),name='dashboard'),
#    path('pdf',views.DisplayPdfView.as_view(),name='pdf'),

   path('received',views.ReceivedListView.as_view(),name='received'),
   path('addreceived',views.ReceivedAddView.as_view(),name='addreceived'),
#    path('viewreceived/<int>:pk',views.viewupload,name='viewupload'),

   path('search/', views.SearchResultsView.as_view(), name='search_results'),
   #Sent
   path('sent',views.SentListView.as_view(),name='sent'),
   path('addsent',views.SentAddView.as_view(),name='addsent'),
   path('download/<int:file_id>/', views.SentDownloadFileView.as_view(), name='sent_download_file'),
   path('received-download/<int:file_id>/', views.ReceivedDownloadFileView.as_view(), name='received-download'),
]