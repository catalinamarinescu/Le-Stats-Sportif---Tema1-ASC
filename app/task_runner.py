from queue import Queue
from threading import Thread, Event
import os
import json

class ThreadPool:
    # Initialize data structures for the implementation and starts the threads
    # Fields:
    #       job_queue - the queue that contains tuples of type (function, argument, job_id)
    #       number_oh_threads - the number of threads that will be used
    #       job_status - a dictionary with the job_id as key and a string that represents
    #                   the status of the job as value
    #       job_dict - a dictionary with the job_id as key and the result of the function as value
    #       threads - an array of threads  
    #       is_shutdown - an event that sets the flag on true if the graceful_shutdown request 
    #                   is received                       

    def __init__(self):
        self.job_queue = Queue()
        if os.getenv("TP_NUM_OF_THREADS"):
            self.number_of_threads = int(os.getenv("TP_NUM_OF_THREADS"))
        else:
            self.number_of_threads = os.cpu_count()
        self.job_status = {}
        self.job_dict = {}
        self.threads = []
        self.is_shutdown = Event()
        for i in range(self.number_of_threads):
            thread = TaskRunner(self.job_queue, self.job_status, self.job_dict, self.is_shutdown)
            thread.start()
            self.threads.append(thread)

    # Function that adds the job to the queue and updates its status in running
    # Argumens:
    #       job - the specific function of the job
    #       data - the argument the job function takes
    #       job_id - the corresponding job_id
    def add_job(self, job, data, job_id):
        self.job_queue.put((job, data, job_id))
        self.job_status[str(job_id)] = 'running'

    # Function that sets the event's flag on true when the request is received
    # and stops the threads
    def shutdown(self):
        self.is_shutdown.set()
        self.job_queue.join()
        for thread in self.threads:
            thread.join()

class TaskRunner(Thread):
    # Receives the arguments from the threadpool
    def __init__(self, job_queue, job_status, job_dict, status):
        Thread.__init__(self)
        self.job_queue = job_queue
        self.job_status = job_status
        self.job_dict = job_dict
        self.status = status

    # Resolves the job
    def run(self):
        while True:
            job, data, job_id = self.job_queue.get()
            try:
                result = job(data)
                self.job_dict[str(job_id)] = result

                # Checks if the results/ dir exists, if not it creates it
                if not os.path.exists('results'):
                    os.mkdir('results')
                file_path = os.path.join(f'results/job_id_{job_id}.json')
                with open(file_path, 'w') as f:
                    f.write(json.dumps(result))

                self.job_status[str(job_id)] = "done"
            except Exception as e:
                print(f"Error processing job {job_id}: {e}")
                self.job_status[str(job_id)] = "error"
            # notifies when a task is done
            self.job_queue.task_done()
