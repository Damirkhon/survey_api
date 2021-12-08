# survey_api
Survey_api app using django-rest-framework

To get all dependencies, run: <code> pip install -r req.txt</code>

To get started with the app, run: <code><ul><li>python manage.py makemigrations</li><li>python manage.py migrate</li><li>python manage.py runserver</li></ul></code>

# API documentation:
<code>/surveys/actualSurveys/</code> - get actual surveys

<code>/surveys/actualSurveys/\<int:surveyId\></code> - get actual survey details and questions by its ID

<code>/answers/</code> - post answer to any survey question using *user_id, survey_id, question_id, answer*

<code>/answers/user/\<int:userId\></code> - get all the answers of any user, with details about survey,question, verification of the answer, using *user_id*
