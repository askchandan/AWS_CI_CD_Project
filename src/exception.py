import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Generates a detailed error message with file name, line number, and the error message itself.
    
    Parameters:
    - error: The exception object.
    - error_detail: Usually the sys module (to access exc_info).

    Returns:
    - A formatted error message string.
    """
    _, _, exc_tb = error_detail.exc_info()  # Only using traceback object from exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename  # Extracts the filename where the error occurred
    
    error_message = "Error occurred in Python script: [{0}], Line number: [{1}], Error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    return error_message


class CustomException(Exception):
    """
    Custom exception class that provides detailed error messages with traceback info.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Initialize base Exception with the raw message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message  # Return the detailed error message when str() is called
 

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")  # Assuming logger.log is defined to handle logging
        raise CustomException(e, sys)  # Raise the custom exception with detailed info