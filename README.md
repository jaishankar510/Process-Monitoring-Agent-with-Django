Step1 :- 

#Activate  
**.venv\Scripts\activate**


Step 2:-
**pip install -r requirements.txt**


step3:-

Reset Database (if starting fresh)

If you deleted db.sqlite3, recreate it:

**python manage.py makemigrations
python manage.py migrate**


✅ This creates all tables (monitor_systeminfo, monitor_processinfo, etc.).


step4:- 

Create Superuser (for admin panel)
**python manage.py createsuperuser**


Step5

Run the Django Server
python manage.py runserver


working usl
Now your backend is running at:
👉 http://127.0.0.1:8000/

API root: http://127.0.0.1:8000/api/

Admin panel: http://127.0.0.1:8000/admin/

Frontend :- http://127.0.0.1:8000/frontend/


. Run the Agent

If you are still testing in Python:

python agent/agent.py


If you already built the EXE:

dist\agent.exe


You should see messages like:

✅ New system info sent successfully!
✅ Process data sent successfully!
Press Enter to exit...
