from edital.models import EditalModel


class EditalService():
    
    def find_all_editais(self):
        return EditalModel.objects.all()
    
    def find_by_id(self, id) -> EditalModel:
        return EditalModel.objects.filter(id = id).first()