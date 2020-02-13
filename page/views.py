from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from leave.models import LeaveEmployee, EmployeeInstance, LeaveHoliday
from django.conf import settings


@login_required(login_url='/accounts/login/')
def index(request):
    approved_leave_request_count = EmployeeInstance.objects.filter(emp_id=request.user.username, status='a').count()
    rejected_leave_request_count = EmployeeInstance.objects.filter(emp_id=request.user.username, status='r').count()
    pending_leave_request_count = EmployeeInstance.objects.filter(emp_id=request.user.username, status='p').count()
    cancel_leave_request_count = EmployeeInstance.objects.filter(emp_id=request.user.username, status='c').count()   

    if request.user.has_perm('leave.approve_leaveplan'):
        team_leave_request_count = EmployeeInstance.TeamLeaveRequestCount(request)
    else:
        team_leave_request_count = 0

    return render(request, 'index.html', {'pending_leave_request_count':pending_leave_request_count, 'approved_leave_request_count':approved_leave_request_count, 'rejected_leave_request_count':rejected_leave_request_count, 'team_leave_request_count':team_leave_request_count})

@login_required(login_url='/accounts/login/')
def PhoneList(request):
    return render(request, 'page/phone_list.html', {})


@login_required(login_url='/accounts/login/')
def PublicHoliday(request):
    public_holiday_instance = LeaveHoliday.PublicHolidayInstance
    return render(request, 'page/public_holiday.html', {'public_holiday_instance': public_holiday_instance})


@login_required(login_url='/accounts/login/')
def StaffProfile(request):
    EmployeeInstance = LeaveEmployee.EmployeeInstance(request)
    SuperVisorInstance = LeaveEmployee.SuperVisorInstance(request)
    TeamMemberList = LeaveEmployee.TeamMemberList(request)

    return render(request, 'page/staff_profile.html', {
        'EmployeeInstance': EmployeeInstance,
        'SuperVisorInstance': SuperVisorInstance,
        'TeamMemberList': TeamMemberList,
        })

@login_required(login_url='/accounts/login/')
def StaffTrophy(request):
    project_name = settings.PROJECT_NAME
    return render(request, 'page/staff_trophy.html', {'project_name': project_name})
