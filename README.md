QSee
====

A microservice to view git branches on remote machines
------------------------------------------------------

To run the server:
gunicorn --bind 0.0.0.0:5000 qsee:app

Installation:
  mkdir qsee
  chown {user}:{group} qsee
  git clone git@github.com:cschreep/qsee.git qsee
  cd qsee/
  virtualenv -p python3 env
  source env/bin/activate
  pip install -r requirements.txt 
  sudo cp service.example /etc/systemd/system/qsee.service
  sudo systemctl start qsee
