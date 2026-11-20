
/* =====================================
   NVIDIA NetQ Network Observability Lab
   Network Monitoring Module
===================================== */

window.NetQLab = window.NetQLab || {};

NetQLab.devices = [
    { id: "SW-01", status: "Online", latency: 12 },
    { id: "SW-02", status: "Online", latency: 18 },
    { id: "RTR-01", status: "Warning", latency: 85 },
    { id: "SRV-01", status: "Online", latency: 10 },
    { id: "SW-03", status: "Offline", latency: null }
];

NetQLab.getMonitoringData = function () {
    return NetQLab.devices;
};

NetQLab.checkNetworkHealth = function () {
    const devices = NetQLab.getMonitoringData();

    const online = devices.filter(
        d => d.status === "Online"
    ).length;

    const offline = devices.filter(
        d => d.status === "Offline"
    ).length;

    const warnings = devices.filter(
        d => d.status === "Warning"
    ).length;

    return {
        total: devices.length,
        online,
        offline,
        warnings
    };
};

NetQLab.displayNetworkHealth = function () {
    const health = NetQLab.checkNetworkHealth();

    console.log("Network Health Report");
    console.table(health);

    return health;
};

console.log("Network monitoring module loaded.");
