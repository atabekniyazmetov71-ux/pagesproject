from django.shortcuts import render
from django.views.generic import TemplateView
from services.pravodka import Hasaplar, Pravodka


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class HelpPageView(TemplateView):
    template_name = 'help.html'
    





# Minimal Hasaplar va Pravodka klasslari
class Hasaplar:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Pravodka:
    def __init__(self):
        self.dt = []
        self.kt = []
        self.debit_total = 0
        self.credit_total = 0

    def pravodka_DT(self, hasap):
        self.dt.append(hasap)

    def pravodka_KT(self, hasap):
        self.kt.append(hasap)

    def DT_sum(self, val):
        if val > 0:
            self.debit_total += val
        return self.debit_total

    def KT_sum(self, val):
        if val > 0:
            self.credit_total += val
        return self.credit_total

# View
def pravodkaView(request):
    PR = Pravodka()
    result = None

    # Hisoblar
    hasap1 = Hasaplar("Hasaplashyk hasaby", "62125500")
    hasap2 = Hasaplar("Haryt ugradyjylara begiler", "63185100")
    hasaplar = {hasap1.code: hasap1, hasap2.code: hasap2}

    if 'entries' not in request.session:
        request.session['entries'] = []

    if request.method == 'POST':
        debit_code = request.POST.get("debit_code")
        credit_code = request.POST.get("credit_code")
        debit_sum = float(request.POST.get("debit_sum"))
        credit_sum = float(request.POST.get("credit_sum"))

        PR.pravodka_DT(hasaplar.get(debit_code, hasap2))
        PR.pravodka_KT(hasaplar.get(credit_code, hasap1))
        PR.DT_sum(debit_sum)
        PR.KT_sum(credit_sum)

        entries = request.session['entries']
        entries.append({
            'dt': debit_code,
            'kt': credit_code,
            'debit': debit_sum,
            'credit': credit_sum
        })
        request.session['entries'] = entries

    # Natijani hisoblash
    entries = request.session.get('entries', [])
    PR = Pravodka()
    for e in entries:
        PR.pravodka_DT(hasaplar.get(e['dt'], hasap2))
        PR.pravodka_KT(hasaplar.get(e['kt'], hasap1))
        PR.DT_sum(e['debit'])
        PR.KT_sum(e['credit'])

    result = {
        "entries": entries,
        "total_debit": PR.DT_sum(0),
        "total_credit": PR.KT_sum(0)
    }

    return render(request, "pravodka.html", {"result": result})