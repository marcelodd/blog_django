from django.shortcuts import render
from django.views.generic import ListView, DetailView
from models import Post

class index_view(ListView):
	model = Post
	template_name  = "index.html"
	paginate_by = 2
	
class detalhe_post(DetailView):
	model = Post
	template_name = "post.html"
	

