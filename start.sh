#!/bin/sh

# Setting up the environment variables
printenv |
while read -r line
do
  echo "export '$line'" >> $HOME/.bash_profile
  echo "export '$line'" >> $HOME/.bashrc
done

while IFS= read -r line
do
  echo "export '$line'" >> $HOME/.bash_profile
  echo "export '$line'" >> $HOME/.bashrc
done < "/code/invisible_backend/environments/.env_$PYTHON_ENVIRONMENT"
# Environment variables done

service cron start

python3 /code/manage.py migrate
python3 /code/manage.py crontab add

exec "$@"
