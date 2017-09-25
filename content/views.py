from django.shortcuts import render, redirect
from django.views import View
from content.models import ContentItem, ContentTag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from content.view_utils import *
from .forms import AddContentForm


class HomePage(View):
    """Home page view"""

    def get(self, request):
        # Get the menu
        menu = get_menu_items()

        # Get the latest content for sidebar and footer
        latest_content = get_latest_content()

        # Render the view
        return render(request, "pages/home.html",
                                            {"latest_content" : latest_content,
                                             "menu" : menu,})


class ContentDisplay(View):
    """Single item display"""

    def get(self, request, content_id):
        # Get the menu
        menu = get_menu_items()

        # Query the DB for content by ID
        content = ContentItem.objects.get(pk=content_id)

        # Get the latest content for sidebar and footer
        latest_content = get_latest_content()

        # Get the latest featured content
        featured_content = get_featured_content()

        # get all tags for sidebar
        tags = ContentTag.objects.all()

        # Set the layout based on the content's layout value
        layout = layout_selector(content.layout.selected)

        # Render the view
        return render(request, layout, {"content" : content,
                                        "latest_content" : latest_content,
                                        "featured_content" : featured_content,
                                        "tags" : tags,
                                        "menu" : menu,})


class ContentDisplayList(View):
    """List recent posts of tag type (default all tags)"""

    def get(self, request, tag=None):
        if tag:
            # If there is a tag, query the database with it
            posts = ContentItem.objects.filter(content_type__selected='post').filter(tags__name=tag).order_by('updated_at')
            title = tag
        else:
            # If there is no tag, query the database for all posts
            posts = ContentItem.objects.filter(content_type__selected='post').order_by('updated_at')
            title = "Recent Posts"

        # Paginate the posts object and show 5 posts per page
        paginator = Paginator(posts, 5)

        # Get the page number from the request url (?page=)
        page = request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            posts = paginator.page(paginator.num_pages)

        # Get the menu
        menu = get_menu_items()

        # Get the latest content for sidebar and footer
        latest_content = get_latest_content()

        # Get the latest featured content
        featured_content = get_featured_content()

        # Get the tags that exist in the database
        tags = ContentTag.objects.all()

        # Render the view
        return render(request, "pages/content/content_base.html",
                                                            {"title" : title,
                                                            "posts" : posts,
                                                            "latest_content" : latest_content,
                                                            "featured_content" : featured_content,
                                                            "tags" : tags,
                                                            "menu" : menu,})




class ContentAdmin(View):
    """Content Administrator View"""

    def get(self, request, tag=None):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = AddContentForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                print(form.cleaned_data)
                # redirect to a new URL:
                return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = AddContentForm()

        return render(request, "pages/content/admin/content_admin.html",{"form": form})
