from flask import request, jsonify
from app import webserver
from threading import Lock

# Example endpoint definition
@webserver.route('/api/post_endpoint', methods=['POST'])
def post_endpoint():
    if request.method == 'POST':
        # Assuming the request contains JSON data
        data = request.json
        print(f"got data in post {data}")

        # Process the received data
        # For demonstration purposes, just echoing back the received data
        response = {"message": "Received data successfully", "data": data}

        # Sending back a JSON response
        return jsonify(response)

    # Method Not Allowed
    return jsonify({"error": "Method not allowed"}), 405

@webserver.route('/api/get_results/<job_id>', methods=['GET'])
def get_response(job_id):
    print(f"JobID is {job_id}")

    if job_id not in webserver.tasks_runner.job_status:
        return jsonify({
            'status': 'error',
            'reason': 'Invalid job_id'
        })
    if webserver.tasks_runner.job_status[job_id] == 'done':
        res = webserver.tasks_runner.job_dict[job_id]
        return jsonify({
            'status': 'done',
            'data': res
        })
    status = webserver.tasks_runner.job_status[job_id]
    return jsonify({'status': status})

@webserver.route('/api/states_mean', methods=['POST'])
def states_mean_request():
    lock = Lock()
    data = request.json
    print(f"Got request {data}")

    # Checks if graceful_shutdown was received
    if webserver.tasks_runner.is_shutdown.is_set():
        return jsonify({ 'job_id' : -1, 'reason' : 'shutting down' })

    copy = webserver.job_counter
    # Adds the job to the queue
    webserver.tasks_runner.add_job(webserver.data_ingestor.states_mean, data, copy)
    lock.acquire()
    webserver.job_counter += 1
    lock.release()
    return jsonify({'job_id': str(copy)})

@webserver.route('/api/state_mean', methods=['POST'])
def state_mean_request():
    lock = Lock()
    data = request.json
    print(f"Got request {data}")
    # Checks if graceful_shutdown was received
    if webserver.tasks_runner.is_shutdown.is_set():
        return jsonify({ 'job_id' : -1, 'reason' : 'shutting down' })

    copy = webserver.job_counter
    # Adds the job to the queue
    webserver.tasks_runner.add_job(webserver.data_ingestor.state_mean, data, copy)
    lock.acquire()
    webserver.job_counter += 1
    lock.release()
    return jsonify({'job_id': str(copy)})

@webserver.route('/api/best5', methods=['POST'])
def best5_request():
    lock = Lock()
    data = request.json
    print(f"Got request {data}")
    # Checks if graceful_shutdown was received
    if webserver.tasks_runner.is_shutdown.is_set():
        return jsonify({ 'job_id' : -1, 'reason' : 'shutting down' })

    copy = webserver.job_counter
    # Adds the job to the queue
    webserver.tasks_runner.add_job(webserver.data_ingestor.best5, data, copy)
    lock.acquire()
    webserver.job_counter += 1
    lock.release()
    return jsonify({'job_id': str(copy)})


@webserver.route('/api/worst5', methods=['POST'])
def worst5_request():
    lock = Lock()
    data = request.json
    print(f"Got request {data}")
    # Checks if graceful_shutdown was received
    if webserver.tasks_runner.is_shutdown.is_set():
        return jsonify({ 'job_id' : -1, 'reason' : 'shutting down' })

    copy = webserver.job_counter
    # Adds the job to the queue
    webserver.tasks_runner.add_job(webserver.data_ingestor.worst5, data, copy)
    lock.acquire()
    webserver.job_counter += 1
    lock.release()
    return jsonify({'job_id': str(copy)})

@webserver.route('/api/global_mean', methods=['POST'])
def global_mean_request():
    lock = Lock()
    data = request.json
    print(f"Got request {data}")
    # Checks if graceful_shutdown was received
    if webserver.tasks_runner.is_shutdown.is_set():
        return jsonify({ 'job_id' : -1, 'reason' : 'shutting down' })

    copy = webserver.job_counter
    # Adds the job to the queue
    webserver.tasks_runner.add_job(webserver.data_ingestor.global_mean, data, copy)
    lock.acquire()
    webserver.job_counter += 1
    lock.release()
    return jsonify({'job_id': str(copy)})

