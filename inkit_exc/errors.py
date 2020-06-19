from . import CustomHTTPError


class NotFoundError(CustomHTTPError):
    status = '404 Not Found'
    code = 404
    title = 'Not Found'
    code_name = 'NOT_FOUND'
    default_detail = 'requested entity is not found'
    help_url = ''


class AuthenticationFailedError(CustomHTTPError):
    status = '403 Forbidden'
    code = 403
    title = 'Forbidden'
    code_name = 'FORBIDDEN'
    default_detail = 'Authentication failed'
    help_url = ''


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
    code_name = 'UNSUPPORTED_MEDIA_TYPE'
    default_detail = 'Valid JSON data expected'
    help_url = ''


class ValidationError(CustomHTTPError):
    status = '422 Unprocessable Entity'
    code = 422
    title = 'Unprocessable Entity'
    code_name = 'UNPROCESSABLE_ENTITY'
    default_detail = ''
    help_url = ''


class AlreadyExistsError(CustomHTTPError):
    status = '409 Conflict'
    code = 409
    title = 'Already Exists'
    code_name = 'ALREADY_EXISTS'
    default_detail = ''
    help_url = ''


class InvalidFileTypeError(CustomHTTPError):
    status = '422 Unprocessable Entity'
    code = 422
    title = 'Invalid file type'
    code_name = 'INVALID_FILE_TYPE'
    default_detail = ''
    help_url = ''


class UndeliverableAddressError(CustomHTTPError):
    status = '422 Unprocessable Entity'
    code = 422
    title = 'Undeliverable Address'
    code_name = 'UNDELIVERABLE_ADDRESS'
    default_detail = ''
    help_url = ''


class UserNotAuthorizedError(CustomHTTPError):
    status = '403 Forbidden'
    code = 403
    title = 'Forbidden'
    code_name = 'FORBIDDEN'
    default_detail = 'user not authorized'
    help_url = ''


class UserDeactivatedError(CustomHTTPError):
    status = '403 Forbidden'
    code = 403
    title = 'Forbidden'
    code_name = 'FORBIDDEN'
    default_detail = 'User has been deactivated'
    help_url = ''


class PlaidError(CustomHTTPError):

    status = '500 Internal Server Error',
    code = 500,
    title = 'Internal Server Error',
    description = 'plaid operation failed',
    code_name = 'SERVER_ERROR',
    help_url = '',


class PlaidLinkUpdateRequiredError(CustomHTTPError):

    status = '400 Bad Request',
    code = 400,
    title = 'Link Update Required',
    description = '',
    code_name = 'LINK_UPDATE_REQUIRED',
    help_url = '',


class StripeCardError(CustomHTTPError):

    status = '402 Payment Required',
    code = 402,
    title = 'Stripe Card Error',
    description = '',
    code_name = 'STRIPE_ERROR',
    help_url = '',


class StripeGenericError(CustomHTTPError):

    status = '402 Payment Required',
    code = 402,
    title = '',
    description = '',
    code_name = 'STRIPE_ERROR',
    help_url = '',


class MissingObjectIDError(CustomHTTPError):

    status = '400 Bad Request',
    code = 400,
    title = '',
    description = '',
    code_name = 'MISSING_OBJECT_ID',
    help_url = '',


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
