from edital.models import EditalModel


class EditalService():
    
    def find_all_editais(self):
        return EditalModel.objects.all()