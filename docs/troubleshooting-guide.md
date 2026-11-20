
# NVIDIA NetQ Network Observability Lab
## Troubleshooting Guide

This guide helps identify and resolve common issues in the educational network observability lab.

---

## 1. Flask Module Not Found

**Problem:**

`ModuleNotFoundError: No module named 'flask'`

**Solution:**

Install the dependencies:

```bash
pip install -r requirements.txt
```

Make sure your virtual environment is activated.

---

## 2. Port 5000 Already in Use

**Problem:**

Another application is already using port 5000.

**Solution:**

Stop the other application or change the Flask port in `backend/app.py`:

```python
app.run(
    host="127.0.0.1",
    port=5001,
    debug=True
)
```

Then open:

http://127.0.0.1:5001/

---

## 3. Flask Backend Not Starting

**Possible causes:**

- Python is not installed correctly.
- Required dependencies are missing.
- Incorrect file paths.
- Python syntax errors.

**Solution:**

Check your Python version:

```bash
python --version
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the backend from the project root:

```bash
python backend/app.py
```

---

## 4. API Returns an Error

**Problem:**

An API endpoint does not return the expected JSON response.

**Solution:**

Verify that:

- The Flask server is running.
- The endpoint URL is correct.
- The route exists in `backend/app.py`.
- The browser is accessing the correct local port.

Available endpoints:

- `/api/status`
- `/api/devices`
- `/api/health`
- `/api/alerts`

---

## 5. Network Device Shows Offline

**Possible causes:**

- The simulated device status is set to Offline.
- The sample monitoring data contains an offline device.

**Solution:**

Check the device information in:

`backend/network_monitor.py`

Update the sample status if you want to test a healthy network scenario.

---

## 6. High Network Latency Warning

**Problem:**

A device displays unusually high latency.

**Solution:**

Review the simulated latency value in the monitoring dataset.

For demonstration purposes, you can modify the latency values and observe how the monitoring dashboard responds.

---

## 7. GitHub Pages Does Not Run Flask

**Problem:**

The frontend works on GitHub Pages, but Python API endpoints are unavailable.

**Explanation:**

GitHub Pages supports static website hosting. It does not execute Python Flask backend code.

**Solution:**

Deploy the Flask backend separately using a suitable Python hosting provider and configure the frontend to communicate with its API.

---

## 8. General Troubleshooting Checklist

- [ ] Python is installed.
- [ ] Flask dependencies are installed.
- [ ] Virtual environment is activated.
- [ ] Project files are in the correct folders.
- [ ] Flask server starts successfully.
- [ ] API endpoints return JSON.
- [ ] Browser console has no JavaScript errors.
- [ ] Frontend API URL is correctly configured.

---

## 9. Need More Help?

If an issue persists:

1. Check the terminal error messages.
2. Review the Flask application logs.
3. Inspect the browser developer console.
4. Verify the project configuration.
5. Open an issue in the GitHub repository.

---

**Developed by Heer Patel**

GitHub: https://github.com/Heer4204-bit
