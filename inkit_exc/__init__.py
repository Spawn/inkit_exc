try:
    from falcon import HTTPError as ErrClass
    framework = 'falcon'
except ImportError:
    framework = 'flask'
    from flask import jsonify
    from werkzeug.exceptions import HTTPException as ErrClass


class CustomHTTPError(ErrClass):

    code = None
    title = None
    code_name = None
    default_detail = None
    help_url = None
    description = None
    status = None
    headers = None
    response = None

    def __init__(self, status=None, errors=None, detail=None, meta=None):

        self.code = self.code or status
        self.errors = errors or [{
            'meta': meta or {},
            'detail': detail or self.default_detail
        }]

        if isinstance(self.errors, dict):
            self.errors = [{err_name: err_value} for err_name, err_value in self.errors.items()]

        for i in range(len(self.errors)):
            self.errors[i]['id'] = i + 1
            self.errors[i]['title'] = self.title
            self.errors[i]['code_name'] = self.code_name
            if self.help_url:
                self.errors[i]['help_url'] = self.help_url
            if 'meta' not in self.errors[i]:
                self.errors[i]['meta'] = {}
        if framework == 'flask':
            self.response = jsonify({'errors': self.errors})
            self.response.status_code = self.code

    def to_dict(self, obj_type=dict):
        res = obj_type()
        res['errors'] = self.errors
        return res
