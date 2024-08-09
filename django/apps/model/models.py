# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Athletes(models.Model):
  code = models.BigIntegerField(blank=True, null=True)
  name = models.TextField(blank=True, null=True)
  name_short = models.TextField(blank=True, null=True)
  name_tv = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  function = models.TextField(blank=True, null=True)
  country_code = models.TextField(blank=True, null=True)
  country = models.TextField(blank=True, null=True)
  country_full = models.TextField(blank=True, null=True)
  nationality = models.TextField(blank=True, null=True)
  nationality_full = models.TextField(blank=True, null=True)
  nationality_code = models.TextField(blank=True, null=True)
  height = models.BigIntegerField(blank=True, null=True)
  weight = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  disciplines = models.TextField(blank=True, null=True)
  events = models.TextField(blank=True, null=True)
  birth_date = models.DateField(blank=True, null=True)
  birth_place = models.TextField(blank=True, null=True)
  birth_country = models.TextField(blank=True, null=True)
  residence_place = models.TextField(blank=True, null=True)
  residence_country = models.TextField(blank=True, null=True)
  nickname = models.TextField(blank=True, null=True)
  hobbies = models.TextField(blank=True, null=True)
  occupation = models.TextField(blank=True, null=True)
  education = models.TextField(blank=True, null=True)
  family = models.TextField(blank=True, null=True)
  lang = models.TextField(blank=True, null=True)
  coach = models.TextField(blank=True, null=True)
  reason = models.TextField(blank=True, null=True)
  hero = models.TextField(blank=True, null=True)
  influence = models.TextField(blank=True, null=True)
  philosophy = models.TextField(blank=True, null=True)
  sporting_relatives = models.TextField(blank=True, null=True)
  ritual = models.TextField(blank=True, null=True)
  other_sports = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'athletes'


class AuthGroup(models.Model):
  name = models.CharField(unique=True, max_length=150)

  class Meta:
    managed = False
    db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
  id = models.BigAutoField(primary_key=True)
  group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
  permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

  class Meta:
    managed = False
    db_table = 'auth_group_permissions'
    unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
  name = models.CharField(max_length=255)
  content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
  codename = models.CharField(max_length=100)

  class Meta:
    managed = False
    db_table = 'auth_permission'
    unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
  password = models.CharField(max_length=128)
  last_login = models.DateTimeField(blank=True, null=True)
  is_superuser = models.BooleanField()
  username = models.CharField(unique=True, max_length=150)
  first_name = models.CharField(max_length=150)
  last_name = models.CharField(max_length=150)
  email = models.CharField(max_length=254)
  is_staff = models.BooleanField()
  is_active = models.BooleanField()
  date_joined = models.DateTimeField()

  class Meta:
    managed = False
    db_table = 'auth_user'


class AuthUserGroups(models.Model):
  id = models.BigAutoField(primary_key=True)
  user = models.ForeignKey(AuthUser, models.DO_NOTHING)
  group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

  class Meta:
    managed = False
    db_table = 'auth_user_groups'
    unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
  id = models.BigAutoField(primary_key=True)
  user = models.ForeignKey(AuthUser, models.DO_NOTHING)
  permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

  class Meta:
    managed = False
    db_table = 'auth_user_user_permissions'
    unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
  action_time = models.DateTimeField()
  object_id = models.TextField(blank=True, null=True)
  object_repr = models.CharField(max_length=200)
  action_flag = models.SmallIntegerField()
  change_message = models.TextField()
  content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
  user = models.ForeignKey(AuthUser, models.DO_NOTHING)

  class Meta:
    managed = False
    db_table = 'django_admin_log'


class DjangoContentType(models.Model):
  app_label = models.CharField(max_length=100)
  model = models.CharField(max_length=100)

  class Meta:
    managed = False
    db_table = 'django_content_type'
    unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
  id = models.BigAutoField(primary_key=True)
  app = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  applied = models.DateTimeField()

  class Meta:
    managed = False
    db_table = 'django_migrations'


