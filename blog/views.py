from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import BlogAuthor, Blog, Movie, Collection
from django.contrib.auth.models import User #Blog author or commenter

def index(request):

	blogs = Blog.objects.all()

	return render(
		request,  
		'index.html', 
		context={'blogs':blogs},
	)

class BlogListView(generic.ListView):
	model: Blog
	paginate_by = 10
	
	def get_queryset(self):
		return Blog.objects.all().order_by('-post_date')


from django.shortcuts import get_object_or_404

class BlogDetailView(generic.ListView): #lol
	"""
	Generic class-based view for a list of blogs posted by a particular BlogAuthor.
	"""
	model = Blog
	paginate_by = 5
	template_name ='blog/blog_detail.html'

	def get_queryset(self):
		"""
		Return list of Blog objects created by BlogAuthor (author id specified in URL)
		"""
		id = self.kwargs['pk']
		target_collection=get_object_or_404(Collection, pk = id)
		return Movie.objects.filter(collection=target_collection).order_by('-release_date')

	def get_context_data(self, **kwargs):
		"""
		Add BlogAuthor to context so they can be displayed in the template
		"""
		# Call the base implementation first to get a context
		context = super(BlogDetailView, self).get_context_data(**kwargs)
		# Get the blogger object from the "pk" URL parameter and add it to the context
		context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
		return context


class BlogAuthorListView(generic.ListView):
	model: BlogAuthor
	paginate_by = 10
	
	def get_queryset(self):
		return BlogAuthor.objects.all() #.order_by('name')


class BlogAuthorDetailView(generic.ListView): #lol
    """
    Generic class-based view for a list of blogs posted by a particular BlogAuthor.
    """
    model = Blog
    paginate_by = 5
    template_name ='blog/blogauthor_detail.html'
    
    #what's the difference betwee get_queryset and get_context_data

    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor (author id specified in URL)
        """
        id = self.kwargs['pk']
        target_author=get_object_or_404(BlogAuthor, pk = id)
        return Blog.objects.filter(author=target_author)
        
    def get_context_data(self, **kwargs):
        """
        Add BlogAuthor to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(BlogAuthorDetailView, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blogger'] = get_object_or_404(BlogAuthor, pk = self.kwargs['pk'])
        return context

#import services

"""from .services import get_books
class BooksPage(generic.TemplateView):
	print("BooksPage")
	def get(self,request):
		print(self)
		print(request)
		books_list = services.get_books('2009', 'edwards')
		print("books_list");
		return render(request,'books.html',books_list)"""
