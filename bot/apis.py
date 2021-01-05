import requests
from bs4 import BeautifulSoup
from random import randint
import wikipedia

def showCmnds(user_name):
    res = "Hi "+user_name+", I'm mochazbot. 🤖"
    cmnds = [
        "\n\n/start - Start the bot.😜",
        "\n\n/psc - Shows 20 PSC ques & ans.📖",
        "\n\n/compile\_lang\_code - Programming language compiler. 💻",
        "\n\[ *lang : *`C Cpp Python3` ]",
        "\n\n/ans\_question - Answers the _question_.",
        "\n\n/fakenumber - Gives fake mobile numbers which you can use for registrations.📱",
        "\n\n/inbox\_number\_count - Shows last _count_ messages recieved in the _number_. 📥",
    ]
    for cmnd in cmnds:
        res = res + cmnd
    return res


def mobile_API():
    res = "📱 *FAKE MOBILE NUMBERS* 📱\n\n"
    nums = ["🇮🇳 : 917428723247","\n🇮🇳 : 918160651749",
            "\n\n _You can use these numbers for registrations and recieving OTP/SMS_ \n"]
    for num in nums:
        res = res + num
    return res


def inbox_API(number, count):
    urlDict = {'917428723247':'https://receive-sms-free.net/Free-India-Phone-Number/917428723247/',
               '918160651749':'https://receive-sms.cc/India-Phone-Number/918160651749'}
    if count.isnumeric():
        count = min(10,int(count))
    else:
        count = 5
    url = urlDict.get(number, -1)
    if url != -1:
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.content, 'html.parser')
            div = soup.findAll('div', {'class':'row border-bottom table-hover bg-messages'}, limit = count)
            content = list(map(lambda x:x.text.split('\n'), div))
            inbox = ['*' + el[1][el[1].find('From'):] + '*' + "\n" +
                    el[3] + "\n" for el in content]
            res = "\n\n".join(inbox)
        except:
            return "Sorry! Service currently Unavailable.😢"
        else:
            return "📥 *INBOX* 📥\n\n" + res + "\n\n⚠️ *If the message you are looking for is not shown, Please retry after few minutes.*"
    else:
        return "❌ This number is not available in our service.."

def psc_API():
    try:
        page_no = randint(1, 20)
        params = {'page':page_no, 'question':'GK'}
        url = "https://www.pscquestion.in/question.php"
        res = requests.get(url, params = params)
        soup = BeautifulSoup(res.content, "html.parser")
        ques =list(map(lambda x:x.replace("\t","").replace("\n","").replace("\u200b","").replace("\u200c","").replace("\u200d","")[x.find(".")+2:], [q.strong.text for q in soup.findAll("div", {"name":"searchitem"})]))
        ans = [a.p.text.replace("\u200b","").replace("\u200c","").replace("\u200d","") for a in soup.findAll("div",{"name":"searchitem"})]
        res = ""
        for i in range(len(ques)):
            res = res+"*"+str(i+1)+". "+ques[i]+"*\n"+ans[i]+"\n\n"
        return res
    except:
        return "Sorry! Service currently Unavailable.😢"

def complier_API(lang, code):
    try:
        data ={
            'python':{
                    'referer':'https://www.tutorialspoint.com/execute_python3_online.php',
                    'lang':'python3',
                    'ext':'py',
                    'compile':0,
                    'execute':'python3 main.py',
                    'mainfile':'main.py'
                    },
            'c':{
                    'referer':'https://www.tutorialspoint.com/compile_c_online.php',
                    'lang':'c',
                    'ext':'c',
                    'compile':'gcc -o main *.c',
                    'execute':'main',
                    'mainfile':'main.c'
                    },
            'cpp':{
                    'referer':'https://www.tutorialspoint.com/compile_cpp11_online.php',
                    'lang':'cpp11',
                    'ext':'cpp',
                    'compile':'g++ -std=c++11 -o main *.cpp',
                    'execute':'main',
                    'mainfile':'main.cpp'
                    }
            }

        lang = lang.lower()

        if data.get(lang, -1) != -1:
            headers = {
                'Origin': 'https://www.tutorialspoint.com',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': 'tpcg.tutorialspoint.com',
                'Referer': data[lang]['referer'],
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            }
            data = {
                'lang': data[lang]['lang'],
                'device': '',
                'code': code,
                'stdinput': '',
                'ext': data[lang]['ext'],
                'compile': data[lang]['compile'],
                'execute' : data[lang]['execute'],
                'mainfile': data[lang]['mainfile'],
                'uid': 2345678
            }
            response = requests.post('https://tpcg.tutorialspoint.com/tpcg.php', headers=headers, data=data)
            res = str(response.content)
            start = res.find('<pre>') + 5
            end = res.find('</pre>')
            res = res[start:end]
            return "✅ *Output*\n"+res.replace('\\n','\n').replace('"','')
        else:
            return "Sorry! I can't compile this Language.😕"
    except:
        return "Sorry! Service currently Unavailable.😢"

def ques_API(ques):
    print("yes")
    if ('whocreatedyou' in ques.replace(' ','').lower()) or ('whoisyourcreator' in ques.replace(' ','').lower()):
        return "*MOCHA*"
    elif 'whatisyourname' in ques.replace(' ','').lower():
        return "I'm *mochazbot*"
    else:
        try:
            query = ques.replace(' ', '+')
            #params = {
                #'access_key' : '39831b76d7e9036321e88567517613be',
                #'url' : "https://google.com/search?q=" + query
            #}
            #res = requests.get('http://api.scrapestack.com/scrape', params)

            url = "https://google.com/search?q=" + query
            res = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'})
            soup = BeautifulSoup(res.content, "html.parser")
            ans = soup.find('div', class_=['Z0LcW','Z0LcW AZCkJd'])
            if ans:
                return ans.text
            else:
                ans = soup.find('span', class_='e24Kjd')
                if ans:
                    return ans.text
                else:
                    srch_res = wikipedia.search(ques, results=1)
                    if srch_res:
                        ans = wikipedia.summary(srch_res[0], sentences = 3)
                        return ans
                    else:
                        return "Sorry! I don't know the Answer.😕"
        except:
            return "Sorry! Service currently Unavailable.😢"
