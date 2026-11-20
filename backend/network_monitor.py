
"""
NVIDIA NetQ Network Observability Lab
Network Monitoring Module

Educational simulation using sample network data.
"""

from datetime import datetime, timezone


# Sample network devices
NETWORK_DEVICES = [
    {
        "id": "SW-01",
        "name": "Core Switch",
        "type": "Switch",
        "status": "Online",
        "latency": 12
    },
    {
        "id": "SW-02",
        "name": "Distribution Switch",
        "type": "Switch",
        "status": "Online",
        "latency": 18
    },
    {
        "id": "RTR-01",
        "name": "Main Router",
        "type": "Router",
        "status": "Warning",
        "latency": 85
    },
    {
        "id": "SRV-01",
        "name": "Network Server",
        "type": "Server",
        "status": "Online",
        "latency": 10
    },
    {
        "id": "SW-03",
        "name": "Access Switch",
        "type": "Switch",
        "status": "Offline",
        "latency": None
    }
]


def get_network_devices():
    """Return sample network device information."""
    return NETWORK_DEVICES


def get_network_health():
    """Calculate network health statistics."""

    devices = get_network_devices()

    online = sum(
        1 for device in devices
        if device["status"] == "Online"
    )

    offline = sum(
        1 for device in devices
        if device["status"] == "Offline"
    )

    warnings = sum(
        1 for device in devices
        if device["status"] == "Warning"
    )

    return {
        "total_devices": len(devices),
        "online_devices": online,
        "offline_devices": offline,
        "warning_devices": warnings,
        "health_status": (
            "Critical" if offline > 0
            else "Warning" if warnings > 0
            else "Healthy"
        ),
        "last_updated": datetime.now(
            timezone.utc
        ).isoformat()
    }


def get_network_alerts():
    """Generate alerts from simulated device status."""

    alerts = []

    for device in get_network_devices():

        if device["status"] == "Offline":
            alerts.append({
                "device": device["name"],
                "severity": "Critical",
                "message": "Device is offline."
            })

        elif device["status"] == "Warning":
            alerts.append({
                "device": device["name"],
                "severity": "Warning",
                "message": "Device requires attention."
            })

    return alerts
