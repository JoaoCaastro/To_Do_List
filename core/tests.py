from django.test import TestCase
from .models import TasksModel
from .forms import TasksModelForm

class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_index(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_texto(self):
        self.assertContains(self.resp, 'tarefa')

class createTest(TestCase):
     def setUp(self):
        self.resp = self.client.get('/create')
    
     def test_301_response(self):
        self.assertEqual(301, self.resp.status_code)
    
class tarefaModelTest(TestCase):
    def setUp(self):   
        self.create = TasksModel(
            tarefa = 'Prova',
            descricao = 'Prova do Orlando DES WEB III',
            data = '2023-05-03'
        )
        self.create.save()
    
    def test_created(self):
        self.assertTrue(TasksModel.objects.exists())

    def test_created_only_one(self):        
         self.assertTrue( len(TasksModel.objects.all()) == 1)

class tarefaFormTest(TestCase):
    def test_form_has_fields(self):
        form = TasksModelForm()
        expected = ['tarefa','descricao','data']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_validated_form(self, **kwargs):
        valid = dict(
            tarefa='Test',
            descricao='Assert-Test',
            data='2023-05-16'
        )

        data = dict(valid, **kwargs)
        form = TasksModelForm(data)
        form.is_valid()
        return form