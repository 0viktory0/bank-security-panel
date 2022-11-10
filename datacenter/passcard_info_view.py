from datacenter.models import Passcard, Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render, get_object_or_404, get_list_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = get_list_or_404(Visit, passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(visit, minutes=60)
            },
        )

        context = {
            'passcard': passcard,
            'this_passcard_visits': this_passcard_visits
        }
    return render(request, 'passcard_info.html', context)
