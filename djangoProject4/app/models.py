from django.db import models


class School(models.Model):
    schoolName = models.CharField(max_length=200, default='No Data')
    className = models.CharField(max_length=200, default='No Data')
    studentName = models.CharField(max_length=200, default='No Data')
    studentGrade = models.IntegerField(null=True, blank=True)
    professorName = models.CharField(max_length=200, default='No Data')

    def __str__(self):
        return self.schoolName


    class Meta:
        unique_together = [['schoolName', 'className', 'studentName']]



""" For reference:
class Professor(models.Model):
    professorName = models.CharField(max_length=200)

    def __str__(self):
        return self.professorName


class Grade(models.Model):
    gradeNumber = models.CharField(max_length=200)

    def __str__(self):
        return self.gradeNumber


class Student(models.Model):
    studentName = models.CharField(max_length=200)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.studentName


class ScClass(models.Model):
    scClassName = models.CharField(max_length=200, unique=True)
    student = models.ManyToManyField(Student)
    professor = models.ManyToManyField(Professor)

    def __str__(self):
        return self.scClassName


class School(models.Model):
    schoolName = models.CharField(max_length=200, unique=True)
    scClass = models.ManyToManyField(ScClass)
    #professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    #student = models.ManyToManyField(Student)
    #grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.schoolName


class SchoolRegestry(models.Model):
    scClass = models.ManyToManyField(ScClass)
    #professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    #student = models.ManyToManyField(Student)
    #grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

"""