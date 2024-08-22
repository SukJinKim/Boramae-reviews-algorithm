import functools

def post_error_comment(pr):
    def wrapper(func):

        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Post error comment
                pr.create_issue_comment(f'다음과 같은 에러가 발생했습니다.\n{e}')
        
        return inner
    return wrapper
