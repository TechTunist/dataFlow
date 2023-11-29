from django.shortcuts import render
from django.views import View
import requests


# initial page if not logged in or new user
# class DashView(View):
#     def get(self, request):
#         return(render(request, 'DashFlow/dashboard.html'))


def dash_view(request):

    api_url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

    ## prints response code of api call
    # response = requests.get(api_url)
    # print(f"The response status code is: {response.status_code}")

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            print(data['bitcoin'])
            # print(data['usd'])
    except:
        pass

    context = {'data': data['bitcoin']}

    return render(request, 'DashFlow/dashboard.html', context)


class DashView(View):

    template_name = 'DashFlow/dashboard.html'

    def get(self, request, *args, **kwargs):
        api_url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

        data = {}

        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                print(data['bitcoin']) # test in the terminal
        except Exception as e:
            print(e)

        # dict.get() is a type of error handling as it returns the second arg as default if key not found
        context = {'data': data.get('bitcoin', {})} 

        return render(request, self.template_name, context)