class DjangoSession(models.Model):
  session_key = models.CharField(primary_key=True, max_length=40)
  session_data = models.TextField()
  expire_date = models.DateTimeField()

  class Meta:
    managed = False
    db_table = 'django_session'


class Events(models.Model):
  event = models.TextField(blank=True, null=True)
  tag = models.TextField(blank=True, null=True)
  sport = models.TextField(blank=True, null=True)
  sport_code = models.TextField(blank=True, null=True)
  sport_url = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'events'


class Medallists(models.Model):
  medal_date = models.DateField(blank=True, null=True)
  medal_type = models.TextField(blank=True, null=True)
  medal_code = models.BigIntegerField(blank=True, null=True)
  name = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  country = models.TextField(blank=True, null=True)
  country_code = models.TextField(blank=True, null=True)
  nationality = models.TextField(blank=True, null=True)
  team = models.TextField(blank=True, null=True)
  team_gender = models.TextField(blank=True, null=True)
  discipline = models.TextField(blank=True, null=True)
  event = models.TextField(blank=True, null=True)
  event_type = models.TextField(blank=True, null=True)
  url_event = models.TextField(blank=True, null=True)
  birth_date = models.DateField(blank=True, null=True)
  code = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'medallists'


class Medals(models.Model):
  medal_type = models.TextField(blank=True, null=True)
  medal_code = models.BigIntegerField(blank=True, null=True)
  medal_date = models.DateField(blank=True, null=True)
  name = models.TextField(blank=True, null=True)
  country_code = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline = models.TextField(blank=True, null=True)
  event = models.TextField(blank=True, null=True)
  event_type = models.TextField(blank=True, null=True)
  url_event = models.TextField(blank=True, null=True)
  code = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'medals'


class MedalsTotal(models.Model):
  country_code = models.TextField(blank=True, null=True)
  gold_medal = models.BigIntegerField(blank=True, null=True)
  silver_medal = models.BigIntegerField(blank=True, null=True)
  bronze_medal = models.BigIntegerField(blank=True, null=True)
  total = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'medals_total'


