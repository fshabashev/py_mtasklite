import copy
import inspect
import platform
import multiprocessing
from typing import Dict, Any, Tuple

KwArgs = Dict[str, Any]


def is_sized_iterator(input_iterable):
    return hasattr(input_iterable, '__len__')


def is_exception(result):
    return isinstance(result, Exception)


def set_process_start_method():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        multiprocessing.set_start_method('spawn')
    else:
        multiprocessing.set_start_method('fork')


def divide_kwargs(kwargs: KwArgs, first_type) -> Tuple[KwArgs, KwArgs]:
    """
        A slightly modified version of kwarg "divider" from https://github.com/niedakh/pqdm/blob/master/pqdm/utils.py#L24

        Given a dictionary of all keyword arguments and the second type, we divided keyword arguments into
        two "buckets".

        :param kwargs:
        :param first_type:
        :return:
    """
    first_type_args = {
        k: kwargs[k] for k in inspect.getfullargspec(first_type)[0] if k in kwargs
    }
    second_type_kwargs = copy.copy(kwargs)
    for k in inspect.getfullargspec(first_type)[0]:
        if k in second_type_kwargs:
            del second_type_kwargs[k]

    assert kwargs.keys() == first_type_args.keys() | second_type_kwargs.keys()

    return first_type_args, second_type_kwargs
