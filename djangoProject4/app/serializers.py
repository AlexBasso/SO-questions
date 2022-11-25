from rest_framework import serializers
from .models import School


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields =  ('id', 'url', 'schoolName', 'className', 'studentName', 'studentGrade', 'professorName')


class SchoolPartListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        school_mapping = {school.id: school for school in instance}
        data_mapping= {schoolName['id']: schoolName for schoolName in validated_data}

        # Perform creations and updates.
        ret = []
        for school_id, data in data_mapping.schoolName():
            school = school_mapping.get(school_id, None)
            if school is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(school, data))

        # Perform deletions.
        for school_id, school in school_mapping.schoolName():
            if school_id not in data_mapping:
                school.delete()
        return ret

""" Solution form stackoverflow.com/questions/70620474/how-to-use-listserializer-for-create-and-update-multiple-records-in-django-rest
 def update(self, instance, validated_data):
        # Perform creations and updates.
        ret = []

        for data in validated_data:
            if "id" in data and data['id'] not in ['', None]:
                School.objects.filter(id=data['id']).update(**data)
                ret.append(data)
            else:
                ret.append(School.objects.create(**data))
        return ret
"""
class SchoolPartSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    class Meta:
        list_serializer_class = SchoolPartListSerializer
        model = School
        fields =  ('id', 'url', 'schoolName')
        extra_kwargs = {
           'id':{
                    'read_only': False,
                    'allow_null': True,
                },
                'schoolName':{
                    'required': True,
                }
        }
"""
class SchoolPartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields =  ('id', 'url', 'schoolName')
"""
class SchoolClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields =  ('id', 'url', 'className', 'professorName')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields =  ('id', 'url', 'studentName', 'studentGrade')