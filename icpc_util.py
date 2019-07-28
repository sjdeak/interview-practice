import inspect


# https://stackoverflow.com/questions/6200270/decorator-to-print-function-call-details-parameters-names-and-effective-values
def dump_args(func):
  """
  Decorator to print function call details - parameters names and effective values.
  """

  def wrapper(*args, **kwargs):
    func_args = inspect.signature(func).bind(*args, **kwargs).arguments
    func_args_str = ', '.join('{} = {!r}'.format(*item) for item in func_args.items())
    ret = func(*args, **kwargs)
    print('[DEBUG]:', f'{func.__module__}.{func.__qualname__} ( {func_args_str} ) -> {ret}')
    return ret

  return wrapper


def debug(*args, **kwargs):
  print('[DEBUG]:', *args, **kwargs)