@webserver.route('/api/diff_from_mean', methods=['POST'])
def diff_from_mean_request():
    lock = Lock()
    data = request.json
    print(f"Got request {data}")
    # Checks if graceful_shutdown was received
    if webserver.tasks_runner.is_shutdown.is_set():
        return jsonify({ 'job_id' : -1, 'reason' : 'shutting down' })

    copy = webserver.job_counter
    # Adds the job to the queue
    webserver.tasks_runner.add_job(webserver.data_ingestor.diff_from_mean, data, copy)
    lock.acquire()
    webserver.job_counter += 1
    lock.release()
    return jsonify({'job_id': str(copy)})


@webserver.route('/api/state_diff_from_mean', methods=['POST'])
def state_diff_from_mean_request():
    lock = Lock()
    data = request.json
    print(f"Got request {data}")
    # Checks if graceful_shutdown was received
    if webserver.tasks_runner.is_shutdown.is_set():
        return jsonify({ 'job_id' : -1, 'reason' : 'shutting down' })

    copy = webserver.job_counter
    # Adds the job to the queue
    webserver.tasks_runner.add_job(webserver.data_ingestor.state_diff_from_mean, data, copy)
    lock.acquire()
    webserver.job_counter += 1
    lock.release()
    return jsonify({'job_id': str(copy)})

@webserver.route('/api/mean_by_category', methods=['POST'])
def mean_by_category_request():
    lock = Lock()
    data = request.json
    print(f"Got request {data}")
    # Checks if graceful_shutdown was received
    if webserver.tasks_runner.is_shutdown.is_set():
        return jsonify({ 'job_id' : -1, 'reason' : 'shutting down' })

    copy = webserver.job_counter
    # Adds the job to the queue
    webserver.tasks_runner.add_job(webserver.data_ingestor.mean_by_category, data, copy)
    lock.acquire()
    webserver.job_counter += 1
    lock.release()
    return jsonify({'job_id': str(copy)})

@webserver.route('/api/state_mean_by_category', methods=['POST'])
def state_mean_by_category_request():
    lock = Lock()
    data = request.json
    print(f"Got request {data}")
    # Checks if graceful_shutdown was received
    if webserver.tasks_runner.is_shutdown.is_set():
        return jsonify({ 'job_id' : -1, 'reason' : 'shutting down' })

    copy = webserver.job_counter
    # Adds the job to the queue
    webserver.tasks_runner.add_job(webserver.data_ingestor.state_mean_by_category, data, copy)
    lock.acquire()
    webserver.job_counter += 1
    lock.release()
    return jsonify({'job_id': str(copy)})
    
@webserver.route('/api/graceful_shutdown', methods=['GET'])
def graceful_shutdown():
    webserver.tasks_runner.shutdown()

@webserver.route('/api/num_jobs', methods=['GET'])
def num_jobs():
    num_jobs_val = len(webserver.tasks_runner.job_queue)
    if webserver.tasks_runner.is_shutdown.is_set() & num_jobs_val == 0:
        return jsonify({'jobs' : 0})
    return jsonify({'jobs' : num_jobs_val})

@webserver.route('/api/jobs', methods=['GET'])
def jobs():
    res = webserver.tasks_runner.job_dict
    return jsonify({'status': 'done',
                    'data': res})


# You can check localhost in your browser to see what this displays
@webserver.route('/')
@webserver.route('/index')
def index():
    routes = get_defined_routes()
    msg = f"Hello, World!\n Interact with the webserver using one of the defined routes:\n"

    # Display each route as a separate HTML <p> tag
    paragraphs = ""
    for route in routes:
        paragraphs += f"<p>{route}</p>"

    msg += paragraphs
    return msg

def get_defined_routes():
    routes = []
    for rule in webserver.url_map.iter_rules():
        methods = ', '.join(rule.methods)
        routes.append(f"Endpoint: \"{rule}\" Methods: \"{methods}\"")
    return routes
