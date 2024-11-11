from common_schemas import ApiResponse


def get_api_response(details, status):
    return ApiResponse(status=status, details=details)