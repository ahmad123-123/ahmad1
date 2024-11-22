from django.shortcuts import HttpResponse

def home_page(request):
    html_response = """
        <1>Blog site</h1>
        """

    return HttpResponse(html_response)


