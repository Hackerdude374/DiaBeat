## Running the Application

### Backend

1. Open a terminal and navigate to the `/backend` directory of the project.

2. Start the Flask server by running:
    ```
    $ flask run
    ```
   Alternatively, you can use:
    ```
    $ python -m flask run
    ```

### Frontend

1. Open a new terminal window/tab.

2. Navigate to the `/frontend` directory of the project.

3. Start the frontend development server by running:
    ```
    $ npm start
    ```

## Debugger Setup

To enable the debugger while running the application, follow these steps:

1. In the terminal where you're running the Flask backend, set the Flask debug mode:
    ```
    $ export FLASK_DEBUG=1
    ```
    Or in powershell:
    ```
    $env:FLASK_DEBUG = 1
    ```

2. Verify that debug mode is properly set by running:
    ```
    $ echo $FLASK_DEBUG
    ```
   The output should be `1`.

3. Now, run the Flask server as usual:
    ```
    $ flask run
    ```
   or:
    ```
    $ python -m flask run
    ```

With the debugger properly set up, you can now debug your Flask application effectively.
