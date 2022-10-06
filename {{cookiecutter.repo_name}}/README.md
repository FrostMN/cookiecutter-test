{{ cookiecutter.project_name }}

Version: {{ cookiecutter.version }}

{{ cookiecutter.project_description }}

{% if cookiecutter.includeDsDeps == 'True' %}
    included
{% endif %}
