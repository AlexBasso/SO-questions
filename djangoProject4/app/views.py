from .serializers import SchoolSerializer, SchoolPartSerializer, SchoolClassSerializer, StudentSerializer
from .models import School
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


"""  SchoolAPI  """

class SchoolList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tmp_school_list.html'

    def get(self, request):
        print('printing SchoolClasslList request get:', request.data)
        queryset = School.objects.values('schoolName').distinct()
        print('start')
        sort = School.objects.values('schoolName').distinct()
        print('step 1')
        print('printing SchoolClasslList sort get:', sort.values)
        print('printing SchoolClasslList queryset get:', queryset.values)
        return Response({'schools': queryset, 'sort': sort})


class SchoolCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tmp_school_create.html'

    def get(self,request):
        serializer= SchoolSerializer
        return Response({'serializer':serializer})

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('tmp_school-list')


class SchoolDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tmp_school_detail.html'

    def get(self, request, name, *args, **kwargs):
        school = School.objects.filter(schoolName=name)
        #school = get_object_or_404(School.objects.only('id', 'schoolName'))
        print('printing SchoolDetail get:', school)
        serializer_context = {'request': request, }
        print('printing SchoolDetail serializer_context get:', serializer_context)
        serializer = SchoolPartSerializer(instance=school, many=True, context=serializer_context)
        return Response({'serializer': serializer, 'school': school})

    def post(self, request, name):
        print('printing SchoolDetail star post:')
        school = School.objects.filter(schoolName=name)
        #school = get_object_or_404(School.objects.only('id', 'schoolName'))
        print('printing SchoolDetail post:', school)
        serializer_context = {
            'request': request,
        }
        print('printing SchoolDetail serializer_context  post:', serializer_context)
        print('printing SchoolDetail request.data post:', request.data)
        serializer = SchoolPartSerializer(instance=school, many=True, data=request.data, context=serializer_context)

        if not serializer.is_valid():
            return Response({'serializer': serializer, 'school': school})
        serializer.save()
        print('printing SchoolDetail serializer after saving post:',serializer)
        return redirect('tmp_school-list')


class SchoolDelete(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tmp_school_delete.html'

    def get(self, request, name):
        school = School.objects.filter(schoolName = name)
        return Response({'school': school})

    def post(self, request, name):
        school = School.objects.filter(schoolName=name)
        school.delete()
        return redirect('tmp_school-list')


"""  ClassAPI  """

class SchoolClassList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_class_list.html'

    def get(self, request, name):
        print('printing SchoolClasslList self get:', self)
        print('printing SchoolClasslList request get:', request.data)
        print('printing SchoolClasslList name get:', name)
        queryset = School.objects.filter(schoolName = name)
        print('printing SchoolClasslList queryset get:', queryset.values())
        return Response({'schoolclasses': queryset})


class SchoolClassCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_class_create.html'


    def get(self,request, name):
        print('printing SchoolClassCreate name get', name)
        school = School.objects.filter(schoolName = name, className ='No Data')
        print('printing SchoolClassCreate school get', school.values())
        serializer_context = {
            'request': request,
        }
        serializer= SchoolSerializer(school, context=serializer_context)
        print('printing SchoolClassCreate serializer get', serializer)
        return Response({'serializer':serializer})

    def post(self, request, name):
        serializer = SchoolSerializer(data=request.data)
        print('printing SchoolClassCreate serializer post', serializer)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('school_class-list', name=name)


class SchoolClassDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_class_detail.html'

    def get(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = SchoolClassSerializer(school, context=serializer_context)
        return Response({'serializer': serializer, 'school': school})

    def post(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        serializer_context = {
            'request': request,
        }
        print('printing serializer_context saving:', serializer_context)
        serializer = SchoolClassSerializer(school, data=request.data, context=serializer_context)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'school': school})
        serializer.save()
        print('printing serializer after saving:',serializer)
        return redirect('school_class-list', name=school.schoolName)


class SchoolClassDelete(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_class_delete.html'

    def get(self, request, name, className):
        print('printing SchoolClassDelete self get:', self)
        print('printing SchoolClassDelete request get:', request.data)
        print('printing SchoolClassDelete name get:', name)
        print('printing SchoolClassDelete className get:', className)
        school = School.objects.filter(schoolName = name, className = className)
        print('printing SchoolClassDelete school get:', school.values())
        return Response({'school': school})

    def post(self, request, name, className):
        print('print DeleteSchool delete started')
        school = School.objects.filter(schoolName=name, className = className)
        print('print DeleteSchool school object delete:', school)

        school.delete()
        checkifschoolexists = School.objects.filter(schoolName=name)
        if checkifschoolexists:
            return redirect('school_class-list', name=name)
        else:
            return redirect('tmp_school-list')




"""  StudentAPI  """

class StudentList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'student_list.html'

    def get(self, request, name, className):
        print('printing SchoolClasslList self get:', self)
        print('printing SchoolClasslList request get:', request.data)
        print('printing SchoolClasslList name get:', name)
        queryset = School.objects.filter(schoolName = name, className = className)
        print('printing SchoolClasslList queryset get:', queryset.values())
        return Response({'students': queryset})

class StudentDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'student_detail.html'

    def get(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = StudentSerializer(school, context=serializer_context)
        return Response({'serializer': serializer, 'school': school})

    def post(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        serializer_context = {
            'request': request,
        }
        print('printing StudentDetail serializer_context saving post:', serializer_context)
        print('printing StudentDetail request.data saving post:', request.data)
        serializer = StudentSerializer(school, data=request.data, context=serializer_context)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'school': school})
        serializer.save()
        print('printing StudentDetail serializer after saving post:',serializer)
        return redirect('student-list', name=school.schoolName, className = school.className)


class StudentDelete(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'student_delete.html'

    def get(self, request, name, className, studentName):
        print('printing StudentDelete self get:', self)
        print('printing StudentDelete request get:', request.data)
        print('printing StudentDelete name get:', name)
        print('printing StudentDelete className get:', className)
        print('printing StudentDelete studentName get:', studentName)
        school = School.objects.filter(schoolName = name, className = className, studentName= studentName)
        print('printing StudentDelete school get:', school.values())
        return Response({'students': school})

    def post(self, request, name, className, studentName):
        print('print DeleteSchool delete started')
        school = School.objects.filter(schoolName=name, className = className, studentName = studentName)
        print('print DeleteSchool school object delete:', school)

        school.delete()
        checkifschoolexists = School.objects.filter(schoolName=name, className = className)
        if checkifschoolexists:
            return redirect('student-list', name=name, className = className)
        else:
            return redirect('tmp_school-list')
