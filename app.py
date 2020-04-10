from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import json
from utils import fetch_reply

url="https://covid-193.p.rapidapi.com/statistics"
querystring = {"country":"Morocco"}
headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "" #add key here
    }
response = requests.request("GET", url, headers=headers, params=querystring)
y = json.loads(response.text)
today = y['response'][0]

faq = "Q : Faut-il éviter de se serrer la main à cause du nouveau coronavirus ?\nR : Oui. On peut contracter les virus respiratoires en serrant la main à quelqu’un puis en se touchant les yeux, le nez ou la bouche. Saluez d’un signe de la main ou de la tête, ou encore en vous inclinant.\nQ : Comment saluer une personne pour éviter d’attraper le nouveau coronavirus ?\nR : Le moyen le plus sûr de se saluer pour prévenir la COVID-19 est d’éviter les contacts physiques. On peut saluer d’un signe de la main ou de la tête, ou encore en s’inclinant.\nQ : Le port de gants en caoutchouc dans les lieux publics permet-il d’éviter l’infection par le nouveau coronavirus ?\nR : Non. Le fait de se laver les mains régulièrement protège mieux contre la COVID-19 que le port de gants en caoutchouc. Le virus peut se trouver sur les gants et il y a un risque de contamination si vous vous touchez le visage avec les gants.\n*Source: Organisation Mondiale de la Santé*"

rec = "*Se laver les mains* avec une solution hydroalcoolique ou à l’eau et au savon tue le virus s’il est présent sur vos mains.\n*Maintenir une distance* d’au moins 1 mètre avec les autres personnes, en particulier si elles toussent, éternuent ou ont de la fièvre.\n*Éviter de se toucher les yeux, le nez et la bouche.* Les mains sont en contact avec de nombreuses surfaces qui peuvent être contaminées par le virus.\n*Respecter les règles d’hygiène respiratoire.* Se couvrir la bouche et le nez avec le pli du coude ou avec un mouchoir en cas de toux ou d’éternuement – jeter le mouchoir immédiatement après dans une poubelle fermée et se laver les mains avec une solution hydroalcoolique ou à l’eau et au savon.\n*Tenez-vous informé* et suivez les conseils de votre médecin, des autorités de santé nationales et locales ou de votre employeur pour savoir comment vous protéger et protéger les autres de la COVID-19.\n*Source: Organisation Mondiale de la Santé*"

symp = "Les symptômes les plus courants de la COVID-19 sont la fièvre, la fatigue et une toux sèche. Certains patients présentent des douleurs, une congestion nasale, un écoulement nasal, des maux de gorge ou une diarrhée. Ces symptômes sont généralement bénins et apparaissent de manière progressive. Certaines personnes, bien qu’infectées, ne présentent aucun symptôme et se sentent bien. La plupart (environ 80 pour cent) des personnes guérissent sans avoir besoin de traitement particulier. Environ une personne sur six contractant la maladie présente des symptômes plus graves, notamment une dyspnée. Les personnes âgées et celles qui ont d’autres problèmes de santé (hypertension artérielle, problèmes cardiaques ou diabète) ont plus de risques de présenter des symptômes graves. Toute personne qui a de la fièvre, qui tousse et qui a des difficultés à respirer doit consulter un médecin.\n*Source: Organisation Mondiale de la Santé*"

faq_a = "*ما هو مرض كوفيد-19؟*\n مرض كوفيد-19 هو مرض معد يسببه فيروس كورونا المُكتشف مؤخراً\n*ما هي أعراض مرض كوفيد-19؟*\nتتمثل الأعراض الأكثر شيوعاً لمرض كوفيد-19 في الحمى والإرهاق والسعال الجاف. وقد يعاني بعض المرضى من الآلام والأوجاع، أو احتقان الأنف، أو الرشح، أو ألم الحلق، أو الإسهال وعادة ما تكون هذه الأعراض خفيفة وتبدأ تدريجياً. ويصاب بعض الناس بالعدوى دون أن تظهر عليهم أي أعراض ودون أن يشعروا بالمرض. ويتعافى معظم الأشخاص (نحو 80 في المائة) من المرض دون الحاجة إلى علاج خاص. وتشتد حدة المرض لدى شخص واحد تقريباً من كل 6 أشخاص يصابون بعدوى كوفيد-19 حيث يعانون من صعوبة التنفس. وتزداد احتمالات إصابة المسنين والأشخاص المصابين بمشكلات طبية أساسية مثل ارتفاع ضغط الدم أو أمراض القلب أو داء السكري، بأمراض وخيمة. وقد توفى نحو 2 في المائة من الأشخاص الذين أُصيبوا بالمرض. وينبغي للأشخاص الذين يعانون من الحمى والسعال وصعوبة التنفس التماس الرعاية الطبية\n*المصدر : منظمة الصحة العالمية*"

