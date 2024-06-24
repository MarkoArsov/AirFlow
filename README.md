

##   Running Airflow in Docker

This guide will walk you through setting up and running Apache Airflow in a Docker container using Dockerfile and docker-compose.yml files provided.

### Prerequisites

Before getting started, ensure you have Docker installed on your system. You can download and install Docker from here.

### Installation Steps

1.  **Clone the Repository**:

    `git clone <repository_url>` 
    
2.  **Navigate to the Project Directory**:
    
    `cd <project_directory>` 
    
3.  **Build the Docker Image**:
    
    `docker build -t airflow .` 
    
4.  **Run Docker Compose**:
    
    `docker-compose up -d` 
    
    This command will start the Airflow container in detached mode, meaning it will run in the background.
    

### Accessing Airflow UI

Once the Docker container is up and running, you can access the Airflow UI by navigating to `http://localhost:8080` in your web browser.

### Directory Structure

Your project directory should have the following structure:
```
airflow/
├── dockerfile
├── docker-compose.yml
└── airflow/
	├── <Airflow DAGs and configuration files>
```


-   `dockerfile`: Contains instructions for building the Airflow Docker image.
-   `docker-compose.yml`: Defines the services, volumes, ports, and commands for running the Airflow container.
-   `airflow/`: Directory where Airflow DAGs (Directed Acyclic Graphs) and configuration files are stored.

### Usage

After setting up Airflow, you can start creating and managing workflows using Airflow's UI. Here's a basic overview of using Airflow:

1.  **Create DAGs**:
    
    DAGs are Python scripts that define workflows. You can create DAGs in the `airflow/` directory.
    
2.  **Start the Scheduler**:
    
    In the Airflow UI, navigate to the Admin tab and start the scheduler. The scheduler orchestrates the execution of tasks defined in your DAGs.
    
3.  **Trigger DAGs**:
    
    Once the scheduler is running, you can trigger DAGs manually or set up schedules for them to run automatically.
    
4.  **Monitor Execution**:
    
    You can monitor the execution of tasks and view logs in the Airflow UI.
    
5.  **Manage Connections and Variables**:
    
    Airflow provides features to manage connections (e.g., database connections) and variables (e.g., configuration settings) through its UI.
    

### Additional Resources

-   [Apache Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html): Official documentation for Apache Airflow.
-   [Airflow Tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html): A tutorial to get started with Airflow.

### Notes

-   Ensure that any customizations or additional dependencies required for your workflows are included in the Dockerfile.
-   Adjust ports and volumes in the docker-compose.yml file as needed.
-   For production deployments, consider configuring Airflow with a production-grade database backend and setting up authentication and access controls.
