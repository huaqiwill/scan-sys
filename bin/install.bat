pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
@REM python ./init.py initdb
@REM python ./manage.py makemigrations
@REM python ./manage.py migrate --fake-initial
@REM python ./init.py initsql
@REM python ./manage.py shell -c "from django.contrib.auth.models import User;User.objects.filter(username='abo').exists() or User.objects.create_superuser('abo','abo@example.com', 'abo')"
