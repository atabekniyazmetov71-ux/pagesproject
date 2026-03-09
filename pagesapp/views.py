from django.shortcuts import render
from django.views.generic import TemplateView

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

    def DT_sum(self, val=0):
        if val > 0:
            self.debit_total += val
        return self.debit_total

    def KT_sum(self, val=0):
        if val > 0:
            self.credit_total += val
        return self.credit_total

# TemplateView misollar
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class HelpPageView(TemplateView):
    template_name = 'help.html'

# Pravodka view
def pravodkaView(request):
    result = {"entries": [], "total_debit": 0, "total_credit": 0, "error": None}
    try:
        PR = Pravodka()

        # Hisoblar
        hasap1 = Hasaplar("Hasaplashyk hasaby", "62125500")
        hasap2 = Hasaplar("Haryt ugradyjylara begiler", "63185100")
        hasaplar = {hasap1.code: hasap1, hasap2.code: hasap2}

        # Session entries
        entries = request.session.get('entries', [])
        request.session['entries'] = entries

        if request.method == 'POST':
            debit_code = request.POST.get("debit_code")
            credit_code = request.POST.get("credit_code")

            # Safe float konvertatsiyasi
            try:
                debit_sum = float(request.POST.get("debit_sum", 0))
            except ValueError:
                debit_sum = 0

            try:
                credit_sum = float(request.POST.get("credit_sum", 0))
            except ValueError:
                credit_sum = 0

            # Safe lookup
            debit_hasap = hasaplar.get(debit_code, hasap2)
            credit_hasap = hasaplar.get(credit_code, hasap1)

            # Update PR
            PR.pravodka_DT(debit_hasap)
            PR.pravodka_KT(credit_hasap)
            PR.DT_sum(debit_sum)
            PR.KT_sum(credit_sum)

            # Update session
            entries.append({
                'dt': debit_code,
                'kt': credit_code,
                'debit': debit_sum,
                'credit': credit_sum
            })
            request.session['entries'] = entries

        # Session entries bilan natijani hisoblash
        PR = Pravodka()
        for e in entries:
            debit_hasap = hasaplar.get(e['dt'], hasap2)
            credit_hasap = hasaplar.get(e['kt'], hasap1)
            PR.pravodka_DT(debit_hasap)
            PR.pravodka_KT(credit_hasap)
            PR.DT_sum(e['debit'])
            PR.KT_sum(e['credit'])

        result.update({
            "entries": entries,
            "total_debit": PR.DT_sum(0),
            "total_credit": PR.KT_sum(0),
        })

    except Exception as e:
        # Xatolikni frontendga chiqarish
        result['error'] = str(e)

    return render(request, "pravodka.html", {"result": result})
