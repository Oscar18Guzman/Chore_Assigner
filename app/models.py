from django.db import models
from django.utils import timezone
from datetime import timedelta
from random import shuffle

# Create your models here.
class Student(models.Model):
    name = models.TextField()
    class_year = models.IntegerField()
    chore_one_pref = models.TextField(choices=[
        ['Chore Captain', 'Chore Captain'],
        ['Pre-lunch Bathroom Inspection', 'Pre-lunch Bathroom Inspection'],
        ['Lunch Set-up', 'Lunch Set-up'],
        ['Lunch Clean-up', 'Lunch Clean-up'],
        ['Bathroom Cleaner 1', 'Bathroom Cleaner 1'],
        ['Bathroom Cleaner 2', 'Bathroom Cleaner 2'],
        ['Classroom Clean and Inspection', 'Classroom Clean and Inspection'],
        ['End of Day Classroom Clean and Inspection', 'End of Day Classroom Clean and Inspection'],
        ['Hallway Sweep', 'Hallway Sweep'],
        ['Classroom Sweeper 1','Classroom Sweeper 1'],
        ['Classroom Sweeper 2','Classroom Sweeper 2'],
        ['End of Day Bathroom Clean and Inspection', 'End of Day Bathroom Clean and Inspection']

    ])
    chore_two_pref = models.TextField(choices=[
        ['Chore Captain', 'Chore Captain'],
        ['Pre-lunch Bathroom Inspection', 'Pre-lunch Bathroom Inspection'],
        ['Lunch Set-up', 'Lunch Set-up'],
        ['Lunch Clean-up', 'Lunch Clean-up'],
        ['Bathroom Cleaner 1', 'Bathroom Cleaner 1'],
        ['Bathroom Cleaner 2', 'Bathroom Cleaner 2'],
        ['Classroom Clean and Inspection', 'Classroom Clean and Inspection'],
        ['End of Day Classroom Clean and Inspection', 'End of Day Classroom Clean and Inspection'],
        ['Hallway Sweep', 'Hallway Sweep'],
        ['Classroom Sweeper 1','Classroom Sweeper 1'],
        ['Classroom Sweeper 2','Classroom Sweeper 2'],
        ['End of Day Bathroom Clean and Inspection', 'End of Day Bathroom Clean and Inspection']

    ])
    chore_three_pref = models.TextField(choices=[
        ['Chore Captain', 'Chore Captain'],
        ['Pre-lunch Bathroom Inspection', 'Pre-lunch Bathroom Inspection'],
        ['Lunch Set-up', 'Lunch Set-up'],
        ['Lunch Clean-up', 'Lunch Clean-up'],
        ['Bathroom Cleaner 1', 'Bathroom Cleaner 1'],
        ['Bathroom Cleaner 2', 'Bathroom Cleaner 2'],
        ['Classroom Clean and Inspection', 'Classroom Clean and Inspection'],
        ['End of Day Classroom Clean and Inspection', 'End of Day Classroom Clean and Inspection'],
        ['Hallway Sweep', 'Hallway Sweep'],
        ['Classroom Sweeper 1','Classroom Sweeper 1'],
        ['Classroom Sweeper 2','Classroom Sweeper 2'],
        ['End of Day Bathroom Clean and Inspection', 'End of Day Bathroom Clean and Inspection']

    ])

class Chore(models.Model):
    name = models.TextField()
    description = models.TextField()
    time = models.TextField(choices=[
        ['morning', 'morning'],
        ['afternoon', 'afternoon']
    ])
    complete = models.BooleanField(default=False)
    

class ChoreAssignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    chore = models.ForeignKey(Chore, on_delete=models.PROTECT)
    date = models.DateField()
    completed = models.BooleanField(default=False)

    @staticmethod
    def for_this_week():
        today = timezone.now()
        todays_day_of_week = today.weekday()
        distance_from_monday = todays_day_of_week
        distance_from_friday = 4 - todays_day_of_week
        this_monday = today - timedelta(days=distance_from_monday)
        this_friday = today + timedelta(days=distance_from_friday)
        assignments = ChoreAssignment.objects.filter(date__gte=this_monday, date__lte=this_friday)
        
        result = {}

        if not assignments.exists():
            chores = Chore.objects.all()
            students = list(Student.objects.all())
            for day_offset, day in enumerate(['monday','tuesday', 'wednesday', 'thursday', 'friday']):
                day = this_monday + timedelta(days=day_offset)
                result[day] = []
                shuffle(students)
                for student, chore in zip(students, chores):
                    result[day].append(ChoreAssignment.objects.create(
                        student=student,
                        chore=chore,
                        date=day
                    ))
        else:
            result['monday'] = [a for a in assignments if a.date.weekday() == 0]
            result['tuesday'] = [a for a in assignments if a.date.weekday() == 1]
            result['wednesday'] = [a for a in assignments if a.date.weekday() == 2]
            result['thursday'] = [a for a in assignments if a.date.weekday() == 3]
            result['friday'] = [a for a in assignments if a.date.weekday() == 4]
        return result 