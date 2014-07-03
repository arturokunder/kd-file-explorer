from django.contrib.auth.decorators import login_required
from home.models import Permission


def client_auth(func):
  @login_required(login_url='/login/', )
  def decorator(request, path=''):

    p = Permission.objects.get(user_id=request.user.id)
    print p

    #p = Permission(user=request.user)
    #p.folder = '/534c4546bae656020080728c'
    #p.save();

    bucket = 'files.survey.kunder.cl/reports'
    folder = p.folder

    allowed_path = bucket + folder

    if not allowed_path in path:
      path = allowed_path

    return func(request, path)
  return decorator
