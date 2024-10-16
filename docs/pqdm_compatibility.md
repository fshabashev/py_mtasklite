# PQDM (in) compatibility notes

**and works on Mac OS without setting the process creation method to `fork`**

Although we have a pqmd compatibility mode, for various reasons, we have decided to not make our code
100% compatible. There are a couple of crucial differences:

1. We return an iterable, not a list.

2. Because semantics of the worker parameter is extended (it can be a list including both functions and statefull class objects) we changed the parameter name `function` to `worker_or_worker_arr`. Likewise, because we support generic iterables rather than lists, the parameter name `array` was changed into `input_iterable`. However, the order of these arguments remains the same, so renaming should matter little in practice.

3. The 'direct' argument passing mode name is confusing and we called it a single-argument mode instead (and define a new constant). Fortunately, this is a default argument passing value, so we anticipate that no code change will be required.

4. Regarding the bounded execution flag, we set it to false by default. Moreover, we cannot support it for un-sized iterators. However, if the iterator is for the object with a known size, we simulate unbounded execution by setting the chunk size to be equal to the length of the input (and setting prefill ratio to 1).

5. We always start a thread/process for a worker even if n_jobs == 1.

6. Clarify on the default behavior of the exceptions, which is IGNORE