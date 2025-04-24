import sys



def get_error_details(message, details:sys):
    '''
    This fuction create custom error message.
    '''
    if details is None:
        return message
    
    _,_,error_tb = details.exc_info()
    error_file = error_tb.tb_frame.f_code.co_filename
    error_line = error_tb.tb_lineno

    custom_error = f'Error Occured in: [{error_file}] at line no: [{error_line}] with message: [{message}]'
    return custom_error 




# Create CustomException Class
class CustomException(Exception):

    def __init__(self, error_message, error_details=None):
        super().__init__(error_message)
        self.error_message = get_error_details(message=error_message, details=error_details)

    def __str__(self):
        return self.error_message