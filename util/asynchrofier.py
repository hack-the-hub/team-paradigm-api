# #
# # Convert long running functions in to Tornado futures that.  So long as the function takes only pickelable arguments
# # and returns only pickelable results.   This module can wrap arbitrary python functions up asynchronously and run
# # them on different threads using the multiprocess module and not being hung up by the GIL.
# #
#
# import concurrent.futures
#
# import tornado.gen
#
#
# def create_threat_pool(count=20):
#     """
#     Create a thread worker pool for doing synchronous functions asynchronously jobs.   This needs to persist across a
#     class of work.  We could have one of these globally but I think we want to have one per task-type.
#     Somewhere it needs to persist
#     :param count:   number of threads
#     :return:        a new ThreadPoolExecutor
#     """
#     thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=count)
#     return thread_pool
#
#
# def async_wrapper(worker_pool, callback, callback_function, args):
#     """
#     Wraps up a synchronous function in a tornado future.
#     :param worker_pool:
#         client created python thread pool to execute the function in
#     :param callback:
#         callback to call when the function is completed.  It's a JS style fn(err,result) callback
#     :param callback_function:
#         synchronous function to invoke
#     :param args:
#         tuple of arguments to pass in to the function
#     :return:
#         a tornado future
#     """
#
#     @tornado.gen.coroutine
#     def _function_gateway(worker_pool, callback_function, args):
#         """
#         Take any function and run it on a thread pool wrapped in a Tornado future
#         :param worker_pool:
#             ThreadPool to use for the work
#         :param callback_function:
#             Callback function to invoke when complete
#         :param args:
#             arguments for the function  the arguments and return need to be pickelable
#         :return:
#             None
#         """
#
#         def _exception_handling_wrapper(arg):
#             nonlocal callback_function
#             try:
#                 return "success", callback_function(arg)
#             except Exception as e:
#
#                 return "fail", e
#
#         # Call the function
#         result = yield worker_pool.submit(_exception_handling_wrapper, args)
#         return result
#
#     def _call_back_wrapper(tornado_future):
#         """
#         Crack the tornado style callback in to a JS style callback.  This then calls the callback passed in on the parent
#         :param tornado_future:  the actual tornado future with a result
#         :return: None
#         """
#
#         nonlocal callback
#         (e, r) = tornado_future.result()
#         if e is "fail":
#             callback(r, None)
#         else:
#             callback(None, r)
#
#     # Produce a tornado future for a worker_pool enqueued function
#     tornado_future = _function_gateway(worker_pool, callback_function, args)
#
#     ## Attach a finish callback to the tornado future, this is a tornado compatible future
#     tornado_future.add_done_callback(_call_back_wrapper)
#     return tornado_future