faq_a2 = "*كيف ينتشر مرض كوفيد-19؟*\nيمكن أن يصاب الأشخاص بعدوى مرض كوفيد-19 عن طريق الأشخاص الآخرين المصابين بالفيروس. ويمكن للمرض أن ينتقل من شخص إلى شخص عن طريق القُطيرات الصغيرة التي تتناثر من الأنف أو الفم عندما يسعل الشخص المصاب بمرض كوفيد-19 أو يعطس. وتتساقط هذه القُطيرات على الأشياء والأسطح المحيطة بالشخص. ويمكن حينها أن يصاب الأشخاص الآخرون بمرض كوفيد-19 عند ملامستهم لهذه الأشياء أو الأسطح ثم لمس عينيهم أو أنفهم أو فمهم. كما يمكن أن يصاب الأشخاص بمرض كوفيد-19 إذا تنفسوا القُطيرات التي تخرج من الشخص المصاب بالمرض مع سعاله أو زفيره. ولذا فمن الأهمية بمكان الابتعاد عن الشخص المريض بمسافة تزيد على متر واحد (3 أقدام)\n*هل يمكن للفيروس المسبب لمرض كوفيد-19 أن ينتقل عبر الهواء؟*\nتشير الدراسات التي أُجريت حتى يومنا هذا إلى أن الفيروس الذي يسبب مرض كوفيد-19 ينتقل في المقام الأول عن طريق ملامسة القُطيرات التنفسية لا عن طريق الهواء\n*المصدر : منظمة الصحة العالمية*"

rec_a = "- نظف يديك جيداً بانتظام بفركهما مطهر كحولي لليدين أو بغسلهما بالماء والصابون لأن ذلك  من شأنه أن يقتل الفيروسات التي قد تكون على يديك\n- احتفظ بمسافة لا تقل عن متر واحد (3 أقدام) بينك وبين أي شخص يسعل أو يعطس، ذلك أنه عندما يسعل الشخص أو يعطس، تتناثر من أنفه أو فمه قُطيرات سائلة صغيرة قد تحتوي على الفيروس. فإذا كنت شديد الاقتراب منه يمكن أن تتنفس هذه القُطيرات، بما في ذلك الفيروس المسبب لمرض كوفيد-19 إذا كان الشخص مصاباً به\n- تأكد من اتّباعك أنت والمحيطين بك لممارسات النظافة التنفسية الجيدة. ويعني ذلك أن تغطي فمك وأنفك بكوعك المثني أو بمنديل ورقي عند السعال أو العطس، ثم التخلص من المنديل المستعمل على الفور\n- إلزم المنزل إذا شعرت بالمرض. إذا كنت مصاباً بالحمى والسعال وصعوبة التنفس، التمس الرعاية الطبية واتصل بمقدم الرعاية قبل التوجه إليه. واتّبع توجيهات السلطات الصحية المحلية\n- اطلع باستمرار على آخر تطورات مرض كوفيد-19. واتّبع المشورة التي يسديها مقدم الرعاية الصحية أو سلطات الصحة العمومية الوطنية والمحلية\n*المصدر : منظمة الصحة العالمية*"

symp = "Les symptômes les plus courants de la COVID-19 sont la fièvre, la fatigue et une toux sèche. Certains patients présentent des douleurs, une congestion nasale, un écoulement nasal, des maux de gorge ou une diarrhée. Ces symptômes sont généralement bénins et apparaissent de manière progressive. Certaines personnes, bien qu’infectées, ne présentent aucun symptôme et se sentent bien. La plupart (environ 80 pour cent) des personnes guérissent sans avoir besoin de traitement particulier. Environ une personne sur six contractant la maladie présente des symptômes plus graves, notamment une dyspnée. Les personnes âgées et celles qui ont d’autres problèmes de santé (hypertension artérielle, problèmes cardiaques ou diabète) ont plus de risques de présenter des symptômes graves. Toute personne qui a de la fièvre, qui tousse et qui a des difficultés à respirer doit consulter un médecin.\n*Source: Organisation Mondiale de la Santé*"

