1. Create an Virtual Environment
 ```bash
    conda create -n FastAPI python=3.11 -y
 ```
    

2. Activate Virtual Environment
 ```bash
    conda activate FastAPI
 ```

3. install requirements.txt
 ```bash
    pip install -r requirements.txt
 ```

4. Delete a Virtual Environment
    - 1. Deactivate the Environment
        ```bash
            conda deactivate
                or
            conda activate base
        ```

    - 2.  Remove the Environment
        ```bash
            conda env remove -n GenAI -y
        ```
    - 3.  Verify the Environment
        ```bash
            conda env list
        ```
