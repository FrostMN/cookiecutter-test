{{ cookiecutter.project_name }}
{{ cookiecutter.project_name|allLower }}

Version: {{ cookiecutter.version }}

{{ cookiecutter.project_description }}

{% if cookiecutter.include_ag_grid == 'Y' %}
w/ag-grid
{% endif %}

{% if cookiecutter.include_ds_dependencies == 'Y' %}
w/ds dependencies
{% endif %}