class Results3X3Basketball(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_3x3basketball'


class ResultsArchery(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_archery'


class ResultsArtisticGymnastics(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_artistic_gymnastics'


class ResultsArtisticSwimming(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=4, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=4, blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_artistic_swimming'


class ResultsAthletics(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  bib = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_athletics'


class ResultsBadminton(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_badminton'


class ResultsBasketball(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_basketball'


class ResultsBeachVolleyball(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_beach_volleyball'


class ResultsBoxing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_boxing'


class ResultsCanoeSlalom(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.TextField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_canoe_slalom'


class ResultsCanoeSprint(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_canoe_sprint'


class ResultsCyclingBmxFreestyle(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_cycling_bmx_freestyle'


class ResultsCyclingBmxRacing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_cycling_bmx_racing'


class ResultsCyclingMountainBike(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TimeField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_cycling_mountain_bike'


class ResultsCyclingRoad(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_cycling_road'


class ResultsCyclingTrack(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_cycling_track'


class ResultsDiving(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_diving'


class ResultsEquestrian(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_equestrian'


class ResultsFencing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_fencing'


class ResultsFootball(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_football'


class ResultsGolf(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_golf'


class ResultsHandball(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_handball'


class ResultsHockey(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_hockey'


class ResultsJudo(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_judo'


class ResultsMarathonSwimming(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TimeField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_marathon_swimming'


class ResultsModernPentathlon(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_modern_pentathlon'


class ResultsRhythmicGymnastics(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_rhythmic_gymnastics'


class ResultsRowing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_rowing'


class ResultsRugbySevens(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_rugby_sevens'


class ResultsSailing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_sailing'


class ResultsShooting(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_shooting'


class ResultsSkateboarding(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_skateboarding'


class ResultsSportClimbing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_sport_climbing'


class ResultsSurfing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_surfing'


class ResultsSwimming(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_swimming'


class ResultsTableTennins(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_table_tennins'


class ResultsTaekwondo(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_taekwondo'


class ResultsTennis(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_tennis'


class ResultsTrampolineGymnastics(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_trampoline_gymnastics'


class ResultsTriathlon(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TimeField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_triathlon'


class ResultsVolleyball(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_volleyball'


class ResultsWaterPolo(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_water_polo'


class ResultsWeightlifting(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_weightlifting'


class ResultsWrestling(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_wrestling'


class Schedules(models.Model):
  start_date = models.TextField(blank=True, null=True)  # This field type is a guess.
  end_date = models.TextField(blank=True, null=True)  # This field type is a guess.
  day = models.DateField(blank=True, null=True)
  status = models.TextField(blank=True, null=True)
  discipline = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  event = models.TextField(blank=True, null=True)
  event_medal = models.BigIntegerField(blank=True, null=True)
  phase = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  event_type = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  venue_code = models.TextField(blank=True, null=True)
  location_description = models.TextField(blank=True, null=True)
  location_code = models.TextField(blank=True, null=True)
  url = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'schedules'


class SchedulesPreliminary(models.Model):
  date_start_utc = models.TextField(blank=True, null=True)  # This field type is a guess.
  date_end_utc = models.TextField(blank=True, null=True)  # This field type is a guess.
  estimated = models.BooleanField(blank=True, null=True)
  estimated_start = models.BooleanField(blank=True, null=True)
  start_text = models.TimeField(blank=True, null=True)
  medal = models.BigIntegerField(blank=True, null=True)
  venue_code = models.TextField(blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  venue_code_other = models.TextField(blank=True, null=True)
  discription_other = models.TextField(blank=True, null=True)
  team_1_code = models.TextField(blank=True, null=True)
  team_1 = models.TextField(blank=True, null=True)
  team_2_code = models.TextField(blank=True, null=True)
  team_2 = models.TextField(blank=True, null=True)
  tag = models.TextField(blank=True, null=True)
  sport = models.TextField(blank=True, null=True)
  sport_code = models.TextField(blank=True, null=True)
  sport_url = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'schedules_preliminary'


class Teams(models.Model):
  code = models.TextField(blank=True, null=True)
  team = models.TextField(blank=True, null=True)
  team_gender = models.TextField(blank=True, null=True)
  country = models.TextField(blank=True, null=True)
  country_full = models.TextField(blank=True, null=True)
  country_code = models.TextField(blank=True, null=True)
  discipline = models.TextField(blank=True, null=True)
  disciplines_code = models.TextField(blank=True, null=True)
  events = models.TextField(blank=True, null=True)
  athletes = models.TextField(blank=True, null=True)
  coaches = models.TextField(blank=True, null=True)
  athletes_codes = models.TextField(blank=True, null=True)
  num_athletes = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  coaches_codes = models.TextField(blank=True, null=True)
  num_coaches = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'teams'


class TorchRoute(models.Model):
  title = models.TextField(blank=True, null=True)
  city = models.TextField(blank=True, null=True)
  date_start = models.TextField(blank=True, null=True)  # This field type is a guess.
  date_end = models.TextField(blank=True, null=True)  # This field type is a guess.
  tag = models.TextField(blank=True, null=True)
  url = models.TextField(blank=True, null=True)
  stage_number = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'torch_route'


class Venues(models.Model):
  venue = models.TextField(blank=True, null=True)
  sports = models.TextField(blank=True, null=True)
  date_start = models.TextField(blank=True, null=True)  # This field type is a guess.
  date_end = models.TextField(blank=True, null=True)  # This field type is a guess.
  tag = models.TextField(blank=True, null=True)
  url = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'venues'
