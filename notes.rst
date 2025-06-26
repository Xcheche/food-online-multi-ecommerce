"""
Django forms provide two types of error collections: field errors and non-field errors.

- Field errors are associated with specific form fields. They are stored in the form's `errors` dictionary, where each key is the field name and the value is a list of error messages for that field. These errors are typically displayed next to the corresponding form field in the template.

- Non-field errors are errors that do not pertain to a specific field, but rather to the form as a whole (for example, validation that involves multiple fields). These are accessed via the form's `non_field_errors()` method and are not included in the `errors` dictionary. In templates, non-field errors are usually displayed at the top of the form or in a general error section.

When rendering forms in templates, field errors should be displayed next to their respective fields, while non-field errors should be rendered in a separate section, often above the form fields, to alert the user to issues not tied to a single input.
"""