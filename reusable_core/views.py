from django.conf import settings
from graphql.error import GraphQLSyntaxError, GraphQLError
from graphql.error.located_error import GraphQLLocatedError
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from graphene_django.views import GraphQLView

from django.utils.translation import ugettext as _
from django.utils import translation

from .errors import PermissionDenied, HasRelationsException


class SafeGraphQLView(GraphQLView):
    @staticmethod
    def format_error(error):
        print("\nERROR: {}\n".format(str(error)))
        data = {
            'message': str(error),
        }

        if isinstance(error, GraphQLLocatedError):
            print("\n\n\nGraphQLLocatedError\n\n\n")
            
            if isinstance(error.original_error, PermissionDenied):
                data.update({
                    'message': _("You are not allowed to perform this action!"),
                    'statusCode': 401
                })
                
            if isinstance(error.original_error, HasRelationsException):
                data.update({
                    'message': _(str(error)),
                    'statusCode': 400
                })

            if isinstance(error.original_error, ObjectDoesNotExist):
                data.update({
                    'message': _("There is no matching result for this query."),
                    'message_base': str(error),
                    'statusCode': 404
                })
            
            if isinstance(error.original_error, ValidationError):
                print('\n\n\n\n')
                print('422')
                print('\n\n\n\n')

        elif isinstance(error, GraphQLSyntaxError):
            print("\n\n\nGraphQLLocatedError\n\n\n")

        elif isinstance(error, GraphQLError):
            print("\n\n\nGraphQLError\n\n\n")
            data.update({
                'message': _('A failure occurred during this operation. Please make sure everything is alright. If the problem persists contact support!'),
                'message_base': str(error),
                'statusCode': 500
            })         

        else:
            data['code'] = _('unhandled_exception')
            if not settings.DEBUG:
                data['message'] = _('Server error')
            else:
                data.update({
                    'message': _('Server error'),
                    'erro': _(str(error))
                })

        return data
