<form method="post">{% csrf_token %}
    Are you sure you want to delete "{{ object }}" ?
    <input type="submit" value="Submit" />
</form>