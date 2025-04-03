from  django  import  forms
from  llm.models import  Gemini2, ChatGPT

class  GeminiForm(forms.ModelForm):
    class  Meta:
        model = Gemini2
        #fields = ['title','name','content']
        exclude = ['today']

class  ChatGPTForm(forms.ModelForm):
    class  Meta:
        model = ChatGPT
        #fields = ['title','name','content']
        exclude = ['today']


