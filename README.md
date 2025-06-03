## Quick Start

1.  **Build and Run:**
    Navigate to the project root (where `docker-compose.yml` is) and run:
    ```bash
    docker-compose up --build
    ```
    The server will start on port `8084`.


2.  **Test**
   - download file: `curl -OJ http://localhost:5000/download/wireguard`
   - list files: `curl http://localhost:5000/list-files`
    
