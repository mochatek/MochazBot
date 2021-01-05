from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import telepot
from . import apis
import re
import os

@csrf_exempt
def handler(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user_id = body['message']['chat']['id']
        user_name = body['message']['chat']['first_name']
        cmnd = body['message']['text']

        bot = telepot.Bot(os.environ.get('TELEGRAM_TOKEN'))
        if cmnd[0] == "/":
            if cmnd == "/start":
                msg = apis.showCmnds(user_name)
            elif cmnd == "/psc":
                msg = apis.psc_API()
            elif cmnd == "/fakenumber":
                msg = apis.mobile_API()
            else:
                indx = [m.start() for m in re.finditer(r"_", cmnd)]
                if cmnd[:indx[0]].strip() == '/compile':
                    msg = apis.complier_API(cmnd[indx[0]+1:indx[1]].strip(), cmnd[indx[1]+1:])
                elif cmnd[:indx[0]].strip() == '/ans':
                    msg = apis.ques_API(cmnd[indx[0]+1:])
                elif cmnd[:indx[0]].strip() == '/inbox':
                    msg = apis.inbox_API(cmnd[indx[0]+1:indx[1]].strip(), cmnd[indx[1]+1:])
        else:
            msg = "Sorry! I don't understand this command. 😕"
        bot.sendMessage(user_id, msg, parse_mode='Markdown')

    return HttpResponse('ok')
        
