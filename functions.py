from datacenter.models import Schoolkid
from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Lesson
from datacenter.models import Mark


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in bad_marks:
        mark.update(points=5)
    return bad_marks.count()


pupil_ivan = Schoolkid.objects.get(full_name__contains="Фролов Иван")
fix_marks(pupil_ivan)


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        chastisement.remove()

## TODO дописать функцию
def create_commendation(fullname, subject):
    text = 'gj'
    pupil_subject=Lesson.objects.filter()
    Commendation.objects.create(text="Хвалю", created=math_ivan.first().date,schoolkid=pupil_ivan,subject=math_ivan.first().subject, teacher=math_ivan.first().teacher) 