symp_a = "تتمثل الأعراض الأكثر شيوعاً لمرض كوفيد-19 في الحمى والإرهاق والسعال الجاف. وقد يعاني بعض المرضى من الآلام والأوجاع، أو احتقان الأنف، أو الرشح، أو ألم الحلق، أو الإسهال. وعادة ما تكون هذه الأعراض خفيفة وتبدأ تدريجياً. ويصاب بعض الناس بالعدوى دون أن تظهر عليهم أي أعراض ودون أن يشعروا بالمرض. ويتعافى معظم الأشخاص (نحو 80 في المائة) من المرض دون الحاجة إلى علاج خاص. وتشتد حدة المرض لدى شخص واحد تقريباً من كل 6 أشخاص يصابون بعدوى كوفيد-19 حيث يعانون من صعوبة التنفس. وتزداد احتمالات إصابة المسنين والأشخاص المصابين بمشكلات طبية أساسية مثل ارتفاع ضغط الدم أو أمراض القلب أو داء السكري، بأمراض وخيمة. وقد توفى نحو 2 في المائة من الأشخاص الذين أُصيبوا بالمرض. وينبغي للأشخاص الذين يعانون من الحمى والسعال وصعوبة التنفس التماس الرعاية الطبية.\n*المصدر : منظمة الصحة العالمية*"

contact = "Veille épidémiologique:\n080 100 47 47 \nAssistance médicale d'urgence *Allô SAMU* :\n141\nPortail Officiel du Coronavirus au Maroc:\nwww.covidmaroc.ma \nOrganisation Mondiale de la Santé:\nwww.who.int/fr"

contact_a = "الرقم الاقتصادي *ألو اليقظة الوبائية*:\n080 100 47 47 \nالمساعدة الطبية الاستعجالية:\n141 \nالبوابة الرسمية لفيروس كورونا بالمغرب:\nwww.covidmaroc.ma \nمنظمة الصحة العالمية:\nwww.who.int/ar"

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    reply = fetch_reply(msg, phone_no)

    # Create reply
    resp = MessagingResponse()
    #resp.message(reply)
    if (format(msg) in ['Hi', 'hi', 'Hello', 'hello', 'Bonjour', 'bonjour', 'Salut', 'salut']):
        resp.message("Salut! Je suis ravi de vous fournir des informations concernant COVID19:\n Merci de choisir votre langue:\nArabe : 0\nFrançais : 1")
        resp.message("مرحبًا! يسعدني أن أقدم لك معلومات بخصوص مرض كوفيد 19. الرجاء اختيار لغتك: \nالعربية : 0\nالفرنسية : 1")
    elif (format(msg) == '0'):
        resp.message("الرجاء اختيار الرقم المناسب: \n2: أحدث الإحصائيات \n3: التوصيات \n4: الأسئلة الشائعة\n5: أعراض المرض\n6: مراكز الإتصال")
    elif (format(msg) == '1'):
        resp.message("Merci de choisir le numero adéquat :\na : Dernières stats\nb: Recommandations\nc : FAQ\nd : Symptômes\ne : Numéros et liens utils")
    elif (format(msg) in ['a', 'A']):
        resp.message("Stats du Maroc le : {}\nNombre de cas : {}\nMorts : {}\nGueris : {}\navec une différence de {} cas et {} décès par rapport à hier".format(today.get('day'), today.get('cases').get('total'), today.get('deaths').get('total'), today.get('cases').get('recovered'), today.get('cases').get('new'),today.get('deaths').get('new')))
    elif (format(msg) in ['b', 'B']):
        resp.message(format(rec))
    elif (format(msg) in ['c', 'C']):
        resp.message(format(faq))
    elif (format(msg) in ['d', 'D']):
        resp.message(format(symp))
    elif (format(msg) in ['e', 'E']):
        resp.message(format(contact))
    elif (format(msg) == '2'):
        resp.message("إحصائيات المغرب يوم {} حول فيروس كورونا\nعدد الحالات المؤكدة {}\nعدد الوفيات {} \nالمتعافون {}\nمقارنة بيوم أمس، سجل المغرب {} حالة مؤكدة و {} وفاة".format(today.get('day'), today.get('cases').get('total'), today.get('deaths').get('total'), today.get('cases').get('recovered'), today.get('cases').get('new'),today.get('deaths').get('new')))
    elif (format(msg) == '3'):
        resp.message(format(rec_a))
    elif (format(msg) == '4'):
        resp.message(format(faq_a))
        resp.message(format(faq_a2))
    elif (format(msg) == '5'):
        resp.message(format(symp_a))
    elif (format(msg) == '6'):
        resp.message(format(contact_a))
    elif (format(msg) in ['bye', 'Bye']):
        resp.message("Bye & *#StayHome*")
    else:
        resp.message("Merci de choisir le numero adéquat :\na : Dernières stats\nb: Recommandations\nc : FAQ\nd : Symptômes\ne : Numéros et liens utils")
        resp.message("الرجاء اختيار الرقم المناسب: \n2: أحدث الإحصائيات \n3: التوصيات \n4: الأسئلة الشائعة\n5: أعراض المرض\n6: مراكز الإتصال")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
