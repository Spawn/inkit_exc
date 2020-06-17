from . import CustomHTTPError


class MissingAccountHeaderError(CustomHTTPError):
    status = '403 Forbidden'
    code = 403
    title = 'Forbidden'
    code_name = 'FORBIDDEN'
    default_detail = 'not authorized'
    help_url = ''


class AccountNotFoundError(CustomHTTPError):
    status = '403 Forbidden'
    code = 403
    title = 'Forbidden'
    code_name = 'FORBIDDEN'
    default_detail = 'account not found'
    help_url = ''


class AccountNotActivatedError(CustomHTTPError):
    status = '403 Forbidden'
    code = 403
    title = 'Forbidden'
    code_name = 'FORBIDDEN'
    default_detail = 'account is not activated'
    help_url = ''


class AccountNotAdmin(CustomHTTPError):
    status = '403 Forbidden'
    code = 403
    title = 'Forbidden'
    code_name = 'FORBIDDEN'
    default_detail = 'admin access required'
    help_url = ''


class InternalServerError(CustomHTTPError):
    status = '500 Internal Server Error'
    code = 500
    title = "Internal Server Error"
    code_name = 'SERVER_ERROR'
    default_detail = 'undefined internal server error'
    help_url = ''


class MissingUserHeaderError(CustomHTTPError):
    status = '403 Forbidden'
    code = 403
    title = 'Forbidden'
    code_name = 'FORBIDDEN'
    default_detail = 'missing user id header'
    help_url = ''


class UserNotFoundError(CustomHTTPError):
    status = '403 Forbidden'
    code = 403
    title = 'Forbidden'
    code_name = 'FORBIDDEN'
    default_detail = 'user not found'
    help_url = ''


class NotJSONError(CustomHTTPError):
    status = '415 Unsupported Media Type'
    code = 415
    title = 'Unsupported Media Type'
    code_name = 'UNSUPPORTED MEDIA TYPE'
    default_detail = 'Valid JSON data expected'
    help_url = ''


class ValidationError(CustomHTTPError):
    status = '422 Unprocessable Entity'
    code = 422
    title = 'Unprocessable Entity'
    code_name = 'UNPROCESSABLE ENTITY'
    default_detail = ''
    help_url = ''


class AlreadyExistsError(CustomHTTPError):
    status = '409 Conflict'
    code = 409
    title = 'Already Exists'
    code_name = 'ALREADY EXISTS'
    default_detail = ''
    help_url = ''


class InvalidFileTypeError(CustomHTTPError):
    status = '422 Unprocessable Entity'
    code = 422
    title = 'Invalid file type'
    code_name = 'INVALID FILE TYPE'
    default_detail = ''
    help_url = ''


class InvalidParamWarning:
    title = 'Invalid URL Parameter'
    help_url = ''

    def __init__(self, detail=None, meta=None):
        self.detail = detail
        self.meta = meta or {}

    def to_dict(self):
        res = {
            'title': self.title,
            'detail': self.detail,
            'meta': self.meta,
        }
        if self.help_url:
            res['help_url'] = self.help_url
        return res
