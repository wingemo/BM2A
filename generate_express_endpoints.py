# Create an Express template
express_template = """
const express = require('express');
const app = express();

{% for data, operations in data_objects.items() %}
{% for operation, _ in operations.items() %}
app.{{ operation }}('/{{ data }}', (req, res) => {
  // Implement your {{ operation }} logic for {{ data }}
  res.send('{{ operation }} {{ data }} endpoint');
});
{% endfor %}
{% endfor %}

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
"""

# Create a Jinja2 template and fill it with data_objects
template = Template(express_template)
express_code = template.render(data_objects=data_objects)

# Save the generated JavaScript code to a file
with open('express_app.js', 'w') as file:
    file.write(express_code)
