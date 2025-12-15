# Numerical-Integration-of-Atmospheric-Re-Entry-Thermal-Loads
ASTE404 Mini Project: A Python-based numerical simulation of atmospheric re-entry heating using ODE integration to model velocity, altitude, heat flux, and thermal loading along a simplified descent trajectory.

## Requirements
- Python 3.10
- numpy
- matplotlib
- scipy

## Run Instructions

1. Install required Python packages:
    
    ```bash
    pip install numpy matplotlib scipy
    ```

2. Navigate to the project root directory:
    
    ```bash
    cd ThisFileLocation
    ```

3. Run the simulation from the root folder:
    
    ```bash
    python src/main.py
    ```

4. To change the timestep:
    
    - Open `src/main.py`
    - Modify the value of `dt`
    - Run again:
      
      ```bash
      python src/main.py
      ```

