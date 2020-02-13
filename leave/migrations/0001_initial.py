# Generated by Django 2.2 on 2020-02-12 00:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveEmployee',
            fields=[
                ('emp_id', models.DecimalField(db_column='emp_id', decimal_places=0, max_digits=7, primary_key=True, serialize=False)),
                ('emp_fname_en', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_lname_en', models.CharField(blank=True, max_length=40, null=True)),
                ('emp_fname_th', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_lname_th', models.CharField(blank=True, max_length=40, null=True)),
                ('pos_th', models.CharField(blank=True, max_length=50, null=True)),
                ('pos_en', models.CharField(blank=True, max_length=50, null=True)),
                ('div_th', models.CharField(blank=True, max_length=50, null=True)),
                ('div_en', models.CharField(blank=True, max_length=50, null=True)),
                ('emp_type', models.CharField(blank=True, max_length=2, null=True)),
                ('emp_join_date', models.DateTimeField(blank=True, null=True)),
                ('emp_term_date', models.DateTimeField(blank=True, null=True)),
                ('upd_date', models.DateTimeField()),
                ('upd_by', models.CharField(max_length=6)),
                ('emp_passcode', models.CharField(blank=True, db_column='Emp_passcode', max_length=4, null=True)),
                ('emp_spid', models.CharField(blank=True, db_column='emp_SpID', max_length=10, null=True)),
                ('password', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'Leave_employee',
                'permissions': (('approve_leaveplan', 'Can approve leave employee'),),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LeaveHoliday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hol_date', models.DateTimeField()),
                ('pub_id', models.SmallIntegerField(blank=True, null=True)),
                ('pub_th', models.CharField(blank=True, db_column='PUB_TH', max_length=50, null=True)),
                ('pub_en', models.CharField(blank=True, db_column='PUB_EN', max_length=50, null=True)),
                ('upd_date', models.DateTimeField()),
                ('upd_by', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'LEAVE_HOLIDAY',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LeavePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lve_year', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('emp_id', models.DecimalField(blank=True, decimal_places=0, max_digits=7, null=True)),
                ('lve_code', models.CharField(blank=True, max_length=3, null=True)),
                ('lve_plan', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('lve_plan_hr', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('lve_act', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('lve_act_hr', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('lve_miss', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('lve_miss_hr', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('upd_date', models.DateTimeField()),
                ('upd_by', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'Leave_Plan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('lve_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('lve_th', models.CharField(blank=True, max_length=50, null=True)),
                ('lve_en', models.CharField(blank=True, max_length=50, null=True)),
                ('lve_code', models.CharField(blank=True, max_length=3, null=True)),
                ('pay_type', models.CharField(blank=True, max_length=3, null=True)),
                ('upd_date', models.DateTimeField(blank=True, null=True)),
                ('upd_by', models.CharField(blank=True, max_length=10, null=True)),
                ('upd_flag', models.CharField(blank=True, max_length=1, null=True)),
                ('lve_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'LEAVE_TYPE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.DecimalField(decimal_places=0, max_digits=7, null=True)),
                ('lve_act', models.IntegerField(blank=True, null=True)),
                ('lve_act_hr', models.IntegerField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('updated_by', models.DecimalField(blank=True, decimal_places=0, max_digits=7, null=True)),
                ('status', models.CharField(blank=True, choices=[('a', 'Approved'), ('p', 'Pending'), ('r', 'Rejected'), ('c', 'Cancel')], default='p', help_text='Leave Request Status', max_length=1)),
                ('emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leave.LeaveEmployee')),
                ('leave_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leave.LeaveType')),
            ],
            options={
                'ordering': ['-created_date', '-start_date'],
            },
        ),
    ]
